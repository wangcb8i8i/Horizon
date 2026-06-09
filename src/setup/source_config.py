"""CLI wizard for Twitter and Telegram source configuration."""

import os
import subprocess
import sys

from dotenv import load_dotenv, set_key
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

from ..models import (
    Config,
    TelegramChannelConfig,
    TelegramConfig,
    TwitterConfig,
)
from ..storage.manager import StorageManager

console = Console()
ENV_PATH = ".env"


def print_banner():
    banner = r"""
[bold blue]
  _    _            _
 | |  | |          (_)
 | |__| | ___  _ __ _ ___  ___  _ __
 |  __  |/ _ \| '__| |_  / / _ \| '_ \
 | |  | | (_) | |  | |/ / | (_) | | | |
 |_|  |_|\___/|_|  |_/___| \___/|_| |_|
[/bold blue]
[cyan]  Source Configuration Wizard — Twitter + Telegram[/cyan]
    """
    console.print(banner)


def configure_twitter(config: Config) -> Config:
    console.print("\n[bold]Step 1: Twitter[/bold]\n")
    console.print(
        "Horizon uses [link=https://apify.com/altimis/scweet]Apify Scweet actor[/link] "
        "to fetch tweets."
    )
    console.print(
        "  1. Sign up at [link=https://console.apify.com]https://console.apify.com[/link]"
    )
    console.print(
        "  2. Get your API token from Dashboard → Settings → API & Keys"
    )
    console.print("  3. Paste it below (leave empty to skip Twitter)\n")

    show_help = Confirm.ask("Need help setting up Apify?", default=False)
    if show_help:
        console.print(
            "\n[dim]1. Go to https://console.apify.com and create a free account[/dim]"
        )
        console.print(
            "[dim]2. Once logged in, go to Settings → API & Keys[/dim]"
        )
        console.print("[dim]3. Copy your Personal API Token[/dim]")
        console.print(
            "[dim]4. Paste it when prompted below[/dim]\n"
        )

    existing_token = os.environ.get("APIFY_TOKEN")
    if existing_token:
        console.print(f"  ✓ APIFY_TOKEN already set (…{existing_token[-4:]})")
        token = existing_token
    else:
        token = Prompt.ask("Apify API Token", default="").strip()
        if token:
            set_key(ENV_PATH, "APIFY_TOKEN", token)
            os.environ["APIFY_TOKEN"] = token
            console.print("[green]  ✓ APIFY_TOKEN saved to .env[/green]")
        else:
            console.print(
                "[yellow]  ⚠ No APIFY_TOKEN set — Twitter will be skipped at runtime[/yellow]"
            )
    usernames_input = Prompt.ask(
        "Twitter usernames to follow (comma-separated, without @)",
        default="",
    ).strip()

    usernames = [u.strip().lstrip("@") for u in usernames_input.split(",") if u.strip()]

    keywords_input = Prompt.ask(
        "Twitter keywords to search (comma-separated, e.g. LLM, AI agents, Rust)",
        default="",
    ).strip()

    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]

    if not usernames and not keywords:
        config.sources.twitter = None
        console.print("[yellow]  Twitter: skipped (no usernames or keywords)[/yellow]\n")
        return config

    config.sources.twitter = TwitterConfig(
        users=usernames,
        keywords=keywords,
        fetch_limit=10,
        enabled=True,
    )

    parts = []
    if usernames:
        parts.append(f"{len(usernames)} user(s)")
    if keywords:
        parts.append(f"{len(keywords)} keyword(s)")
    console.print(f"  ✓ {', '.join(parts)} configured\n")
    return config


def configure_telegram(config: Config) -> Config:
    console.print("\n[bold]Step 2: Telegram[/bold]\n")
    console.print(
        "Enter public Telegram channel usernames (without @ or t.me/s/ prefix)."
    )
    console.print("Example: [bold]zaihuapd[/bold] for https://t.me/s/zaihuapd\n")

    channels_input = Prompt.ask(
        "Channel names (comma-separated)",
        default="",
    ).strip()

    channel_names = [c.strip() for c in channels_input.split(",") if c.strip()]

    if not channel_names:
        config.sources.telegram = TelegramConfig(enabled=False, channels=[])
        console.print("[yellow]  Telegram: skipped (no channels)[/yellow]\n")
        return config

    channels = [
        TelegramChannelConfig(channel=name, fetch_limit=20, enabled=True)
        for name in channel_names
    ]
    config.sources.telegram = TelegramConfig(enabled=True, channels=channels)
    console.print(f"  ✓ {len(channels)} channel(s) configured\n")
    return config


def show_summary(config: Config):
    table = Table(title="Configuration Summary", show_header=True, header_style="bold")
    table.add_column("Platform", width=12)
    table.add_column("Status", width=40)

    tw = config.sources.twitter
    if tw and tw.enabled and (tw.users or tw.keywords):
        token_ok = "✓" if os.environ.get("APIFY_TOKEN") else "⚠ no token"
        parts = []
        if tw.users:
            users = ", ".join(f"@{u}" for u in tw.users)
            parts.append(f"{len(tw.users)} user(s): {users}")
        if tw.keywords:
            parts.append(f"keywords: {', '.join(tw.keywords)}")
        status = "  |  ".join(["; ".join(parts), token_ok])
        table.add_row("Twitter", status)
    else:
        table.add_row("Twitter", "[dim]disabled[/dim]")

    tg = config.sources.telegram
    if tg and tg.enabled and tg.channels:
        channels = ", ".join(c.channel for c in tg.channels)
        table.add_row("Telegram", f"{len(tg.channels)} channel(s): {channels}")
    else:
        table.add_row("Telegram", "[dim]disabled[/dim]")

    console.print()
    console.print(table)
    console.print()


def _disable_other_sources(config: Config) -> Config:
    for src in config.sources.github:
        src.enabled = False
    config.sources.hackernews.enabled = False
    for src in config.sources.rss:
        src.enabled = False
    config.sources.reddit.enabled = False
    if config.sources.openbb:
        config.sources.openbb.enabled = False
    config.sources.ossinsight.enabled = False
    return config


def main():
    load_dotenv()
    print_banner()

    storage = StorageManager(data_dir="data")

    try:
        config = storage.load_config()
    except FileNotFoundError:
        console.print(
            "[yellow]No config.json found. Run [bold]uv run horizon-wizard[/bold] "
            "first to set up AI and basic settings.[/yellow]"
        )
        sys.exit(1)

    config = _disable_other_sources(config)
    config = configure_twitter(config)
    config = configure_telegram(config)
    show_summary(config)

    tw_enabled = bool(
        config.sources.twitter
        and config.sources.twitter.enabled
        and (config.sources.twitter.users or config.sources.twitter.keywords)
    )
    tg_enabled = bool(
        config.sources.telegram
        and config.sources.telegram.enabled
        and config.sources.telegram.channels
    )

    if not tw_enabled and not tg_enabled:
        console.print("[yellow]No sources configured. Nothing to save.[/yellow]")
        sys.exit(0)

    save = Confirm.ask("\nSave configuration?", default=True)
    if not save:
        console.print("[yellow]Cancelled.[/yellow]")
        sys.exit(0)

    storage.save_config(config, backup=True)
    console.print(f"[green]✓ Configuration saved to {storage.config_path}[/green]\n")

    run_now = Confirm.ask("Run horizon now?", default=True)
    if run_now:
        console.print("[cyan]Starting horizon...[/cyan]\n")
        try:
            subprocess.run(
                [sys.executable, "-m", "src.main"],
                check=False,
            )
        except FileNotFoundError:
            console.print(
                "[red]Failed to launch horizon. Run [bold]uv run horizon[/bold] manually.[/red]"
            )
    else:
        console.print(
            "\n[dim]Run [bold]uv run horizon[/bold] when you're ready.[/dim]"
        )


if __name__ == "__main__":
    main()
