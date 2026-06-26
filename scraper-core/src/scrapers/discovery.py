"""Plugin discovery: scan a directory for scraper plugins.

Usage::

    from scrapers.discovery import ScraperScanner

    scanner = ScraperScanner("scrapers/")
    plugins = scanner.scan()          # discovers + registers
"""

from __future__ import annotations

import importlib.util
import logging
import sys
from pathlib import Path
from types import ModuleType
from typing import List, Optional, Set, Type

from .plugin import BaseScraper, PluginInfo, ScraperRegistry

logger = logging.getLogger(__name__)


class ScraperScanner:
    """Discover and register :class:`BaseScraper` subclasses from a directory.

    Scans a directory for ``.py`` modules, imports each, and registers
    every ``BaseScraper`` subclass found.  Files whose names start with
    ``_`` (e.g. ``__init__.py``, ``_helpers.py``) are skipped.

    The scan directory does **not** need an ``__init__.py`` — the scanner
    uses ``importlib.util.spec_from_file_location`` to load files as
    standalone modules.
    """

    def __init__(self, scan_dir: str | Path = "scrapers") -> None:
        self.scan_dir = Path(scan_dir)

    # ── public API ──────────────────────────────────────────────────────

    def scan(self, recursive: bool = False, register: bool = True) -> List[PluginInfo]:
        """Discover plugins under ``self.scan_dir``.

        Args:
            recursive: If True, walk subdirectories recursively.
            register:  If True (default), register each discovered plugin
                       with ``ScraperRegistry`` automatically.

        Returns:
            List of ``PluginInfo`` for newly discovered plugins.
            Only returns plugins that were actually registered (skips
            files with import errors or no valid ``BaseScraper``
            subclass).
        """
        if not self.scan_dir.exists():
            logger.warning("Scanner directory not found: %s", self.scan_dir)
            return []

        discovered: List[PluginInfo] = []
        seen_before: Set[str] = set(ScraperRegistry.all_names())

        for py_file in self._iter_py_files(recursive):
            plugins = self._load_and_find_plugins(py_file)
            for info in plugins:
                name = info.name
                if name in seen_before:
                    logger.debug("Plugin '%s' already registered, skipping", name)
                    continue
                seen_before.add(name)
                if register:
                    try:
                        ScraperRegistry.register(info.cls)
                    except (TypeError, ValueError, KeyError) as exc:
                        logger.warning("Failed to register %s: %s", name, exc)
                        continue
                discovered.append(info)

        return discovered

    # ── internals ───────────────────────────────────────────────────────

    def _iter_py_files(self, recursive: bool):
        """Yield ``.py`` files, skipping those starting with ``_``."""
        method = self.scan_dir.rglob if recursive else self.scan_dir.glob
        for f in method("*.py"):
            # skip __init__.py, _private.py, _helpers.py etc.
            if f.stem.startswith("_"):
                continue
            yield f

    def _load_and_find_plugins(self, py_file: Path) -> List[PluginInfo]:
        """Import one ``.py`` file and extract ``BaseScraper`` subclasses."""
        mod = self._import_file(py_file)
        if mod is None:
            return []
        return self._extract_plugins(mod)

    def _import_file(self, py_file: Path) -> Optional[ModuleType]:
        """Import a ``.py`` file as a module (no ``__init__.py`` required)."""
        try:
            module_name = f"_scanner_{py_file.stem}"
            spec = importlib.util.spec_from_file_location(module_name, py_file)
            if spec is None or spec.loader is None:
                return None
            mod = importlib.util.module_from_spec(spec)
            # Keep in sys.modules so relative imports within the scanned
            # file work if the directory happens to be an importable package.
            sys.modules[module_name] = mod
            spec.loader.exec_module(mod)
            return mod
        except Exception:
            logger.warning(
                "Skipping %s: failed to import", py_file, exc_info=True
            )
            return None

    @staticmethod
    def _extract_plugins(mod: ModuleType) -> List[PluginInfo]:
        """Find all ``BaseScraper`` subclasses in a module."""
        plugins: List[PluginInfo] = []
        for name in dir(mod):
            obj = getattr(mod, name)
            if (
                isinstance(obj, type)
                and issubclass(obj, BaseScraper)
                and obj is not BaseScraper
                and not getattr(obj, "__abstractmethods__", None)  # concrete only
            ):
                plugins.append(
                    PluginInfo(
                        cls=obj,
                        name=obj.name,
                        description=obj.description,
                        config_schema=obj.config_schema(),
                    )
                )
        return plugins
