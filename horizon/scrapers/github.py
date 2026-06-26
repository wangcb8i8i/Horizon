"""GitHub scraper — framework plugin."""

import logging
import os
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    name = "github"
    description = "GitHub user events and repo releases"

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"
        self.sources = plugin_config.get("sources", [])

    def _headers(self) -> dict:
        h = {"Accept": "application/vnd.github.v3+json", "User-Agent": "Horizon"}
        if self.token:
            h["Authorization"] = f"token {self.token}"
        return h

    async def fetch(self, since: datetime) -> List[ContentItem]:
        items = []
        for src in self.sources:
            if not src.get("enabled", True):
                continue
            if src.get("type") == "user_events" and src.get("username"):
                items.extend(await self._user_events(src["username"], since))
            elif src.get("type") == "repo_releases" and src.get("owner") and src.get("repo"):
                items.extend(await self._repo_releases(src["owner"], src["repo"], since))
        return items

    async def _user_events(self, username: str, since: datetime) -> List[ContentItem]:
        try:
            resp = await self.client.get(
                f"{self.base_url}/users/{username}/events/public",
                headers=self._headers(),
                follow_redirects=True,
            )
            resp.raise_for_status()
        except httpx.HTTPError as e:
            logger.warning("GitHub events for %s failed: %s", username, e)
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
                    metadata={"event_type": etype, "repo": repo},
                )
            )
        return items

    async def _repo_releases(self, owner: str, repo: str, since: datetime) -> List[ContentItem]:
        try:
            resp = await self.client.get(
                f"{self.base_url}/repos/{owner}/{repo}/releases",
                headers=self._headers(),
                follow_redirects=True,
            )
            resp.raise_for_status()
        except httpx.HTTPError as e:
            logger.warning("GitHub releases for %s/%s failed: %s", owner, repo, e)
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
                    },
                )
            )
        return items
