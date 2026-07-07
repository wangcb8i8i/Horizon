"""Twitter scraper (Apify) — framework plugin."""

import asyncio
import logging
import os
from datetime import datetime, timezone
from html import unescape
from typing import List, Optional

from dateutil.parser import isoparse
import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)

_APIFY_BASE = "https://api.apify.com/v2"
_POLL_INTERVAL = 3.0
_MAX_WAIT = 180


class TwitterScraper(BaseScraper):
    name = "twitter"
    description = "Twitter/X tweets via Apify"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.cfg = plugin_config

        categories = plugin_config.get("_filter_categories")
        raw_users: list = plugin_config.get("users", []) or []

        users: list[dict] = []
        for u in raw_users:
            if isinstance(u, str):
                username = u.strip().lstrip("@")
                if username:
                    users.append({
                        "username": username,
                        "enabled": True,
                        "categories": [],
                        "fetch_limit": None,
                    })
            elif isinstance(u, dict):
                username = u.get("username", "").strip().lstrip("@")
                if username:
                    users.append({
                        "username": username,
                        "enabled": u.get("enabled", True),
                        "categories": u.get("categories", []),
                        "fetch_limit": u.get("fetch_limit"),
                    })

        if categories is not None:
            users = [u for u in users if u["enabled"] and self._matches_categories(u["categories"], categories)]

        self._users = users
        self._global_fetch_limit = min(plugin_config.get("fetch_limit", 10), 50)

    @staticmethod
    def _matches_categories(user_cats, filter_cats):
        if not user_cats:
            return False
        if isinstance(user_cats, str):
            cats_set = {user_cats.strip().lower()}
        elif isinstance(user_cats, list):
            cats_set = {c.strip().lower() for c in user_cats if c and c.strip()}
        else:
            return False
        return bool(cats_set & filter_cats)

    @property
    def _enabled(self) -> bool:
        return self.cfg.get("enabled", True)

    @property
    def _usernames(self) -> List[str]:
        return [u["username"] for u in self._users]

    @property
    def _token(self) -> Optional[str]:
        env = self.cfg.get("apify_token_env", "APIFY_TOKEN")
        return os.environ.get(env)

    @property
    def _actor_id(self) -> str:
        return self.cfg.get("actor_id", "altimis~scweet")

    @property
    def _fetch_limit(self) -> int:
        return self.cfg.get("fetch_limit", 10)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self._enabled:
            return []
        users = self._usernames
        if not users:
            return []
        token = self._token
        if not token:
            logger.warning("Apify token not found, skipping Twitter")
            return []

        run_id, dataset_id = await self._start_run(token, users)
        if not run_id:
            return []
        if not await self._wait_for_run(token, run_id):
            return []

        raw_items = await self._fetch_dataset(token, dataset_id)
        items = []
        for raw in raw_items:
            if isinstance(raw, dict) and raw.get("noResults"):
                continue
            parsed = self._parse_item(raw, since)
            if parsed:
                items.append(parsed)
        return items

    async def _start_run(self, token: str, users: List[str]) -> tuple[Optional[str], Optional[str]]:
        payload = {
            "source_mode": "profiles",
            "profile_urls": users,
            "search_sort": "Latest",
            "max_items": max(100, self._fetch_limit),
        }
        try:
            resp = await self.client.post(
                f"{_APIFY_BASE}/acts/{self._actor_id}/runs?token={token}",
                json=payload,
                timeout=30.0,
            )
            resp.raise_for_status()
            data = resp.json()["data"]
            return data["id"], data["defaultDatasetId"]
        except Exception as exc:
            logger.error("Apify run start failed: %s", exc)
            return None, None

    async def _wait_for_run(self, token: str, run_id: str) -> bool:
        url = f"{_APIFY_BASE}/actor-runs/{run_id}?token={token}"
        elapsed = 0.0
        while elapsed < _MAX_WAIT:
            try:
                resp = await self.client.get(url, timeout=10.0)
                resp.raise_for_status()
                status = resp.json()["data"]["status"]
                if status == "SUCCEEDED":
                    return True
                if status in ("FAILED", "ABORTED", "TIMED-OUT"):
                    return False
            except Exception as exc:
                self._report_error("apify_poll", exc)
            await asyncio.sleep(_POLL_INTERVAL)
            elapsed += _POLL_INTERVAL
        return False

    async def _fetch_dataset(self, token: str, dataset_id: str) -> list:
        try:
            resp = await self.client.get(
                f"{_APIFY_BASE}/datasets/{dataset_id}/items?token={token}",
                timeout=30.0,
            )
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            logger.error("Apify dataset fetch failed: %s", exc)
            return []

    async def fetch_replies_for_item(self, item: ContentItem) -> List[str]:
        if not self.cfg.get("fetch_reply_text", False):
            return []
        token = self._token
        if not token:
            return []
        conversation_id = str(item.metadata.get("conversation_id") or "")
        if not conversation_id:
            return []
        max_replies = max(self.cfg.get("max_replies_per_tweet", 3), 0)
        if max_replies == 0:
            return []
        payload = {
            "source_mode": "search",
            "search_query": f"conversation_id:{conversation_id}",
            "search_sort": "Latest",
            "max_items": max(100, max_replies * 5),
        }
        try:
            resp = await self.client.post(
                f"{_APIFY_BASE}/acts/{self._actor_id}/runs?token={token}",
                json=payload, timeout=30.0,
            )
            resp.raise_for_status()
            data = resp.json()["data"]
        except Exception as exc:
            return []
        if not await self._wait_for_run(token, data["id"]):
            return []
        rows = await self._fetch_dataset(token, data["defaultDatasetId"])
        return self._extract_reply_lines(item, rows, max_replies)

    def _extract_reply_lines(self, item: ContentItem, rows: list, max_replies: int) -> List[str]:
        min_likes = max(self.cfg.get("reply_min_likes", 0), 0)
        tweet_id = str(item.metadata.get("tweet_id") or "")
        own_author = (item.author or "").lstrip("@")
        candidates = []
        for row in rows:
            if not isinstance(row, dict) or row.get("noResults"):
                continue
            row_id = str(row.get("id") or "").replace("tweet-", "")
            if tweet_id and row_id == tweet_id:
                continue
            handle = (
                (row.get("user") or {}).get("handle")
                or row.get("handle")
                or row.get("username")
                or "unknown"
            )
            if handle and own_author and handle.lower() == own_author.lower():
                continue
            text = unescape((row.get("text") or "").strip())
            if not text:
                continue
            likes = int(row.get("favorite_count") or 0)
            replies_count = int(row.get("reply_count") or 0)
            if likes < min_likes:
                continue
            score = likes * 2 + replies_count
            candidates.append((score, f"[@{handle}] {text[:280]}"))
        candidates.sort(key=lambda x: x[0], reverse=True)
        return [line for _, line in candidates[:max_replies]]

    def _parse_item(self, item: dict, since: datetime) -> Optional[ContentItem]:
        try:
            created_str = item.get("created_at")
            if not created_str:
                return None
            try:
                published_at = datetime.strptime(created_str, "%a %b %d %H:%M:%S %z %Y")
            except ValueError:
                published_at = isoparse(created_str)
            if published_at.tzinfo is None:
                published_at = published_at.replace(tzinfo=timezone.utc)
            if published_at < since:
                return None

            raw_id = str(item.get("id") or "").replace("tweet-", "")
            if not raw_id:
                return None

            screen_name = (
                (item.get("user") or {}).get("screen_name")
                or (item.get("user") or {}).get("username")
                or item.get("handle")
                or "unknown"
            )
            author = (item.get("user") or {}).get("name") or screen_name
            text = unescape((item.get("full_text") or item.get("text") or "").strip())
            if not text:
                return None

            url = item.get("url") or f"https://twitter.com/{screen_name}/status/{raw_id}"
            return ContentItem(
                id=self._generate_id("twitter", "tweet", raw_id),
                source_type="twitter",
                title=f"@{screen_name}",
                url=url,
                content=text,
                author=author,
                published_at=published_at,
                metadata={
                    "tweet_id": raw_id,
                    "conversation_id": item.get("conversation_id") or "",
                    "favorite_count": item.get("favorite_count", 0),
                    "retweet_count": item.get("retweet_count", 0),
                    "reply_count": item.get("reply_count", 0),
                },
            )
        except Exception:
            return None
