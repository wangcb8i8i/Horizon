"""AI-powered topic curation — groups items into themes and selects top picks."""

import json
import logging
import re
import sys
from datetime import timezone
from typing import List

from ..models import ContentItem, CuratedTopic, CurationResult
from .client import AIClient
from .prompts import (
    CURATION_SYSTEM,
    CURATION_USER,
    CURATION_SEARCH_SYSTEM,
    CURATION_SEARCH_USER,
    CURATION_GUIDE_SYSTEM,
    CURATION_GUIDE_USER,
)
from .utils import clean_item_text, parse_json_response

logger = logging.getLogger(__name__)

_MIN_CURATION_SCORE = 5.0


class TopicCurator:
    """Identify the most curator-worthy topics from a batch of items."""

    def __init__(self, client: AIClient):
        self.client = client

    async def curate(self, items: List[ContentItem]) -> CurationResult:
        """Analyze items and return 0-2 curated topics.

        Topics with curation_score < 5 are filtered out.
        Items whose cleaned content is too short (noise) are skipped silently.
        """
        if not items:
            return CurationResult(date=_now_str(), total_items=0, topics=[])

        items_summary = []
        for item in items:
            cleaned = clean_item_text(item.content, 600)
            if not cleaned:
                continue
            items_summary.append(
                {
                    "id": item.id,
                    "title": item.title,
                    "summary": cleaned,
                    "source": item.source_type.value,
                    "url": str(item.url),
                }
            )

        try:
            response = await self.client.complete(
                system=CURATION_SYSTEM,
                user=CURATION_USER.format(
                    count=len(items_summary),
                    items=json.dumps(items_summary, ensure_ascii=False, indent=2),
                ),
            )
        except Exception as exc:
            logger.warning(f"Curation AI call failed: {exc}")
            return CurationResult(date=_now_str(), total_items=len(items), topics=[])

        parsed = parse_json_response(response)
        if not parsed or "topics" not in parsed:
            logger.warning("Curation AI response missing 'topics' key")
            return CurationResult(date=_now_str(), total_items=len(items), topics=[])

        known_ids = {item.id for item in items}
        topics = []

        for t in parsed.get("topics", []):
            score = float(t.get("curation_score", 0))
            if score < _MIN_CURATION_SCORE:
                continue

            valid_ids = [i for i in t.get("item_ids", []) if i in known_ids]
            if not valid_ids:
                continue

            top_pick = t.get("top_pick_id")
            if top_pick and top_pick not in known_ids:
                top_pick = None

            topics.append(
                CuratedTopic(
                    name=t.get("name", "Untitled Topic"),
                    relevance=t.get("relevance", ""),
                    curation_score=score,
                    item_ids=valid_ids,
                    top_pick_id=top_pick,
                )
            )

        return CurationResult(
            date=_now_str(),
            total_items=len(items),
            topics=topics[:2],
        )

    async def generate_search_queries(
        self, topic: CuratedTopic, items: List[ContentItem]
    ) -> List[str]:
        """Generate targeted search queries using full article content."""
        articles = []
        for item in items:
            cleaned = clean_item_text(item.content, 800)
            if not cleaned:
                cleaned = item.title
            articles.append(
                {
                    "title": item.title,
                    "url": str(item.url),
                    "content": cleaned,
                }
            )

        try:
            response = await self.client.complete(
                system=CURATION_SEARCH_SYSTEM,
                user=CURATION_SEARCH_USER.format(
                    topic_name=topic.name,
                    topic_relevance=topic.relevance,
                    source_articles=json.dumps(articles, ensure_ascii=False, indent=2),
                ),
            )
        except Exception as exc:
            logger.warning(f"Search query generation failed: {exc}")
            return []

        parsed = parse_json_response(response)
        if not parsed or "search_queries" not in parsed:
            logger.warning("Search query AI response missing 'search_queries'")
            return []

        queries = parsed["search_queries"][:5]
        return [q for q in queries if isinstance(q, str) and q.strip()]

    async def generate_curation_guide(
        self,
        topic: CuratedTopic,
        items: List[ContentItem],
        web_results: List[dict],
    ) -> str:
        """Write a complete curation direction guide in Markdown."""
        source_lines = []
        for item in items:
            cleaned = clean_item_text(item.content, 500)
            if not cleaned:
                cleaned = "(no body content)"
            source_lines.append(
                f"- [{item.title}]({item.url})\n"
                f"  Content: {cleaned}"
            )

        web_lines = []
        for wr in web_results:
            web_lines.append(
                f"- [{wr['title']}]({wr['url']})\n"
                f"  Snippet: {(wr.get('snippet') or '')[:300]}"
            )

        try:
            response = await self.client.complete(
                system=CURATION_GUIDE_SYSTEM,
                user=CURATION_GUIDE_USER.format(
                    topic_name=topic.name,
                    topic_relevance=topic.relevance,
                    source_articles="\n".join(source_lines),
                    web_results="\n".join(web_lines) or "No supplementary results.",
                ),
                temperature=0.5,
                json_mode=False,
            )
        except Exception as exc:
            logger.warning(f"Curation guide generation failed: {exc}")
            print("⚠️ Curation guide AI generation failed, using fallback.", file=sys.stderr)
            return _fallback_guide(topic)

        if not response:
            print("⚠️ Curation guide AI response empty, using fallback.", file=sys.stderr)
            return _fallback_guide(topic)
        return response


def _now_str() -> str:
    from datetime import datetime

    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _slug(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:60].rstrip("-")


def _fallback_guide(topic: CuratedTopic) -> str:
    ref = f"data/curated/.../{_slug(topic.name)}/materials/"
    materials = "\n".join(
        f"- `{tid}` — 见 {ref}"
        for tid in (topic.item_ids or [])[:10]
    )
    return f"""# 策展方向：{topic.name}

## 为什么选择这个主题

{topic.relevance}

## 素材清单

{materials if materials else f"参考 {ref} 目录中的素材文件。"}

## 编撰方向建议

<!-- 建议结构、重点内容、读者假设、注意事项 -->
"""
