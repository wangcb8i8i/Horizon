"""Reddit scraper — framework plugin."""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Any, List, Optional

import httpx

from scrapers.plugin import BaseScraper, ContentItem
from scrapers.text_utils import clean_html

logger = logging.getLogger(__name__)

REDDIT_BASE = "https://www.reddit.com"
REDDIT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "application/json,text/plain,*/*",
}
MAX_COMMENT_CONCURRENCY = 2


class RedditScraper(BaseScraper):
    name = "reddit"
    description = "Reddit posts and comments"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.enabled = plugin_config.get("enabled", True)
        self.fetch_comments = plugin_config.get("fetch_comments", 5)
        self._comment_sem = asyncio.Semaphore(MAX_COMMENT_CONCURRENCY)

        categories = plugin_config.get("_filter_categories")

        raw_subreddits = plugin_config.get("subreddits", [])
        if categories is not None:
            raw_subreddits = [
                s for s in raw_subreddits
                if self._matches_categories(s, categories)
            ]
        self.subreddits = raw_subreddits

        # Users don't carry categories — excluded when filtering by category
        self.users = plugin_config.get("users", [])
        if categories is not None:
            self.users = []

    @staticmethod
    def _matches_categories(item: dict, categories: set[str]) -> bool:
        raw = item.get("categories") or item.get("category")
        if not raw:
            return False
        if isinstance(raw, str):
            item_cats = {raw.strip().lower()}
        elif isinstance(raw, list):
            item_cats = {c.strip().lower() for c in raw if c and c.strip()}
        else:
            return False
        return bool(item_cats & categories)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.enabled:
            return []
        tasks = []
        for sub in self.subreddits:
            if sub.get("enabled", True):
                tasks.append(self._fetch_subreddit(sub, since))
        for user in self.users:
            if user.get("enabled", True):
                tasks.append(self._fetch_user(user, since))
        if not tasks:
            return []
        results = await asyncio.gather(*tasks, return_exceptions=True)
        items = []
        for r in results:
            if isinstance(r, Exception):
                self._report_error("fetch", r)
            elif isinstance(r, list):
                items.extend(r)
        return items

    async def _fetch_subreddit(self, cfg: dict, since: datetime) -> List[ContentItem]:
        sort = cfg.get("sort", "hot")
        params: dict = {"limit": min(cfg.get("fetch_limit", 25), 100), "raw_json": 1}
        if sort in ("top", "controversial"):
            params["t"] = cfg.get("time_filter", "day")
        data = await self._get(f"{REDDIT_BASE}/r/{cfg['subreddit']}/{sort}.json", params)
        if not data:
            return []
        posts = [c["data"] for c in data.get("data", {}).get("children", []) if c.get("kind") == "t3"]
        return await self._process_posts(posts, since, "subreddit", cfg["subreddit"], cfg.get("min_score", 10), cfg.get("categories"))

    async def _fetch_user(self, cfg: dict, since: datetime) -> List[ContentItem]:
        params = {"limit": min(cfg.get("fetch_limit", 10), 100), "sort": cfg.get("sort", "new"), "raw_json": 1}
        data = await self._get(f"{REDDIT_BASE}/user/{cfg['username']}/submitted.json", params)
        if not data:
            return []
        posts = [c["data"] for c in data.get("data", {}).get("children", []) if c.get("kind") == "t3"]
        return await self._process_posts(posts, since, "user", cfg["username"], 0, None)

    async def _process_posts(self, posts: list, since: datetime, subtype: str, source_name: str, min_score: int, categories: list | None = None) -> List[ContentItem]:
        valid = []
        comment_tasks = []
        for p in posts:
            created = datetime.fromtimestamp(p.get("created_utc", 0), tz=timezone.utc)
            if created < since or p.get("score", 0) < min_score:
                continue
            valid.append(p)
            if self.fetch_comments > 0:
                comment_tasks.append(self._fetch_comments(p.get("subreddit", ""), p["id"]))
            else:
                comment_tasks.append(self._empty())
        all_comments = await asyncio.gather(*comment_tasks, return_exceptions=True)
        items = []
        for p, comments in zip(valid, all_comments):
            c = comments if not isinstance(comments, Exception) else []
            item = self._parse_post(p, c, subtype, categories)
            if item:
                items.append(item)
        return items

    async def _fetch_comments(self, subreddit: str, post_id: str) -> list:
        async with self._comment_sem:
            data = await self._get(
                f"{REDDIT_BASE}/r/{subreddit}/comments/{post_id}.json",
                {"limit": self.fetch_comments, "depth": 1, "sort": "top", "raw_json": 1},
            )
        if not isinstance(data, list) or len(data) < 2:
            return []
        comments = []
        for child in data[1].get("data", {}).get("children", []):
            if child.get("kind") != "t1":
                continue
            c = child["data"]
            if c.get("body") and c.get("distinguished") != "moderator":
                comments.append(c)
        comments.sort(key=lambda c: c.get("score", 0), reverse=True)
        return comments[: self.fetch_comments]

    @staticmethod
    async def _empty() -> list:
        return []

    def _parse_post(self, post: dict, comments: list, subtype: str, categories: list | None = None) -> Optional[ContentItem]:
        post_id = post["id"]
        title = post.get("title", "")
        is_self = post.get("is_self", False)
        subreddit = post.get("subreddit", "")
        discussion_url = f"https://www.reddit.com{post.get('permalink', '')}"
        url = discussion_url if is_self else post.get("url", discussion_url)
        author = post.get("author", "unknown")
        created = datetime.fromtimestamp(post.get("created_utc", 0), tz=timezone.utc)

        parts = []
        if post.get("selftext"):
            text = clean_html(post["selftext"])
            if len(text) > 1500:
                text = text[:1497] + "..."
            parts.append(text)
        if comments:
            parts.append("\n--- Top Comments ---")
            for c in comments:
                body = clean_html(c.get("body", ""))[:497].strip()
                parts.append(f"[{c.get('author', 'anon')} ({c.get('score', 0)} pts)]: {body}")

        return ContentItem(
            id=self._generate_id("reddit", subtype, post_id),
            source_type="reddit",
            title=title,
            url=url,
            content="\n\n".join(parts),
            author=author,
            published_at=created,
            metadata={
                "score": post.get("score", 0),
                "num_comments": post.get("num_comments", 0),
                "subreddit": subreddit,
                "discussion_url": discussion_url,
                "categories": categories,
            },
        )

    async def _get(self, url: str, params: dict) -> Any:
        try:
            resp = await self.client.get(url, params=params, headers=REDDIT_HEADERS, follow_redirects=True)
            if resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", 5))
                logger.warning("Reddit rate limited, retrying after %ds", retry_after)
                await asyncio.sleep(retry_after)
                resp = await self.client.get(url, params=params, headers=REDDIT_HEADERS, follow_redirects=True)
            if resp.status_code == 403 and "/comments/" in url:
                return None
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPError:
            return None
