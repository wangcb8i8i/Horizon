"""Text processing utilities for scrapers."""

from __future__ import annotations

import html
import re

# Tags that separate paragraphs/blocks — both opening and closing variants
# produce a newline so content doesn't run together.
_BLOCK_TAGS = (
    "p|div|h[1-6]|blockquote|li|tr|dd|dt|pre|ol|ul|dl|table|section|article|nav|header|footer"
)
_RE_OPEN_BLOCK = re.compile(
    rf"<\s*(?:{_BLOCK_TAGS})(?:\s[^>]*)?\s*>",
    re.IGNORECASE,
)
_RE_CLOSE_BLOCK = re.compile(
    rf"<\s*/\s*(?:{_BLOCK_TAGS})\s*>",
    re.IGNORECASE,
)
_RE_LINE_BREAK = re.compile(r"<br\s*/?>", re.IGNORECASE)
_RE_HORIZONTAL = re.compile(r"<hr\s*/?>", re.IGNORECASE)
_RE_ANY_TAG = re.compile(r"<[^>]+>")


def clean_html(text: str) -> str:
    """Convert HTML to readable plain text.

    * Unescapes HTML entities (``&#x27;`` → ``'``, ``&amp;`` → ``&``)
    * Strips all tags while preserving paragraph-like structure
    * Normalises horizontal whitespace without collapsing paragraph breaks
    """
    if not text:
        return ""

    # 1. Unescape HTML entities
    text = html.unescape(text)

    # 2. Self-closing line/block elements
    text = _RE_LINE_BREAK.sub("\n", text)
    text = _RE_HORIZONTAL.sub("\n---\n", text)

    # 3. Block-level open/close tags → newlines
    text = _RE_CLOSE_BLOCK.sub("\n", text)
    text = _RE_OPEN_BLOCK.sub("\n", text)

    # 4. Strip any remaining tags
    text = _RE_ANY_TAG.sub("", text)

    # 5. Normalise whitespace
    text = re.sub(r"[ \t]+", " ", text)       # collapse horizontal
    text = re.sub(r"\n{3,}", "\n\n", text)    # at most one blank line

    # 6. Trim leading/trailing whitespace per line
    text = "\n".join(line.strip() for line in text.split("\n"))

    return text.strip()
