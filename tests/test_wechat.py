"""Unit tests for WeChat article renderer (new group-based API)."""

from datetime import datetime, timezone

from src.ai.wechat import (
    GroupResult,
    ClassificationResult,
    WeChatFormatter,
)
from src.models import ContentItem, SourceType


def _make_item(idx: int, **overrides) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=overrides.pop("title", f"Important Item {idx}"),
        url=overrides.pop("url", f"https://example.com/items/{idx}"),
        content="content",
        author="tester",
        published_at=datetime(2026, 4, 25, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = overrides.pop("ai_score", 8.0)
    item.ai_summary = overrides.pop("ai_summary", f"Summary for item {idx}.")
    item.ai_tags = overrides.pop("ai_tags", ["AI", "News"])
    meta = item.metadata
    meta["title_zh"] = overrides.pop("title_zh", f"重要消息 {idx}")
    return item


def _classification(
    groups: list[tuple[str, str, list[ContentItem]]],
    insight_headline: str = "",
    insight_body: str = "",
) -> ClassificationResult:
    return ClassificationResult(
        groups=[GroupResult(name=n, report=r, items=its) for n, r, its in groups],
        insight_headline=insight_headline,
        insight_body=insight_body,
    )


class TestWeChatFormatter:
    def test_generate_article_returns_html(self):
        formatter = WeChatFormatter()
        items = [_make_item(1)]
        classification = _classification([("你的服务器可能正在裸奔", "/proc没有校验很危险。", items)])
        result = formatter.generate_article(classification, "2026-06-07")

        assert isinstance(result, str)
        assert len(result) > 0
        assert result.startswith("<section")
        assert result.endswith("</section>")
        assert "技术信号" in result
        assert "2026.06.07" in result
        assert "你的服务器可能正在裸奔" in result
        assert "/proc没有校验很危险" in result

    def test_generate_article_empty_classification(self):
        formatter = WeChatFormatter()
        classification = ClassificationResult(groups=[])
        result = formatter.generate_article(classification, "2026-06-07")
        assert result == ""

    def test_generate_article_multiple_groups(self):
        formatter = WeChatFormatter()
        items_a = [_make_item(1)]
        items_b = [_make_item(2)]
        classification = _classification([
            ("你的服务器可能正在裸奔", "/proc安全很重要。", items_a),
            ("两个被忽视的性能盲区", "Go微架构和队列陷阱。", items_b),
        ])
        result = formatter.generate_article(classification, "2026-06-07")

        assert "你的服务器可能正在裸奔" in result
        assert "两个被忽视的性能盲区" in result
        assert "/proc安全很重要。" in result
        assert "Go微架构和队列陷阱。" in result

    def test_item_link_in_output(self):
        formatter = WeChatFormatter()
        item = _make_item(1)
        classification = _classification([("动态", "解读", [item])])
        result = formatter.generate_article(classification, "2026-06-07")

        assert "▸" in result
        assert "example.com" in result
        assert "重要消息 1" in result

    def test_insight_headline_rendered_when_present(self):
        formatter = WeChatFormatter()
        items = [_make_item(1)]
        classification = _classification(
            [("动态", "解读", items)],
            insight_headline="从内核到架构",
            insight_body="今天信号指向系统思维。",
        )
        result = formatter.generate_article(classification, "2026-06-07")

        assert "从内核到架构" in result
        assert "今天信号指向系统思维。" in result

    def test_insight_skipped_when_empty(self):
        formatter = WeChatFormatter()
        items = [_make_item(1)]
        classification = _classification([("动态", "解读", items)])
        result = formatter.generate_article(classification, "2026-06-07")

        assert "技术信号" in result
        assert "动态" in result

    def test_group_with_multiple_items(self):
        formatter = WeChatFormatter()
        items = [_make_item(1), _make_item(2)]
        classification = _classification([("两个盲区", "优化要全链路审视。", items)])
        result = formatter.generate_article(classification, "2026-06-07")

        assert "重要消息 1" in result
        assert "重要消息 2" in result
        assert "优化要全链路审视。" in result

    def test_no_tags_or_score_in_output(self):
        formatter = WeChatFormatter()
        item = _make_item(1, ai_tags=["security", "Linux"], ai_score=9.0)
        classification = _classification([("安全", "解读", [item])])
        result = formatter.generate_article(classification, "2026-06-07")

        assert "#security" not in result
        assert "⭐" not in result
        assert "9.0" not in result

    def test_no_focus_label(self):
        formatter = WeChatFormatter()
        items = [_make_item(1), _make_item(2)]
        classification = _classification([("类别", "解读", items)])
        result = formatter.generate_article(classification, "2026-06-07")

        assert "🔥 焦点" not in result
        assert "🔥" not in result or "🔥 焦点" not in result
