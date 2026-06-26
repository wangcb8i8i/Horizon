"""Smoke test: verify directory discovery finds and registers plugins."""

import sys
import tempfile
from pathlib import Path

# Add framework to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from scrapers.discovery import ScraperScanner
from scrapers.plugin import BaseScraper, ScraperRegistry
from datetime import datetime

# ── Write a demo scraper to a temp directory ───────────────────────────────

DEMO_SCRAPER = '''
"""Demo scraper for testing directory discovery."""
from datetime import datetime
from typing import List
from scrapers.plugin import BaseScraper, ContentItem


class HackerNewsScraper(BaseScraper):
    name = "hackernews"
    description = "Hacker News top stories"

    async def fetch(self, since: datetime) -> List[ContentItem]:
        return [
            ContentItem(
                id=self._generate_id("hn", "story", "1"),
                source_type="hackernews",
                title="Hello from discovered plugin",
                url="https://example.com",
                published_at=since,
            )
        ]
'''

# ── An abstract-only class that should NOT be registered ───────────────────
DEMO_ABSTRACT = '''
"""Abstract base — should be skipped by discovery."""
from scrapers.plugin import BaseScraper
import abc


class BaseSocialScraper(BaseScraper):
    @abc.abstractmethod
    async def fetch(self, since): ...
'''

# ── A file starting with _ — should be skipped ─────────────────────────────
DEMO_PRIVATE = '''
"""Private helpers — should be skipped by discovery."""
# no BaseScraper subclass here
'''

with tempfile.TemporaryDirectory() as tmpdir:
    d = Path(tmpdir)
    (d / "_private.py").write_text(DEMO_PRIVATE)
    (d / "base_social.py").write_text(DEMO_ABSTRACT)
    (d / "hackernews_scraper.py").write_text(DEMO_SCRAPER)

    # Scan
    scanner = ScraperScanner(str(d))
    found = scanner.scan()
    print(f"Discovered {len(found)} plugins:")
    for p in found:
        print(f"  ✔ {p.name}: {p.description}")

    assert len(found) == 1, f"Expected 1, got {len(found)}"
    assert found[0].name == "hackernews"
    assert ScraperRegistry.get("hackernews") is not None

    # Verify _private.py and base_social.py were skipped
    assert ScraperRegistry.get("basesocialscraper") is None
    print("\n✔ All assertions passed — discovery works as expected.")

    ScraperRegistry.clear()
