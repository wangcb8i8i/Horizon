"""OpenBB scraper — framework plugin."""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Any, List, Optional

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)


class OpenBBScraper(BaseScraper):
    name = "openbb"
    description = "Financial news via OpenBB Platform SDK"

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.enabled = plugin_config.get("enabled", True)
        self.watchlists = plugin_config.get("watchlists", [])
        self._obb = self._try_import_obb()

    @staticmethod
    def _try_import_obb():
        try:
            from openbb import obb
            return obb
        except ImportError:
            logger.warning("OpenBB package not installed (pip install openbb)")
            return None

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self._obb or not self.enabled:
            return []
        since_utc = self._ensure_utc(since)
        items: List[ContentItem] = []
        seen: set = set()
        for wl in self.watchlists:
            if not wl.get("enabled", True) or not wl.get("symbols"):
                continue
            try:
                fetched = await self._fetch_watchlist(wl, since_utc)
            except Exception as exc:
                logger.warning("OpenBB watchlist '%s' failed: %s", wl.get("name"), exc)
                continue
            for item in fetched:
                key = str(item.url)
                if key in seen:
                    continue
                seen.add(key)
                items.append(item)
        return items

    async def _fetch_watchlist(self, wl: dict, since_utc: datetime) -> List[ContentItem]:
        symbols = ",".join(wl["symbols"])
        response = await asyncio.to_thread(
            self._obb.news.company,
            symbol=symbols,
            limit=wl.get("fetch_limit", 20),
            provider=wl.get("provider", "yfinance"),
        )
        results = getattr(response, "results", None) or []
        items = []
        for raw in results:
            item = self._raw_to_item(raw, wl, since_utc)
            if item:
                items.append(item)
        return items

    def _raw_to_item(self, raw: Any, wl: dict, since_utc: datetime) -> Optional[ContentItem]:
        url = self._coerce_url(getattr(raw, "url", None))
        if not url:
            return None
        published = self._coerce_datetime(getattr(raw, "date", None))
        if published is None or published <= since_utc:
            return None
        title = (getattr(raw, "title", None) or "").strip()
        if not title:
            return None
        body = getattr(raw, "body", None) or getattr(raw, "excerpt", None)
        author = getattr(raw, "author", None)
        native_id = f"{published.strftime('%Y%m%dT%H%M%S')}::{url}"
        return ContentItem(
            id=self._generate_id("openbb", "news", native_id),
            source_type="openbb",
            title=title,
            url=url,
            content=body,
            author=author or "",
            published_at=published,
            metadata={
                "watchlist": wl.get("name"),
                "provider": wl.get("provider"),
                "category": wl.get("category"),
            },
        )

    @staticmethod
    def _ensure_utc(dt: datetime) -> datetime:
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    @staticmethod
    def _coerce_datetime(value: Any) -> Optional[datetime]:
        if value is None:
            return None
        if isinstance(value, datetime):
            dt = value
        elif isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                return None
        else:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    @staticmethod
    def _coerce_url(value: Any) -> Optional[str]:
        return str(value).strip() if value else None
