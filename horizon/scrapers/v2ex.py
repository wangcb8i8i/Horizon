"""V2EX scraper — framework plugin."""

import asyncio
import logging
import os
from datetime import datetime, timezone
from typing import List

import httpx

from scrapers.plugin import BaseScraper, ContentItem

logger = logging.getLogger(__name__)

_V2EX_BASE = "https://www.v2ex.com/api/v2"

# V2EX rate limits (unauthenticated: 10 req/60s, authenticated: 120 req/60s)
_UNAUTH_RATE = 8       # leave headroom under 10/60s
_AUTH_RATE = 100        # leave headroom under 120/60s
_RETRY_MAX = 3
_RETRY_BASE_DELAY = 1.0

# Status codes that are safe to retry
_RETRYABLE_STATUSES = frozenset({429, 502, 503, 504})


class V2exScraper(BaseScraper):
    name = "v2ex"
    description = "V2EX topics by node"
    has_categories = True

    def __init__(self, plugin_config, http_client, framework_config):
        super().__init__(plugin_config, http_client, framework_config)
        self.cfg = plugin_config

        categories = plugin_config.get("_filter_categories")
        raw_nodes = plugin_config.get("nodes", "")

        nodes: list[dict] = []
        if isinstance(raw_nodes, str):
            for n in raw_nodes.split(","):
                n = n.strip()
                if n:
                    nodes.append({"name": n, "enabled": True, "categories": [], "fetch_limit": None})
        elif isinstance(raw_nodes, list):
            for n in raw_nodes:
                if isinstance(n, str):
                    nodes.append({"name": n.strip(), "enabled": True, "categories": [], "fetch_limit": None})
                elif isinstance(n, dict):
                    name = n.get("name", "").strip()
                    if name:
                        nodes.append({
                            "name": name,
                            "enabled": n.get("enabled", True),
                            "categories": n.get("categories", []),
                            "fetch_limit": n.get("fetch_limit"),
                        })

        if categories is not None:
            nodes = [n for n in nodes if n["enabled"] and self._matches_categories(n["categories"], categories)]

        self._nodes = nodes
        self._global_fetch_limit = min(plugin_config.get("fetch_limit", 20), 50)
        token_env = plugin_config.get("token_env", "V2EX_TOKEN")
        self.token = os.environ.get(token_env)

        # Rate limiter — sequentialise requests with a sliding window semaphore
        rate = _AUTH_RATE if self.token else _UNAUTH_RATE
        self._rate_sem = asyncio.Semaphore(rate)
        self._rate_window = 62.0  # slightly wider than 60s to be safe

    @staticmethod
    def _matches_categories(node_cats, filter_cats):
        if not node_cats:
            return False
        if isinstance(node_cats, str):
            cats_set = {node_cats.strip().lower()}
        elif isinstance(node_cats, list):
            cats_set = {c.strip().lower() for c in node_cats if c and c.strip()}
        else:
            return False
        return bool(cats_set & filter_cats)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.cfg.get("enabled", True) or not self._nodes:
            return []

        # Sequential fetches with per-request rate limiting.
        # No asyncio.gather — V2EX rate limits make concurrency counterproductive.
        items: List[ContentItem] = []
        for node in self._nodes:
            try:
                result = await self._fetch_node(node, since)
                if isinstance(result, list):
                    items.extend(result)
            except Exception as e:
                self._report_error(f"node '{node['name']}'", e)
        return items

    async def _request_with_retry(
        self, url: str, headers: dict, params: dict
    ) -> httpx.Response:
        """GET with exponential-backoff retry for transient errors.

        Retries on:
        - Connection-level errors (``RemoteProtocolError``, ``TimeoutException``)
        - Retryable HTTP statuses (429, 502, 503, 504)
        """
        last_exc: Exception | None = None

        for attempt in range(1, _RETRY_MAX + 1):
            # Rate-limit: acquire slot before each request
            async with self._rate_sem:
                try:
                    resp = await self.client.get(
                        url,
                        headers=headers,
                        params=params,
                        follow_redirects=True,
                    )
                except httpx.RemoteProtocolError as e:
                    last_exc = e
                    delay = _RETRY_BASE_DELAY * (2 ** (attempt - 1))
                    logger.warning(
                        "V2EX connection lost (attempt %d/%d), retrying in %.1fs",
                        attempt, _RETRY_MAX, delay,
                    )
                    await asyncio.sleep(delay)
                    continue
                except httpx.TimeoutException as e:
                    last_exc = e
                    delay = _RETRY_BASE_DELAY * (2 ** (attempt - 1))
                    logger.warning(
                        "V2EX timeout (attempt %d/%d), retrying in %.1fs",
                        attempt, _RETRY_MAX, delay,
                    )
                    await asyncio.sleep(delay)
                    continue
                except httpx.RequestError as e:
                    # Transport-level errors (DNS, connection refused, etc.)
                    last_exc = e
                    delay = _RETRY_BASE_DELAY * (2 ** (attempt - 1))
                    logger.warning(
                        "V2EX request error (attempt %d/%d): %s, retrying in %.1fs",
                        attempt, _RETRY_MAX, e, delay,
                    )
                    await asyncio.sleep(delay)
                    continue

            # Retry on server-side / rate-limit statuses
            if resp.status_code in _RETRYABLE_STATUSES:
                if attempt < _RETRY_MAX:
                    delay = _RETRY_BASE_DELAY * (2 ** (attempt - 1))
                    logger.warning(
                        "V2EX %d (attempt %d/%d), retrying in %.1fs",
                        resp.status_code, attempt, _RETRY_MAX, delay,
                    )
                    await asyncio.sleep(delay)
                    continue
                # Last attempt failed — let raise_for_status surface the error
                last_exc = httpx.HTTPStatusError(
                    f"V2EX returned {resp.status_code} after {_RETRY_MAX} attempts",
                    request=resp.request,
                    response=resp,
                )
                break

            # Non-retryable status (4xx except 429, successful)
            resp.raise_for_status()
            return resp

        raise last_exc or httpx.HTTPError("V2EX request failed after all retries")

    async def _fetch_node(self, node: dict, since: datetime) -> List[ContentItem]:
        node_name = node["name"]
        per_node_limit = node.get("fetch_limit") or self._global_fetch_limit
        headers = {"User-Agent": "Horizon/1.0", "Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        try:
            resp = await self._request_with_retry(
                f"{_V2EX_BASE}/nodes/{node_name}/topics",
                headers=headers,
                params={"p": 1},
            )
        except httpx.HTTPError as e:
            logger.warning("V2EX fetch node '%s' failed: %s", node_name, e)
            return []

        if resp.status_code == 404:
            logger.warning("V2EX node '%s' not found", node_name)
            return []

        # V2EX API v2 returns the node list directly as a JSON array
        data = resp.json()
        topics = data if isinstance(data, list) else data.get("result", [])

        items = []
        for topic in topics[: per_node_limit]:
            raw_created = topic["created"]
            if isinstance(raw_created, int):
                created = datetime.fromtimestamp(raw_created, tz=timezone.utc)
            else:
                created = datetime.fromisoformat(raw_created.replace("Z", "+00:00"))
            if created < since:
                continue

            title = topic.get("title", "")
            tid = topic.get("id")
            node_name_out = topic.get("node", {}).get("name", node_name)
            member = topic.get("member", {})

            items.append(
                ContentItem(
                    id=self._generate_id("v2ex", node_name_out, str(tid)),
                    source_type="v2ex",
                    title=title,
                    url=f"https://www.v2ex.com/t/{tid}",
                    content=topic.get("content", "") or "",
                    author=member.get("username", "unknown"),
                    published_at=created,
                    metadata={
                        "node": node_name_out,
                        "replies": topic.get("replies", 0),
                        "likes": topic.get("likes", 0),
                    },
                )
            )
        return items
