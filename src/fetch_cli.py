"""CLI entry point for Horizon fetch + curation pipeline."""

import argparse
import asyncio
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt

from .storage.manager import ConfigError, StorageManager
from .orchestrator import HorizonOrchestrator
from .ai.client import create_ai_client
from .ai.curator import TopicCurator
from .models import ContentItem, CuratedTopic, SourceType

console = Console()
logger = logging.getLogger(__name__)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:60].rstrip("-")


def main():
    parser = argparse.ArgumentParser(
        description="Horizon - Fetch pipeline + AI curation + interactive curation workflow"
    )
    parser.add_argument("--hours", type=int, help="Force fetch from last N hours")
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output JSON file path (default: data/raw/raw-<date>.json)",
    )
    args = parser.parse_args()

    try:
        load_dotenv()

        data_dir = Path("data")
        storage = StorageManager(data_dir=str(data_dir))

        try:
            config = storage.load_config()
        except FileNotFoundError:
            console.print("[bold red]Configuration file not found![/bold red]")
            console.print("Run [bold cyan]uv run horizon-wizard[/bold cyan] to set up.")
            sys.exit(1)
        except ConfigError as e:
            console.print(f"[bold red]Error loading configuration: {e}[/bold red]")
            sys.exit(1)
        except Exception as e:
            console.print(f"[bold red]Error loading configuration: {e}[/bold red]")
            sys.exit(1)

        # ── Steps 1-4: Fetch pipeline ──────────────────────────────
        orchestrator = HorizonOrchestrator(config, storage)
        items = asyncio.run(orchestrator.run_fetch_only(force_hours=args.hours))

        if not items:
            console.print("[yellow]No items fetched. Exiting without output.[/yellow]")
            sys.exit(1)

        raw_dir = Path("data/raw")
        raw_dir.mkdir(parents=True, exist_ok=True)

        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        output_path = args.output or str(raw_dir / f"raw-{date_str}.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                [item.model_dump(mode="json") for item in items],
                f,
                ensure_ascii=False,
                indent=2,
            )

        console.print(f"[green]Saved {len(items)} items to {output_path}[/green]")

        # ── Steps 5-6: Curation (async entry) ────────────────────
        asyncio.run(_run_curation_pipeline(items, config, date_str))

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Fatal error: {e}[/bold red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


async def _run_curation_pipeline(items: List[ContentItem], config, date_str: str):
    """Run AI curation analysis (step 5) and interactive workflow (step 6)."""
    # ── Step 5: AI Curation Analysis ──────────────────────────
    console.print("\n🧠 Running AI curation analysis...")
    try:
        ai_client = create_ai_client(config.ai)
    except Exception as e:
        console.print(f"[yellow]Failed to create AI client: {e}. Skipping curation.[/yellow]")
        return

    curator = TopicCurator(ai_client)
    curation_result = await curator.curate(items)

    curated_dir = Path("data/curated")
    curated_dir.mkdir(parents=True, exist_ok=True)

    curated_path = curated_dir / f"curated-{date_str}.json"
    with open(curated_path, "w", encoding="utf-8") as f:
        json.dump(
            curation_result.model_dump(mode="json"),
            f,
            ensure_ascii=False,
            indent=2,
        )
    console.print(f"[green]Curation analysis saved to {curated_path}[/green]")

    # ── Decide next step based on topic count ────────────────
    n = len(curation_result.topics)

    if n == 0:
        console.print("[yellow]No high-value curation topics found this cycle. Skipping curation workflow.[/yellow]")
        return

    items_by_id = {item.id: item for item in items}

    if n == 1:
        topic = curation_result.topics[0]
        console.print(f"\n[bold]🎯 Found 1 curation-worthy topic: {topic.name}[/bold] (auto-selected)")
        await _run_curation_workflow(topic, items_by_id, date_str, curator)
        return

    # n == 2: user picks one topic, then done
    console.print(f"\n[bold]🎯 Found 2 curation-worthy topics:[/bold]")
    for i, topic in enumerate(curation_result.topics, 1):
        count = sum(1 for t_id in topic.item_ids if t_id in items_by_id)
        score = topic.curation_score
        console.print(f"  [{i}] {topic.name}  ({count} items, score {score}/10)")
        console.print(f"      {topic.relevance[:120]}")

    allowed = ["1", "2", "q"]
    choice = Prompt.ask(
        "\nSelect a topic to curate",
        choices=allowed,
        default="q",
    )

    if choice == "q":
        console.print("[yellow]Exiting curation workflow.[/yellow]")
        return

    topic = curation_result.topics[int(choice) - 1]
    await _run_curation_workflow(topic, items_by_id, date_str, curator)


async def _run_curation_workflow(
    topic: CuratedTopic,
    items_by_id: dict[str, ContentItem],
    date_str: str,
    curator: TopicCurator,
):
    """Execute full curation for a selected topic: search → materials → guide."""
    from ddgs import DDGS

    topic_items = [items_by_id[i] for i in topic.item_ids if i in items_by_id]

    topic_slug = slugify(topic.name)
    out_dir = Path("data/curated") / date_str / topic_slug
    materials_dir = out_dir / "materials"
    materials_dir.mkdir(parents=True, exist_ok=True)

    console.print(f"\n[bold]📦 Curating: {topic.name}[/bold]")
    console.print(f"   Output: {out_dir}\n")

    # ── AI search query generation ─────────────────────────────
    console.print("   🤖 Generating search queries from article content...")
    search_queries = await curator.generate_search_queries(topic, topic_items)
    console.print(f"   Generated {len(search_queries)} search queries")

    # ── DuckDuckGo search ──────────────────────────────────────
    web_results: List[dict] = []
    ddgs = DDGS()

    for query in search_queries:
        console.print(f"   🔍 Searching: {query}")
        try:
            results = await asyncio.to_thread(ddgs.text, query, max_results=5)
            for r in results:
                if r.get("url") and r.get("title"):
                    web_results.append({
                        "url": r["url"],
                        "title": r["title"],
                        "snippet": (r.get("body") or "")[:300],
                        "query": query,
                    })
        except Exception:
            pass

    if web_results:
        console.print(f"   Found {len(web_results)} supplementary results\n")
    else:
        console.print("   [yellow]No supplementary results found.[/yellow]\n")

    # ── Write material files ────────────────────────────────────
    _ITEM_MAX_CHARS = 5000

    for idx, item in enumerate(topic_items, 1):
        from .ai.utils import clean_item_text as _clean

        item_slug = slugify(item.title)[:40] or f"item-{idx:03d}"
        filename = f"item-{idx:03d}-{item_slug}.md"
        filepath = materials_dir / filename

        cleaned = _clean(item.content, _ITEM_MAX_CHARS)
        is_truncated = bool(item.content and len(cleaned) == _ITEM_MAX_CHARS)
        content = cleaned or "(no body content)"
        if is_truncated:
            content += "\n\n*--- 内容已截断 —— 原始内容超过上限 ---*"

        meta_lines = [
            f"- **Source**: {item.source_type.value}",
            f"- **Author**: {item.author or 'N/A'}",
            f"- **URL**: {item.url}",
            f"- **Published**: {item.published_at.strftime('%Y-%m-%d %H:%M:%S')}",
        ]
        if item.ai_score is not None:
            meta_lines.append(f"- **Score**: {item.ai_score}/10")
        if item.ai_tags:
            meta_lines.append(f"- **Tags**: {', '.join(item.ai_tags)}")

        # Content source label
        content_note = None
        if item.source_type == SourceType.HACKERNEWS and item.content and "--- Top Comments ---" in item.content:
            content_note = (
                f"> **Note**: 以下为 Hacker News 社区讨论，非原文。\n"
                f"> 原文见 [{item.url}]({item.url})"
            )
        elif item.source_type == SourceType.RSS:
            content_note = "> **Note**: 文章全文（经清洗）"
        elif item.source_type == SourceType.REDDIT:
            content_note = "> **Note**: Reddit 帖文及热评"

        note_block = f"\n{content_note}\n" if content_note else ""
        md = f"""# {item.title}

{chr(10).join(meta_lines)}{note_block}
## Content

{content}
"""
        filepath.write_text(md, encoding="utf-8")

    for idx, wr in enumerate(web_results, 1):
        web_slug = slugify(wr["title"])[:40] or f"web-{idx:03d}"
        filename = f"web-{idx:03d}-{web_slug}.md"
        filepath = materials_dir / filename

        md = f"""# {wr["title"]}

- **URL**: {wr["url"]}
- **Source**: Search ({wr["query"]})

## Snippet

{wr["snippet"] or "No snippet available."}
"""
        filepath.write_text(md, encoding="utf-8")

    # ── AI curation guide ──────────────────────────────────────
    console.print("   🤖 Writing curation guide...")
    guide_md = await curator.generate_curation_guide(topic, topic_items, web_results)

    guide_path = out_dir / "curation-guide.md"
    guide_path.write_text(guide_md, encoding="utf-8")

    console.print("[green]✅ Curation output:[/green]")
    console.print(f"   {out_dir}/")
    console.print(f"   ├── materials/")
    for fname in sorted(materials_dir.iterdir()):
        console.print(f"   │   ├── {fname.name}")
    console.print(f"   ├── curation-guide.md")
    console.print()


if __name__ == "__main__":
    main()
