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
from scrapers.text_utils import clean_html

logger = logging.getLogger(__name__)


class RSSScraper(BaseScraper):
    name = "rss"
    description = "RSS/Atom feeds"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        raw_feeds = plugin_config.get("feeds", [])
        categories = plugin_config.get("_filter_categories")

        feeds = []
        for f in raw_feeds:
            if not f.get("enabled", True):
                continue
            if categories is not None:
                feed_cats = self._get_categories(f)
                if not feed_cats or not feed_cats.intersection(categories):
                    continue
            feeds.append(RSSFeed(**f))
        self.feeds = feeds

    @staticmethod
    def _get_categories(feed: dict) -> set[str]:
        """Extract categories from a feed config dict."""
        raw = feed.get("categories")
        if not raw:
            return set()
        if isinstance(raw, str):
            return {raw.strip().lower()}
        if isinstance(raw, list):
            return {c.strip().lower() for c in raw if c and c.strip()}
        return set()

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
            self._report_error(f"feed '{feed.name}'", e)
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
                        "categories": list(feed.categories) if feed.categories else None,
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
        raw = ""
        if "summary" in entry:
            raw = entry.summary
        elif "description" in entry:
            raw = entry.description
        elif entry.get("content"):
            raw = entry.content[0].get("value", "")
        return clean_html(raw)


from dataclasses import dataclass


@dataclass
class RSSFeed:
    url: str
    name: str = ""
    categories: tuple[str, ...] | None = None
    enabled: bool = True
