"""WeChat Official Account API client — publish drafts with clickable links.

Decoupled from wechat.py (page rendering).  Callers pass in pre-rendered HTML.
"""

import os
import re
from html import unescape
from datetime import datetime, timedelta
from typing import Optional

import httpx


class WeChatAPIError(Exception):
    """WeChat API returned an error."""


class WeChatAPIClient:
    """Thin wrapper around the Official Account draft API.

    ``draft/add`` preserves ``<a>`` tags as clickable links — unlike
    copy-pasting HTML into the web editor.
    """

    BASE = "https://api.weixin.qq.com/cgi-bin"

    def __init__(
        self,
        app_id: str,
        app_secret: str,
        proxy: Optional[str] = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self._token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None
        self.proxy = proxy or os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY")

    async def _ensure_token(self) -> str:
        """Obtain or refresh an access_token (cached until 5 min before expiry)."""
        if self._token and self._token_expires_at and datetime.now() < self._token_expires_at:
            return self._token
        async with httpx.AsyncClient(proxy=self.proxy, timeout=15.0) as c:
            r = await c.get(
                f"{self.BASE}/token",
                params=dict(grant_type="client_credential", appid=self.app_id, secret=self.app_secret),
            )
        body = r.json()
        if body.get("errcode"):
            raise WeChatAPIError(f"get token failed: {body}")
        self._token = body["access_token"]
        self._token_expires_at = datetime.now() + timedelta(seconds=body["expires_in"] - 300)
        return self._token

    async def resolve_thumb_media_id(self, config) -> str:
        """Resolve a thumbnail media_id with fallback to material library.

        Priority:
          1. env var named by ``config.wechat.thumb_media_id_env``
          2. first image in WeChat material library
          3. error with setup instructions
        """
        wc = config.wechat
        if wc and wc.thumb_media_id_env:
            thumb_id = os.environ.get(wc.thumb_media_id_env)
            if thumb_id:
                return thumb_id

        token = await self._ensure_token()

        async with httpx.AsyncClient(proxy=self.proxy, timeout=15.0) as c:
            r = await c.post(
                f"{self.BASE}/material/batchget_material",
                params=dict(access_token=token),
                json=dict(type="image", offset=0, count=1),
            )
        body = r.json()
        items = body.get("item") or []
        if items:
            return items[0]["media_id"]

        name = wc.thumb_media_id_env if wc else "WECHAT_THUMB_MEDIA_ID"
        raise WeChatAPIError(
            "No cover image available.\n"
            f"  Option 1: Upload an image to WeChat material library (素材管理), "
            f"then retry.\n"
            f"  Option 2: Set env var `{name}` with a valid media_id."
        )

    @staticmethod
    def sanitize_html(html: str) -> str:
        """Adapt rendered HTML for the WeChat reader.

        Transformations:
          - Reduce side padding (WeChat viewer has its own margins).
          - Replace serif group-name font with sans-serif for mobile clarity.
        """
        html = html.replace("padding: 24px 20px 32px", "padding: 0 0 32px")
        html = html.replace("margin: 24px 0;", "margin: 0 0 24px;")
        html = html.replace("; background: #FAF9F5", "")
        html = html.replace(
            "Georgia, 'Times New Roman', 'PingFang SC', serif",
            "-apple-system-font, BlinkMacSystemFont, Helvetica Neue, "
            "PingFang SC, Hiragino Sans GB, Microsoft YaHei UI, "
            "Microsoft YaHei, Arial, sans-serif",
        )
        return html

    def _remove_masthead(self, content: str) -> str:
        """Strip the masthead <section> from the rendered HTML."""
        return re.sub(
            r'<section data-masthead[^>]*>.*?</section>',
            '',
            content,
            flags=re.DOTALL,
        )

    @staticmethod
    def _extract_insight(html: str) -> tuple[str, str]:
        """Parse insight_headline and insight_body from a rendered article's HTML.

        Relies on ``data-insight-headline`` / ``data-insight-body`` attributes
        written by ``WeChatFormatter._render_insight()``.
        """
        h = re.search(
            r'<p\s+data-insight-headline[^>]*>(.*?)</p>', html, re.DOTALL
        )
        headline = unescape(h.group(1).strip()) if h else ""
        b = re.search(
            r'<p\s+data-insight-body[^>]*>(.*?)</p>', html, re.DOTALL
        )
        body = unescape(b.group(1).strip()) if b else ""
        return headline, body

    async def create_draft(
        self,
        content: str,
        author: str = "",
        thumb_media_id: str = "",
        insight_headline: str = "",
        insight_body: str = "",
        date: str = "",
        brand_name: str = "",
    ) -> tuple[str, str, str]:
        """Create a draft in the WeChat Official Account.

        Args:
            content: Full article HTML (``<a>`` tags will be clickable).
            author: Display author name.
            thumb_media_id: Cover image media_id (upload first via ``material/add_material``).
            insight_headline: Used as article title (fallback: brand · date).
            insight_body: Used as digest (fallback: brand · date).
            date: Date string (YYYY-MM-DD) for fallback title/digest.
            brand_name: Brand name for fallback title/digest.

        Returns:
            Tuple of ``(media_id, title, digest)``.
        """
        author = author or brand_name
        dot_date = date.replace("-", ".")

        if not insight_headline or not insight_body:
            extracted_h, extracted_b = self._extract_insight(content)
            insight_headline = insight_headline or extracted_h
            insight_body = insight_body or extracted_b

        title = f"{dot_date} · {insight_headline}" if insight_headline else f"{brand_name} · {dot_date}"
        digest = insight_body if insight_body else f"{brand_name} · {dot_date}"

        content = self._remove_masthead(content)
        content = self.sanitize_html(content)
        token = await self._ensure_token()
        article = dict(
            title=title,
            author=author,
            digest=digest,
            content=content,
            content_source_url="",
            need_open_comment=0,
            only_fans_can_comment=0,
        )
        if thumb_media_id:
            article["thumb_media_id"] = thumb_media_id
        async with httpx.AsyncClient(proxy=self.proxy, timeout=15.0) as c:
            r = await c.post(
                f"{self.BASE}/draft/add",
                params=dict(access_token=token),
                json=dict(articles=[article]),
            )
        body = r.json()
        if body.get("errcode"):
            raise WeChatAPIError(f"draft/add failed: {body}")
        return body["media_id"], title, digest
