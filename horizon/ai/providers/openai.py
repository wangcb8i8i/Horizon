"""OpenAI-compatible provider implementation."""

from __future__ import annotations

import logging

from openai import AsyncOpenAI

from scrapers.plugin import ContentItem

from ..processor import (
    AIFilterResult,
    AIProcessor,
    _load_pair,
    _parse_filter_response,
)

logger = logging.getLogger(__name__)


class OpenAIProcessor(AIProcessor):
    """AI processor using any OpenAI-compatible API endpoint.

    Works with:
    - OpenAI API (https://api.openai.com/v1)
    - vLLM / Ollama (local)
    - Any OpenAI-compatible proxy
    """

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        *,
        scoring_section: str = "",
        timeout: float = 30.0,
    ) -> None:
        self._client = AsyncOpenAI(api_key=api_key, base_url=base_url, timeout=timeout)
        self._model = model
        self._scoring_section = scoring_section

    async def filter(self, item: ContentItem) -> AIFilterResult:
        system, user = _load_pair(
            "filter",
            title=item.title or "",
            source_type=item.source_type,
            content=item.content or "",
            scoring_section=self._scoring_section,
        )
        if not user:
            return AIFilterResult(parsed=False, reason="prompt_not_found")

        text = await self._call(system, user)
        return _parse_filter_response(text)

    async def summarize(self, item: ContentItem) -> str:
        system, user = _load_pair(
            "summarize",
            title=item.title or "",
            author=item.author or "",
            source_type=item.source_type,
            content=item.content or "",
        )
        if not user:
            return ""

        text = await self._call(system, user)
        return text.strip()

    async def _call(
        self,
        system: str,
        user: str,
        *,
        max_tokens: int = 1024,
        temperature: float = 0.1,
    ) -> str:
        """Low-level LLM call."""
        try:
            resp = await self._client.chat.completions.create(
                model=self._model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            content = resp.choices[0].message.content
            return content or ""
        except Exception as exc:
            logger.error("LLM call failed (%s): %s", self._model, exc)
            raise
