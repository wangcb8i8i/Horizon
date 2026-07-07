"""YouTube scraper — framework plugin."""

import asyncio
import json
import logging
import re
import subprocess
from datetime import datetime, timezone
from typing import List, Optional

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)

_YTDLP_CMD = "yt-dlp"
_CHANNEL_ID_RE = re.compile(r"^UC[\w-]{22}$")


class YouTubeScraper(BaseScraper):
    name = "youtube"
    description = "YouTube channel videos via yt-dlp"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.cfg = plugin_config

        categories = plugin_config.get("_filter_categories")
        raw_channels: list = plugin_config.get("channels", []) or []

        channels: list[dict] = []
        for ch in raw_channels:
            if isinstance(ch, str):
                handle = ch.strip()
                if handle:
                    channels.append({
                        "handle": handle,
                        "enabled": True,
                        "categories": [],
                        "fetch_limit": None,
                    })
            elif isinstance(ch, dict):
                handle = ch.get("handle", "").strip()
                if handle:
                    channels.append({
                        "handle": handle,
                        "enabled": ch.get("enabled", True),
                        "categories": ch.get("categories", []),
                        "fetch_limit": ch.get("fetch_limit"),
                    })

        if categories is not None:
            channels = [
                ch for ch in channels
                if ch["enabled"] and self._matches_categories(ch["categories"], categories)
            ]

        self._channels = channels
        self._global_fetch_limit = min(plugin_config.get("fetch_limit", 10), 50)

    @staticmethod
    def _matches_categories(ch_cats, filter_cats):
        if not ch_cats:
            return False
        if isinstance(ch_cats, str):
            cats_set = {ch_cats.strip().lower()}
        elif isinstance(ch_cats, list):
            cats_set = {c.strip().lower() for c in ch_cats if c and c.strip()}
        else:
            return False
        return bool(cats_set & filter_cats)

    @property
    def _channel_handles(self) -> list[str]:
        return [ch["handle"] for ch in self._channels]

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.cfg.get("enabled", True) or not self._channels:
            return []

        tasks = [self._fetch_channel(ch, since) for ch in self._channels]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        items = []
        for r in results:
            if isinstance(r, Exception):
                self._report_error("fetch", r)
            elif isinstance(r, list):
                items.extend(r)
        return items

    def _channel_url(self, channel: str) -> str:
        ch = channel.strip()
        if _CHANNEL_ID_RE.match(ch):
            return f"https://www.youtube.com/channel/{ch}/videos"
        handle = ch.lstrip("@")
        return f"https://www.youtube.com/@{handle}/videos"

    async def _fetch_channel(self, channel: dict, since: datetime) -> List[ContentItem]:
        handle = channel["handle"]
        url = self._channel_url(handle)
        logger.info("Fetching YouTube channel: %s", url)
        per_ch_limit = channel.get("fetch_limit") or self._global_fetch_limit

        # Build yt-dlp argument list, injecting framework proxy + socket
        # timeout so slow/blocked networks fail fast instead of hanging.
        args = [
            _YTDLP_CMD,
            "--dump-json",
            "--no-download",
            "--ignore-errors",
            "--socket-timeout", "15",
            url,
        ]
        proxy = getattr(self.framework_config, "proxy", None)
        if proxy:
            args[1:1] = ["--proxy", proxy]

        timeout = max(self.framework_config.timeout, 30.0)
        try:
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(), timeout=timeout
            )
        except asyncio.TimeoutError:
            try:
                proc.kill()
            except ProcessLookupError:
                pass
            logger.warning("yt-dlp timed out after %ss for %s", timeout, channel)
            return []
        except FileNotFoundError:
            logger.warning("yt-dlp not found; skipping YouTube channel %s", channel)
            return []

        if proc.returncode != 0:
            err = stderr.decode("utf-8", errors="replace")[:500]
            logger.warning("yt-dlp failed for %s: %s", channel, err)
            return []

        items = []
        for line in stdout.decode("utf-8", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            published = self._parse_published(entry)
            if published is None or published < since:
                continue

            video_id = entry.get("id")
            if not video_id:
                continue

            title = entry.get("title", "")
            description = entry.get("description", "") or ""
            # Collapse long descriptions
            if len(description) > 500:
                description = description[:497] + "..."

            items.append(
                ContentItem(
                    id=self._generate_id("youtube", "video", video_id),
                    source_type="youtube",
                    title=title,
                    url=f"https://www.youtube.com/watch?v={video_id}",
                    content=description,
                    author=entry.get("channel", entry.get("uploader", handle)),
                    published_at=published,
                    metadata={
                        "channel": handle,
                        "video_id": video_id,
                        "duration": entry.get("duration", 0),
                        "view_count": entry.get("view_count", 0),
                    },
                )
            )
            if len(items) >= per_ch_limit:
                break

        return items

    @staticmethod
    def _parse_published(entry: dict) -> Optional[datetime]:
        raw = entry.get("release_timestamp") or entry.get("timestamp")
        if raw:
            return datetime.fromtimestamp(raw, tz=timezone.utc)
        raw_str = entry.get("release_date") or entry.get("upload_date")
        if raw_str:
            try:
                return datetime.strptime(str(raw_str), "%Y%m%d").replace(tzinfo=timezone.utc)
            except ValueError:
                pass
        return None
