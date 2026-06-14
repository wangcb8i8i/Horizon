# horizon-fetch 策展管道改造设计

## 背景

`horizon-fetch` 是 Horizon 的交互式策展子管道：抓取 → AI 评分 → 用户选择 → 搜索补充 → 产出策展素材。实际使用中发现**选题输入狭窄**，候选池太小，无法选出优秀的策展选题。

## 根源诊断

五个瓶颈全部存在，最核心的矛盾是评估体系与公众号"琐思碎记"的定位不匹配：

| 瓶颈 | 当前状态 | 影响 |
|---|---|---|
| 信息源 | 仅 RSS + Reddit，Twitter 禁用，无 ArXiv | 覆盖领域窄 |
| 评估 prompt | `news → score ≤ 4`；AI/ML +1 偏置；无 opinion/reflection 评分维度 | 观点类内容天生被压制 |
| 阈值 | 8.0 | 仅 ~top 5% 能进入候选池 |
| 清洗 | 评估阶段截断 800 字符 | 观点内容上下文不足，评分失真 |
| 时间窗口 | 24h | 用户确认保持 |

## 方案：Fix the Knobs（方案 A）

不改管道结构，只修每个环节的参数和 prompt。

### 1. ArXiv 论文源

**新组件** `src/scrapers/arxiv.py`

- 每天用 ArXiv API 按分类轮询最近 24h 新论文
- **关键词预筛**：标题+摘要匹配关键词列表，命中的才进入 AI 评估
- 关键词可配置，初始列表：reasoning, alignment, safety, verification, protocol, architecture, formal, inference, optimization, compiler, type, concurrency, distributed, performance, security, privacy, analysis, design, evaluation, proof
- 跟踪分类：cs.AI, cs.LG, cs.SE, cs.CR, cs.SY, cs.PL, cs.DC

**设计决策**：关键词预筛而非 AI 预筛——日均 150-400 篇论文，关键词可将进入 AI 评估的数量降到 15-30 篇，成本为零。

### 2. Twitter 源启用

已有 `TwitterScraper` 和 `TwitterConfig`，仅需：

- `config.json` 中 `enabled: false → true`
- 用户填入追踪账号（tech opinion leader）
- 用户设 `APIFY_TOKEN` 环境变量
- 代码**完全不动**

### 3. 评估 prompt 重写

`src/ai/prompts.py` 中 `ITEM_EVALUATION_SYSTEM` 重写：

**移除**：
- `news → score ≤ 4` 硬约束
- AI/ML topic → score +1 偏置

**新增评分维度**：
- 有原创观点、思辨张力、能引发讨论
- 对中文技术社区有增量价值
- 不从来源类型预判（推文可以有深度，论文可以没观点）

**惩罚**：
- 纯新闻搬运、公司 PR 稿、无观点的工具教程

**新增 `content_type` 选项**：`reflection`（反思类），原有 `technical_deep_dive / opinion / news` 保留。

### 4. 阈值调整

`ai_score_threshold: 8.0 → 6.0`

候选池从 top ~5% 扩大到 top ~30%。

### 5. 清洗调整

`src/ai/curator.py` 评估阶段截断长度 `800 → 1500` 字符。素材文件保存（`_ITEM_MAX_CHARS=5000`）和其他截断（搜索查询等）不变。

## 改动清单

| 文件 | 改动 |
|---|---|
| `src/models.py` | 新增 `SourceType.ARXIV`、`ArXivConfig` |
| `src/scrapers/arxiv.py` | 新建 — ArXiv API 抓取 + 关键词预筛 |
| `src/scrapers/__init__.py` | 导出 ArxivScraper |
| `src/orchestrator.py` | `fetch_all_sources()` 新增 ArXiv 分支；`_sub_source_label()` 加 arxiv 处理 |
| `src/ai/prompts.py` | `ITEM_EVALUATION_SYSTEM` 重写 |
| `src/ai/curator.py` | `evaluate_items()` 截断 800 → 1500 |
| `data/config.json` | 加 arxiv 配置、启用 twitter、阈值 8.0→6.0 |

**不修改**：`src/fetch_cli.py`、`src/ai/utils.py`、`src/scrapers/twitter.py`

## 不做的事

- 不增加自动成文步骤（素材管道产出仍是策展指南 + 素材文件）
- 不改变管道编排流程（仍为 fetch → evaluate → user pick → search → materials）
- 不引入两阶段筛选或 persona 驱动（留待后续需要时从 A 演进）
