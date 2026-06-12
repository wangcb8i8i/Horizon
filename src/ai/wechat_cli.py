"""CLI entry point for WeChat article generation and publishing.

Usage:
  Generate HTML from summary items JSON:  horizon-wechat data/items.json
  Publish existing HTML:                   horizon-wechat data/wechat/2026-06-09.html --publish
"""

import argparse
import asyncio
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .client import create_ai_client
from .wechat import generate_article_from_file
from ..storage.manager import ConfigError, StorageManager

console = Console()


async def _run(input_path: str, date: str, brand: str, output: str | None, publish: bool = False, proxy: str | None = None) -> None:
    path = Path(input_path)
    if not path.exists():
        console.print(f"[bold red]File not found: {input_path}[/bold red]")
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

    # ── Read or generate HTML ───────────────────────────────────────────
    headline = ""
    body = ""
    if path.suffix == ".html":
        html = path.read_text(encoding="utf-8")
        console.print(f"[dim]Read existing HTML from {input_path}[/dim]\n")
    else:
        ai_client = create_ai_client(config.ai)
        link_noopener = config.wechat.link_noopener if config.wechat else True
        html, headline, body = await generate_article_from_file(input_path, date, ai_client, brand, link_noopener=link_noopener)

        if not html:
            console.print("[yellow]No article generated (no classified items).[/yellow]")
            sys.exit(0)

    if not path.suffix == ".html":
        if output:
            out_path = Path(output)
        else:
            default_dir = (config.wechat.output_dir if config.wechat else "data/wechat")
            stem = path.stem
            out_path = Path(default_dir) / f"{stem}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")
        console.print(f"[green]Article saved to {out_path}[/green]")

    # ── Publish via WeChat API ──────────────────────────────────────────
    if publish:
        if not config.wechat or not config.wechat.api_enabled:
            console.print("[yellow]--publish requires wechat.api_enabled = true in config[/yellow]")
            sys.exit(1)

        from .wechat_api import WeChatAPIClient, WeChatAPIError

        wc = config.wechat
        client = WeChatAPIClient(
            app_id=os.environ[wc.app_id_env],
            app_secret=os.environ[wc.app_secret_env],
            proxy=proxy,
        )
        try:
            thumb_media_id = await client.resolve_thumb_media_id(config)
            media_id, title, digest = await client.create_draft(
                content=html,
                author=wc.author,
                thumb_media_id=thumb_media_id,
                insight_headline=headline,
                insight_body=body,
                date=date,
                brand_name=wc.brand_name,
            )
            console.print()
            console.print("[bold cyan]📰  标题[/bold cyan]")
            console.print(f"[white]{title}[/white]")
            console.print()
            console.print("[bold cyan]📝  摘要[/bold cyan]")
            console.print(f"[white]{digest}[/white]")
            console.print()
            console.print(f"[green]✅ 草稿已发布  media_id: {media_id}[/green]")
        except WeChatAPIError as e:
            console.print(f"[red]Publish failed: {e}[/red]")
            sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate and/or publish a WeChat article",
    )
    parser.add_argument("input", help="Path to .json (generate + save) or .html (read + publish)")
    parser.add_argument("--date", default=None, help="Date string (YYYY-MM-DD, defaults to today)")
    parser.add_argument("--brand", default="技术信号", help="Brand name for the article")
    parser.add_argument("-o", "--output", default=None, help="Output HTML file path (default: data/wechat/{stem}.html)")
    parser.add_argument("--publish", action="store_true", help="Publish via WeChat API")
    parser.add_argument("--proxy", default=None, help="Proxy URL, e.g. http://127.0.0.1:7890")
    args = parser.parse_args()

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        asyncio.run(_run(args.input, date, args.brand, args.output, publish=args.publish, proxy=args.proxy))
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
