---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> From 29 items, 13 important content pieces were selected

---

1. [GLM 5.2 在网络安全基准测试中超越 Claude](#item-1) ⭐️ 8.0/10
2. [用 Claude Code 分析 MRI：AI 医疗新尝试引发信任讨论](#item-2) ⭐️ 8.0/10
3. [布朗大学教授谴责大规模 AI 作弊事件](#item-3) ⭐️ 8.0/10
4. [Tokenmaxxing 终结与新策略涌现](#item-4) ⭐️ 8.0/10
5. [航天飞机 I/O 处理器电路板深度解析](#item-5) ⭐️ 8.0/10
6. [历史内存价格 1960-2026 图表引发方法争议](#item-6) ⭐️ 7.0/10
7. [Librepods：开源项目解放 AirPods 全部功能](#item-7) ⭐️ 7.0/10
8. [OpenAI Codex 敏感文件排除功能引发安全讨论](#item-8) ⭐️ 7.0/10
9. [波兰字母ś与浏览器快捷键冲突之谜](#item-9) ⭐️ 7.0/10
10. [KIDS 法案要求在线年龄验证引发隐私担忧](#item-10) ⭐️ 7.0/10
11. [VictoriaLogs 列式存储原理解析](#item-11) ⭐️ 7.0/10
12. [基于类型代数的解析方法（2019）](#item-12) ⭐️ 7.0/10
13. [破窗构建中的离奇 bug 解析](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GLM 5.2 在网络安全基准测试中超越 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.0/10

Semgrep 发布博客称，其网络安全基准测试显示 GLM 5.2（753B 参数开源模型）表现优于 Claude。该测试专门评估模型在代码安全审查和漏洞发现方面的能力。 这是开源模型首次在特定专业领域（网络安全）超越闭源前沿模型，可能大幅降低企业网络安全 AI 应用的成本。GLM 5.2 的高性价比和开源特性将推动更多团队在安全工具链中采用类似模型。 GLM 5.2 拥有 7530 亿参数，支持 1M token 上下文窗口，由 Z.AI 开发并通过 Hugging Face 发布。Semgrep 的基准测试专注于静态分析中的真实漏洞模式匹配，而非通用能力评估。

hackernews · Lobsters · Jun 28, 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48709670)

**背景**: Semgrep 是一个流行的开源静态代码分析工具，广泛应用于安全漏洞扫描。GLM 系列是中国公司智谱 AI 研发的大语言模型，5.2 版本是其最新旗舰。网络安全基准测试专门针对代码缺陷的发现能力，与常规综合测试不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM-5.2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>

</ul>
</details>

**社区讨论**: 用户普遍认可 GLM 5.2 在编程和网络安全任务中的性价比，如有人表示“用它编程一天仅花费 20 美元”。但也有用户指出，在部分测试中 DeepSeek V4 Pro 表现更稳定，且本地部署 753B 模型需要极高硬件配置。

**标签**: `#LLM`, `#benchmarking`, `#open-source`, `#GLM`, `#cybersecurity`

---

<a id="item-2"></a>
## [用 Claude Code 分析 MRI：AI 医疗新尝试引发信任讨论](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

一位用户使用 Claude Code（基于 Anthropic 的 Claude 模型）分析自己的 MRI 影像报告，并分享了这一体验。 这展示了大型语言模型在个人医疗分析中的创新应用，但同时也引发了关于 AI 诊断可靠性、医患信任以及过度依赖技术的广泛讨论。 Claude Code 本是用于代码辅助开发的工具，但用户将其用于分析 MRI 文本报告；一位放射科医生评论指出，仅凭报告无法全面评估，且超声检测钙化存在局限。

hackernews · engmarketer · Jun 28, 16:35 · [社区讨论](https://news.ycombinator.com/item?id=48708941)

**背景**: Claude 是 Anthropic 公司开发的一系列大型语言模型，采用“宪法 AI”技术训练以提升伦理合规性。Claude Code 是 Anthropic 推出的 AI 编程辅助工具。近年来，AI 在医疗辅助诊断中的应用日益增多，但准确性、可解释性和信任问题仍是核心挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**社区讨论**: 社区讨论热烈，放射科医生指出无法仅凭 2D 报告判断；用户们表达了对 AI 的复杂态度：既享受 AI 无限次追问的便利，又担忧其不可靠。有用户分享自身经历，指出医疗误诊的现实风险，认为 AI 可能加剧或缓解这一问题。

**标签**: `#AI in healthcare`, `#medical imaging`, `#trust`, `#Claude Code`, `#LLMs`

---

<a id="item-3"></a>
## [布朗大学教授谴责大规模 AI 作弊事件](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) ⭐️ 8.0/10

布朗大学一位教授公开谴责在一次考试中发生的大规模 AI 作弊行为，学生普遍使用大型语言模型完成考核。 此事件凸显了生成式 AI 对传统教育评估体系的严重冲击，可能促使高校重新设计课程和考试形式，以维护学术诚信。 该教授的研究领域是博弈论，而社区评论中有观点指出，当其他学生都使用 AI 时，个体理性选择就是也使用 AI。

hackernews · geox · Jun 28, 16:41 · [社区讨论](https://news.ycombinator.com/item?id=48708991)

**背景**: 随着 ChatGPT 等大型语言模型的普及，学生利用 AI 工具完成作业和考试的现象日益严重，传统开卷或在线考试难以防范 AI 作弊。高校面临调整教学评估方式的压力，例如恢复线下手写考试和增加一对一面试环节。

**社区讨论**: 社区讨论热烈，多数人认为 AI 作弊问题严重，提出线下笔试和面试等解决方案。也有教授质疑评分系统的意义，认为应改为只给 A 等由公司自行筛选。部分评论从博弈论角度指出使用 AI 是理性选择，批评考试设计本身不合理。

**标签**: `#AI fraud`, `#academic integrity`, `#education`, `#assessments`, `#university policies`

---

<a id="item-4"></a>
## [Tokenmaxxing 终结与新策略涌现](https://12gramsofcarbon.com/p/agentics-tech-things-tokenmaxxing) ⭐️ 8.0/10

本文探讨了从“tokenmaxxing”（以 token 消耗量为指标的 AI 采用策略）向“复合正确性”（通过增加 token 投入提升任务准确率）的转变。 这标志着企业 AI 实践从追求使用量的粗放阶段进入注重输出质量的新阶段，影响 AI 代理的实际业务价值及投资回报。 作者声称当前更多 token 投入通常能带来更好结果，但社区评论指出该观点争议较大；tokenmaxxing 曾被用作强迫员工采用 AI 的临时手段。

hackernews · theahura · Jun 28, 16:24 · [社区讨论](https://news.ycombinator.com/item?id=48708795)

**背景**: Tokenmaxxing 指员工为应对企业设定的 token 使用指标而大量调用 AI，导致“AI 剧场”效应，即表面使用而无实质变革。“复合正确性”则强调在复杂任务中通过更多 token 迭代来修正错误，提升最终结果可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cio.com/article/4178320/tokenmaxxing-when-ai-adoption-metrics-go-bad.html">Tokenmaxxing: When AI adoption metrics go bad | CIO</a></li>
<li><a href="https://www.tigergraph.com/blog/tokenmaxxing-is-a-phase-inference-yield-is-the-strategy/">Tokenmaxxing is a Phase. Inference Yield is the Strategy. - TigerGraph</a></li>

</ul>
</details>

**社区讨论**: 社区对“更多 token 带来更好结果”普遍质疑，有评论认为 tokenmaxxing 仅是过渡策略，员工已学会区分 AI 适用场景；也有观点指出多步骤代理仍面临错误累积问题，与文章论点相悖。

**标签**: `#AI agents`, `#token economics`, `#software engineering`, `#AI adoption`

---

<a id="item-5"></a>
## [航天飞机 I/O 处理器电路板深度解析](http://www.righto.com/2026/06/space-shuttle-io-processor-boards.html) ⭐️ 8.0/10

一篇新文章详细剖析了航天飞机 I/O 处理器（IOP）的电路板，展示了其内部工程设计和组件布局。 该 I/O 处理器是航天飞机计算机系统的关键部件，首次将多线程计算机技术应用于太空任务，对理解早期航天电子系统有重要价值。此分析为硬件爱好者和复古计算社区提供了珍贵的实物资料。 I/O 处理器通过 24 条高速网络与航天飞机的传感器和系统通信，充当 CPU 与外部设备的桥梁。文章展示了来自 RR Auction 的照片，对比了 IOP 与 AP-101B CPU 的物理结构。

rss · Lobsters · Jun 28, 18:11

**背景**: 航天飞机使用的计算机是基于 IBM System/4 Pi 系列的 AP-101B，由 IBM 联邦系统部门开发。I/O 处理器负责处理输入输出任务，是多线程架构在太空领域的早期应用，由 Peter Kogge 设计。该系列计算机也曾用于 F-15、E-3 预警机等军用平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IBM_System/4_Pi">IBM System/4 Pi - Wikipedia</a></li>
<li><a href="https://www.righto.com/2026/06/space-shuttle-io-processor-boards.html">Examining circuit boards from the Space Shuttle's I/O Processor</a></li>

</ul>
</details>

**标签**: `#hardware`, `#retrocomputing`, `#space shuttle`, `#circuit boards`, `#I/O processor`

---

<a id="item-6"></a>
## [历史内存价格 1960-2026 图表引发方法争议](https://dam.stanford.edu/memory-prices.html) ⭐️ 7.0/10

斯坦福大学发布了 1960 年至 2026 年内存每 GB 价格的图表和分析，展示了长达 66 年的价格下降趋势。社区批评其未调整通货膨胀且$/GB 单位在不同时代缺乏实用性。 该图表反映了半导体技术的飞速进步，但也暴露了数据可视化中指标选择的问题，可能误导对当前内存昂贵程度的理解。讨论有助于改进技术历史数据的呈现方式。 图表未进行通胀调整，导致 1960-1980 年价格被严重低估。评论指出，早期系统容量远小于 1GB，使用$/GB 衡量当时成本毫无意义。

hackernews · vga1 · Jun 28, 18:32 · [社区讨论](https://news.ycombinator.com/item?id=48710092)

**背景**: 内存价格从 1960 年代每 GB 数百万美元降至 2020 年代约几美元，但近年因 AI 需求激增而价格上涨。数据可视化需要精心选择指标，否则可能歪曲历史趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepintellica.com/finance-economics/historical-memory-prices-1960-2026/">Historical memory prices 1960 - 2026 - Deep Intellica</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024–present_global_memory_supply_shortage">2025–present global memory supply shortage - Wikipedia</a></li>
<li><a href="https://www.business.com/articles/data-visualization-downfalls/">Data Visualization Tips: Common Problems & Solutions</a></li>

</ul>
</details>

**社区讨论**: 社区看法不一：有用户批评未调整通胀和单位选择不当；有人建议改用$/平均工作站内存；也有人指出加密货币和 AI 导致近期波动，并讨论未来产能变化。

**标签**: `#memory prices`, `#hardware history`, `#data visualization`, `#semiconductor industry`

---

<a id="item-7"></a>
## [Librepods：开源项目解放 AirPods 全部功能](https://github.com/librepods-org/librepods) ⭐️ 7.0/10

Librepods 是一个开源项目，通过逆向工程实现了苹果专有的 AAP 协议，让 AirPods 在非 Apple 设备上也能使用电池状态、入耳检测、降噪控制等高级功能。 该项目解决了 AirPods 用户长期以来的痛点——在 Android、Linux 等非苹果设备上被锁定功能，促进了设备互操作性，也展示了社区逆向工程的能力。 Librepods 基于逆向工程实现了苹果的 AAP 协议，目前支持电池状态、入耳检测、降噪模式切换等功能，但可能因 AirPods 固件更新而需要持续适配。

hackernews · rbanffy · Jun 28, 18:48 · [社区讨论](https://news.ycombinator.com/item?id=48710232)

**背景**: AirPods 在非苹果设备上只能作为普通蓝牙耳机使用，许多高级功能被苹果系统独占。AAP 是苹果专有的音频协议，用于 AirPods 与苹果设备之间的通信。Librepods 通过逆向工程重现了该协议，使得这些功能在非苹果设备上可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/librepods-org/librepods">GitHub - librepods-org/librepods: AirPods liberated from ...</a></li>
<li><a href="https://deepwiki.com/kavishdevar/librepods/2-aap-protocol-and-communication">AAP Protocol & Communication | kavishdevar/librepods | DeepWiki</a></li>
<li><a href="https://www.squaredtech.co/librepods-brings-full-airpods-features-to-android-and-linux">AirPods On Android: LibrePods Explained — New Open-Source</a></li>

</ul>
</details>

**社区讨论**: 社区讨论中，有用户指出 AirPods 在非苹果设备上原本就能作为普通蓝牙耳机使用，本项目的意义在于恢复额外功能。也有用户担心苹果未来会通过固件更新封锁此类逆向工程实现。

**标签**: `#AirPods`, `#Bluetooth`, `#open-source`, `#reverse-engineering`, `#interoperability`

---

<a id="item-8"></a>
## [OpenAI Codex 敏感文件排除功能引发安全讨论](https://github.com/openai/codex/issues/2847) ⭐️ 7.0/10

GitHub 上关于 OpenAI Codex 的一个 issue（#2847）讨论了如何防止 AI 编码代理意外泄露敏感文件，该问题获得 172 分和 118 条评论。 随着 AI 编码代理的普及，数据泄露风险成为关键安全挑战，该讨论反映了社区对沙箱和 opt-in 访问机制的迫切需求。 用户提出通过修改文件权限或容器隔离来阻止 Codex 访问敏感文件，但也有人认为仅依靠排除列表（blocklist）是不够的，可能带来虚假安全感。

hackernews · pikseladam · Jun 28, 12:27 · [社区讨论](https://news.ycombinator.com/item?id=48706714)

**背景**: 数据泄露（data exfiltration）是指数据被未经授权地传输到外部，AI 编码代理如 Codex 在运行命令时可能无意中包含敏感内容。沙箱（sandboxing）技术通过隔离执行环境来防止这种泄露，但标准容器可能共享主机内核，需要更严格的隔离方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_exfiltration">Data exfiltration</a></li>
<li><a href="https://www.firecrawl.dev/blog/ai-agent-sandbox">AI Agent Sandbox: How to Safely Run Autonomous Agents in 2026</a></li>

</ul>
</details>

**社区讨论**: 社区观点分歧：部分用户认为可通过系统工具（如 chmod）或容器解决；另一些人主张应默认 opt-in 而非 opt-out；还有评论者建议使用代理处理 API 密钥，或采用远程 devcontainer 方案彻底隔离。

**标签**: `#security`, `#AI coding agents`, `#sandboxing`, `#data privacy`, `#LLM security`

---

<a id="item-9"></a>
## [波兰字母ś与浏览器快捷键冲突之谜](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/) ⭐️ 7.0/10

一篇 2015 年的文章详细探讨了波兰语字母'ś'（AltGr+S 或右 Alt+S 组合）在浏览器中被快捷键（如 Ctrl+S）拦截，导致用户无法正常输入该字符的问题。 这一问题凸显了键盘本地化与浏览器默认快捷键之间的普遍冲突，影响波兰语用户的输入效率，并引发对 Unicode 标准化及浏览器键盘事件处理的深入思考。 文章指出该冲突在多个浏览器中普遍存在，且开发者常忽略不同键盘布局下修饰键的差异；社区评论补充说明 Unicode 规范化分解（NFD）会将大部分波兰字母（如ś）分解为基字加组合变音符号，但字母'ł'保持完整，这会影响 SQLite 等工具的文本搜索功能。

hackernews · colinprince · Jun 28, 12:44 · [社区讨论](https://news.ycombinator.com/item?id=48706814)

**背景**: 波兰语采用拉丁字母并附加变音符号（如ś上的尖音节），输入时通常需要组合键（例如右 Alt+S）。浏览器快捷键（如 Ctrl+S 保存）常与这些组合键冲突，导致系统优先响应浏览器。Unicode 规范化定义了字符的等价形式：预组合字符（如ś作为一个码位）与分解形式（s + 组合变音符号）被视为相同，但某些字符（如ł）没有分解形式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unicode_equivalence">Unicode equivalence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Precomposed_character">Precomposed character - Wikipedia</a></li>
<li><a href="http://www.unicode.org/reports/tr15/">UAX #15: Unicode Normalization Forms</a></li>

</ul>
</details>

**社区讨论**: 评论者从多角度展开讨论：有人指出类似问题在 Microsoft Copilot 中也存在（干扰'Ć'输入）；有人批评浏览器缺乏简便的键组合检测 API，开发者也不愿自行实现；还有人从语言学视角称赞文章的文化背景介绍。整体认可技术深度，并呼吁浏览器改进快捷键冲突处理。

**标签**: `#Polish`, `#keyboard shortcuts`, `#Unicode`, `#browser bugs`, `#localization`

---

<a id="item-10"></a>
## [KIDS 法案要求在线年龄验证引发隐私担忧](https://www.eff.org/deeplinks/2026/06/kids-act-would-require-age-checks-get-online) ⭐️ 7.0/10

电子前哨基金会（EFF）警告，美国《KIDS 法案》要求在线平台进行年龄验证，这可能导致用户隐私和言论自由受到威胁。该法案旨在保护儿童，但 EFF 认为其实施方式会破坏在线匿名性。 如果该法案通过，所有用户在上网时都可能需要提交身份认证，这将大幅增加个人数据收集风险，并可能被用于监控和审查。对自由开放的互联网生态构成深远影响。 法案覆盖那些利用用户个人信息进行广告、营销或内容推荐的平台。年龄验证技术可能包括 AI 自拍、数字 ID 等，但批评者指出这些技术仍会暴露用户身份，且法案定义模糊，容易扩大适用范围。

hackernews · bilsbie · Jun 28, 11:56 · [社区讨论](https://news.ycombinator.com/item?id=48706560)

**背景**: 近年来，多国以保护儿童为由推动在线年龄验证立法，但争议不断。年龄验证通常要求用户提供政府 ID 或生物特征，这与互联网长期倡导的匿名原则相悖。类似法案如《儿童在线安全法案》（KOSA）也面临隐私担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiuntethered.com/news/kids-act-age-verification-online-access/">KIDS Act Proposes Age Verification for Online Access | AiUntethered</a></li>
<li><a href="https://misryoum.com/kids-act-age-checks-could-strip-online-anonymity">KIDS Act Age Checks Could Strip Online Anonymity</a></li>

</ul>
</details>

**社区讨论**: 评论中，有用户质疑法案是否覆盖 Hacker News 这类不带广告推荐功能的网站；另有人指出社交媒体影响心理健康的证据并不充分，怀疑背后有政治或行业游说推动。还有用户讽刺过去教导不要泄露个人信息，如今却被强制要求认证。

**标签**: `#privacy`, `#age verification`, `#legislation`, `#internet regulation`

---

<a id="item-11"></a>
## [VictoriaLogs 列式存储原理解析](https://victoriametrics.com/blog/victorialogs-internals-columnar-storage-on-disk/) ⭐️ 7.0/10

VictoriaMetrics 团队发布技术博客，详细解释了其开源日志数据库 VictoriaLogs 如何采用列式布局高效存储日志数据。 该博客深入展示了列式存储在日志管理中的应用优势，有助于用户理解如何通过列式存储提升大规模日志的压缩率和查询性能。 列式存储将同一字段的数据连续存放，便于高效压缩和快速扫描，但写入操作相对行式存储有更高开销。VictoriaLogs 针对日志场景优化了列式存储的实现。

rss · Lobsters · Jun 28, 12:23

**背景**: 列式存储（Columnar Storage）是一种数据组织方式，将表格中同一列的数据连续存储，不同于行式存储将整行数据存为一体。列式存储适合分析型查询（如只需少数列），能显著减少 I/O 并提高压缩率，因此在 OLAP 场景中广泛使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://victoriametrics.com/products/victorialogs/">VictoriaLogs : Scalable | Open Source | Logs DB & Logging Solution</a></li>
<li><a href="https://en.wikipedia.org/wiki/Column_storage">Column storage</a></li>

</ul>
</details>

**标签**: `#log management`, `#columnar storage`, `#VictoriaLogs`, `#database internals`

---

<a id="item-12"></a>
## [基于类型代数的解析方法（2019）](https://www.cl.cam.ac.uk/~nk480/parsing.pdf) ⭐️ 7.0/10

这篇论文提出了一种使用类型化上下文无关表达式来描述语法的方法，并从中推导出一个保证线性时间解析、无回溯、单符号前瞻的解析器组合子库。 该方法将类型系统和代数方法引入解析领域，提高了解析器的安全性和效率，对函数式编程和编译器实现有重要指导意义。 该库不仅遵守上下文无关表达式的自然指称语义，还利用类型信息实现了分阶段版本，从而大幅提升性能。

rss · Lobsters · Jun 28, 15:45

**背景**: 解析是将文本转换为结构化数据的过程，传统方法如回溯解析可能效率低下。本文提出的类型代数方法通过类型约束保证解析的线性时间和无回溯特性，为构建高效、可靠的解析器提供了新思路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dl.acm.org/doi/10.1145/3314221.3314625">A typed, algebraic approach to parsing | Proceedings of the ...</a></li>
<li><a href="https://www.cl.cam.ac.uk/~jdy22/papers/a-typed-algebraic-approach-to-parsing.pdf">A Typed, Algebraic Approach to Parsing - University of Cambridge</a></li>

</ul>
</details>

**标签**: `#parsing`, `#formal methods`, `#type theory`, `#functional programming`

---

<a id="item-13"></a>
## [破窗构建中的离奇 bug 解析](https://algassert.com/post/2603) ⭐️ 7.0/10

软件工程师在《Unfathomable bugs》系列第 10 期中，揭示了一个与“破窗效应”相关的构建系统疑难杂症。该 bug 源于编译过程中未修复的小问题逐渐累积，最终导致构建失败或产生意外行为。 该案例深刻警示了软件工程中维护代码整洁的重要性，忽视小问题可能引发难以调试的连锁故障。这对开发团队制定代码评审和持续重构策略具有借鉴意义。 文章标题明确指出“Broken Windows Build”，暗示构建环境因长期忽视微小警告而出现非预期错误。虽然具体技术细节未公开，但该系列以深入浅出的方式剖析真实 bug，具有较高教学价值。

rss · Lobsters · Jun 28, 20:38

**背景**: “破窗效应”原本是犯罪学理论，指环境中的无序现象若不及时纠正，会诱使他人效仿恶化。在软件工程中，该理论用于比喻代码库中未修复的小缺陷会逐渐降低整体质量，增加维护成本和出错概率。本文正是基于这一视角，探讨构建系统如何因“破窗”而崩溃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danielemargutti.com/2022/03/28/broken-window-principle-applied-to-software">The broken window principle applied to software - Daniele Margutti</a></li>

</ul>
</details>

**标签**: `#software engineering`, `#debugging`, `#bugs`, `#build systems`

---