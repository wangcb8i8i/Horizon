"""URL deduplication — per-run in-memory + optional cross-run persistent.

Usage::

    from scrapers.dedup import Deduplicator

    dedup = Deduplicator()                           # in-memory only
    dedup = Deduplicator(storage=my_storage)         # + cross-run

    for item in fetched_items:
        if dedup.is_new(item.url):
            deduped.append(item)

    await dedup.persist()   # flush cross-run state
"""

from __future__ import annotations

import logging
from typing import List, Optional, Set
from urllib.parse import urlparse

from .plugin import ContentItem
from .storage import Storage

logger = logging.getLogger(__name__)


# ── URL normalization ──────────────────────────────────────────────────────

class URLNormalizer:
    """Canonical normalization for dedup keys.

    Strategy (matches Horizon's existing behaviour)::

        scheme  →  stripped entirely (http / https map to the same key)
        www     →  stripped from host
        path    →  trailing slash stripped
        query   →  kept as-is
        fragment → stripped
    """

    @staticmethod
    def normalize(raw_url: str) -> str:
        """Reduce a URL to its canonical dedup key."""
        parsed = urlparse(raw_url)

        # Normalise host
        host = (parsed.hostname or "").lower()
        if host.startswith("www."):
            host = host[4:]

        # Normalise path
        path = parsed.path.rstrip("/") or "/"

        # Keep query (many sites use ?id=xxx as the canonical form)
        query = f"?{parsed.query}" if parsed.query else ""

        return f"{host}{path}{query}"


# ── Deduplicator ───────────────────────────────────────────────────────────

class Deduplicator:
    """Deduplicate ContentItems by normalized URL.

    Two layers:

    * **In-memory** (always on): prevents the same URL from being
      returned by multiple plugins in the same run.
    * **Cross-run** (opt-in via *storage*): loads previously-seen URLs
      from a :class:`Storage` backend and skips them in the current run.
      Call :meth:`persist` at the end of the run to commit new URLs.

    Cross-run dedup is **off by default** — the primary time-filtering
    mechanism is the ``since`` parameter passed to plugins.
    """

    def __init__(
        self,
        storage: Optional[Storage] = None,
        normalizer: Optional[URLNormalizer] = None,
    ) -> None:
        """Initialize the deduplicator.

        Args:
            storage: Optional backend for cross-run dedup state.
            normalizer: URL normalizer (defaults to ``URLNormalizer()``).
        """
        self._storage = storage
        self._normalizer = normalizer or URLNormalizer()
        # Seen this run (always on)
        self._seen_in_run: Set[str] = set()
        # Seen in previous runs (loaded from storage, never modified in-place)
        self._seen_persistent: Set[str] = set()

    async def load(self) -> None:
        """Load persistent seen URLs (call once before a run)."""
        if self._storage:
            self._seen_persistent = await self._storage.load_seen_urls()
            logger.debug(
                "Loaded %d seen URLs from storage", len(self._seen_persistent)
            )
        else:
            self._seen_persistent = set()

    def reset_run_state(self) -> None:
        """Clear per-run seen set (call before each new run)."""
        self._seen_in_run.clear()

    def is_new(self, url: str) -> bool:
        """Check whether *url* has been seen before.

        If new, it is immediately recorded as seen in the current run.

        Returns:
            True if the URL has NOT been seen (in-memory or persistent).
        """
        key = self._normalizer.normalize(url)
        if key in self._seen_in_run:
            return False
        if key in self._seen_persistent:
            return False
        self._seen_in_run.add(key)
        return True

    def filter(self, items: List[ContentItem]) -> List[ContentItem]:
        """Return only items whose normalized URL has not been seen."""
        return [item for item in items if self.is_new(item.url)]

    async def persist(self) -> None:
        """Merge this run's seen URLs into persistent storage.

        Safe to call multiple times (idempotent — only new-in-run URLs
        are added to the persistent set).
        """
        if not self._storage or not self._seen_in_run:
            return
        merged = self._seen_persistent | self._seen_in_run
        await self._storage.save_seen_urls(merged)
        logger.debug("Persisted %d seen URLs (+%d new)", len(merged), len(self._seen_in_run))
