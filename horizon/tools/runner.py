"""Core async scraper runner — shared by CLI and web layers.

The runner orchestrates plugin discovery, category filtering, and the
scraper lifecycle.  Progress is reported through injectable
``ProgressHooks`` so that CLI (Rich Live) and web (SSE) can plug in
their own display logic.
"""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable
from datetime import datetime
from typing import TypedDict

from scrapers.orchestrator import ScraperOrchestrator
from scrapers.plugin import ContentItem
from scrapers.storage import MemoryStorage

from horizon.tools.config import DEFAULT_SCAN_DIR, discover_and_filter

logger = logging.getLogger(__name__)


# ── progress hooks ──────────────────────────────────────────────────────────


class ProgressHooks(TypedDict, total=False):
    """Injectable callbacks for scraper lifecycle events.

    All callbacks are async.  When ``ProgressHooks`` is ``None`` the
    runner runs silently (no progress reporting).
    """

    on_plugin_start: Callable[[str], Awaitable[None]]
    """Called when a plugin begins executing.  *arg* = plugin name."""

    on_plugin_complete: Callable[[str, int], Awaitable[None]]
    """Called when a plugin finishes.  *args* = (name, item_count)."""

    on_item: Callable[[str, ContentItem], Awaitable[None]]
    """Called for each ContentItem right after dedup. *args* = (plugin_name, item)."""

    on_plugin_error: Callable[[str, str], Awaitable[None]]
    """Called when a plugin errors.  *args* = (name, error_message)."""


# ── runner ──────────────────────────────────────────────────────────────────


async def run_scrapers(
    since: datetime,
    cfg: dict,
    *,
    source_names: set[str] | None = None,
    category_names: set[str] | None = None,
    hooks: ProgressHooks | None = None,
) -> list[ContentItem]:
    """Execute all enabled plugins and return deduped items.

    Parameters
    ----------
    since:
        Scrape items published after this UTC datetime.
    cfg:
        Full Horizon config dict (parsed from ``horizon.yaml``).
    source_names:
        Optional whitelist of plugin names to run (``--source``).
    category_names:
        Optional set of categories to filter by (``--profile``).
    hooks:
        Optional progress callbacks.  When ``None`` the runner is silent.
    """
    to_run = discover_and_filter(cfg, source_names)
    if not to_run:
        logger.warning("No enabled plugins found.")
        return []

    # Build the plugin list for the orchestrator, applying category filtering
    plugin_list: list[tuple[type, dict]] = []
    skipped: list[str] = []
    for info, pcfg in to_run:
        if category_names is not None and not getattr(info.cls, "has_categories", False):
            skipped.append(info.name)
            continue
        if category_names is not None and getattr(info.cls, "has_categories", False):
            pcfg = {**pcfg, "_filter_categories": category_names}
        plugin_list.append((info.cls, pcfg))

    if not plugin_list:
        logger.warning("No plugins to run (all skipped by category filter).")
        return []

    # Wire hooks into orchestrator callbacks
    on_start = hooks.get("on_plugin_start") if hooks else None
    on_complete = hooks.get("on_plugin_complete") if hooks else None
    on_error = hooks.get("on_plugin_error") if hooks else None
    on_item = hooks.get("on_item") if hooks else None

    orch = ScraperOrchestrator(
        scan_dir=str(DEFAULT_SCAN_DIR),
        config=cfg,
        storage=MemoryStorage(),
        on_item=on_item,
        on_plugin_start=on_start,
        on_complete=on_complete,
        on_error=on_error,
    )

    items = await orch.run(since, plugins=plugin_list)
    return items
