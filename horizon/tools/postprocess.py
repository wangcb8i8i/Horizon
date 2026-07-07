"""Post-processing pipeline for scraped items — shared between CLI and web.

Always filters out items with insufficient content.  Optionally scores and
filters via LLM when AI is enabled.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from horizon.ai import KEEP_PCT, filter_items

if TYPE_CHECKING:
    from horizon.ai.processor import AIProcessor
    from scrapers.plugin import ContentItem

MIN_CONTENT_LEN = 10


async def postprocess_items(
    items: list[ContentItem],
    *,
    ai_enabled: bool = False,
    processor: AIProcessor | None = None,
    threshold: int | None = None,
) -> list[ContentItem]:
    """Filter and refine items after scraping.

    Always removes items whose ``content`` is empty, whitespace-only, or
    shorter than ``MIN_CONTENT_LEN`` (10 characters).

    When *ai_enabled* is True, also scores each item via the LLM and drops
    those below *threshold*.
    """
    items = [
        it for it in items
        if it.content and len(it.content.strip()) >= MIN_CONTENT_LEN
    ]

    if ai_enabled and processor and items:
        items = await filter_items(processor, items, threshold=threshold or KEEP_PCT)

    return items
