"""Shared AI utility functions."""

import html
import json
import re
from typing import Optional


_RE_HTML = re.compile(r"<[^>]+>")

# Items with fewer than this many meaningful characters after cleanup are noise.
_MIN_MEANINGFUL_CHARS = 30


def clean_item_text(raw: str | None, max_chars: int = 600) -> str:
    """Strip HTML, collapse whitespace, and filter noise.

    Returns the cleaned text (≤ *max_chars* characters), or an empty string
    when the content is considered noise (too short or no real substance).
    """
    if not raw:
        return ""

    # Strip HTML tags
    text = _RE_HTML.sub("", raw)

    # Unescape HTML entities
    text = html.unescape(text)

    # Preserve paragraph breaks; collapse intra-paragraph whitespace
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)  # lone newline → space
    text = re.sub(r"[^\S\n]+", " ", text)           # horiz whitespace → single space
    text = re.sub(r"\n{3,}", "\n\n", text)          # 3+ newlines → paragraph break
    text = text.strip()

    # Strip known noise prefixes/suffixes left by aggregators
    text = re.sub(
        r"^Title trimmed slightly without altering meaning\.?\s*", "", text
    )
    text = re.sub(r"\s*Comments?\s*$", "", text, flags=re.IGNORECASE)

    text = text.strip()

    if len(text) < _MIN_MEANINGFUL_CHARS:
        return ""

    return text[:max_chars]


def parse_json_response(response: str) -> Optional[dict]:
    """Try multiple strategies to extract a JSON object from an AI response.

    Returns the parsed dict, or None if all strategies fail.
    """
    text = response.strip()

    # Strategy 1: direct parse
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        pass

    # Strategy 2: extract from ```json ... ``` code block
    if "```json" in text:
        try:
            json_str = text.split("```json")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 3: extract from ``` ... ``` code block
    if "```" in text:
        try:
            json_str = text.split("```")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 4: find the first { ... } block using brace matching
    start = text.find("{")
    if start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start : i + 1])
                    except (json.JSONDecodeError, ValueError):
                        break

    # Strategy 5: regex extraction as last resort
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group())
        except (json.JSONDecodeError, ValueError):
            pass

    return None
