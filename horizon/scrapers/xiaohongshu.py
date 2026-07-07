"""Xiaohongshu (小红书) scraper — framework plugin.

Uses Jina Reader (r.jina.ai) to fetch explore page content as a feed.
Jina Reader handles the SSR rendering and returns structured Markdown,
bypassing Xiaohongshu's client-side rendering requirements.

Inspired by Agent Reach's xiaohongshu channel (Jina Reader fallback tier).
"""

import logging
import re
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)

_JINA_BASE = "https://r.jina.ai"
_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
_EXPLORE_URL = "https://www.xiaohongshu.com/explore"


class XiaohongshuScraper(BaseScraper):
    name = "xiaohongshu"
    description = "Xiaohongshu trending notes"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.enabled = plugin_config.get("enabled", True)
        self.fetch_limit = min(plugin_config.get("fetch_limit", 20), 50)
        self.keywords = plugin_config.get("keywords", [])
        # Disable when profile categories don't overlap with plugin categories
        categories = plugin_config.get("_filter_categories")
        if categories is not None:
            plugin_cats = plugin_config.get("categories", [])
            plugin_cats_set = {c.strip().lower() for c in plugin_cats if c and c.strip()}
            if not plugin_cats_set or not plugin_cats_set.intersection(categories):
                self.enabled = False

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.enabled:
            return []

        items = await self._fetch_explore(since)
        return items

    async def _fetch_explore(self, since: datetime) -> List[ContentItem]:
        """Fetch Xiaohongshu explore page via Jina Reader.

        Jina Reader renders the page server-side and returns Markdown with
        note titles and URLs. Individual note content requires login, so
        we treat the explore page as a feed of note previews.
        """
        jina_url = f"{_JINA_BASE}/{_EXPLORE_URL}"
        headers = {
            "Accept": "text/plain",
            "User-Agent": _UA,
        }

        try:
            resp = await self.client.get(jina_url, headers=headers, follow_redirects=True, timeout=30.0)
            resp.raise_for_status()
        except Exception as e:
            self._report_error("explore", e)
            return []

        text = resp.text

        # Jina returns Markdown with links like:
        # [Title](https://www.xiaohongshu.com/explore/note_id)
        pattern = re.compile(
            r"\[([^\]]+)\]\(https://www\.xiaohongshu\.com/explore/([a-zA-Z0-9]+)\)"
        )
        matches = pattern.findall(text)

        # Also try discovery/item URL format
        pattern2 = re.compile(
            r"\[([^\]]+)\]\(https://www\.xiaohongshu\.com/discovery/item/([a-zA-Z0-9]+)\)"
        )
        matches2 = pattern2.findall(text)

        all_matches = list(matches) + list(matches2)

        if not all_matches:
            logger.warning("No notes found in Xiaohongshu explore page")
            return []

        items = []
        seen: set = set()
        now = datetime.now(timezone.utc)

        for title, note_id in all_matches[:self.fetch_limit]:
            if not note_id or note_id in seen:
                continue
            seen.add(note_id)

            # Clean title: remove emoji-only titles
            clean_title = title.strip()
            if not clean_title:
                continue

            url = f"https://www.xiaohongshu.com/explore/{note_id}"

            items.append(
                ContentItem(
                    id=self._generate_id("xiaohongshu", "explore", note_id),
                    source_type="xiaohongshu",
                    title=clean_title[:100],
                    url=url,
                    content=None,
                    author="xiaohongshu",
                    published_at=now,
                    metadata={
                        "note_id": note_id,
                        "source": "explore",
                    },
                )
            )

        return items
