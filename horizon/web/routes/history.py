"""GET /api/history + GET /api/history/{run_id} — browse past scraping runs."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["history"])

_OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent.parent / "output"


def _parse_run_id(run_id: str) -> datetime:
    """Parse a run_id like ``2026-07-03T120000Z`` into a datetime."""
    try:
        return datetime.strptime(run_id, "%Y-%m-%dT%H%M%SZ")
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid run_id format: {run_id}")


def _list_run_files() -> list[Path]:
    """Return sorted list of JSON run files, newest first."""
    if not _OUTPUT_DIR.exists():
        return []
    files = sorted(
        _OUTPUT_DIR.glob("*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return files[:10]


@router.get("/history")
async def list_history() -> list[dict]:
    """Return the latest 10 historical runs with metadata."""
    entries = []
    for fp in _list_run_files():
        run_id = fp.stem
        try:
            mtime = fp.stat().st_mtime
            ts = datetime.fromtimestamp(mtime)
            with open(fp) as f:
                data = json.load(f)
            item_count = len(data) if isinstance(data, list) else 0
        except (OSError, json.JSONDecodeError):
            continue

        entries.append({
            "run_id": run_id,
            "timestamp": ts.isoformat(),
            "item_count": item_count,
        })

    return entries


@router.get("/history/{run_id}")
async def get_history_run(run_id: str) -> list[dict]:
    """Return the full result set for a historical run."""
    fp = _OUTPUT_DIR / f"{run_id}.json"
    if not fp.exists():
        raise HTTPException(status_code=404, detail=f"Run not found: {run_id}")

    try:
        with open(fp) as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=500, detail=f"Failed to read run data: {exc}")

    if not isinstance(data, list):
        raise HTTPException(status_code=500, detail="Invalid run data format")

    return data
