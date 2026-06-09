```

horizon
├── 1. Load Config
│   └── data/config.json → Config (Pydantic)
│
├── 2. Check Email Subscriptions (当前禁用)
│   └── IMAP 扫描 SUBSCRIBE/UNSUBSCRIBE
│
├── 3. Determine Time Window
│   └── config.filtering.time_window_hours (默认 24h) 或 --hours 覆盖
│
├── 4. Fetch All Sources (asyncio.gather 并发)
│   ├── GitHub
│   │   ├── events (用户/组织事件流)
│   │   └── releases (仓库版本发布)
│   ├── Hacker News (Firebase API / topstories)
│   ├── RSS Feeds (feedparser)
│   ├── Reddit
│   │   ├── subreddits (热门/新帖)
│   │   └── users (用户动态)
│   ├── Telegram (公开频道抓取)
│   ├── Twitter/X (Apify)
│   │   ├── timeline
│   │   ├── search (关键词)
│   │   └── list
│   ├── OpenBB (财经新闻 SDK)
│   └── OSS Insight (趋势仓库 / 语言维度)
│   └── 所有 scraper 返回统一 List[ContentItem]
│
├── 5. Cross-Source Dedup
│   └── normalize URL → 同 URL 合并（保留内容最丰富的，合并 metadata）
│   └── save → data/raw/{date}.json
│
├── 6. AI Score (ContentAnalyzer.analyze_batch)
│   └── 每个 item 1 次 LLM 调用 (temperature=0.3, 重试 3 次)
│   │   ├── 输入: title + source + author + url + content[:800-1000] + discussion
│   │   └── 输出: score(0-10) + reason + summary + tags
│   └── 并发: analysis_concurrency=1 (可配)
│
├── 7. Filter by Threshold
│   ├── config.filtering.ai_score_threshold (默认 7.0)
│   ├── 保留 score >= threshold 的项
│   └── 按 score 降序排列
│
├── 8. Topic Dedup (merge_topic_duplicates)
│   └── 1 次 LLM 调用，识别同一事件的重复报道
│   │   ├── 输入: [index] title + tags + summary (全部 items)
│   │   └── 输出: [[primary_idx, dup_idx, ...], ...]
│   └── 保留 primary（分数最高），drop dup，合并 content
│
├── 9. Twitter Reply Expansion (可选)
│   └── 条件: config.sources.twitter.fetch_reply_text == true
│   ├── 对高分 Twitter item 拉取回复正文 (Apify 二次调用)
│   └── 追加评论后重新 AI 评分 (analyze_batch)
│
├── 10. Enrichment (ContentEnricher.enrich_batch)
│   └── 每个高分 item:
│       ├── Step 1: 概念提取 (LLM 调用 #1)
│       │   └── "需要解释哪些技术概念？" → 0-3 条查询词
│       ├── Step 2: DuckDuckGo 搜索
│       │   └── 每 query → 3 条结果
│       └── Step 3: 双语分析生成 (LLM 调用 #2, 重试 3 次)
│           └── title / whats_new / why_it_matters / key_details /
│               background / community_discussion → EN + ZH 各一份
│           └── 写入 item.metadata.*
│   └── 并发: enrichment_concurrency=1 (可配)
│
├── 11. Generate Summary (DailySummarizer.generate_summary)
│   └── 纯程序化 Markdown 渲染（无 AI 调用）
│   ├── 按 tag 分组
│   ├── 每个 item 渲染: 标题 + score + reason + summary + tags + 来源
│   └── 语言: 仅中文 (pipeline-simplify 后)
│
├── 12. Save & Publish
│   ├── data/summaries/horizon-{date}-zh.md
│   └── docs/_posts/{date}-summary-zh.md (Jekyll front matter 包装)
│
└── 13. Token Usage Report (终盘打印)
    └── 本次 run 的 tokens: input / output / per-provider

```
