"""Horizon CLI — run, list, and configure scrapers.

Usage::

    horizon run [--since 24h]
    horizon list
    horizon config
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

import click
import yaml
from dotenv import load_dotenv
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.cells import cell_len

from scrapers.dedup import Deduplicator
from scrapers.discovery import ScraperScanner
from scrapers.plugin import ScraperConfig, ContentItem

from horizon.ai import KEEP_PCT, filter_items, create_processor

logger = logging.getLogger(__name__)

# ── paths ───────────────────────────────────────────────────────────────────

_HERE = Path(__file__).resolve().parent
_DEFAULT_CONFIG = _HERE.parent / "config" / "horizon.yaml"
_DEFAULT_SCAN_DIR = _HERE / "scrapers"

# ── formatting — panel output ────────────────────────────────────────────────

_PARAGRAPH_MAX_CHARS = 500


def _group_items(items: list[ContentItem]) -> list[tuple[str, list[ContentItem]]]:
    """Group items by (source_type, feed_name) for section rendering."""
    groups: list[tuple[str, list[ContentItem]]] = []
    for item in items:
        if item.source_type == "rss":
            feed = item.metadata.get("feed_name", "") or ""
            label = f"RSS · {feed}" if feed else "RSS"
        elif item.source_type == "github":
            repo = item.metadata.get("repo", "") or ""
            label = f"GitHub · {repo}" if repo else "GitHub"
        else:
            label = item.source_type.capitalize()
        if not groups or groups[-1][0] != label:
            groups.append((label, []))
        groups[-1][1].append(item)
    return groups


# Content after HTML cleaning that matches these patterns is treated as
# leftover link label text (e.g. ``<a href="…">Comments</a>`` → "Comments")
_NOISE_WORDS = frozenset({
    "comments", "read more", "continue reading", "permalink",
    "more", "link", "full article", "read full article",
    "read story", "continue", "details", "show more", "show hn",
})


def _is_content_noise(text: str) -> bool:
    """Return True when cleaned content is just a leftover link label."""
    t = text.strip()
    if not t:
        return True
    if len(t) > 25:
        return False
    # Has real sentence structure → keep it
    if any(c in t for c in ".!?。！？"):
        return False
    return t.lower().strip() in _NOISE_WORDS


def _truncate_at_word(text: str, limit: int) -> str:
    """Truncate at the last word boundary before *limit* (display width).

    Uses ``cell_len`` so CJK characters are counted as width 2.
    """
    if cell_len(text) <= limit:
        return text
    # Walk characters to find where display width exceeds the limit
    width = 0
    trunc_idx = len(text)
    for i, ch in enumerate(text):
        w = cell_len(ch)
        if width + w > limit:
            trunc_idx = i
            break
        width += w
    truncated = text[:trunc_idx]
    last_space = truncated.rfind(" ")
    if last_space > trunc_idx // 2:
        truncated = truncated[:last_space]
    return truncated + "… (truncated)"


def _build_run_output(items: list[ContentItem]) -> Group:
    """Build Rich renderable with grouped panels (Ticket #1, #2, #4).

    Each (source_type, feed_name) group → one Rich Panel.
    Items inside: bold title, dim summary, dim cyan URL.
    Footer shows per-source-type counts.
    """
    groups = _group_items(items)
    panels: list[Panel | Text] = []

    for label, group_items in groups:
        renderables: list[Text] = []
        for i, item in enumerate(group_items):
            if i > 0:
                renderables.append(Text("─" * 50, style="dim"))

            # Title + AI score (inline)
            title_text = Text(item.title or "", style="bold")
            if item.ai_score is not None:
                title_text.append(f"  ({item.ai_score}.0)", style="italic yellow")
            renderables.append(title_text)

            # Content summary — prefer ai_summary over raw content, first line indented
            content_text = item.ai_summary or item.content or ""
            if _is_content_noise(content_text):
                content_text = ""
            if content_text:
                # Collapse internal newlines so indentation stays consistent
                content_text = " ".join(content_text.splitlines()).strip()
                if cell_len(content_text) > _PARAGRAPH_MAX_CHARS:
                    content_text = _truncate_at_word(content_text, _PARAGRAPH_MAX_CHARS)
                renderables.append(Text(""))
                renderables.append(Text("  " + content_text, style="dim", overflow="fold"))

            # URL
            renderables.append(Text(""))
            renderables.append(Text(item.url, style="dim cyan"))

        panel = Panel(
            Group(*renderables) if renderables else Text("(no items)"),
            title=f"[bold cyan]{label}[/bold cyan]",
            border_style="dim",
            padding=(0, 2),
        )
        panels.append(panel)

    # Footer — grouped statistics (Ticket #4)
    _source_labels = {"rss": "RSS", "github": "GitHub"}
    type_counts: Counter[str] = Counter()
    for item in items:
        label = _source_labels.get(item.source_type, item.source_type.capitalize())
        type_counts[label] += 1
    stat_parts = "  •  ".join(f"{k}: {v}" for k, v in type_counts.most_common())
    footer = Text.assemble(
        ("Summary: ", "bold"),
        (stat_parts, ""),
        ("  |  ", "dim"),
        (f"Total: {len(items)}", "bold"),
    )

    return Group(*panels, Text(""), footer)


# ── helpers ─────────────────────────────────────────────────────────────────

def _load_config(path: Path) -> dict:
    if not path.exists():
        raise click.ClickException(
            f"Config not found: {path}\n"
            f"  Create config/horizon.yaml to get started."
        )
    with open(path) as f:
        cfg = yaml.safe_load(f) or {}
    return cfg


def _parse_since(text: str) -> datetime:
    """Parse relative time like ``24h``, ``7d``, ``2w``."""
    m = re.match(r"^(\d+)([hdw])$", text.strip().lower())
    if not m:
        raise click.BadParameter(
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


def _discover_and_filter(cfg: dict) -> list:
    """Discover plugins from the scan dir and filter by enabled status."""
    scanner = ScraperScanner(str(_DEFAULT_SCAN_DIR))
    all_plugins = scanner.scan(register=False)

    plugin_configs = cfg.get("plugins", {})
    enabled = []
    for info in all_plugins:
        pcfg = plugin_configs.get(info.name, {}) or {}
        if not pcfg.get("enabled", True):
            continue
        enabled.append((info, pcfg))

    return enabled


def _to_json(items: list[ContentItem]) -> str:
    """Pretty-printed JSON array of ContentItem dicts."""
    data = [item.model_dump(exclude_none=True) for item in items]
    return json.dumps(data, indent=2, ensure_ascii=False, default=str)


def _output_filename() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    return f"{now}.json"


# ── async runner ─────────────────────────────────────────────────────────────

async def _run_scrapers(
    since: datetime,
    cfg: dict,
    console: Console,
) -> list[ContentItem]:
    """Execute all enabled plugins and return deduped items."""
    import httpx
    from rich.live import Live
    from rich.spinner import Spinner

    # Discover and filter
    to_run = _discover_and_filter(cfg)
    if not to_run:
        console.print("[yellow]No enabled plugins found in config.[/yellow]")
        return []

    fw_cfg = ScraperConfig(**cfg.get("framework", {}))
    dedup = Deduplicator()
    all_items: list[ContentItem] = []
    done_lines: list[Text] = []

    # ── lifecycle per plugin ──────────────────────────────────────────────
    async with httpx.AsyncClient(
        timeout=fw_cfg.timeout,
        limits=httpx.Limits(
            max_connections=fw_cfg.max_connections,
            max_keepalive_connections=fw_cfg.max_connections,
        ),
        proxy=fw_cfg.proxy,
        headers=fw_cfg.extra_headers or None,
    ) as client:

        live = Live(
            Panel(Spinner("dots", text="Initialising…"), title="Scraping", border_style="cyan"),
            console=console,
            refresh_per_second=10,
            transient=True,
        )
        live.start()

        try:
            for info, pcfg in to_run:
                inst = info.cls(pcfg, client, fw_cfg)

                # Show progress with animated spinner
                progress_content: list[Text | Group | Spinner] = [*done_lines]
                progress_content.append(Spinner("dots", text=f" {info.name}…"))
                live.update(Panel(
                    Group(*progress_content),
                    title="Scraping",
                    border_style="cyan",
                ))

                try:
                    await inst.setup()
                except Exception as exc:
                    logger.warning("%s.setup() failed: %s", info.name, exc)
                    done_lines.append(Text(f"  [yellow]✘ {info.name}[/yellow] (setup failed)"))
                    continue

                try:
                    raw_items = await inst.fetch(since)
                except Exception as exc:
                    logger.error("%s.fetch() failed: %s", info.name, exc)
                    raw_items = []
                finally:
                    try:
                        await inst.teardown()
                    except Exception as exc:
                        logger.warning("%s.teardown() failed: %s", info.name, exc)

                filtered = dedup.filter(raw_items)
                all_items.extend(filtered)

                if filtered:
                    done_lines.append(Text(f"  [green]✔[/green] {info.name}: {len(filtered)} items"))
                else:
                    done_lines.append(Text(f"  [dim]─[/dim] {info.name}: 0 items"))
        finally:
            live.stop()

    # Print final progress panel (static)
    if done_lines:
        console.print(Panel(Group(*done_lines), title="Scraping", border_style="dim"))

    return all_items


# ── click commands ──────────────────────────────────────────────────────────

# Suppress noisy import-failure warnings from the discovery module
logging.getLogger("scrapers").setLevel(logging.ERROR)


@click.group()
def main():
    """Horizon — personal content aggregator."""


@main.command()
@click.option(
    "--since",
    default="24h",
    show_default=True,
    help='Time window (e.g. 24h, 7d, 2w)',
)
@click.option(
    "--scorer",
    default=None,
    help='Scoring scheme name (e.g. "tech", "news"). Defaults to "default".',
)
@click.option(
    "--threshold",
    type=int,
    default=None,
    help="Score threshold 0-10. Overrides config and code default.",
)
def run(since: str, scorer: str | None, threshold: int | None) -> None:
    """Run all enabled scrapers."""
    console = Console()

    # Load .env from config/
    _env_path = _HERE.parent / "config" / ".env"
    if _env_path.exists():
        load_dotenv(_env_path)

    cfg = _load_config(_DEFAULT_CONFIG)
    since_dt = _parse_since(since)

    # Resolve scorer name and threshold
    scorer_name = scorer or "default"
    scoring_cfgs = cfg.get("scoring", {})
    scorer_cfg = scoring_cfgs.get(scorer_name, {}) if isinstance(scoring_cfgs, dict) else {}
    config_threshold = scorer_cfg.get("keep_pct") if isinstance(scorer_cfg, dict) else None
    effective_threshold = threshold if threshold is not None else config_threshold or KEEP_PCT

    console.print(f"Running scrapers (since [cyan]{since}[/cyan])…")
    items = asyncio.run(_run_scrapers(since_dt, cfg, console))

    if not items:
        console.print("\n[dim]No items collected.[/dim]")
        return

    # Pretty JSON to output/{timestamp}.json (persist before terminal output)
    json_str = _to_json(items)
    out_path = _HERE.parent / "output"
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / _output_filename()
    file_path.write_text(json_str, encoding="utf-8")

    # AI: filter + summarize (only affects terminal output)
    if os.environ.get("LLM_API_KEY"):
        try:
            processor = create_processor(scorer_name=scorer_name)
            items = asyncio.run(filter_items(processor, items, threshold=effective_threshold))
            if not items:
                console.print("\n[dim]No items passed AI filter (scorer=[cyan]{scorer_name}[/cyan], threshold=[cyan]{effective_threshold}[/cyan]).[/dim]")
                return
        except Exception as exc:
            logger.warning("AI processing failed, falling back to raw items: %s", exc)

    # Terminal output (Rich panels, summary)
    console.print()
    console.print(_build_run_output(items))
    console.print(f"\n[green]Written[/green] {len(items)} items → [bold]{file_path}[/bold]")


@main.command()
def list() -> None:
    """List discovered scraper plugins."""
    cfg = _load_config(_DEFAULT_CONFIG)
    to_run = _discover_and_filter(cfg)

    scanner = ScraperScanner(str(_DEFAULT_SCAN_DIR))
    all_plugins = scanner.scan(register=False)

    if not all_plugins:
        click.echo("No plugins found.")
        return

    plugin_configs = cfg.get("plugins", {})
    enabled_names = {info.name for info, _ in to_run}

    table = Table(title="Discovered Plugins", box=None)
    table.add_column("Plugin", style="cyan", no_wrap=True)
    table.add_column("Status", no_wrap=True)
    table.add_column("Description")
    table.add_column("Class")

    for info in sorted(all_plugins, key=lambda p: p.name):
        status = "[green]enabled[/green]" if info.name in enabled_names else "[dim]disabled[/dim]"
        has_schema = " ✓ schema" if info.config_schema else ""
        table.add_row(info.name, status, info.description, f"{info.cls.__name__}{has_schema}")

    console = Console()
    console.print(table)


@main.command()
def config() -> None:
    """Show the current configuration."""
    from rich.syntax import Syntax

    cfg = _load_config(_DEFAULT_CONFIG)
    yaml_text = yaml.dump(cfg, default_flow_style=False, allow_unicode=True)
    syntax = Syntax(yaml_text, "yaml", theme="ansi_dark")

    console = Console()
    console.print(f"Config: [bold]{_DEFAULT_CONFIG}[/bold]")
    console.print(syntax)


if __name__ == "__main__":
    main()
