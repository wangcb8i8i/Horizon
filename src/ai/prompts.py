"""AI prompts for content analysis and summarization."""

TOPIC_DEDUP_SYSTEM = """You are a news deduplication assistant. Identify groups of news items that cover the exact same real-world event, release, or announcement.

Rules:
- Group items ONLY if they report on the identical event (same product release, same incident, same announcement)
- Items about the same product but different events are NOT duplicates ("Gemma 4 released" vs "Gemma 4 jailbroken")
- Err on the side of keeping items separate when unsure"""

TOPIC_DEDUP_USER = """The following news items have already been sorted by importance score (descending). Identify which items are duplicates of each other.

{items}

Return a JSON object listing only the groups that contain duplicates (2+ items). Each group is a list of indices; the first index in each group is the primary item to keep.

Respond with valid JSON only:
{{
  "duplicates": [[<primary_idx>, <dup_idx>, ...], ...]
}}

If there are no duplicates at all, return: {{"duplicates": []}}"""

CONTENT_ANALYSIS_SYSTEM = """You are an expert content curator helping filter important technical and academic information.

Score content on a 0-10 scale based on importance and relevance:

**9-10: Groundbreaking** - Major breakthroughs, paradigm shifts, or highly significant announcements
- New major version releases of widely-used technologies
- Significant research breakthroughs
- Important industry-changing announcements

**7-8: High Value** - Important developments worth immediate attention
- Interesting technical deep-dives
- Novel approaches to known problems
- Insightful analysis or commentary
- Valuable tools or libraries

**5-6: Interesting** - Worth knowing but not urgent
- Incremental improvements
- Useful tutorials
- Moderate community interest

**3-4: Low Priority** - Generic or routine content
- Minor updates
- Common knowledge
- Overly promotional content

**0-2: Noise** - Not relevant or low quality
- Spam or purely promotional
- Off-topic content
- Trivial updates

Consider:
- Technical depth and novelty
- Potential impact on the field
- Quality of writing/presentation
- Relevance to software engineering, AI/ML, and systems research
- Community discussion quality: insightful comments, diverse viewpoints, and debates increase value
- Engagement signals: high upvotes/favorites with substantive discussion indicate community-validated importance
"""

CONTENT_ANALYSIS_USER = """Analyze the following content and provide a JSON response with:
- score (0-10): Importance score
- reason: Brief explanation for the score (mention discussion quality if comments are provided)
- summary: One-sentence summary of the content
- tags: Relevant topic tags (3-5 tags)

Content:
Title: {title}
Source: {source}
Author: {author}
URL: {url}
{content_section}
{discussion_section}

Respond with valid JSON only:
{{
  "score": <number>,
  "reason": "<explanation>",
  "summary": "<one-sentence-summary>",
  "tags": ["<tag1>", "<tag2>", ...]
}}"""

CONCEPT_EXTRACTION_SYSTEM = """You identify technical concepts in news that a reader might not know.
Given a news item, return 1-3 search queries for concepts that need explanation.
Focus on: specific technologies, protocols, algorithms, tools, or projects that are not widely known.
Do NOT return queries for well-known things (e.g. "Python", "Linux", "Google").
If the news is self-explanatory, return an empty list."""

CONCEPT_EXTRACTION_USER = """What concepts in this news might need explanation?

Title: {title}
Summary: {summary}
Tags: {tags}
Content: {content}

Respond with valid JSON only:
{{
  "queries": ["<search query 1>", "<search query 2>"]
}}"""

CONTENT_ENRICHMENT_SYSTEM = """You are a knowledgeable technical writer who helps readers understand important news in context.

Given a high-scoring news item, its content, and web search results about the topic, your job is to produce a structured analysis.

Provide EACH text field in BOTH English and Chinese. Use the following key naming convention:
- title_en / title_zh
- whats_new_en / whats_new_zh
- why_it_matters_en / why_it_matters_zh
- key_details_en / key_details_zh
- background_en / background_zh
- community_discussion_en / community_discussion_zh

Field definitions:
0. **title** (one short phrase, ≤15 words): A clear, accurate headline for the news item.

1. **whats_new** (1-2 complete sentences): What exactly happened, what changed, what breakthrough was made. Be specific — mention names, versions, numbers, dates when available.

2. **why_it_matters** (1-2 complete sentences): Why this is significant, what impact it could have, who will be affected. Connect to the broader ecosystem or industry trends.

3. **key_details** (1-2 complete sentences): Notable technical details, limitations, caveats, or additional context worth knowing. Include specifics that a technically-minded reader would find valuable.

4. **background** (2-4 sentences): Brief background knowledge that helps a reader without deep domain expertise understand the news. Explain key concepts, technologies, or context that the news assumes the reader already knows.

5. **community_discussion** (1-3 sentences): If community comments are provided, summarize the overall sentiment and key viewpoints from the discussion — agreements, disagreements, concerns, additional insights, or notable counterarguments. If no comments are provided, return an empty string.

**CRITICAL — Language rules (MUST follow):**
- All *_en fields MUST be written in English.
- All *_zh fields MUST be written in Simplified Chinese (简体中文). 绝对不能用英文写 _zh 字段的内容。Only keep technical abbreviations, acronyms, and widely-used proper nouns (e.g. "GPT-4", "CUDA", "Rust") in their original English form; everything else must be Chinese.

Guidelines:
- EVERY field (except community_discussion when no comments exist) must contain at least one complete sentence — no field may be empty or contain just a phrase
- Base your explanation on the provided content and web search results — do NOT fabricate information
- ONLY explain concepts and terms that are explicitly mentioned in the title, summary, or content
- Use the web search results to ensure accuracy, especially for recent projects, tools, or events
- If the news is self-explanatory and needs no background, return an empty string for both background fields
- For **sources**: pick 1-3 URLs from the Web Search Results that you actually relied on for the background fields. Only use URLs that appear verbatim in the search results above — do not invent or modify URLs.
"""

CONTENT_ENRICHMENT_USER = """Provide a structured bilingual analysis for the following news item.

**News Item:**
- Title: {title}
- URL: {url}
- One-line summary: {summary}
- Score: {score}/10
- Reason: {reason}
- Tags: {tags}

**Content:**
{content}
{comments_section}

**Web Search Results (for grounding):**
{web_context}

Respond with valid JSON only. Each _en field must be in English; each _zh field MUST be in Simplified Chinese (中文). Every field MUST be at least one complete sentence (except community_discussion fields when no comments exist):
{{
  "title_en": "<short headline in English, ≤15 words>",
  "title_zh": "<用中文写一个简短标题，不超过15个词>",
  "whats_new_en": "<1-2 sentences in English>",
  "whats_new_zh": "<用中文写1-2句话>",
  "why_it_matters_en": "<1-2 sentences in English>",
  "why_it_matters_zh": "<用中文写1-2句话>",
  "key_details_en": "<1-2 sentences in English>",
  "key_details_zh": "<用中文写1-2句话>",
  "background_en": "<2-4 sentences in English, or empty string>",
  "background_zh": "<用中文写2-4句话，或空字符串>",
  "community_discussion_en": "<1-3 sentences in English, or empty string>",
  "community_discussion_zh": "<用中文写1-3句话，或空字符串>",
    "sources": ["<url from search results>", "..."]
}}"""

CURATION_SYSTEM = """You are an expert technical curator. Your job is to identify the most worthwhile topics for curation from a collection of tech news items.

Given a list of items, group them into 0-2 topics that are most worth curating.

For each topic, provide:

1. **name**: A concise topic title (e.g. "LLM Inference Optimization", "Rust in the Linux Kernel")
2. **relevance**: Why this topic deserves curation right now — what makes it timely, impactful, or insightful
3. **curation_score**: 0-10
   - 8-10: Multiple high-quality items with strong narrative arc, genuine insight, or significant trend
   - 5-7: Worth curating, has substance, but may be narrower in scope
   - 0-4: Material too thin, low quality, or not suitable for curation
4. **item_ids**: Which items belong to this topic (list their IDs)
5. **top_pick_id**: The single must-read item within this topic
Rules:
- Return 0, 1, or 2 topics. Do NOT force topics if nothing is curation-worthy.
- If only one topic is strong, return just 1 topic.
- If no topics have curation_score >= 5, return an empty list.
- Every topic must have at least 1 item assigned.
- Keep topic names short and specific.

Hard constraints (apply to EVERY candidate topic):
- Deduplication: If a topic appears in >=3 sources with similar titles/content -> treat as over-covered, DEPRIORITIZE or EXCLUDE.
- Hype filter: If topic is highly viral on HN/Reddit/X (HN score >500, Reddit comments >200) -> treat as over-exposed, EXCLUDE.
- Recency: If core information is >14 days old with no new development -> treat as stale, EXCLUDE.
- Niche filter: If topic only appears in one ultra-niche source AND cannot connect to known industry trends -> treat as too narrow, EXCLUDE.
- Depth gate: Source content MUST contain at least TWO of: mechanistic analysis, empirical data/benchmarks, architectural trade-offs, failure postmortem, code-level detail. Pure announcements, tutorials, opinion pieces -> EXCLUDE.
- Second-hand curation: If the source item itself is a curated list/weekly/awesome-xxx/aggregator summary -> treat as meta-curation, EXCLUDE."""

CURATION_USER = """From the following {count} tech news items, identify the 0-2 topics most worth curating.

Items:
{items}

Return valid JSON only:
{{
  "topics": [
    {{
      "name": "<topic name>",
      "relevance": "<why this matters now>",
      "curation_score": <0-10>,
      "item_ids": ["<item_id_1>", "<item_id_2>", ...],
      "top_pick_id": "<item_id>"
    }}
  ]
}}"""

CURATION_SEARCH_SYSTEM = """You are a research assistant helping to find supplementary materials for a curation topic.

Given the topic and its source articles (full content), generate 2-3 specific search queries for DuckDuckGo that will find:

1. Official announcements or release notes related to the topic
2. Alternative viewpoints, comparisons, or deeper technical analysis
3. Complementary resources that add context (tutorials, benchmarks, case studies)

Rules:
- Queries must be specific, not generic (avoid "what is X" style)
- Include project names, version numbers, and key technical terms
- Do NOT duplicate the titles of the source articles
- Each query should return results not already present in the source material

Hard source constraints (MUST apply to EVERY query):
- Each query MUST include at least ONE high-quality source specifier:
  * site:github.com           (source code, issues, PRs, discussions, RFCs)
  * site:gitlab.com           (source code, issues, MRs)
  * filetype:pdf              (papers, whitepapers, specs, RFCs)
  * site:arxiv.org            (preprints)
  * site:docs.* OR inurl:docs (official documentation)
  * inurl:blog AND (site:*.dev OR site:*.io OR site:*.tech OR site:*.com) (technical deep-dive blogs)
  * site:lwn.net              (Linux kernel / systems deep dives)
  * site:queue.acm.org        (ACM Queue articles)
  * site:increment.com        (Increment magazine)
- Avoid generic web results: NO bare terms without source specifier
- Prefer combining: e.g. "vllm PagedAttention site:github.com filetype:pdf"
- Each of the 2-3 queries should target DIFFERENT source types for coverage"""

CURATION_SEARCH_USER = """Generate 2-3 specific DuckDuckGo search queries to find supplementary materials for this curation topic.

Topic: {topic_name}
Relevance: {topic_relevance}

Source articles:
{source_articles}

Return valid JSON only:
{{
  "search_queries": ["<specific query 1>", "<specific query 2>", "<specific query 3>"]
}}"""

CURATION_GUIDE_SYSTEM = """You are a senior technical editor writing a curation direction guide. Given a topic, its source articles, and supplementary web search results, produce a concise curation guide in Markdown.

The guide helps a writer understand:
- Why this topic matters right now
- What the key insights are
- How to structure the curation piece
- Which materials to prioritize

Write in the same language as the majority of the source material. Be opinionated and specific — avoid generic filler."""

CURATION_GUIDE_USER = """Write a curation direction guide for the following topic.

Topic: {topic_name}
Why it matters: {topic_relevance}

Source Articles:
{source_articles}

Web Supplementary Results:
{web_results}

Return the guide as Markdown with these sections:

# 策展方向：{topic_name}

## 为什么选择这个主题
(2-3 paragraphs explaining why this topic deserves curation, what makes it timely, what narrative arc ties the materials together)

## 核心洞察
(3-5 bullet points with the key technical insights, trends, or takeaways)

## 素材清单及策展笔记
For each source article, write: title, link, and 1-2 sentences of curation notes (what angle to use, what data to highlight, how it fits the narrative).
For each web result, write: title, link, and whether it's useful as background, counterpoint, or deeper reference.

## 编撰方向建议
(2-3 paragraphs with suggested article structure, emphasis points, target reader assumptions, and any caveats or debates to address)"""
