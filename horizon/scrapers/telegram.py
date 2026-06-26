"""Telegram scraper — framework plugin."""

import asyncio
import logging
import re
from datetime import datetime, timezone
from typing import List, Optional

import httpx
from bs4 import BeautifulSoup

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)

TELEGRAM_WEB_BASE = "https://t.me/s"
USER_AGENT = "Mozilla/5.0 (compatible; Horizon/1.0)"


class TelegramScraper(BaseScraper):
    name = "telegram"
    description = "Telegram public channels"

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.enabled = plugin_config.get("enabled", True)
        self.channels = plugin_config.get("channels", [])

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.enabled:
            return []
        tasks = []
        for ch in self.channels:
            if ch.get("enabled", True):
                tasks.append(self._fetch_channel(ch, since))
        if not tasks:
            return []
        results = await asyncio.gather(*tasks, return_exceptions=True)
        items = []
        for r in results:
            if isinstance(r, Exception):
                logger.warning("Telegram error: %s", r)
            elif isinstance(r, list):
                items.extend(r)
        return items

    async def _fetch_channel(self, cfg: dict, since: datetime) -> List[ContentItem]:
        url = f"{TELEGRAM_WEB_BASE}/{cfg['channel']}"
        headers = {"User-Agent": USER_AGENT}
        try:
            resp = await self.client.get(url, headers=headers, follow_redirects=True, timeout=120.0)
            if resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", 5))
                await asyncio.sleep(retry_after)
                resp = await self.client.get(url, headers=headers, follow_redirects=True, timeout=120.0)
            resp.raise_for_status()
        except Exception as e:
            logger.warning("Telegram request failed for %s: %s", cfg["channel"], e)
            return []
        return self._parse_html(resp.text, cfg, since)

    def _parse_html(self, html: str, cfg: dict, since: datetime) -> List[ContentItem]:
        soup = BeautifulSoup(html, "html.parser")
        messages = soup.select("div.tgme_widget_message[data-post]")[-cfg.get("fetch_limit", 20):]
        items = []
        ch = cfg["channel"]
        for msg in messages:
            data_post = msg.get("data-post", "")
            msg_id = data_post.split("/")[-1] if "/" in data_post else data_post
            if not msg_id:
                continue
            time_el = msg.select_one("time[datetime]")
            if not time_el:
                continue
            try:
                published_at = datetime.fromisoformat(time_el["datetime"].replace("Z", "+00:00"))
            except (ValueError, KeyError):
                continue
            if published_at < since:
                continue
            text_el = msg.select_one("div.tgme_widget_message_text")
            if not text_el:
                continue
            for br in text_el.find_all("br"):
                br.replace_with("\n")
            text = text_el.get_text(separator="").strip()
            if not text:
                continue

            first = text.split("\n\n")[0].replace("\n", " ").strip()
            title = first[:80]

            msg_url = f"https://t.me/{ch}/{msg_id}"
            canonical = msg_url
            for a in text_el.find_all("a", href=True):
                href = a["href"]
                if href.startswith("http") and "t.me" not in href:
                    canonical = href
                    break

            items.append(
                ContentItem(
                    id=self._generate_id("telegram", ch, msg_id),
                    source_type="telegram",
                    title=title,
                    url=canonical,
                    content=text,
                    author=ch,
                    published_at=published_at,
                    metadata={"msg_url": msg_url, "channel": ch},
                )
            )
        return items
