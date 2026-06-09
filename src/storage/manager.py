"""Storage manager for configuration and state persistence."""

import json
import os
import re
import shutil
from pathlib import Path
from typing import Any, List

from pydantic import ValidationError

from ..models import Config, ContentItem


# Matches ${VAR_NAME} in string config values. Names follow env-var rules
# (ASCII letters, digits, underscore; must not start with a digit).
_ENV_VAR_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")


def _expand_env_vars(value: Any) -> Any:
    """Recursively expand ``${VAR}`` references inside any string leaves.

    Containers (dicts, lists, tuples) are walked; non-string leaves are
    returned unchanged. Strings with no ``${...}`` tokens are returned
    unchanged. References to unset variables are **left as-is**, so
    ``${MISSING}`` round-trips to ``${MISSING}`` and surfaces as a clear
    downstream error rather than a silent empty string.

    This is intentionally identical to the behaviour ``RSSScraper`` uses
    for RSS feed URLs, so a single ``${VAR}`` convention works everywhere
    in the config (AI ``base_url``, feed URLs, webhook URLs, ...).
    """
    if isinstance(value, str):
        return _ENV_VAR_PATTERN.sub(
            lambda m: os.environ.get(m.group(1), m.group(0)),
            value,
        )
    if isinstance(value, dict):
        return {k: _expand_env_vars(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_env_vars(v) for v in value]
    if isinstance(value, tuple):
        return tuple(_expand_env_vars(v) for v in value)
    return value


class ConfigError(ValueError):
    """Raised when configuration is missing or invalid."""

    pass


class StorageManager:
    """Manages file-based storage for configuration and state."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.config_path = self.data_dir / "config.json"
        self.summaries_dir = self.data_dir / "summaries"

        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.summaries_dir.mkdir(parents=True, exist_ok=True)

    def save_wechat_article(self, date: str, html: str, output_dir: str = "data/wechat") -> str:
        """Save WeChat-compatible HTML article to disk.

        Args:
            date: Date string (YYYY-MM-DD).
            html: WeChat article HTML content.
            output_dir: Output directory path.

        Returns:
            str: Path to the saved file.
        """
        dir_path = Path(output_dir)
        dir_path.mkdir(parents=True, exist_ok=True)
        file_path = dir_path / f"{date}.html"
        file_path.write_text(html, encoding="utf-8")
        return str(file_path)

    def load_config(self) -> Config:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Please create it based on the template in README.md"
            )

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(
                f"Invalid JSON in configuration file: {self.config_path}\n" f"Error: {e}"
            ) from e

        # Expand ${VAR} references in every string value before pydantic
        # validation. Keeps credentials / private endpoints / tenant IDs
        # out of the JSON file so it is safe to commit to a public repo.
        data = _expand_env_vars(data)

        try:
            return Config.model_validate(data)
        except ValidationError as e:
            raise ConfigError(
                f"Configuration validation failed for {self.config_path}\n"
                f"Details: {e}"
            ) from e

    def save_config(self, config: Config, backup: bool = True) -> Path:
        """Save configuration to config.json, optionally backing up the existing file.

        Args:
            config: The Config object to save.
            backup: If True and config.json exists, copy it to config.json.bak first.

        Returns:
            Path to the saved config file.
        """
        if backup and self.config_path.exists():
            shutil.copy2(self.config_path, self.config_path.with_suffix(".json.bak"))

        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config.model_dump(mode="json"), f, indent=2, ensure_ascii=False)
            f.write("\n")

        return self.config_path

    def save_raw_items(self, date: str, items: list) -> Path:
        raw_dir = self.data_dir / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

        filepath = raw_dir / f"{date}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            data = [item.model_dump(mode="json") for item in items]
            json.dump(data, f, indent=2, ensure_ascii=False)
        return filepath

    def save_daily_summary(self, date: str, markdown: str, language: str = "en") -> Path:
        filename = f"horizon-{date}-{language}.md"
        filepath = self.summaries_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        return filepath

    def save_summary_items(self, date: str, items: List[ContentItem], language: str = "en") -> Path:
        """Save ContentItems as a JSON sidecar alongside the daily summary markdown.

        This provides a stable structured data source for downstream consumers
        (e.g. WeChat article generation) without fragile markdown parsing.
        """
        filename = f"horizon-{date}-{language}.json"
        filepath = self.summaries_dir / filename
        data = [item.model_dump(mode="json") for item in items]
        filepath.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return filepath

    def load_subscribers(self) -> list:
        """Loads the list of email subscribers."""
        subscribers_path = self.data_dir / "subscribers.json"
        if not subscribers_path.exists():
            return []

        try:
            with open(subscribers_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def add_subscriber(self, email_addr: str):
        """Adds a new subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr not in subscribers:
            subscribers.append(email_addr)
            self._save_subscribers(subscribers)

    def remove_subscriber(self, email_addr: str):
        """Removes a subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr in subscribers:
            subscribers.remove(email_addr)
            self._save_subscribers(subscribers)

    def _save_subscribers(self, subscribers: list):
        """Helper to save subscribers list."""
        subscribers_path = self.data_dir / "subscribers.json"
        with open(subscribers_path, "w", encoding="utf-8") as f:
            json.dump(subscribers, f, indent=2)
