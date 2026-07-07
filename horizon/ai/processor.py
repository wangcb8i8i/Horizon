"""AI processing layer — abstract interface, prompt loading, and orchestration."""

from __future__ import annotations

import json
import logging
import os
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from scrapers.plugin import ContentItem

logger = logging.getLogger(__name__)

_HERE = Path(__file__).resolve().parent
_PROMPTS_DIR = _HERE / "prompts"

# ── Defaults ──────────────────────────────────────────────────────────────────

KEEP_PCT = 6  # default threshold (0-10 scale) when nothing else is configured


# ── Data ──────────────────────────────────────────────────────────────────────

@dataclass
class AIFilterResult:
    """Result of the AI filtering stage.

    raw_score: 0-100 score returned by the LLM.
    reason:    Optional text explanation.
    parsed:    True if JSON was successfully parsed from the LLM response.
    """

    raw_score: int = 0
    reason: str = ""
    parsed: bool = False


# ── Prompt loading ────────────────────────────────────────────────────────────

def _load_prompt(name: str, **kwargs: str) -> str:
    """Load a .prompt file and substitute template variables."""
    path = _PROMPTS_DIR / name
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.error("Prompt file not found: %s", path)
        return ""
    # Use replace rather than str.format() to avoid collisions with
    # curly braces that commonly appear in JSON schemas, code, etc.
    for key, value in kwargs.items():
        text = text.replace("{" + key + "}", value)
    return text


def _load_pair(base: str, **kwargs: str) -> tuple[str, str]:
    """Load system + user prompt pair.

    Returns (system_text, user_text). Either may be empty on error.
    """
    system = _load_prompt(f"{base}-system.prompt")
    user = _load_prompt(f"{base}-user.prompt", **kwargs)
    return system, user


def _load_scorer(name: str) -> str:
    """Load a scoring section by name.

    Loads ``prompts/scoring/{name}.prompt``.  Returns an empty string if
    the file does not exist (the user prompt will render with a blank
    scoring section, which the LLM can still work with).
    """
    path = _PROMPTS_DIR / "scoring" / f"{name}.prompt"
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.error("Scorer prompt not found: %s", path)
        return ""


# ── Abstract interface ────────────────────────────────────────────────────────

class AIProcessor(ABC):
    """Abstract interface for LLM-based content filtering and summarization."""

    @abstractmethod
    async def filter(self, item: ContentItem) -> AIFilterResult:
        """Score and decide whether an item should be kept."""
        ...

    @abstractmethod
    async def summarize(self, item: ContentItem) -> str:
        """Generate a concise summary for a kept item."""
        ...


# ── Orchestration ─────────────────────────────────────────────────────────────

def _extract_json(text: str) -> dict | None:
    """Extract a JSON object from raw LLM output."""
    text = text.strip()
    if "```" in text:
        m = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
        if m:
            text = m.group(1).strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        logger.warning("Failed to parse filter JSON response: %.120s", text)
        return None
    return data if isinstance(data, dict) else None


def _parse_filter_response(text: str) -> AIFilterResult:
    """Parse the LLM response into an ``AIFilterResult``.

    Expected JSON shape:
        {"score": 0..100, "reason": "..."}
    """
    data = _extract_json(text)
    if data is None:
        return AIFilterResult(parsed=False, reason="parse_error")

    raw = data.get("score", 0)
    try:
        raw_score = max(0, min(10, int(raw)))
    except (ValueError, TypeError):
        raw_score = 0

    reason = str(data.get("reason", "")) if data.get("reason") else ""
    return AIFilterResult(raw_score=raw_score, reason=reason, parsed=True)


async def filter_items(
    processor: AIProcessor,
    items: list[ContentItem],
    *,
    concurrency: int = 5,
    threshold: int = KEEP_PCT,
) -> list[ContentItem]:
    """Two-stage AI processing: filter → summarize (for kept items).

    Stage 1 — Score and filter each item via LLM.
    Stage 2 — Summarize only items that passed the threshold.

    Items that fail or error out during filtering are discarded.
    Items that pass filtering but fail summarization keep their original content.
    """
    import asyncio

    sem = asyncio.Semaphore(concurrency)

    async def _process_one(item: ContentItem) -> ContentItem | None:
        async with sem:
            try:
                result = await processor.filter(item)
            except Exception as exc:
                logger.warning("Filter failed for %s: %s", item.title[:60], exc)
                return None

        if not result.parsed:
            logger.debug("Discarded (parse error): %s", item.title[:60])
            return None
        if result.raw_score < threshold:
            logger.debug(
                "Discarded: %s — score %d < %d",
                item.title[:60], result.raw_score, threshold,
            )
            return None

        # Persist score before summarization
        item.ai_score = result.raw_score

        # Stage 2: summarize
        try:
            item.ai_summary = await processor.summarize(item)
        except Exception as exc:
            logger.warning("Summarize failed for %s: %s", item.title[:60], exc)
            # Keep the item but without ai_summary (original content remains)

        return item

    tasks = [_process_one(item) for item in items]
    results = await asyncio.gather(*tasks)

    kept = [r for r in results if r is not None]
    logger.info(
        "AI filter: %d/%d kept (%.0f%%)",
        len(kept),
        len(items),
        (len(kept) / len(items) * 100) if items else 0,
    )
    return kept


# ── Factory ────────────────────────────────────────────────────────────────────

def create_processor(scorer_name: str = "default") -> AIProcessor:
    """Create an AIProcessor from environment variables.

    Reads LLM_BASE_URL, LLM_API_KEY, LLM_MODEL from the environment.
    Uses the OpenAI-compatible provider (works with OpenAI, vLLM, Ollama, etc.).

    *scorer_name* determines which scoring section is injected into the
    filter user prompt (see :func:`_load_scorer`).
    """
    from .providers.openai import OpenAIProcessor

    api_key = os.environ["LLM_API_KEY"]
    base_url = os.environ["LLM_BASE_URL"]
    model = os.environ["LLM_MODEL"]
    scoring_section = _load_scorer(scorer_name)

    return OpenAIProcessor(
        api_key=api_key,
        base_url=base_url,
        model=model,
        scoring_section=scoring_section,
    )
