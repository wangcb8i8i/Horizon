"""Orchestrator — plugin lifecycle and concurrent execution.

Usage::

    from scrapers.orchestrator import ScraperOrchestrator
    from scrapers.storage import MemoryStorage

    orch = ScraperOrchestrator(
        scan_dir="horizon/scrapers",
        config={"framework": {"timeout": 15}},
    )
    items = await orch.run(since=datetime(...))
"""

from __future__ import annotations

import asyncio
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Coroutine, Dict, List, Optional

import httpx

from .dedup import Deduplicator
from .discovery import ScraperScanner
from .plugin import BaseScraper, ContentItem, ScraperConfig
from .storage import Storage

logger = logging.getLogger(__name__)

# Hook type aliases
OnItemHook = Callable[[str, ContentItem], Coroutine[Any, Any, None]]
OnErrorHook = Callable[[str, str, Exception], Coroutine[Any, Any, None]]
OnStartHook = Callable[[str], Coroutine[Any, Any, None]]
OnCompleteHook = Callable[[str, int], Coroutine[Any, Any, None]]


class ScraperOrchestrator:
    """Orchestrate scraper plugins: discover → setup → fetch → dedup → teardown."""

    def __init__(
        self,
        scan_dir: str | Path = "scrapers",
        config: Optional[Dict[str, Any]] = None,
        storage: Optional[Storage] = None,
        *,
        on_item: Optional[OnItemHook] = None,
        on_plugin_start: Optional[OnStartHook] = None,
        on_error: Optional[OnErrorHook] = None,
        on_complete: Optional[OnCompleteHook] = None,
    ) -> None:
        self.scan_dir = Path(scan_dir)
        self.config = config or {}
        self.storage = storage
        self._on_item = on_item
        self._on_plugin_start = on_plugin_start
        self._on_error = on_error
        self._on_complete = on_complete

        self._client: Optional[httpx.AsyncClient] = None
        self._plugins: List[BaseScraper] = []
        self._dedup: Deduplicator = Deduplicator(storage=storage)

    # ── public API ──────────────────────────────────────────────────────

    async def run(
        self,
        since: datetime,
        *,
        plugins: Optional[List[tuple[type[BaseScraper], Dict[str, Any]]]] = None,
    ) -> List[ContentItem]:
        """Execute one full scraping lifecycle.

        Args:
            since: Passed to each plugin's ``fetch(since)``.
            plugins: Optional pre-filtered list of ``(plugin_class, plugin_config)``
                tuples.  When provided, ``scan_dir``-based discovery is skipped
                and these plugins are used directly.  This lets callers (e.g. CLI)
                apply their own filtering (enabled, --source, --category) without
                the orchestrator knowing about config semantics.

        Returns:
            URL-deduplicated list of ``ContentItem``\\ s.
        """
        if plugins is None:
            discovered = await self._discover_plugins()
            # Build (cls, {}) tuples for the internal loop — config is resolved
            # per plugin from self.config in the original code.
            plugins = [(cls, {}) for cls in discovered]
        if not plugins:
            logger.warning("No plugins discovered under %s", self.scan_dir)
            return []

        self._dedup.reset_run_state()
        framework_cfg = ScraperConfig(**self.config.get("framework", {}))
        client = self._build_client(framework_cfg)

        all_items: List[ContentItem] = []

        try:
            await self._dedup.load()

            # Plugin lifecycle: setup → fetch → teardown
            for plugin_cls, plugin_cfg in plugins:
                # Only resolve from self.config when caller didn't provide config
                if not plugin_cfg:
                    plugin_cfg = self.config.get("plugins", {}).get(plugin_cls.name, {})

                if self._on_plugin_start:
                    await self._on_plugin_start(plugin_cls.name)

                inst = plugin_cls(plugin_cfg, client, framework_cfg)
                # Wire up non-fatal error reporting
                inst._on_error_cb = self._on_error

                try:
                    await inst.setup()
                except Exception as exc:
                    logger.warning("%s.setup() failed: %s", inst.name, exc)
                    continue

                fetch_ok = True
                try:
                    raw_items = await inst.fetch(since)
                except Exception as exc:
                    logger.error("%s.fetch() failed: %s", inst.name, exc)
                    if self._on_error:
                        await self._on_error(inst.name, "fetch", exc)
                    raw_items = []
                    fetch_ok = False
                finally:
                    try:
                        await inst.teardown()
                    except Exception as exc:
                        logger.warning("%s.teardown() failed: %s", inst.name, exc)

                # Dedup
                filtered = self._dedup.filter(raw_items)
                for item in filtered:
                    if self._on_item:
                        await self._on_item(inst.name, item)
                all_items.extend(filtered)

                if self._on_complete and fetch_ok:
                    await self._on_complete(inst.name, len(filtered))

        finally:
            await client.aclose()
            await self._dedup.persist()

        return all_items

    # ── internals ───────────────────────────────────────────────────────

    async def _discover_plugins(self) -> List[type[BaseScraper]]:
        scanner = ScraperScanner(self.scan_dir)
        infos = scanner.scan(recursive=True, register=False)
        # Return raw class objects (instantiation happens in run())
        return [info.cls for info in infos]

    @staticmethod
    def _build_client(cfg: ScraperConfig) -> httpx.AsyncClient:
        limits = httpx.Limits(
            max_connections=cfg.max_connections,
            max_keepalive_connections=cfg.max_connections,
        )
        return httpx.AsyncClient(
            timeout=cfg.timeout,
            limits=limits,
            proxy=cfg.proxy,
            headers=cfg.extra_headers or None,
        )
