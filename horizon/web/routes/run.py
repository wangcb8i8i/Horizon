"""POST /api/run + GET /api/run/{run_id}/sse — trigger scraping with SSE progress."""

from __future__ import annotations

import asyncio
import json
import logging
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import sse_starlette.sse
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Request

from horizon.ai import KEEP_PCT, create_processor
from horizon.tools.postprocess import postprocess_items
from horizon.tools.config import (
    DEFAULT_CONFIG,
    DEFAULT_SCAN_DIR,
    discover_and_filter,
    load_config,
    output_filename,
    parse_since,
    resolve_profile,
    to_json,
)
from horizon.tools.runner import ProgressHooks, run_scrapers
from scrapers.discovery import ScraperScanner
from scrapers.plugin import ContentItem

router = APIRouter(tags=["run"])

logger = logging.getLogger(__name__)

# ── in-memory store ─────────────────────────────────────────────────────────

# keyed by run_id → list[ContentItem]
_run_results: dict[str, list[ContentItem]] = {}
# keyed by run_id → asyncio.Queue[dict] (SSE events)
_run_queues: dict[str, asyncio.Queue[dict | None]] = {}

_OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent.parent / "output"
_ENV_PATH = Path(__file__).resolve().parent.parent.parent.parent / "config" / ".env"


# ── helpers ─────────────────────────────────────────────────────────────────


def _push_event(queue: asyncio.Queue, event: str, data: dict[str, Any]) -> None:
    """Push a typed SSE event onto the queue (non-blocking)."""
    queue.put_nowait({"event": event, "data": json.dumps(data)})


# ── routes ──────────────────────────────────────────────────────────────────


@router.post("/run")
async def start_run(request: Request) -> dict:
    """Trigger a new scraping run.  Returns the ``run_id`` for SSE subscription."""
    body = await request.json()
    run_id = uuid.uuid4().hex[:12]

    since = body.get("since", "24h")
    ai = body.get("ai", False)
    scorer = body.get("scorer")
    threshold_raw = body.get("threshold")
    threshold = int(threshold_raw) if threshold_raw else None
    source_raw = body.get("sources")
    profile = body.get("profile")
    report = body.get("report", False)

    # Load config + .env
    if _ENV_PATH.exists():
        load_dotenv(_ENV_PATH)

    cfg = load_config()
    since_dt = parse_since(since)

    # Parse --sources (array of plugin names)
    source_set: set[str] | None = None
    if source_raw and isinstance(source_raw, list):
        source_names = [s.strip().lower() for s in source_raw if isinstance(s, str) and s.strip()]
        source_set = set(source_names)

        # Validate
        discovered = discover_and_filter(cfg)
        all_names = {info.name for info, _ in discovered}
        unknown = source_set - all_names
        if unknown:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown plugin(s): {', '.join(sorted(unknown))}",
            )

    # Parse --profile
    category_set: set[str] | None = None
    if profile:
        try:
            category_set = resolve_profile(cfg, profile)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))

    # Count total plugins for progress
    to_run = discover_and_filter(cfg, source_set)
    total_plugins = len(to_run)

    # Create progress queue
    queue: asyncio.Queue[dict | None] = asyncio.Queue()
    _run_queues[run_id] = queue

    # Spawn the scrape task
    asyncio.create_task(
        _execute_run(
            run_id,
            queue,
            since_dt,
            cfg,
            source_set,
            category_set,
            ai,
            scorer,
            threshold,
            total_plugins,
            report,
        )
    )

    return {"run_id": run_id}


@router.get("/run/{run_id}/sse")
async def stream_run(run_id: str, request: Request):
    """SSE endpoint streaming scraping progress for *run_id*."""
    queue = _run_queues.get(run_id)
    if queue is None:
        raise HTTPException(status_code=404, detail=f"Run not found: {run_id}")

    async def event_generator():
        while True:
            if await request.is_disconnected():
                break
            try:
                msg = await asyncio.wait_for(queue.get(), timeout=30.0)
            except asyncio.TimeoutError:
                # Send keepalive comment
                yield {"comment": ""}
                continue

            if msg is None:
                # Sentinel: run complete
                break

            yield msg

    return sse_starlette.sse.EventSourceResponse(event_generator())


@router.get("/run/{run_id}/results")
async def get_run_results(run_id: str) -> list[dict]:
    """Return the full result set for a completed run."""
    items = _run_results.get(run_id)
    if items is None:
        raise HTTPException(status_code=404, detail=f"Run not found or still in progress: {run_id}")

    return [item.model_dump(exclude_none=True) for item in items]


# ── background execution ────────────────────────────────────────────────────


async def _execute_run(
    run_id: str,
    queue: asyncio.Queue[dict | None],
    since_dt: datetime,
    cfg: dict,
    source_set: set[str] | None,
    category_set: set[str] | None,
    ai: bool,
    scorer: str | None,
    threshold: int | None,
    total_plugins: int,
    report: bool,
) -> None:
    """Background coroutine: run scrapers + optional AI filter, push SSE events."""
    try:
        # Plugin count tracking for progress
        completed_count = 0

        async def _on_item(name: str, item: ContentItem) -> None:
            _push_event(queue, "item", {
                "plugin": name,
                "title": item.title,
                "url": item.url,
                "source_type": item.source_type,
                "timestamp": item.published_at.isoformat() if item.published_at else None,
                "summary": (item.content or item.ai_summary or "")[:200],
                "metadata": item.metadata or {},
            })

        async def _on_start(name: str) -> None:
            _push_event(queue, "plugin:start", {"plugin": name})

        async def _on_complete(name: str, count: int) -> None:
            nonlocal completed_count
            completed_count += 1
            _push_event(queue, "plugin:done", {
                "plugin": name,
                "count": count,
                "completed": completed_count,
                "total": total_plugins,
            })

        async def _on_error(name: str, context: str, exc: Exception) -> None:
            nonlocal completed_count
            completed_count += 1
            _push_event(queue, "plugin:error", {
                "plugin": name,
                "error": f"{context}: {exc}" if str(exc) else context,
                "completed": completed_count,
                "total": total_plugins,
            })

        hooks: ProgressHooks = {
            "on_item": _on_item,
            "on_plugin_start": _on_start,
            "on_plugin_complete": _on_complete,
            "on_plugin_error": _on_error,
        }

        _push_event(queue, "run:start", {"run_id": run_id, "total_plugins": total_plugins})

        items = await run_scrapers(
            since_dt,
            cfg,
            source_names=source_set,
            category_names=category_set,
            hooks=hooks,
        )

        # Post-processing (short content filter + optional AI)
        if ai and items:
            api_key = os.environ.get("LLM_API_KEY")
            if not api_key:
                _push_event(queue, "plugin:error", {
                    "plugin": "ai",
                    "error": "LLM_API_KEY not set in config/.env",
                })
            else:
                scorer_name = scorer or "default"
                scoring_cfgs = cfg.get("scoring", {})
                scorer_cfg = scoring_cfgs.get(scorer_name, {}) if isinstance(scoring_cfgs, dict) else {}
                config_threshold = scorer_cfg.get("keep_pct") if isinstance(scorer_cfg, dict) else None
                effective_threshold = threshold if threshold is not None else config_threshold or KEEP_PCT

                _push_event(queue, "ai:start", {
                    "scorer": scorer_name,
                    "threshold": effective_threshold,
                })

                try:
                    processor = create_processor(scorer_name=scorer_name)
                    total_before = len(items)
                    items = await postprocess_items(items, ai_enabled=True, processor=processor, threshold=effective_threshold)
                    _push_event(queue, "ai:done", {
                        "kept": len(items),
                        "total": total_before,
                    })
                except Exception as exc:
                    _push_event(queue, "plugin:error", {
                        "plugin": "ai",
                        "error": str(exc),
                    })
        elif items:
            items = await postprocess_items(items)

        # Persist to output/ (after AI filtering)
        json_str = to_json(items)
        _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        file_path = _OUTPUT_DIR / output_filename()
        file_path.write_text(json_str, encoding="utf-8")

        # Store in memory for /results endpoint
        _run_results[run_id] = items

        _push_event(queue, "run:done", {
            "total": len(items),
            "json_path": str(file_path.relative_to(_OUTPUT_DIR.parent)),
        })

    except Exception as exc:
        logger.exception("Run %s failed", run_id)
        _push_event(queue, "run:done", {"total": 0, "error": str(exc)})
    finally:
        # Push sentinel + cleanup
        queue.put_nowait(None)
        _run_queues.pop(run_id, None)
        # Keep results around for the /results endpoint
