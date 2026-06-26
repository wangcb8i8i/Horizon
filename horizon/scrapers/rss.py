"""RSS/Atom feed scraper — framework plugin."""

import hashlib
import logging
import os
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import List

import feedparser
import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)


class RSSScraper(BaseScraper):
    name = "rss"
    description = "RSS/Atom feeds"

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.feeds = [
            RSSFeed(**f) for f in plugin_config.get("feeds", [])
            if f.get("enabled", True)
        ]

    async def fetch(self, since: datetime) -> List[ContentItem]:
        items: List[ContentItem] = []
        for feed in self.feeds:
            items.extend(await self._fetch_feed(feed, since))
        return items

    async def _fetch_feed(self, feed: "RSSFeed", since: datetime) -> List[ContentItem]:
        items = []
        try:
            url = re.sub(
                r"\$\{(\w+)\}",
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                feed.url,
            )
            response = await self.client.get(url, follow_redirects=True)
            response.raise_for_status()
            parsed = feedparser.parse(response.text)
        except Exception as e:
            logger.warning("Error fetching RSS feed '%s': %s", feed.name, e)
            return []

        for entry in parsed.entries:
            published_at = self._parse_date(entry)
            if not published_at or published_at < since:
                continue

            feed_id = str(feed.url).split("//")[1].replace("/", "_")
            entry_id = entry.get("id", entry.get("link", ""))
            entry_hash = hashlib.sha256(entry_id.encode()).hexdigest()[:16]
            content = self._extract_content(entry)

            items.append(
                ContentItem(
                    id=self._generate_id("rss", feed_id, entry_hash),
                    source_type="rss",
                    title=entry.get("title", "Untitled"),
                    url=entry.get("link", feed.url),
                    content=content,
                    author=entry.get("author", feed.name),
                    published_at=published_at,
                    metadata={
                        "feed_name": feed.name,
                        "category": feed.category,
                        "tags": [t.term for t in entry.get("tags", [])],
                    },
                )
            )
        return items

    @staticmethod
    def _parse_date(entry: dict) -> datetime | None:
        for field in ("published", "updated", "created"):
            if field in entry:
                try:
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        import calendar
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]), tz=timezone.utc
                        )
                    return parsedate_to_datetime(entry[field])
                except Exception:
                    continue
        return None

    @staticmethod
    def _extract_content(entry: dict) -> str:
        if "summary" in entry:
            return entry.summary
        if "description" in entry:
            return entry.description
        if entry.get("content"):
            return entry.content[0].get("value", "")
        return ""


from dataclasses import dataclass


@dataclass
class RSSFeed:
    url: str
    name: str = ""
    category: str | None = None
    enabled: bool = True
