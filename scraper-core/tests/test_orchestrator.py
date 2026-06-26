"""Smoke test: verify orchestrator lifecycle with a synthetic plugin."""

import sys, tempfile, asyncio, logging
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from datetime import datetime, timezone, timedelta
from scrapers.orchestrator import ScraperOrchestrator
from scrapers.plugin import BaseScraper, ContentItem
from scrapers.storage import MemoryStorage

logging.basicConfig(level=logging.DEBUG)

SYNTH_PLUGIN = '''
from datetime import datetime, timezone
from typing import List
from scrapers.plugin import BaseScraper, ContentItem


class NewsScraper(BaseScraper):
    name = "news"
    description = "Synthetic news scraper"

    async def fetch(self, since: datetime) -> List[ContentItem]:
        return [
            ContentItem(
                id=self._generate_id("news", "top", "1"),
                source_type="news",
                title="Story 1",
                url="https://example.com/1",
                published_at=datetime.now(timezone.utc),
            ),
            ContentItem(
                id=self._generate_id("news", "top", "2"),
                source_type="news",
                title="Story 2",
                url="https://example.com/2",
                published_at=datetime.now(timezone.utc),
            ),
        ]


class DupScraper(BaseScraper):
    name = "dup"
    description = "Returns the same URL — should be deduped"

    async def fetch(self, since: datetime) -> List[ContentItem]:
        return [
            ContentItem(
                id=self._generate_id("dup", "top", "1"),
                source_type="dup",
                title="Dup 1",
                url="https://example.com/1",     # same as NewsScraper → deduped
                published_at=datetime.now(timezone.utc),
            ),
            ContentItem(
                id=self._generate_id("dup", "top", "2"),
                source_type="dup",
                title="Dup 3",                   # truly unique URL
                url="https://example.com/3",
                published_at=datetime.now(timezone.utc),
            ),
        ]
'''

async def main():
    with tempfile.TemporaryDirectory() as tmpdir:
        d = Path(tmpdir)
        (d / "news.py").write_text(SYNTH_PLUGIN)

        storage = MemoryStorage()
        orch = ScraperOrchestrator(
            scan_dir=str(d),
            storage=storage,
        )

        since = datetime.now(timezone.utc) - timedelta(days=1)
        items = await orch.run(since)

        # DupScraper returns 2 items (1 dup of NewsScraper later), NewsScraper returns 2 (1 deduped)
        # → 3 unique across both plugins (1 duplicate dropped)
        assert len(items) == 3, f"Expected 3 (1 deduped), got {len(items)}"
        titles = {i.title for i in items}
        # DupScraper (processed 1st, alpha order) returns Dup 1 + Dup 3
        # NewsScraper (2nd) returns Story 1 (dup url) + Story 2 (new)
        # → dup drops Story 1, keeps Story 2 → total 3
        assert "Dup 1" in titles
        assert "Dup 3" in titles
        assert "Story 2" in titles
        print(f"✔ Orchestrator: {len(items)} items (Story 1 deduped against Dup 1)")
        print(f"   Titles: {sorted(titles)}")

        # Verify cross-run state was persisted
        seen = await storage.load_seen_urls()
        assert "example.com/1" in seen
        assert "example.com/2" in seen
        print(f"✔ Dedup state persisted: {len(seen)} URLs")

        # Second run with same since — should produce 0 new items
        items2 = await orch.run(since)
        assert len(items2) == 0, f"Expected 0 (all seen), got {len(items2)}"
        print("✔ Second run yields 0 new items (cross-run dedup)")

    print("\n✔ All orchestrator tests passed")

asyncio.run(main())
