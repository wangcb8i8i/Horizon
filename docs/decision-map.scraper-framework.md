# Decision Map: Scraper Framework Extraction

Extract Horizon's data scraping capability into a standalone asyncio-based scraper framework.

## Resolved (grilling, 2026-06-25)

| # | Decision | Answer |
|---|----------|--------|
| 1 | 方向 | **框架化 (C)** — 通用 asyncio scraper 框架 + plugin 注册机制 |
| 2 | 框架职责 | 接口定义 / HTTP 客户端管理 / 数据模型 / 调度并发 / URL 去重 / 存储抽象 / 监控日志指标。**CLI 不归框架** |
| 3 | 语言 | Python, asyncio-only |
| 4 | 工作模型 | **Plugin 主动注册到框架，框架自动调度** — 框架负责 HTTP client 创建、并发、限速、收集、URL 去重 |
| 5 | 去重归属 | URL 去重归框架，语义去重归消费者 |
| 6 | `since` 约定 | 框架统一声明传入，plugin 自行决定如何使用 |
| 7 | Plugin 发现 | **约定目录扫描** |
| 8 | HTTP 配置 | 框架定义标准 `ScraperConfig` model |
| 9 | 目标 | **内部可复用** — 不公开发布，不 publish PyPI |

## Fog of War

---

## #1: 持久化 / 存储抽象设计 [已解决]

Blocked by: —
Type: Prototype

### Question

框架的存储抽象管到什么程度？三个候选方案：

- **A — 极小接口**: 框架只定义 `Storage` ABC（`save(items)` / `load(since)`），消费者实现。框架内置一个 JSON file 实现做默认和演示。
- **B — ContentItem 级别**: 框架管理去重状态（已经抓过的 item id 记录）和持久化，基于 `ContentItem.id` 做幂等增量。
- **C — 无存储**: 框架只返回抓取结果 `List[ContentItem]`，不碰持久化。消费者自行处理重跑幂等。

倾向 **B + A 的极小接口**（框架内置默认 JSON 实现，消费者可替换）—— 既满足框架内 URL 去重的状态需要，又保持可替换。

### Answer

**Prototype**: `packages/scrapers/src/scrapers/storage.py`

采用 B+A 方案：框架定义极小 `Storage` ABC，内置 `MemoryStorage`（测试用）和 `JsonFileStorage`（本地默认）。

```python
class Storage(ABC):
    # Dedup state
    async load_seen_urls() -> Set[str]
    async save_seen_urls(urls: Set[str])

    # Item persistence
    async save_items(items: List[ContentItem])
    async load_items(since: datetime) -> List[ContentItem]
```

| 维度 | 决策 | 理由 |
|------|------|------|
| 接口范围 | **去重状态 + 持久化** 两个关注点 | 共享生命周期和 durability 要求，下游实现可以优化成一个 backend |
| 默认实现 | **`JsonFileStorage`** 写入 `.scrapers/` | 零配置本地可用 |
| 文件格式 | seen: `seen_urls.json` (JSON array，全量重写) / items: `items.jsonl` (JSON Lines，append) | seen 规模可控（本地聚合器万级）; items append 天然增量 |
| 测试实现 | **`MemoryStorage`** (进程级不持久) | 测试无文件依赖 |
| `seen` 写入策略 | **run 结束时全量替换** | 避免每 item 都写盘，且反重读时 to 文件可重入 |

---

## #2: Plugin 目录约定与发现机制 [已解决]

Blocked by: #5
Type: Prototype

### Question

框架扫描目录的具体约定：

- 目录路径：消费者通过 config 指定？还是约定 `scrapers/` 或 `plugins/` 在项目根？
- 文件命名：所有 `.py` 都扫描？还是约定 `*_scraper.py`？
- 如何识别哪个类是 Scraper：遍历所有 ABC 子类？还是要求 plugin 暴露特定名字（如 `__scraper__` 或 `register` function）？
- 是否需要 `__init__.py`？

需要 prototype 验证几个方案的可维护性和 IDE 友好度。

### Answer

**Prototype**: `packages/scraper-core/src/scraper_core/discovery.py`

| 决策 | 选择 | 理由 |
|------|------|------|
| 目录路径 | 代码 API 传参 (`ScraperScanner("path")`)，默认 `scrapers/` | 灵活，消费方可自行决定路径 |
| 文件命名 | **不限制** — 扫描所有 `.py` 文件 | 用 BaseScraper ABC 做类检测，无需额外命名约定 |
| 类检测 | `importlib` 加载 → 遍历模块属性找 BaseScraper 子类 | 最鲁棒，不要求 register() 调用或 decorator |
| `__init__.py` | **不需要** — 用 `spec_from_file_location` 加载 | 插件目录是 flat collection，不是 package |
| 递归子目录 | `recursive=False` (默认关闭) | 保持简单，需要时显式开启 |
| `_` 前缀文件 | **跳过** (如 `__init__.py`, `_helpers.py`) | 避免误扫内部模块 |
| 抽象类 | **跳过** (`__abstractmethods__` 非空) | 防止未实现的基类被注册 |

使用示例：

```python
from scraper_core.discovery import ScraperScanner

scanner = ScraperScanner("my_scrapers/")
plugins = scanner.scan()           # 发现 + 自动注册
# scanner 也可只发现不注册：
plugins = scanner.scan(register=False)
```

**Border cases handled**:
- 目录不存在 → 返回空列表，不抛异常
- 文件 import 失败（语法错 / 依赖缺）→ 跳过该文件，不中断整体扫描
- 模块中无 BaseScraper 子类 → 静默跳过
- 文件名冲突（多个 scraper 同名 `name`）→ ScraperRegistry 抛 KeyError

**关联 artifacts**: `discovery.py`, `test_discovery.py`

---

## #3: ScraperConfig model 设计 [已解决 — 随 #5]

Blocked by: #5
Type: Prototype

### Question

HTTP 客户端配置 model 的具体字段和默认值。需要考虑：

```python
class ScraperConfig(BaseModel):
    timeout: float = 30.0
    max_retries: int = 3
    retry_delay: float = 1.0       # base delay for exponential backoff
    max_connections: int = 10       # httpx connection pool size
    proxy: Optional[str] = None
    rate_limit: Optional[RateLimitConfig] = None
    extra_headers: dict[str, str] = {}

class RateLimitConfig(BaseModel):
    requests: int = 10              # max requests
    period: int = 60                # per N seconds
```

同时也需要定义 Scraper-specific config 的透传机制：plugin 可以声明自己的 config model，框架只校验标准字段，其余透传。

核心问题：是否让 plugin 的 `__init__` 接受一个 `ScraperConfig` + plugin 自有 config，还是统一由框架组装后再传入？

### Answer

已在 **#5** 的 prototype 中一并解决。具体设计见 `packages/scraper-core/src/scraper_core/plugin.py`：

- **ScraperConfig**: 框架级 HTTP 配置 model，含 timeout/max_retries/rate_limit/proxy/extra_headers
- **RateLimitConfig**: requests + period_seconds
- **Plugin config 透传**: 框架将消费者的 plugin 专属 config 传给 `plugin_config: Dict[str, Any]`，plugin 自行通过 `config_schema()` 声明期望的校验 model，框架在注册期预校验

---

## #4: 框架包名与项目结构 [已解决]

Blocked by: #5
Type: Research

### Question

框架的包名、namespace 和代码仓库布局：

| 子问题 | 选项 |
|--------|------|
| 包名 | `scraper-core` / `collector` / `horizon-collect` / 其他 |
| namespace 前缀 | 裸 `scraper_core` / `horizon.scraper` |
| 物理位置 | monorepo 内 `packages/scraper-core/` / 独立 repo |
| Python package layout | `src/` 还是扁平 |

### Answer

| 维度 | 决策 | 理由 |
|------|------|------|
| 包名 | **`scrapers`** | 用户指定，简洁且自描述 |
| Python 包名 | **`scrapers`** (同包名) | 不 publish PyPI，无命名冲突顾虑 |
| 物理位置 | monorepo **`packages/scrapers/`** | 与项目共仓库，迭代快 |
| 代码布局 | **`src/` layout** | 防 import 混乱，和 Horizon 主项目一致 |

项目结构：

```
packages/scrapers/
  pyproject.toml            # name = "scrapers", deps: httpx, pydantic
  src/
    scrapers/
      __init__.py
      plugin.py             # BaseScraper, ScraperRegistry, ContentItem, ScraperConfig
      discovery.py          # ScraperScanner
  test_discovery.py         # smoke test
```

---

## #5: 插件注册 / 生命周期 API [已解决]

Blocked by: —
Type: Prototype

### Question

插件从「被扫描发现」到「被调度执行」的完整生命周期：

```
发现 ─→ 实例化 ─→ 注册 ─→ 调度 ─→ 收集结果 ─→ 去重 ─→ 存储
```

具体 API 设计的关键问题：

1. Plugin 类继承 `BaseScraper` 还是实现 `ScraperPlugin` protocol（duck typing）？
2. 是否需要 `setup()` / `teardown()` 钩子？
3. `fetch(since)` 的签名是否接受 / 返回框架统一类型？
4. 框架如何知道每个 plugin 的 config schema？（plugin 暴露 class var 还是用 type annotation？）

需要 prototype 做一套最小的 plugin API 看看手感。

### Answer

**Prototype**: `packages/scraper-core/src/scraper_core/plugin.py`

核心设计：

| 决策 | 选择 | 理由 |
|------|------|------|
| 基类风格 | **ABC** (`BaseScraper`) | 明确契约，IDE 友好，@abstractmethod 防遗漏 |
| setup/teardown | **可选钩子**，默认 no-op | 资源初始化/清理，异常时也调 teardown |
| fetch 签名 | `async fetch(since: datetime) -> List[ContentItem]` | 框架统一类型，ContentItem 与 Horizon 解耦（source_type 是 str 而非枚举） |
| Config 声明 | **classmethod `config_schema()`** 返回 `Optional[Type[BaseModel]]` | 不实例化即可自描述，框架做预校验 |
| 注册机制 | `ScraperRegistry` 进程级 dict 单例 | 简单，足够内部使用 |
| ContentItem | **框架自有 model**，pydantic | 不依赖 Horizon 的 SourceType 枚举 |
| 全局 HTTP 配置 | `ScraperConfig` pydantic model | 独立于 plugin 自有 config |

Plugin 构造函数签名：

```python
def __init__(
    self,
    plugin_config: Dict[str, Any],
    http_client: httpx.AsyncClient,
    framework_config: ScraperConfig,
) -> None
```

- `plugin_config`: 消费者的配置中该 plugin 专属部分（已按 `config_schema()` 校验）
- `http_client`: 框架创建的共享 async client，plugin **禁止**自行创建
- `framework_config`: 框架级配置（超时/代理/限速），plugin 可读不可改

**关联 artifacts**:
- `plugin.py` 包含: `ContentItem`, `ScraperConfig`, `RateLimitConfig`, `BaseScraper`, `ScraperRegistry`, `PluginInfo`

---

## #6: URL 去重具体实现 [已解决]

Blocked by: #1
Type: Prototype

### Question

框架内置的 URL 去重，两个子问题：

1. **归一化策略** — 当前 Horizon 的做法（strip www, trailing slash, fragment）。框架是否采用同样的策略？是否允许 plugin 自定义 URL 归一化？
2. **去重状态生命周期** — 去重状态（seen URLs）在单次 run 内有效，还是跨 run 持久化？
   - 单次 run 内去重：防止同一次调度中多个 plugin 抓了同一 URL
   - 跨 run 持久化：防止历史数据重复入库

框架应该两者都支持：内存中去重 + 可选的持久化 seen set。

### Answer

**Prototype**: `packages/scrapers/src/scrapers/dedup.py`

```
Deduplicator ── 两层去重
├── In-memory (always on)
│   └── is_new() 检查 + 即时标记
└── Cross-run (opt-in via Storage)
    ├── load() 加载持久 seen set
    ├── is_new() 同时检查内存 + 持久
    └── persist() 合并并刷入存储
```

URLNormalizer 归一化策略：

```
输入                         →  归一化键
https://www.example.com/foo/ →  example.com/foo
http://EXAMPLE.COM/foo       →  example.com/foo
https://example.com/foo#ref  →  example.com/foo
https://example.com/foo?q=1  →  example.com/foo?q=1
```

| 维度 | 决策 | 理由 |
|------|------|------|
| 归一化策略 | scheme 去除 / host lower + strip www / path strip trailing slash / query 保留 / fragment 去除 | 与 Horizon 现有行为一致 |
| Plugin 自定义 | **暂不支持** — 使用固定策略 | 框架内部使用，必要可加 hook |
| Cross-run | **opt-in**，默认关闭 | `since` 是主机制，cross-run 为安全网 |
| 默认配置 | `Deduplicator()` — 仅内存去重 | 即开即用 |
| 持久化模式 | `Deduplicator(storage=my_storage)` | load/persist 生命周期由调用者控制 |

---

## #7: 监控 / 日志 / 指标 [实现阶段解决]

Blocked by: —
Type: Research

### Question

框架内置的 observability 契约：

- 日志：使用 `logging` 标准库？还是集成 `structlog`？框架是否在内部创建 logger 还是暴露给消费者配置？
- 指标：暴露 `collected_items`, `failed_requests`, `fetch_duration_seconds` 等基础的 Prometheus 指标？还是只做 logging，指标由消费者包装？
- 异常处理：plugin 内异常是否被框架捕获（不影响其他 plugin）？异常后是否提供回调/钩子？

建议：框架内用标准 `logging` + callbacks（`on_item_collected` / `on_error`），不强制指标框架。消费者可以挂 callbacks 做指标采集。

### Answer

实现阶段直接落地，不单独开 ticket。方针：标准 `logging` + callback hooks。

---

## #8: 测试策略与 Test Utilities [实现阶段解决]

Blocked by: #4
Type: Prototype

### Question

框架需要提供哪些测试设施：

- 是否提供 mock HTTP server / fixture 帮助 plugin 开发者测试？
- 框架自身的测试套件结构（scraper 集成测试 vs plugin 单元测试）
- CI 策略（仅跑框架自身测试？还是需要拉 Horizon 做集成验证？）

建议：框架提供 `ScraperTestCase` 或 pytest fixture，包含 mock HTTP client 和 sample data helpers。

### Answer

实现阶段直接落地。初始 pytest 结构 + `MemoryStorage` 即可覆盖框架核心测试。

---

## #9: Horizon 迁移策略 [已解决]

Blocked by: #4, #5
Type: Grilling

### Question

从 Horizon 现有 scrapers 迁移到新框架的具体步骤和分支策略：

- 分支名：`feat/scraper-framework`？
- 迁移顺序：先定义接口 → 逐个迁移 scraper → 最后替换 orchestrator 中的调用方式？
- 兼容期：Horizon 是否在迁移期间同时支持新旧两套？还是冻结功能直到迁移完成？
- Horizon repo 中 `src/scrapers/` 目录最终是否删除？

建议：独立分支 `feat/scraper-framework`，先定义框架核心接口和目录结构，然后逐个将现有 scrapers 作为 plugin 移入新框架的 demo directory，最后将 Horizon 的 orchestrator 切换到新框架。

### Answer

| 维 | 决策 | 理由 |
|---|------|------|
| 分支 | **`feat/scraper-framework`** 独立分支 | main 零损伤，分支可自由重构 |
| 迁移范围 | **整批迁移** | 一次性将 8 个 scraper 全部改写为 plugin |
| 兼容期 | **无** — 分支上改、合入即生效 | 分文内无需双维护 |
| 旧目录 `src/scrapers/` | 分文内先改后删，合入 main 时同步删除 | 无 dead code |

分支操作顺序：

```
① 框架补全 (orchestrator / 监控 / 测试)
② Horizon scrapers → framework plugins (horizon/scrapers/)
③ orchestrator.py 切换到框架调度
④ 删除旧 src/scrapers/
⑤ 完整 pipeline 验证
⑥ PR → main
```
