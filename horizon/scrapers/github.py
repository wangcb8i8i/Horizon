"""GitHub scraper — framework plugin."""

import logging
import os
import shutil
import subprocess
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    name = "github"
    description = "GitHub user events and repo releases"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        token_env = plugin_config.get("token_env", "GITHUB_TOKEN")
        self.token = os.getenv(token_env)
        if not self.token:
            self.token = self._gh_auth_token()
        self.base_url = "https://api.github.com"

        categories = plugin_config.get("_filter_categories")
        all_sources = plugin_config.get("sources", [])
        if categories is not None:
            all_sources = [
                s for s in all_sources
                if self._source_matches_categories(s, categories)
            ]
        self.sources = all_sources

    @staticmethod
    def _source_matches_categories(src: dict, categories: set[str]) -> bool:
        """Check if a GitHub source entry matches the given category set.

        Uses the ``type`` field as the category identifier.
        """
        src_cats = src.get("categories")
        if not src_cats:
            return False
        if isinstance(src_cats, str):
            src_cats_set = {src_cats.strip().lower()}
        elif isinstance(src_cats, list):
            src_cats_set = {c.strip().lower() for c in src_cats if c and c.strip()}
        else:
            return False
        return bool(src_cats_set & categories)

    def _headers(self) -> dict:
        h = {"Accept": "application/vnd.github.v3+json", "User-Agent": "Horizon"}
        if self.token:
            h["Authorization"] = f"token {self.token}"
        return h

    @staticmethod
    def _gh_auth_token() -> Optional[str]:
        """Fall back to ``gh auth token`` when GITHUB_TOKEN env is unset.

        This avoids a hard dependency on the gh CLI at runtime: if gh is
        not installed or not authenticated, we silently return None and
        proceed unauthenticated (60 req/h core, 10 req/h search). When gh
        *is* logged in, we borrow its OAuth token once to get 5000/30.
        """
        gh = shutil.which("gh")
        if not gh:
            return None
        try:
            result = subprocess.run(
                [gh, "auth", "token"],
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0:
                tok = result.stdout.strip()
                if tok and tok.startswith(("gho_", "ghp_", "ghu_", "github_pat_")):
                    return tok
        except Exception:
            pass
        return None

    async def fetch(self, since: datetime) -> List[ContentItem]:
        items = []
        for src in self.sources:
            if not src.get("enabled", True):
                continue
            if src.get("type") == "user_events" and src.get("username"):
                items.extend(await self._user_events(src["username"], since, src.get("categories")))
            elif src.get("type") == "repo_releases" and src.get("owner") and src.get("repo"):
                items.extend(await self._repo_releases(src["owner"], src["repo"], since, src.get("categories")))
            elif src.get("type") == "trending":
                items.extend(await self._trending(src))
        return items

    async def _user_events(self, username: str, since: datetime, categories: list | None = None) -> List[ContentItem]:
        try:
            resp = await self.client.get(
                f"{self.base_url}/users/{username}/events/public",
                headers=self._headers(),
                follow_redirects=True,
            )
            resp.raise_for_status()
        except httpx.HTTPError as e:
            self._report_error(f"user_events {username}", e)
            return []

        items = []
        for ev in resp.json():
            created_at = datetime.fromisoformat(ev["created_at"].replace("Z", "+00:00"))
            if created_at < since:
                continue
            if ev["type"] not in ("PushEvent", "CreateEvent", "ReleaseEvent", "PublicEvent", "WatchEvent"):
                continue

            repo = ev["repo"]["name"]
            repo_url = f"https://github.com/{repo}"
            etype = ev["type"]
            payload = ev.get("payload", {})

            if etype == "PushEvent":
                commits = payload.get("commits", [])
                title = f"{username} pushed {len(commits)} commit(s) to {repo}"
                content = "\n".join(c.get("message", "") for c in commits[:3])
            elif etype == "CreateEvent":
                title = f"{username} created {payload.get('ref_type', '')} in {repo}"
                content = payload.get("description", "") or ""
            elif etype == "ReleaseEvent":
                release = payload.get("release", {})
                title = f"{username} released {release.get('tag_name', '')} in {repo}"
                content = release.get("body", "") or ""
                repo_url = release.get("html_url", repo_url)
            elif etype == "PublicEvent":
                title = f"{username} made {repo} public"
                content = ""
            elif etype == "WatchEvent":
                title = f"{username} starred {repo}"
                content = ""
            else:
                continue

            items.append(
                ContentItem(
                    id=self._generate_id("github", "event", ev["id"]),
                    source_type="github",
                    title=title,
                    url=repo_url,
                    content=content,
                    author=username,
                    published_at=created_at,
                    metadata={"event_type": etype, "repo": repo, "categories": categories},
                )
            )
        return items

    async def _repo_releases(self, owner: str, repo: str, since: datetime, categories: list | None = None) -> List[ContentItem]:
        try:
            resp = await self.client.get(
                f"{self.base_url}/repos/{owner}/{repo}/releases",
                headers=self._headers(),
                follow_redirects=True,
            )
            resp.raise_for_status()
        except httpx.HTTPError as e:
            self._report_error(f"repo_releases {owner}/{repo}", e)
            return []

        items = []
        for rel in resp.json():
            published_at = datetime.fromisoformat(rel["published_at"].replace("Z", "+00:00"))
            if published_at < since:
                continue
            items.append(
                ContentItem(
                    id=self._generate_id("github", "release", str(rel["id"])),
                    source_type="github",
                    title=f"{owner}/{repo} released {rel['tag_name']}",
                    url=rel["html_url"],
                    content=rel.get("body", ""),
                    author=rel["author"]["login"],
                    published_at=published_at,
                    metadata={
                        "repo": f"{owner}/{repo}",
                        "tag": rel["tag_name"],
                        "prerelease": rel.get("prerelease", False),
                        "categories": categories,
                    },
                )
            )
        return items

    async def _trending(self, src: dict) -> List[ContentItem]:
        """Fetch trending repos via GitHub Search API."""
        from datetime import timedelta

        since_map = {"daily": 1, "weekly": 7, "monthly": 30}
        days = since_map.get(src.get("since", "weekly"), 7)
        cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
        since_str = f">{cutoff}"

        languages = src.get("languages", [])
        q_parts = [f"created:{since_str}"]
        # GitHub Search API only accepts one ``language:`` qualifier per query
        if languages:
            first = languages[0].strip()
            if first:
                q_parts.append(f"language:{first}")
        query = " ".join(q_parts)
        sort = src.get("sort", "stars")
        max_items = min(src.get("max_items", 30), 100)

        params = {"q": query, "sort": sort, "order": "desc", "per_page": max_items}
        try:
            resp = await self.client.get(
                f"{self.base_url}/search/repositories",
                headers=self._headers(),
                params=params,
                follow_redirects=True,
            )
            resp.raise_for_status()
        except httpx.HTTPError as e:
            self._report_error("trending", e)
            return []

        items = []
        for repo in (resp.json().get("items", []) or []):
            items.append(
                ContentItem(
                    id=self._generate_id("github", "trending", str(repo["id"])),
                    source_type="github",
                    title=repo['full_name'],
                    url=repo["html_url"],
                    content=repo.get('description', '') or '',
                    author=repo["owner"]["login"],
                    published_at=datetime.fromisoformat(
                        repo["created_at"].replace("Z", "+00:00")
                    ),
                    metadata={
                        "repo": repo["full_name"],
                        "stars": repo.get("stargazers_count", 0),
                        "forks": repo.get("forks_count", 0),
                        "language": repo.get("language") or "",
                        "categories": src.get("categories"),
                    },
                )
            )
        return items
