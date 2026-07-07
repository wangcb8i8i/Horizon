"""Configuration loading, time parsing, and plugin discovery utilities.

Extracted from ``horizon/cli.py`` so both CLI and web layers can share
these pure-logic functions without depending on Click or Rich.
"""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

import yaml

from scrapers.discovery import ScraperScanner

if TYPE_CHECKING:
    from scrapers.plugin import ContentItem

# ── paths ───────────────────────────────────────────────────────────────────

_HERE = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = _HERE.parent / "config" / "horizon.yaml"
DEFAULT_SCAN_DIR = _HERE / "scrapers"


# ── config loading ──────────────────────────────────────────────────────────


def load_config(path: Path | None = None) -> dict:
    """Load and parse Horizon config YAML.

    Raises ``FileNotFoundError`` (with a helpful message) when *path*
    does not exist.
    """
    p = path or DEFAULT_CONFIG
    if not p.exists():
        raise FileNotFoundError(
            f"Config not found: {p}\n"
            f"  Create config/horizon.yaml to get started."
        )
    with open(p) as f:
        cfg = yaml.safe_load(f) or {}
    return cfg


# ── time parsing ────────────────────────────────────────────────────────────


def parse_since(text: str) -> datetime:
    """Parse a relative time string like ``24h``, ``7d``, ``2w``.

    Raises ``ValueError`` for unrecognised formats.
    """
    m = re.match(r"^(\d+)([hdw])$", text.strip().lower())
    if not m:
        raise ValueError(
            f"Invalid --since format: '{text}'. Use e.g. 24h, 7d, 2w"
        )
    value = int(m.group(1))
    unit = m.group(2)
    if unit == "h":
        delta = timedelta(hours=value)
    elif unit == "d":
        delta = timedelta(days=value)
    else:
        delta = timedelta(weeks=value)
    return datetime.now(timezone.utc) - delta


# ── plugin discovery ────────────────────────────────────────────────────────


def discover_and_filter(
    cfg: dict,
    source_names: set[str] | None = None,
) -> list:
    """Discover plugins from the scan dir and filter by enabled status.

    When *source_names* is set, only plugins whose ``name`` appears in
    the set are returned (still subject to the config ``enabled`` flag).

    Returns a list of ``(PluginInfo, plugin_config)`` tuples.
    """
    scanner = ScraperScanner(str(DEFAULT_SCAN_DIR))
    all_plugins = scanner.scan(register=False)

    plugin_configs = cfg.get("plugins", {})
    enabled = []
    for info in all_plugins:
        pcfg = plugin_configs.get(info.name, {}) or {}
        if not pcfg.get("enabled", True):
            continue
        if source_names is not None and info.name not in source_names:
            continue
        enabled.append((info, pcfg))

    return enabled


# ── serialisation ───────────────────────────────────────────────────────────


def to_json(items: list["ContentItem"]) -> str:
    """Pretty-printed JSON array of ContentItem dicts."""
    data = [item.model_dump(exclude_none=True) for item in items]
    return json.dumps(data, indent=2, ensure_ascii=False, default=str)


def output_filename() -> str:
    """Generate a UTC-timestamped filename: ``2026-07-03T120000Z.json``."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    return f"{now}.json"


# ── category helpers ────────────────────────────────────────────────────────


def collect_known_categories(cfg: dict) -> set[str]:
    """Collect every category label declared anywhere in the plugin config tree."""
    known: set[str] = set()

    def walk(node: object) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "categories" and isinstance(v, list):
                    for c in v:
                        if isinstance(c, str):
                            known.add(c.strip().lower())
                else:
                    walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for pcfg in cfg.get("plugins", {}).values():
        if isinstance(pcfg, dict):
            walk(pcfg)
    return known


def collect_categories_with_plugins(cfg: dict) -> dict[str, set[str]]:
    """Map every declared category to the set of plugin names that use it."""
    mapping: dict[str, set[str]] = {}

    def walk(node: object, plugin_name: str) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "categories" and isinstance(v, list):
                    for c in v:
                        if isinstance(c, str):
                            key = c.strip().lower()
                            mapping.setdefault(key, set()).add(plugin_name)
                else:
                    walk(v, plugin_name)
        elif isinstance(node, list):
            for item in node:
                walk(item, plugin_name)

    for pname, pcfg in cfg.get("plugins", {}).items():
        if isinstance(pcfg, dict):
            walk(pcfg, pname)
    return mapping


# ── profile resolution ──────────────────────────────────────────────────────


def resolve_profile(
    cfg: dict,
    profile_name: str,
    *,
    warn: Callable[[str], None] | None = None,
) -> set[str]:
    """Resolve a named profile to its category set.

    A profile is a named bundle of category preferences defined under the
    top-level ``profiles`` key.  Returns the set of selected category names.

    When *warn* is provided it is called for unknown-category warnings
    (replaces the Rich ``console.print`` in the CLI variant).
    """
    profiles = cfg.get("profiles", {}) or {}
    if not isinstance(profiles, dict) or profile_name not in profiles:
        available = ", ".join(sorted(profiles)) if profiles else "(none defined)"
        raise ValueError(
            f"Unknown profile: '{profile_name}'. Available profiles: {available}"
        )

    pcfg = profiles[profile_name] or {}
    raw_cats = pcfg.get("categories", []) or []
    cat_set = {str(c).strip().lower() for c in raw_cats if str(c).strip()}
    if not cat_set:
        raise ValueError(
            f"Profile '{profile_name}' defines no categories."
        )

    # Warn about categories that no plugin sub-item actually carries.
    known = collect_known_categories(cfg)
    unknown = cat_set - known
    if unknown and warn:
        warn(
            f"profile '{profile_name}' lists categories with no "
            f"matching source: {', '.join(sorted(unknown))}"
        )

    return cat_set
