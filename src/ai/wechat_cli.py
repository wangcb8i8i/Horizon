"""CLI entry point for WeChat article generation from a summary items JSON file."""

import argparse
import asyncio
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .client import create_ai_client
from .wechat import generate_article_from_file
from ..storage.manager import ConfigError, StorageManager

console = Console()


async def _run(json_path: str, date: str, brand: str, output: str | None) -> None:
    if not Path(json_path).exists():
        console.print(f"[bold red]File not found: {json_path}[/bold red]")
        sys.exit(1)

    load_dotenv()
    storage = StorageManager(data_dir=str(Path("data")))
    try:
        config = storage.load_config()
    except FileNotFoundError:
        console.print("[bold red]Configuration file not found![/bold red]")
        console.print("Run [bold cyan]uv run horizon-wizard[/bold cyan] first.")
        sys.exit(1)
    except ConfigError as e:
        console.print(f"[bold red]Error loading configuration: {e}[/bold red]")
        sys.exit(1)

    ai_client = create_ai_client(config.ai)
    html = await generate_article_from_file(json_path, date, ai_client, brand)

    if not html:
        console.print("[yellow]No article generated (no classified items).[/yellow]")
        sys.exit(0)

    if output:
        out_path = Path(output)
    else:
        default_dir = (config.wechat.output_dir if config.wechat else "data/wechat")
        stem = Path(json_path).stem
        out_path = Path(default_dir) / f"{stem}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    console.print(f"[green]Article saved to {out_path}[/green]")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a WeChat article from a summary items JSON file",
    )
    parser.add_argument("json_path", help="Path to the .json file from save_summary_items")
    parser.add_argument("--date", default=None, help="Date string (YYYY-MM-DD, defaults to today)")
    parser.add_argument("--brand", default="技术信号", help="Brand name for the article")
    parser.add_argument("-o", "--output", default=None, help="Output HTML file path (default: data/wechat/{stem}.html)")
    args = parser.parse_args()

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        asyncio.run(_run(args.json_path, date, args.brand, args.output))
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/bold red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
