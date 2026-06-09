"""WeChat Official Account article generator.

Two-stage pipeline:
1. WeChatClassifier — LLM groups items into insight groups + writes report
2. WeChatFormatter — renders ClassificationResult into WeChat-compatible HTML

No enrichment fields are modified — classification lives in a transient result object.
"""

import html
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

from ..models import ContentItem
from .client import AIClient
from .prompts import CLASSIFICATION_SYSTEM, CLASSIFICATION_USER
from .utils import parse_json_response


# ── Transient result types ──────────────────────────────────────────────


@dataclass
class GroupResult:
    name: str
    report: str
    items: List[ContentItem]


@dataclass
class ClassificationResult:
    groups: List[GroupResult]
    excluded: List[ContentItem] = field(default_factory=list)
    insight_headline: str = ""
    insight_body: str = ""


# ── Classifier ──────────────────────────────────────────────────────────


class WeChatClassifier:
    """LLM-powered classifier that groups items into insight groups."""

    # ── Density-based group pruning constants ────────────────────────────
    MAX_CANDIDATE_GROUPS = 8
    DENSE_THRESHOLD = 3.0
    SPARSE_THRESHOLD = 1.0
    MIN_GROUPS = 4
    MAX_GROUPS = 8
    TOP_K_FOR_VALUE = 3

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    def _group_value(self, group: GroupResult, all_items: List[ContentItem]) -> float:
        """Group value = mean of top-K item ai_scores in the group."""
        scores = sorted((item.ai_score or 0.0 for item in group.items), reverse=True)
        top_k = scores[: self.TOP_K_FOR_VALUE]
        return sum(top_k) / len(top_k) if top_k else 0.0

    def _compute_max_groups(self, groups: List[GroupResult]) -> int:
        """Compute max groups to keep (4-8) based on average item density per group."""
        if not groups:
            return self.MIN_GROUPS
        total_items = sum(len(g.items) for g in groups)
        avg_density = total_items / len(groups)
        if avg_density >= self.DENSE_THRESHOLD:
            return self.MIN_GROUPS
        if avg_density <= self.SPARSE_THRESHOLD:
            return self.MAX_GROUPS
        # Linear interpolation between thresholds
        return round(
            self.MAX_GROUPS
            - (avg_density - self.SPARSE_THRESHOLD)
            * (self.MAX_GROUPS - self.MIN_GROUPS)
            / (self.DENSE_THRESHOLD - self.SPARSE_THRESHOLD)
        )

    async def classify(self, items: List[ContentItem]) -> ClassificationResult:
        if not items:
            return ClassificationResult(groups=[])

        item_lines = []
        for i, item in enumerate(items):
            meta = item.metadata
            title_zh = meta.get("title_zh") or str(item.title) or ""
            whats_new = (meta.get("whats_new_zh") or "")[:200]
            why_matters = (meta.get("why_it_matters_zh") or "")[:200]
            discussion = (meta.get("community_discussion_zh") or "")[:200]
            details = (meta.get("key_details_zh") or "")[:200]
            tags = ", ".join(item.ai_tags or [])
            score = item.ai_score or 0.0
            source = item.source_type.value if item.source_type else ""
            item_lines.append(
                f"[{i}]\n"
                f"  title: {title_zh}\n"
                f"  whats_new: {whats_new}\n"
                f"  why_it_matters: {why_matters}\n"
                f"  community_discussion: {discussion}\n"
                f"  key_details: {details}\n"
                f"  tags: [{tags}]\n"
                f"  score: {score}\n"
                f"  source: {source}\n"
            )

        items_text = "\n".join(item_lines)

        response = await self.client.complete(
            system=CLASSIFICATION_SYSTEM,
            user=CLASSIFICATION_USER.format(items=items_text),
        )
        result = parse_json_response(response)
        if result is None or "groups" not in result:
            return ClassificationResult(groups=[])

        insight_headline = (result.get("insight_headline") or "").strip()
        insight_body = (result.get("insight_body") or "").strip()

        raw_groups = result["groups"]
        if not isinstance(raw_groups, list):
            return ClassificationResult(groups=[])

        assigned = set()
        candidate_groups: List[GroupResult] = []
        for rg in raw_groups[: self.MAX_CANDIDATE_GROUPS]:
            name = (rg.get("name") or "").strip()
            if not name or len(name) > 30:
                continue
            report = (rg.get("report") or "").strip()
            if not report:
                continue
            indices = rg.get("item_indices", [])
            if not isinstance(indices, list):
                continue
            grp_items: List[ContentItem] = []
            for idx in indices:
                if not isinstance(idx, int):
                    continue
                if idx < 0 or idx >= len(items):
                    continue
                if idx in assigned:
                    continue
                assigned.add(idx)
                grp_items.append(items[idx])
            if not grp_items:
                continue
            candidate_groups.append(GroupResult(name=name, report=report, items=grp_items))

        # Sort by group value (descending) and prune by density
        candidate_groups.sort(key=lambda g: self._group_value(g, items), reverse=True)
        max_groups = self._compute_max_groups(candidate_groups)
        groups = candidate_groups[:max_groups]

        # Recompute assigned based on final groups
        assigned = set()
        for g in groups:
            for item in g.items:
                # Find the index of this item in the original list
                for i, orig_item in enumerate(items):
                    if orig_item is item:
                        assigned.add(i)
                        break

        excluded = [item for i, item in enumerate(items) if i not in assigned]

        return ClassificationResult(
            groups=groups,
            excluded=excluded,
            insight_headline=insight_headline,
            insight_body=insight_body,
        )


# ── HTML rendering helpers ──────────────────────────────────────────────


def _link(url: str, text: str) -> str:
    return (
        f'<a href="{url}" '
        f'target="_blank" rel="noopener noreferrer" '
        f'data-link="true">{text}</a>'
    )


# ── Formatter ───────────────────────────────────────────────────────────


class WeChatFormatter:
    """Renders a ClassificationResult into WeChat-compatible HTML."""

    def __init__(self, brand_name: str = "技术信号"):
        self.brand_name = brand_name

    # ── Article generation ────────────────────────────────────────────

    def generate_article(
        self,
        classification: ClassificationResult,
        date: str,
    ) -> str:
        groups = classification.groups
        if not groups:
            return ""

        parts: List[str] = []

        # ── Outer container ──
        parts.append(
            '<section style="padding: 24px 20px 32px; '
            'font-size: 16px; line-height: 1.75; '
            'color: rgb(44,44,42); '
            'font-family: -apple-system-font, BlinkMacSystemFont, Helvetica Neue, '
            'PingFang SC, Hiragino Sans GB, Microsoft YaHei UI, Microsoft YaHei, '
            'Arial, sans-serif; background: #FAF9F5;">'
        )

        # Layer 1: Masthead (includes separator)
        parts.append(self._render_masthead(date))

        # Layer 2: Insight
        if classification.insight_headline:
            parts.append(self._render_insight(
                classification.insight_headline,
                classification.insight_body,
            ))

        # Layer 3: Signal groups
        for gi, group in enumerate(groups):
            parts.append(self._render_group(group, gi + 1))

        # Layer 4: Footer (includes separator)
        parts.append(self._render_footer())

        parts.append("</section>")
        return "\n".join(parts)

    # ── Layer 1: Masthead ─────────────────────────────────────────────

    def _render_masthead(self, date: str) -> str:
        formatted_date = date.replace("-", ".")
        return (
            '<section style="text-align: center; padding: 0 0 4px;">'
            '<p style="margin: 0 0 16px;">'
            f'<span style="font-size: 13px; color: #87867F;">'
            f'{self.brand_name} · {formatted_date}</span></p>'
            '<p style="margin: 0;"><span style="color: #D1CFC5;">'
            '─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─</span></p>'
            '</section>'
        )

    # ── Layer 2: Insight ──────────────────────────────────────────────

    def _render_insight(self, headline: str, body: str) -> str:
        parts: List[str] = []
        parts.append(
            '<section style="padding: 20px 24px; '
            'border-left: 4px solid #0F4C81; '
            'border-radius: 8px; '
            'background: rgba(15,76,129,0.04); '
            'margin: 24px 0;">'
        )
        parts.append(
            '<p style="margin: 0 0 10px; '
            'font-family: Georgia, \'Times New Roman\', \'PingFang SC\', serif; '
            'font-size: 22px; line-height: 1.3; font-weight: 550; '
            'letter-spacing: -0.01em; color: rgb(44,44,42);">'
            f'{headline}</p>'
        )
        if body:
            parts.append(
                '<p style="margin: 0; font-size: 14px; line-height: 1.7; '
                'color: #87867F;">'
                f'{body}</p>'
            )
        parts.append('</section>')
        return "\n".join(parts)

    # ── Layer 3: Group ────────────────────────────────────────────────

    def _render_group(self, group: GroupResult, index: int) -> str:
        lines: List[str] = [f'<section style="margin: 28px 0;">']

        numeral = str(index)

        # Title block: number track + group name, shared left border
        lines.append(
            '<p style="margin: 0 0 12px; padding-left: 14px; '
            'border-left: 4px solid #0F4C81;">'
            f'<span style="font-size: 16px; color: #555555; '
            f'font-family: -apple-system-font, BlinkMacSystemFont, Helvetica Neue, '
            f'PingFang SC, Hiragino Sans GB, Microsoft YaHei UI, Microsoft YaHei, '
            f'Arial, sans-serif;">━ {numeral} ━</span> '
            f'<span style="font-family: Georgia, \'Times New Roman\', \'PingFang SC\', serif; '
            f'font-size: 17px; font-weight: 550; color: rgb(44,44,42);">'
            f'{html.escape(group.name)}</span></p>'
        )

        # Report body
        lines.append(
            '<p style="margin: 0 0 14px; padding-left: 18px; '
            'font-size: 15px; line-height: 1.8; color: rgb(44,44,42);">'
            f'{html.escape(group.report)}</p>'
        )

        # Item links with enriched detail
        for item in group.items:
            title = item.metadata.get("title_zh") or str(item.title) or ""
            url = str(item.url) if item.url else ""
            detail = item.metadata.get("detailed_summary_zh") or ""
            lines.append(
                '<p style="margin: 8px 0 0; padding-left: 18px; '
                'font-size: 15px; line-height: 1.7; color: rgb(44,44,42);">'
                f'▶ {_link(url, html.escape(title))}</p>'
            )
            if detail:
                lines.append(
                    '<p style="margin: 4px 0 0; padding-left: 34px; '
                    'font-size: 14px; line-height: 1.6; color: #555555;">'
                    f'{html.escape(detail)}</p>'
                )

        lines.append('</section>')
        return "\n".join(lines)

    # ── Layer 4: Footer ───────────────────────────────────────────────

    def _render_footer(self) -> str:
        return (
            '<section style="text-align: center; padding: 24px 0 0;">'
            '<p style="margin: 0 0 16px;"><span style="color: #D1CFC5;">'
            '─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─</span></p>'
            '<p style="margin: 0;">'
            f'<span style="font-size: 12px; color: #87867F;">📮 明天见。</span></p>'
            '</section>'
        )


# ── Convenience wrapper ────────────────────────────────────────────────


async def generate_article(
    items: List[ContentItem],
    date: str,
    ai_client: AIClient,
    brand_name: str = "技术信号",
) -> str:
    """Convenience wrapper: classify then render in one call."""
    classifier = WeChatClassifier(ai_client)
    classification = await classifier.classify(items)
    fmt = WeChatFormatter(brand_name=brand_name)
    return fmt.generate_article(classification, date)


async def generate_article_from_file(
    filepath: str,
    date: str,
    ai_client: AIClient,
    brand_name: str = "技术信号",
) -> str:
    """Parse a summary items JSON file and generate a WeChat article."""
    items = load_summary_items(filepath)
    return await generate_article(items, date, ai_client, brand_name)


# ── Load summary items ──────────────────────────────────────────────────


def load_summary_items(json_path: str) -> List[ContentItem]:
    """Load ContentItems from a summary items JSON file.

    Args:
        json_path: Path to the ``.json`` file saved by ``StorageManager.save_summary_items``.
    """
    p = Path(json_path)
    if not p.exists():
        raise FileNotFoundError(f"Summary items file not found: {p}")
    data = json.loads(p.read_text(encoding="utf-8"))
    return [ContentItem.model_validate(item) for item in data]
