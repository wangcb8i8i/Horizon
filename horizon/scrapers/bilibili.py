"""Bilibili scraper — framework plugin.

Uses Bilibili public API (no auth required) for popular, ranking, and
search feeds. Search uses the zero-auth search/all/v2 endpoint; ranking
requires wbi signing and is deprecated in favour of search.
Inspired by Agent Reach's bilibili channel architecture.
"""

import logging
import re
from datetime import datetime, timezone
from typing import List

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)

_BILIBILI_API = "https://api.bilibili.com/x/web-interface"
_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

_RID_MAP = {
    "all": 0,
    "animation": 1,
    "music": 3,
    "game": 4,
    "entertainment": 5,
    "tech": 36,
}


class BilibiliScraper(BaseScraper):
    name = "bilibili"
    description = "Bilibili trending and tech videos"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.enabled = plugin_config.get("enabled", True)
        categories = plugin_config.get("_filter_categories")
        all_sections = plugin_config.get("sections", [])
        if categories is not None:
            all_sections = [
                s for s in all_sections
                if self._matches_categories(s, categories)
            ]
        self.sections = all_sections
        self.fetch_limit = plugin_config.get("fetch_limit", 15)

    @staticmethod
    def _matches_categories(sub: dict, categories: set[str]) -> bool:
        src_cats = sub.get("categories")
        if not src_cats:
            return False
        if isinstance(src_cats, str):
            src_cats_set = {src_cats.strip().lower()}
        elif isinstance(src_cats, list):
            src_cats_set = {c.strip().lower() for c in src_cats if c and c.strip()}
        else:
            return False
        return bool(src_cats_set & categories)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.enabled or not self.sections:
            return []

        import asyncio

        tasks = [self._fetch_section(s, since) for s in self.sections]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        items = []
        seen: set = set()
        for r in results:
            if isinstance(r, Exception):
                self._report_error("fetch_section", r)
            elif isinstance(r, list):
                for item in r:
                    if item.id not in seen:
                        seen.add(item.id)
                        items.append(item)
        return items

    async def _fetch_section(self, section: dict, since: datetime) -> List[ContentItem]:
        section_type = section.get("section", "popular")
        rid = section.get("rid", "tech")
        limit = min(section.get("fetch_limit", self.fetch_limit), 50)
        categories = section.get("categories", [])

        if section_type == "search":
            keyword = section.get("keyword", "")
            if not keyword:
                logger.warning("Bilibili search section missing 'keyword'")
                return []
            items = await self._fetch_search(keyword, since, limit, categories)
        elif section_type == "rank":
            rid_val = _RID_MAP.get(rid) if isinstance(rid, str) else int(rid)
            if rid_val is None:
                logger.warning("Unknown Bilibili rid: %s", rid)
                return []
            url = f"{_BILIBILI_API}/ranking/v2?rid={rid_val}&type=all"
            items = await self._fetch_video_list(url, since, limit, categories, f"bilibili_rank_{rid}")
            if not items:
                logger.warning(
                    "Bilibili ranking/v2 returned no items (likely -352 risk "
                    "control: wbi signature required). Use 'section: search' "
                    "with a keyword instead of 'section: rank'."
                )
        else:
            url = f"{_BILIBILI_API}/popular"
            items = await self._fetch_video_list(url, since, limit, categories, "bilibili_popular")

        return items

    async def _fetch_video_list(
        self, url: str, since: datetime, limit: int,
        categories: list, source_subtype: str,
    ) -> List[ContentItem]:
        headers = {"User-Agent": _UA, "Referer": "https://www.bilibili.com/"}
        try:
            resp = await self.client.get(url, headers=headers, follow_redirects=True, timeout=15.0)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            self._report_error(source_subtype, e)
            return []

        if data.get("code") != 0:
            logger.warning("Bilibili API error for %s: %s", source_subtype, data.get("message"))
            return []

        raw_list = data.get("data", {}).get("list", [])
        items = []
        for video in raw_list[:limit]:
            pubtime = video.get("pubdate", 0)
            if pubtime:
                published = datetime.fromtimestamp(pubtime, tz=timezone.utc)
                if published < since:
                    continue
            else:
                published = datetime.now(timezone.utc)

            bvid = video.get("bvid", "")
            title = self._clean_title(video.get("title", ""))
            desc = (video.get("desc") or "").strip()
            owner = video.get("owner", {})
            stat = video.get("stat", {})

            meta: dict = {
                "bvid": bvid,
                "owner_mid": owner.get("mid", 0),
                "view_count": stat.get("view", 0),
                "like_count": stat.get("like", 0),
                "reply_count": stat.get("reply", 0),
                "duration": video.get("duration", 0),
                "section": source_subtype,
            }
            if categories:
                meta["categories"] = categories
            items.append(
                ContentItem(
                    id=self._generate_id("bilibili", source_subtype, bvid),
                    source_type="bilibili",
                    title=title,
                    url=f"https://www.bilibili.com/video/{bvid}",
                    content=desc[:500] if desc else "",
                    author=owner.get("name", "unknown"),
                    published_at=published,
                    metadata=meta,
                )
            )
        return items

    async def _fetch_search(
        self, keyword: str, since: datetime, limit: int,
        categories: list,
    ) -> List[ContentItem]:
        """Fetch videos via Bilibili search API (zero auth, code 0).

        search/all/v2 returns result blocks grouped by result_type; we
        extract the 'video' block whose 'data' is a flat list of video
        objects with a different field schema than popular/ranking.
        """
        url = f"{_BILIBILI_API}/search/all/v2"
        params = {"keyword": keyword, "page": 1, "pagesize": min(limit, 20)}
        headers = {"User-Agent": _UA, "Referer": "https://www.bilibili.com/"}
        try:
            resp = await self.client.get(
                url, params=params, headers=headers,
                follow_redirects=True, timeout=15.0,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            self._report_error(f"search '{keyword}'", e)
            return []

        if data.get("code") != 0:
            logger.warning(
                "Bilibili search API error for '%s': %s",
                keyword, data.get("message"),
            )
            return []

        raw_list = []
        for block in data.get("data", {}).get("result", []) or []:
            if block.get("result_type") == "video":
                raw_list = block.get("data", []) or []
                break

        items = []
        now = datetime.now(timezone.utc)
        for video in raw_list[:limit]:
            pubdate = video.get("pubdate") or video.get("pubdate_ts")
            if pubdate:
                published = datetime.fromtimestamp(int(pubdate), tz=timezone.utc)
                if published < since:
                    continue
            else:
                published = now

            bvid = video.get("bvid", "")
            if not bvid:
                continue
            title = self._clean_title(video.get("title", ""))
            desc = (video.get("description") or "").strip()
            author = video.get("author", "unknown")
            play = video.get("play", 0)
            review = video.get("video_review", 0)
            favorites = video.get("favorites", 0)

            meta: dict = {
                "bvid": bvid,
                "mid": video.get("mid", 0),
                "view_count": play,
                "reply_count": review,
                "favorite_count": favorites,
                "duration": video.get("duration", 0),
                "tag": video.get("tag", ""),
                "section": "bilibili_search",
                "keyword": keyword,
            }
            if categories:
                meta["categories"] = categories
            items.append(
                ContentItem(
                    id=self._generate_id("bilibili", "search", bvid),
                    source_type="bilibili",
                    title=title,
                    url=f"https://www.bilibili.com/video/{bvid}",
                    content=desc[:500] if desc else "",
                    author=author,
                    published_at=published,
                    metadata=meta,
                )
            )
        return items

    @staticmethod
    def _clean_title(raw: str) -> str:
        return re.sub(r"<[^>]+>", "", raw).strip()
