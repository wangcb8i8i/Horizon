"""GET /api/config — provide plugins, profiles, and scorers metadata for the frontend."""

from __future__ import annotations

from fastapi import APIRouter

from horizon.tools.config import DEFAULT_CONFIG, load_config, discover_and_filter

router = APIRouter(tags=["config"])


@router.get("/config")
async def get_config() -> dict:
    """Return plugin list, profiles, and scoring schemes for the sidebar controls."""
    cfg = load_config()

    # Plugins as Record<string, {name, enabled}>
    discovered = discover_and_filter(cfg)
    plugins = {}
    for info, _ in discovered:
        plugins[info.name] = {
            "name": info.name,
            "description": info.description or "",
            "enabled": True,
        }

    # Profiles as Record<string, string[]>
    profiles_raw = cfg.get("profiles", {}) or {}
    profiles = {}
    if isinstance(profiles_raw, dict):
        for pname, pcfg in profiles_raw.items():
            if isinstance(pcfg, dict):
                categories = pcfg.get("categories", [])
                profiles[pname] = categories if isinstance(categories, list) else []

    # Scorers as string[]
    scoring_raw = cfg.get("scoring", {}) or {}
    scorers = list(scoring_raw.keys()) if isinstance(scoring_raw, dict) else []
    if "default" not in scorers:
        scorers.insert(0, "default")

    return {
        "plugins": plugins,
        "profiles": profiles,
        "scorers": scorers,
    }
