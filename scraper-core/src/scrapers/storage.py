"""Storage abstraction for dedup state and item persistence.

The framework defines a minimal :class:`Storage` ABC.  Consumers can swap
the backend; a file-based :class:`JsonFileStorage` is included for local
single-user use.

Two concerns are bundled in one interface because in practice they share
the same lifecycle and durability requirements::

    Dedup state  ──  seen normalized URLs (cross-run)
    Item store   ──  persisted ContentItems
"""

from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Set

from .plugin import ContentItem

logger = logging.getLogger(__name__)


# ── Abstract interface ─────────────────────────────────────────────────────

class Storage(ABC):
    """Storage backend for the scraper framework.

    Two responsibilities:

    * **Dedup state** — track which normalized URLs have been seen
      across runs so the framework can skip them in the next run.
    * **Item persistence** — store fetched :class:`ContentItem`\\ s
      and load them later by time range.
    """

    # -- dedup state -----------------------------------------------------

    @abstractmethod
    async def load_seen_urls(self) -> Set[str]:
        """Load the set of previously-seen normalized URLs."""
        ...

    @abstractmethod
    async def save_seen_urls(self, urls: Set[str]) -> None:
        """Replace the seen-URL set (call once at end of run)."""
        ...

    # -- item persistence -------------------------------------------------

    @abstractmethod
    async def save_items(self, items: List[ContentItem]) -> None:
        """Persist fetched items (append-style)."""
        ...

    @abstractmethod
    async def load_items(self, since: datetime) -> List[ContentItem]:
        """Load items whose ``published_at`` is after *since*."""
        ...


# ── In-memory (for testing / single-run only) ──────────────────────────────

class MemoryStorage(Storage):
    """In-memory storage — state is lost when the process exits.

    Useful for testing and for consumers that don't need cross-run
    dedup or persistence.
    """

    def __init__(self) -> None:
        self._seen_urls: Set[str] = set()
        self._items: List[ContentItem] = []

    async def load_seen_urls(self) -> Set[str]:
        return set(self._seen_urls)

    async def save_seen_urls(self, urls: Set[str]) -> None:
        self._seen_urls = set(urls)

    async def save_items(self, items: List[ContentItem]) -> None:
        self._items.extend(items)

    async def load_items(self, since: datetime) -> List[ContentItem]:
        return [i for i in self._items if i.published_at > since]


# ── JSON file (local single-user) ──────────────────────────────────────────

def _default_json_dir() -> Path:
    """Return ``<cwd>/.scrapers/``."""
    return Path.cwd() / ".scrapers"


class JsonFileStorage(Storage):
    """File-based storage backed by JSON files under *data_dir*.

    Layout::

        {data_dir}/
          seen_urls.json       -- JSON array of normalized URL strings
          items.jsonl          -- JSON Lines, one ContentItem per line

    *seen_urls.json* is fully rewritten at the end of each run (the set is
    expected to fit in memory — typically tens of thousands of URLs at most
    for a personal news aggregator).

    *items.jsonl* is append-only.  New items are appended as lines; the
    file is never compacted by this class (consumers may rotate externally).
    """

    def __init__(self, data_dir: str | Path | None = None) -> None:
        self.data_dir = Path(data_dir) if data_dir else _default_json_dir()
        self._seen_path = self.data_dir / "seen_urls.json"
        self._items_path = self.data_dir / "items.jsonl"
        self._ensure_dir()

    # -- dedup state -----------------------------------------------------

    async def load_seen_urls(self) -> Set[str]:
        if not self._seen_path.exists():
            return set()
        try:
            raw = self._seen_path.read_text(encoding="utf-8")
            return set(json.loads(raw))
        except Exception:
            logger.warning("Failed to read %s, starting fresh", self._seen_path)
            return set()

    async def save_seen_urls(self, urls: Set[str]) -> None:
        raw = json.dumps(sorted(urls), ensure_ascii=False)
        self._seen_path.write_text(raw, encoding="utf-8")

    # -- item persistence -------------------------------------------------

    async def save_items(self, items: List[ContentItem]) -> None:
        lines = "\n".join(
            item.model_dump_json(exclude_none=True) for item in items
        )
        if not lines:
            return
        with open(self._items_path, "a", encoding="utf-8") as f:
            f.write(lines + "\n")

    async def load_items(self, since: datetime) -> List[ContentItem]:
        if not self._items_path.exists():
            return []
        items: List[ContentItem] = []
        with open(self._items_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = ContentItem.model_validate_json(line)
                except Exception:
                    logger.warning("Skipping unparseable line in %s", self._items_path)
                    continue
                if item.published_at > since:
                    items.append(item)
        return items

    # -- helpers ----------------------------------------------------------

    def _ensure_dir(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
