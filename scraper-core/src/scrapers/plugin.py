"""Plugin (Scraper) base class and lifecycle API.

Every scraper plugin is a subclass of ``BaseScraper``.  The framework
discovers, instantiates, and orchestrates plugins — each plugin only
needs to implement ``fetch()`` and declare its metadata.

Lifecycle (per run)::

    discover ──→ [for each plugin] ──→ setup() ──→ fetch(since) ──→ teardown()
                                                ↘  … (可能并发)  ↗
"""

from __future__ import annotations

import abc
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Type

import httpx
from pydantic import BaseModel


# ── Data model ──────────────────────────────────────────────────────────────

class ContentItem(BaseModel):
    """Single piece of content fetched by a plugin."""

    id: str
    source_type: str
    title: str
    url: str
    content: Optional[str] = None
    author: Optional[str] = None
    published_at: datetime
    fetched_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Dict[str, Any] = field(default_factory=dict)


# ── Standard HTTP config (managed by the framework) ─────────────────────────

class RateLimitConfig(BaseModel):
    requests: int = 10
    period_seconds: int = 60


class ScraperConfig(BaseModel):
    """Global framework-level HTTP client configuration."""

    timeout: float = 30.0
    max_retries: int = 3
    retry_delay: float = 1.0  # base delay, exponential backoff applied
    max_connections: int = 10
    proxy: Optional[str] = None
    rate_limit: Optional[RateLimitConfig] = None
    extra_headers: Dict[str, str] = {}


# ── Plugin base class ───────────────────────────────────────────────────────

class BaseScraper(abc.ABC):
    """Abstract scraper plugin.

    Subclass this and override ``fetch()``.  Optionally override
    ``setup()`` / ``teardown()`` for resource lifecycle.

    Class-level attributes (override in subclass)::

        name        — unique plugin identifier (used in logs, metrics)
        description — one-line human-readable summary

    Class-level method (override in subclass)::

        config_schema()  →  a pydantic BaseModel, or None
            Declares what plugin-specific config keys are expected.
            The framework validates consumer config against this before
            passing the ``plugin_config`` dict to ``__init__``.
    """

    # -- metadata (override in subclass) ---------------------------------
    name: str = ""
    description: str = ""

    def __init__(
        self,
        plugin_config: Dict[str, Any],
        http_client: httpx.AsyncClient,
        framework_config: ScraperConfig,
    ) -> None:
        """Initialize the plugin.

        Args:
            plugin_config: Plugin-specific configuration dict (validated
                against ``config_schema()`` if declared).
            http_client: Pre-configured async HTTP client.  The framework
                creates one ``AsyncClient`` per run and reuses it across
                all plugins.  *Do not* create your own client.
            framework_config: The active ``ScraperConfig`` for reference.
        """
        self.plugin_config = plugin_config
        self.client = http_client
        self.framework_config = framework_config

    # -- lifecycle hooks --------------------------------------------------

    async def setup(self) -> None:
        """Called once before the first ``fetch()``.  Optional.

        Use for one-time initialisation (validate credentials, warm
        caches, establish persistent connections).
        """
        pass

    async def teardown(self) -> None:
        """Called once after ``fetch()`` completes or raises.  Optional.

        Use for cleanup (close extra sessions, flush buffers).  Called
        even when ``fetch()`` raises an exception.
        """
        pass

    # -- core fetch -------------------------------------------------------

    @abc.abstractmethod
    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch items published after *since*.

        Args:
            since: Return items published **after** this UTC datetime.
                The framework sets this from the consumer's time window
                configuration.  Plugins that cannot filter by time (e.g.
                Hacker News top stories) should ignore the parameter and
                return everything — the framework deduplicates by URL.
            sdk: httpx.AsyncClient is available as ``self.client``.

        Returns:
            ``List[ContentItem]`` — may be empty.
            Must be JSON-serialisable (pydantic handles this).
        """
        ...

    # -- optional config schema -------------------------------------------

    @classmethod
    def config_schema(cls) -> Optional[Type[BaseModel]]:
        """Return the plugin-specific config pydantic model, or ``None``.

        Example::

            class MyConfig(BaseModel):
                api_key_env: str = "MY_API_KEY"
                fetch_limit: int = 10

            @classmethod
            def config_schema(cls) -> Optional[Type[BaseModel]]:
                return MyConfig

        The framework calls this once at registration time to validate
        the consumer's config for this plugin.
        """
        return None

    # -- helpers ----------------------------------------------------------

    def _generate_id(self, source: str, subtype: str, native_id: str) -> str:
        """Convenience: build a unique ``ContentItem.id``."""
        return f"{source}:{subtype}:{native_id}"


# ── Registry ────────────────────────────────────────────────────────────────

@dataclass
class PluginInfo:
    """Metadata about a registered plugin class."""
    cls: Type[BaseScraper]
    name: str
    description: str
    config_schema: Optional[Type[BaseModel]]


class ScraperRegistry:
    """Holds all discovered/registered scraper plugins.

    Usage (manual registration)::

        ScraperRegistry.register(MyScraper)

    Directory scanning will also call ``register()`` on discovery
    (see ``scrapers.discovery``).
    """

    _plugins: Dict[str, PluginInfo] = {}

    @classmethod
    def register(cls, plugin_cls: Type[BaseScraper]) -> None:
        """Register a scraper plugin class."""
        if not issubclass(plugin_cls, BaseScraper):
            raise TypeError(f"{plugin_cls.__name__} must subclass BaseScraper")
        name = plugin_cls.name
        if not name:
            raise ValueError(f"{plugin_cls.__name__} must set class attr 'name'")
        if name in cls._plugins:
            raise KeyError(f"Plugin '{name}' is already registered")
        desc = plugin_cls.description or ""
        schema = plugin_cls.config_schema()
        cls._plugins[name] = PluginInfo(plugin_cls, name, desc, schema)

    @classmethod
    def get(cls, name: str) -> Optional[PluginInfo]:
        return cls._plugins.get(name)

    @classmethod
    def all(cls) -> List[PluginInfo]:
        return list(cls._plugins.values())

    @classmethod
    def all_names(cls) -> List[str]:
        return list(cls._plugins.keys())

    @classmethod
    def clear(cls) -> None:
        cls._plugins.clear()
