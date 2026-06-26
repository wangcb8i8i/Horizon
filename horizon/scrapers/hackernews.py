"""Hacker News scraper — framework plugin."""

import asyncio
import logging
import re
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)

TOP_COMMENTS_LIMIT = 5


class HackerNewsScraper(BaseScraper):
    name = "hackernews"
    description = "Hacker News top stories with comments"

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.base_url = "https://hacker-news.firebaseio.com/v0"
        self.enabled = plugin_config.get("enabled", True)
        self.fetch_top_stories = plugin_config.get("fetch_top_stories", 30)
        self.min_score = plugin_config.get("min_score", 100)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.enabled:
            return []
        try:
            response = await self.client.get(f"{self.base_url}/topstories.json")
            response.raise_for_status()
            story_ids = response.json()[: self.fetch_top_stories]
            stories = await asyncio.gather(
                *[self._fetch_story(sid) for sid in story_ids],
                return_exceptions=True,
            )
        except httpx.HTTPError as e:
            logger.warning("Error fetching HN stories: %s", e)
            return []

        comment_tasks = []
        valid = []
        for s in stories:
            if isinstance(s, Exception) or s is None:
                continue
            if s.get("score", 0) < self.min_score:
                continue
            published_at = datetime.fromtimestamp(s["time"], tz=timezone.utc)
            if published_at < since:
                continue
            valid.append(s)
            comment_tasks.append(
                asyncio.gather(
                    *[self._fetch_story(cid) for cid in s.get("kids", [])[:TOP_COMMENTS_LIMIT]],
                    return_exceptions=True,
                )
            )

        items = []
        for story, comments in zip(
            valid,
            await asyncio.gather(*comment_tasks, return_exceptions=True),
        ):
            if isinstance(comments, Exception):
                comments = []
            item = self._parse_story(story, comments)
            if item:
                items.append(item)
        return items

    async def _fetch_story(self, story_id: int) -> Optional[dict]:
        try:
            resp = await self.client.get(f"{self.base_url}/item/{story_id}.json")
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPError:
            return None

    def _parse_story(self, story: dict, comments: list) -> ContentItem:
        story_id = story["id"]
        title = story.get("title", "")
        url = story.get("url", f"https://news.ycombinator.com/item?id={story_id}")
        author = story.get("by", "unknown")
        published_at = datetime.fromtimestamp(story["time"], tz=timezone.utc)
        parts = []
        if story.get("text"):
            parts.append(story["text"])
        if comments:
            parts.append("\n--- Top Comments ---")
            for c in comments:
                if not isinstance(c, dict) or not c.get("text") or c.get("deleted") or c.get("dead"):
                    continue
                commenter = c.get("by", "anon")
                text = re.sub(r"<[^>]+>", " ", c["text"]).strip()[:497]
                parts.append(f"[{commenter}]: {text}")

        return ContentItem(
            id=self._generate_id("hackernews", "story", str(story_id)),
            source_type="hackernews",
            title=title,
            url=url,
            content="\n\n".join(parts),
            author=author,
            published_at=published_at,
            metadata={
                "score": story.get("score", 0),
                "descendants": story.get("descendants", 0),
                "discussion_url": f"https://news.ycombinator.com/item?id={story_id}",
            },
        )
