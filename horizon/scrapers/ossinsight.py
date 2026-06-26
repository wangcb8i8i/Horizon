"""OSS Insight scraper — framework plugin."""

import logging
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)


class OSSInsightScraper(BaseScraper):
    name = "ossinsight"
    description = "OSS Insight trending repositories"

    BASE_URL = "https://api.ossinsight.io/v1/trends/repos"

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.cfg = plugin_config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.cfg.get("enabled", False):
            return []
        items = []
        seen = set()
        keywords_lower = [kw.lower() for kw in self.cfg.get("keywords", []) if kw]
        min_stars = self.cfg.get("min_stars", 5)
        max_items = self.cfg.get("max_items", 30)
        period = self.cfg.get("period", "past_24_hours")
        languages = self.cfg.get("languages", ["All", "Python", "TypeScript"])

        for lang in languages:
            rows = await self._fetch_period(period, lang)
            for row in rows:
                repo_name = row.get("repo_name")
                repo_id = row.get("repo_id")
                if not repo_name or not repo_id:
                    continue
                if repo_id in seen:
                    continue
                if min_stars and self._stars(row) < min_stars:
                    continue
                if keywords_lower and not self._matches(row, keywords_lower):
                    continue
                seen.add(repo_id)
                item = self._row_to_item(row, lang, period)
                if item:
                    items.append(item)

        items.sort(key=lambda x: x.metadata.get("stars_gained", 0), reverse=True)
        return items[:max_items]

    async def _fetch_period(self, period: str, language: str) -> List[dict]:
        try:
            resp = await self.client.get(
                self.BASE_URL,
                params={"period": period, "language": language},
                headers={"Accept": "application/json"},
                timeout=20.0,
            )
            resp.raise_for_status()
            rows = (resp.json().get("data") or {}).get("rows") or []
            return rows
        except httpx.HTTPError:
            return []

    def _row_to_item(self, row: dict, language: str, period: str) -> Optional[ContentItem]:
        repo_name = row.get("repo_name")
        stars = self._stars(row)
        description = (row.get("description") or "").strip()
        primary_language = row.get("primary_language") or language
        content = (
            f"Trending GitHub repo: {repo_name}\n"
            f"Stars gained ({period}): {stars}\n"
            f"Forks gained: {row.get('forks', 0)}\n"
            f"Language: {primary_language}"
        )
        if description:
            content += f"\n\n{description}"

        return ContentItem(
            id=self._generate_id("ossinsight", "trending", str(row.get("repo_id"))),
            source_type="ossinsight",
            title=f"{repo_name} (+{stars}⭐ {period})",
            url=f"https://github.com/{repo_name}",
            content=content,
            author=repo_name.split("/")[0] if "/" in repo_name else None,
            published_at=datetime.now(timezone.utc),
            metadata={
                "repo": repo_name,
                "stars_gained": stars,
                "forks_gained": self._int(row.get("forks")),
                "primary_language": primary_language,
                "period": period,
            },
        )

    @staticmethod
    def _stars(row: dict) -> int:
        return OSSInsightScraper._int(row.get("stars"))

    @staticmethod
    def _int(value) -> int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return 0

    @staticmethod
    def _matches(row: dict, keywords: List[str]) -> bool:
        haystack = " ".join(
            (row.get("description") or "").lower(),
            (row.get("collection_names") or "").lower(),
            (row.get("repo_name") or "").lower(),
        )
        return any(kw in haystack for kw in keywords)
