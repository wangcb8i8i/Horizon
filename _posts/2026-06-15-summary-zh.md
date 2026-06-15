---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> From 23 items, 16 important content pieces were selected

---

1. [JavaScript 的诞生与消亡：2014 年预言成真](#item-1) ⭐️ 9.0/10
2. [里约热内卢自研 LLM 被指为现有模型合并](#item-2) ⭐️ 8.0/10
3. [Anthropic 的安全承诺与商业化矛盾遭批评](#item-3) ⭐️ 8.0/10
4. [形式化方法：编程的未来](#item-4) ⭐️ 8.0/10
5. [解构 Datalog](#item-5) ⭐️ 8.0/10
6. [写密集型 sysbench 测试：大服务器上现代 Postgres 与 MySQL 对比](#item-6) ⭐️ 8.0/10
7. [简化 ZGC 弱引用处理](#item-7) ⭐️ 8.0/10
8. [Kage：将网站打包为单个二进制文件离线查看](#item-8) ⭐️ 7.0/10
9. [用 M1 Max 和开源模型索引 669GB GoPro 视频](#item-9) ⭐️ 7.0/10
10. [zeroserve 实现 Caddy 兼容，性能提升 3 倍但缺少 ACME](#item-10) ⭐️ 7.0/10
11. [保罗·格雷厄姆谈如何赚十亿美元引发争议](#item-11) ⭐️ 7.0/10
12. [Zinnia：用 Rust 编写的模块化类 Unix 内核](#item-12) ⭐️ 7.0/10
13. [Emacs 内置功能更丰富，第三方包可替代](#item-13) ⭐️ 7.0/10
14. [ReactOS 里程碑：成功运行《半条命》](#item-14) ⭐️ 7.0/10
15. [Miri 实现每秒 8000 次段错误的 FFI 测试](#item-15) ⭐️ 7.0/10
16. [Siri 的未来：私有推理为何不够隐私](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [JavaScript 的诞生与消亡：2014 年预言成真](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 9.0/10

2014 年的一场演讲准确预测了 JavaScript 将作为编译目标语言的崛起，并最终被 WebAssembly 等新技术取代。 该演讲的预言已被 TypeScript、WebAssembly 等现实发展证实，深刻影响了 Web 开发的演进方向。 演讲中提到的 asm.js 已基本被 WebAssembly 取代，但 JavaScript 仍需作为胶水代码处理 DOM 操作，未完全消亡。

hackernews · subset · Jun 14, 12:38 · [社区讨论](https://news.ycombinator.com/item?id=48526661)

**背景**: 编译目标是指一种语言被设计为其他高级语言编译后的输出格式，例如 C/C++可通过 Emscripten 编译为 JavaScript。转译（Transpilation）是指将一种高级语言转换为另一种高级语言，如 TypeScript 转译为 JavaScript，使得开发者可以使用更现代的语言特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transpilation">Transpilation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Source-to-source_compiler">Source-to-source compiler - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论普遍认为演讲的预测非常准确，但也指出 WebAssembly 进展不如预期，仍依赖 JavaScript 处理 DOM。有人调侃每几年就会发明一个更好的 JavaScript，然后转译到 JavaScript。

**标签**: `#JavaScript`, `#WebAssembly`, `#programming-languages`, `#history`, `#predictions`

---

<a id="item-2"></a>
## [里约热内卢自研 LLM 被指为现有模型合并](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

分析显示，里约热内卢市政府发布的声称自研的大型语言模型 Rio-3.5-Open-397B，实际上是约 60% Nex-N2 Pro 与 40% Qwen3.5-397B-A17B 的加权合并，并非完全自主训练。 这一事件引发了关于开源 AI 社区中模型归属和透明度的讨论，可能影响公众对政府或机构自主 AI 研发能力的信任，并凸显了模型合并技术在缺乏适当披露时可能造成的误导。 该模型的每个权重张量在数千个标准差内与 0.6/0.4 的混合比例一致，覆盖所有 60 层和网络组件，排除了普通微调的可能性。发起讨论的 GitHub issue 提供了详细数学证据。

hackernews · unrvl22 · Jun 14, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并是一种将两个或多个 LLM 的权重直接组合的技术，无需额外训练即可生成新模型。常用方法包括加权平均、线性插值等。这种技术成本低廉，但若未明确披露原始模型来源，可能被误认为原创工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2408.07666">[2408.07666] Model Merging in LLMs , MLLMs, and Beyond: Methods...</a></li>
<li><a href="https://mlabonne.github.io/blog/posts/2024-01-08_Merge_LLMs_with_mergekit.html">Merge Large Language Models with MergeKit – Maxime Labonne</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有人推测官方可能基于相同基模型但未披露 Nex 成分，而改进来自于权重重加后策略蒸馏。也有评论者指出模型合并的稳健性令人惊讶，简单线性组合居然能提升性能。部分用户对可能缺乏署名表示担忧。

**标签**: `#LLM`, `#model merging`, `#open-source`, `#controversy`, `#AI ethics`

---

<a id="item-3"></a>
## [Anthropic 的安全承诺与商业化矛盾遭批评](https://www.verysane.ai/p/did-anthropic-ask-for-this) ⭐️ 8.0/10

Anthropic 因其在 AI 安全上的公开立场与其追求盈利和政府合同的行动不一致而受到广泛批评。社区指出该公司从备受赞誉的安全先锋转变为陷入“安全宣言-变现”陷阱的典型企业。 这反映了 AI 公司在道德理想与商业现实之间的典型困境，可能影响公众对整个 AI 安全领域的信任。Anthropic 作为安全导向的领头羊，其行为转变具有行业警示意义。 评论特别提到 Anthropic 与美国国防部的合同成为公众看法转变的关键节点。公司随后开始“削弱”其安全措施以维持增长，这与早期高调的安全承诺形成对比。

hackernews · ad8e · Jun 14, 22:23 · [社区讨论](https://news.ycombinator.com/item?id=48533504)

**背景**: Anthropic 是一家以 AI 安全为核心理念的初创公司，由前 OpenAI 员工创立，长期强调防止 AI 造成灾难性风险。然而随着行业竞争加剧和商业化压力，其安全立场开始软化，例如接受政府合同并调整产品优先级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/most-important-ai-company-youre-fully-paying-attention-sahil-ansari-vgese">The most important AI company you're not fully paying attention to just...</a></li>

</ul>
</details>

**社区讨论**: 社区普遍认为 Anthropic 陷入了典型的“安全宣言-变现”陷阱，从公众眼中的“最佳公司”迅速跌落。有评论指出其创始人可能出于傲慢而设置只有自己才能达到的安全标准，而另一些人则为 Anthropic 辩护，认为其确实面临生存威胁，需要平衡安全与商业成功。

**标签**: `#AI safety`, `#Anthropic`, `#tech criticism`, `#artificial intelligence`

---

<a id="item-4"></a>
## [形式化方法：编程的未来](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

Jane Street 发布了关于形式化方法在编程中角色与未来的博客文章，引发了社区关于证明自动化、表达类型和 AI 时代验证的深入讨论。 在 AI 生成代码日益增多的背景下，形式化方法能为软件正确性提供数学保证，其发展可能改变编程范式，使验证成为核心技能。 社区评论提及早期证明自动化工具如 Oppen-Nelson 简化器和 Boyer-Moore 证明器，以及 Scala 3 中通过表达类型实现编译时验证的方式，展现了形式化方法的不同技术路线。

hackernews · eatonphil · Jun 14, 12:35 · [社区讨论](https://news.ycombinator.com/item?id=48526633)

**背景**: 形式化方法是一类基于数学逻辑的软件验证技术，包括定理证明、模型检查等，旨在从数学上证明程序满足其规范。尽管历史悠久，但由于其高门槛和复杂性，在工业界应用仍有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/roehst/awesome-formal-methods">GitHub - roehst/awesome- formal - methods : Awesome resources on...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_automation">Proof automation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区观点多元：有评论者分享了早期证明自动化的经验，肯定了自动化工具的作用；有人通过 Scala 3 表达类型减少测试需求；也有人质疑形式化规格与测试的本质差异，认为二者可能面临同样的问题。

**标签**: `#formal methods`, `#programming`, `#verification`, `#Scala`, `#AI`

---

<a id="item-5"></a>
## [解构 Datalog](https://www.rntz.net/post/my-thesis.html) ⭐️ 8.0/10

一篇名为《Deconstructing Datalog》的论文或博文深入剖析了 Datalog 语言的内部设计与实现方法，可能包含作者毕业论文的核心成果。 Datalog 作为逻辑编程和数据库查询领域的重要语言，这篇详细分析有助于开发者理解其底层机制，推动相关工具和系统的优化。 该文章很可能涵盖了 Datalog 的求值策略（如自底向上计算）、规则推理机制以及与传统 Prolog 的差异等关键技术细节。

rss · Lobsters · Jun 14, 17:07

**背景**: Datalog 是一种声明式逻辑编程语言，语法上是 Prolog 的子集，但采用自底向上的求值模型而非 Prolog 的自顶向下模型。它广泛应用于数据库查询语言（如 Datomic）和静态分析等领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Datalog">Datalog - Wikipedia</a></li>

</ul>
</details>

**标签**: `#datalog`, `#logic-programming`, `#databases`, `#programming-languages`

---

<a id="item-6"></a>
## [写密集型 sysbench 测试：大服务器上现代 Postgres 与 MySQL 对比](http://smalldatum.blogspot.com/2026/06/write-heavy-sysbench-tests-large-server.html) ⭐️ 8.0/10

该文章对现代版本的 PostgreSQL 和 MySQL 在大型服务器上进行了写密集型的 sysbench 基准测试，对比了它们的性能表现。 这次测试结果对数据库工程师在生产环境中进行数据库选型和性能调优具有重要参考价值，特别是在高并发写入场景下。 测试使用 sysbench 工具，专注于写密集型工作负载，并运行在一台拥有大量 CPU 核心和内存的大型服务器上，以评估数据库的扩展性。

rss · Lobsters · Jun 14, 15:38

**背景**: Sysbench 是一个开源的、多线程的 Linux 基准测试工具，常用于评估 CPU、内存、文件 I/O 以及数据库（尤其是 MySQL）的性能。写密集型测试模拟大量写入操作，对数据库的并发写入能力和事务处理能力进行压力测试。大型服务器（如多路 CPU、大内存）能够展示现代数据库在高性能硬件上的实际表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sysbench">Sysbench - Wikipedia</a></li>
<li><a href="https://medium.com/@amol.deshmukh_97340/running-custom-workloads-with-sysbench-c6d5338a503b">Running Custom Workloads with Sysbench | by Amol... | Medium</a></li>

</ul>
</details>

**标签**: `#database`, `#postgresql`, `#mysql`, `#performance`, `#sysbench`

---

<a id="item-7"></a>
## [简化 ZGC 弱引用处理](https://inside.java/2026/06/11/thesis-simplify-weak-reference-processing-zgc/) ⭐️ 8.0/10

一篇论文提出了简化 ZGC 中弱引用处理的方法，旨在提升垃圾收集器的性能和可维护性。 弱引用处理是垃圾收集的关键环节，简化其处理可以减少 GC 停顿时间，提高应用响应性，对依赖低延迟的 Java 应用尤为重要。 该论文可能涉及重构弱引用处理流程，减少不必要的同步或简化算法，具体细节需阅读论文原文。

rss · Lobsters · Jun 14, 12:36

**背景**: ZGC 是 OpenJDK 中面向低延迟的垃圾收集器，它并发执行大部分 GC 工作，将暂停时间控制在毫秒级。弱引用（如 WeakReference）允许 GC 在不影响对象可达性的情况下回收对象，其处理流程需要额外的扫描和清理。简化该流程有助于降低 GC 开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.openjdk.org/spaces/zgc/pages/34668579/Main">Main - ZGC - OpenJDK Wiki</a></li>
<li><a href="https://docs.oracle.com/en/java/javase/21/gctuning/z-garbage-collector.html">The Z Garbage Collector</a></li>
<li><a href="https://en.wikipedia.org/wiki/Weak_reference">Weak reference - Wikipedia</a></li>

</ul>
</details>

**标签**: `#ZGC`, `#garbage collection`, `#JVM`, `#performance`, `#weak references`

---

<a id="item-8"></a>
## [Kage：将网站打包为单个二进制文件离线查看](https://github.com/tamnd/kage) ⭐️ 7.0/10

Kage 是一个新发布的命令行工具，能够将网页镜像并打包成一个独立的二进制文件，用户执行该文件即可离线浏览网站内容。 该工具极大简化了离线文档和原型的共享与存档，特别适合无网络环境下的协作和知识保存，为开发者提供了一种便捷的网站离线访问方案。 Kage 使用无头 Chrome 抓取网站静态内容，支持两种输出格式：单个 HTML 文件和自包含的二进制文件。二进制文件内嵌了一个迷你服务器，运行时需执行 kage serve 命令。

hackernews · tamnd · Jun 14, 17:25 · [社区讨论](https://news.ycombinator.com/item?id=48529990)

**背景**: 离线查看网站通常需要保存整个目录结构或使用工具如 SingleFile 生成单个 HTML 文件。Kage 则进一步将站点与一个轻量级 HTTP 服务器打包成一个可执行文件，用户只需运行该文件即可在浏览器中访问，无需额外依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tamnd/kage">GitHub - tamnd/ kage : Shadow any website for offline viewing, with the...</a></li>
<li><a href="https://cybermediacreations.com/show-hn-kage-shadow-any-website-to-a-single-binary-for-offline-viewing/">Show HN: Kage – Shadow any website to a single binary for offline ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48529990">Show HN: Kage – Shadow any website to a single binary for offline ...</a></li>

</ul>
</details>

**社区讨论**: 社区用户对 Kage 的实用性表示认可，提及可用于公司 Wiki 离线访问和 AI 原型版本控制。有用户建议支持直接通过浏览器打开而无需单独服务进程，也有用户指出 SingleFile 能更轻量地实现类似功能。

**标签**: `#offline`, `#website mirroring`, `#static site`, `#tool`, `#binary`

---

<a id="item-9"></a>
## [用 M1 Max 和开源模型索引 669GB GoPro 视频](https://news.ycombinator.com/item?id=48528029) ⭐️ 7.0/10

一位开发者使用 M1 Max 电脑和开源机器学习模型，在本地索引了 669GB（约 2207 个）的 GoPro 视频，并实现了通过自然语言搜索精彩片段，然后直接导出到 DaVinci Resolve 时间线。 该项目展示了个人开发者利用本地硬件和开源 ML 模型实现大规模视频索引的可行性，为户外运动爱好者和视频创作者提供了无需云服务的隐私友好型解决方案，同时也引发了关于本地 AI 能力与传统编辑工具融合的讨论。 共索引 628 个视频（总时长 15 小时 13 分钟），帧分析管道以 1fps 速率处理了 57,537 帧，总共耗时 67 小时 40 分钟。但社区指出 DaVinci Resolve 21 Studio 版已内置 AI 智能搜索功能，可能降低了这类自建项目的独特价值。

hackernews · iliashad · Jun 14, 15:13

**背景**: 视频索引是指从视频中提取元数据（如场景、物体、语音等），以便快速搜索和检索。传统上这需要大量人工或依赖云端 AI 服务，而开源的机器学习模型（如用于图像分类、目标检测的模型）可以在本地运行，保护隐私。GoPro 相机常用于户外运动，用户积累大量视频后难以手动回顾。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oneuptime.com/blog/post/2026-02-16-ai-powered-video-indexing-azure-video-indexer-cognitive-search/view">How to Create an AI-Powered Video Indexing Solution with Azure Video Indexer</a></li>
<li><a href="https://www.progress.com/agentic-rag/use-cases/ai-video-indexing">AI Video Indexing & AI Search with a RAG Database</a></li>
<li><a href="https://www.litmedia.ai/resource-video-tips/open-source-ai-video-analysis/">Best Open Source AI Video Analysis Tools in 2025</a></li>

</ul>
</details>

**社区讨论**: 社区整体持积极态度，但讨论了实用性问题：有用户指出 DaVinci Resolve 21 已内置类似索引功能，削弱了项目的创新性；也有用户质疑索引结果的质量，认为示例视频中的“亮点”并不出彩。同时，另一位开发者分享了几乎相同的项目，并感叹本地 AI 的潜力巨大。

**标签**: `#Video Indexing`, `#Machine Learning`, `#GoPro`, `#Local AI`, `#Personal Project`

---

<a id="item-10"></a>
## [zeroserve 实现 Caddy 兼容，性能提升 3 倍但缺少 ACME](https://su3.io/posts/zeroserve-caddy-compat) ⭐️ 7.0/10

zeroserve 宣布与 Caddy 配置兼容，实现了 3 倍吞吐量提升和 70%延迟降低，但缺少 ACME 自动证书管理和插件支持。 这一性能突破对 Web 服务器领域具有重要意义，但缺失的关键功能可能限制其实际采用，尤其在需要自动 HTTPS 证书管理的场景中。 zeroserve 基于 io_uring 实现高性能，但社区批评其 ACME 支持和插件生态缺失，且 io_uring 在网络安全方面存在潜在风险。

hackernews · losfair · Jun 14, 13:43 · [社区讨论](https://news.ycombinator.com/item?id=48527145)

**背景**: io_uring 是 Linux 内核 5.1 引入的异步 I/O 接口，旨在提高文件及网络 I/O 性能。zeroserve 是一个零配置、基于 io_uring 的 HTTPS 服务器，可直读 Caddy 配置文件。Caddy 则以自动 HTTPS 和插件系统著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/losfair/zeroserve">GitHub - losfair/zeroserve: Zero-config, fast `io_uring`-based HTTPS server. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io_uring - Wikipedia</a></li>
<li><a href="https://blogs.oracle.com/linux/an-introduction-to-the-io-uring-asynchronous-io-framework">An Introduction to the io_uring Asynchronous I/O Framework | linux</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍认为缺少 ACME 是重大缺陷，有用户指出 io_uring 存在安全风险，另有人惊讶于 nginx 的性能仍表现良好。

**标签**: `#performance`, `#webserver`, `#io_uring`, `#caddy`, `#zeroserve`

---

<a id="item-11"></a>
## [保罗·格雷厄姆谈如何赚十亿美元引发争议](https://paulgraham.com/earn.html) ⭐️ 7.0/10

保罗·格雷厄姆发表了一篇关于如何通过创业赚取十亿美元的文章，引发了社区对财富创造与道德的热烈讨论。 这篇文章反映了科技界对财富本质的深层分歧：一方认为创业创造巨大价值，另一方则质疑巨额财富的正当性。这种辩论对于理解当代创业者心态和公众对科技巨头的看法至关重要。 格雷厄姆在文中强调“赚取”一词的道德含义，但评论者指出其用法与公众理解（如 AOC 所提倡的）不同。部分评论也讨论了指数增长模型和创造性破坏带来的道德责任。

hackernews · kingstoned · Jun 14, 11:50 · [社区讨论](https://news.ycombinator.com/item?id=48526360)

**背景**: 保罗·格雷厄姆是知名创业孵化器 Y Combinator 的联合创始人，其文章常聚焦创业哲学。本文延续了他对创业财富的思考，但未提供具体方法，更侧重于价值判断。

**社区讨论**: 社区反应两极化：有人批评负面评论是“空洞的意识形态”，也有人引用指数增长论证巨富可能性；多个评论指出格雷厄姆对“赚取”的定义具有误导性，忽略了财富积累中的外部性。

**标签**: `#startups`, `#wealth`, `#entrepreneurship`, `#Paul Graham`, `#software engineering`

---

<a id="item-12"></a>
## [Zinnia：用 Rust 编写的模块化类 Unix 内核](https://zinnia-os.org/) ⭐️ 7.0/10

Zinnia 是一个采用 Rust 语言编写的、模块化的 64 位类 Unix 内核，现已作为新的开源项目发布。 该项目展示了利用 Rust 的内存安全特性构建操作系统内核的可行性，可能为操作系统开发提供更安全的替代方案。 Zinnia 采用模块化架构，允许灵活组合内核组件；相比单体内核，模块化设计在嵌入式系统或定制场景中更具优势。

rss · Lobsters · Jun 14, 21:05

**背景**: 类 Unix 操作系统指行为类似 Unix 的系统，如 Linux 和 FreeBSD，但无需遵循单一 Unix 规范。模块化内核架构允许将部分内核功能作为独立模块运行，提高灵活性和可维护性。Rust 语言以其内存安全性著称，适合开发系统软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Monolithic_kernel">Monolithic kernel - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unix-like_operating_system">Unix-like operating system</a></li>
<li><a href="https://thamizhelango.medium.com/netbsds-rump-kernel-framework-a-deep-dive-into-modular-kernel-architecture-b19e5aaad06d">NetBSD’s Rump Kernel Framework: A Deep Dive into Modular Kernel ...</a></li>

</ul>
</details>

**标签**: `#kernel`, `#Rust`, `#operating system`, `#Unix-like`, `#modular`

---

<a id="item-13"></a>
## [Emacs 内置功能更丰富，第三方包可替代](https://karthinks.com/software/even-more-batteries-included-with-emacs/) ⭐️ 7.0/10

博客作者 Karthik 发表了一篇文章，展示了 Emacs 内置功能可以替代许多常用的第三方包，并提供了实用示例。 这篇文章对 Emacs 用户很有价值，可以帮助他们减少对第三方包的依赖，提高编辑器的稳定性和一致性，同时揭示 Emacs 的深度和灵活性。 该文章是 Karthik 关于 Emacs 内置功能的系列之一，作者本人拥有 10 年 Emacs 使用经验，表示每次阅读都能发现新内容。

rss · Lobsters · Jun 14, 18:43

**背景**: Emacs 是一款高度可扩展的文本编辑器，其核心基于 Emacs Lisp (Elisp) 语言，允许用户和第三方开发者轻松定义扩展。‘Batteries included’ 意指 Emacs 自带大量功能和工具，无需额外安装包即可完成任务。

**标签**: `#Emacs`, `#productivity`, `#elisp`, `#text-editor`, `#software-engineering`

---

<a id="item-14"></a>
## [ReactOS 里程碑：成功运行《半条命》](https://www.phoronix.com/news/ReactOS-Running-Half-Life) ⭐️ 7.0/10

ReactOS 这一开源操作系统近日达到重要里程碑，成功运行了经典游戏《半条命》（Half-Life），验证了其对 Windows 应用程序的二进制兼容性。 这一进展表明 ReactOS 在兼容 Windows 软件方面取得实质性突破，对于希望使用开源替代品替代 Windows 的用户和开发者具有重要意义。 运行《半条命》需要稳定的系统调用和 DirectX 支持，这展示了 ReactOS 在驱动和图形 API 上的进步，但仍需进一步完善以支持更复杂的现代应用。

rss · Lobsters · Jun 14, 01:01

**背景**: ReactOS 是一个旨在二进制兼容 Windows NT 系列操作系统的自由开源项目，目标是无缝运行 Windows 应用程序和驱动程序。此前 ReactOS 已能运行部分简单软件，但游戏对系统稳定性要求更高，成功运行《半条命》标志其兼容性的重大提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ReactOS">ReactOS - Wikipedia</a></li>
<li><a href="https://github.com/reactos/reactos">GitHub - reactos/reactos: A free Windows-compatible Operating System</a></li>
<li><a href="https://reactos.org/">Front Page | ReactOS Project</a></li>

</ul>
</details>

**社区讨论**: 在 lobste.rs 讨论中，社区对 ReactOS 进步表示认可，但也指出距离完全兼容现代 Windows 应用仍有很大距离，部分用户对开发速度表示担忧。

**标签**: `#ReactOS`, `#open-source`, `#Windows compatibility`, `#Half-Life`, `#operating systems`

---

<a id="item-15"></a>
## [Miri 实现每秒 8000 次段错误的 FFI 测试](https://youtu.be/9X-ngiKo_Y0) ⭐️ 7.0/10

在 RustWeek 上，Nia Deckers 发表了一场演讲，展示了如何使用 Miri 工具对 FFI（外部函数接口）代码进行压力测试，并达到了每秒触发 8000 次段错误（segfaults）的速度。 这展示了 Miri 在检测不安全代码中的未定义行为方面的强大能力，尤其对于依赖 FFI 的 Rust 项目，能够帮助开发者发现潜在的内存安全漏洞，提高 Rust 生态系统的整体安全性。 演讲中强调 Miri 可以在运行测试时模拟大量未定义行为，例如越界访问和释放后使用，从而以极高的频率触发段错误，帮助开发者快速定位问题。

rss · Lobsters · Jun 14, 17:12

**背景**: Miri 是一个 Rust 代码的中间级解释器，能够检测未定义行为（UB），如内存越界、未初始化数据使用等。FFI（外部函数接口）是 Rust 与其他语言交互的机制，但容易引入 unsafe 代码和 UB 风险。通过 Miri 对 FFI 代码进行符号执行和检测，可以在测试阶段发现潜在崩溃点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rust-lang/miri">GitHub - rust-lang/miri: An interpreter for Rust's mid-level ...</a></li>
<li><a href="https://research.ralfj.de/papers/2026-popl-miri.pdf">PDF Miri: Practical Undefined Behavior Detection for Rust</a></li>
<li><a href="https://www.rustfaq.org/en/how-to-use-miri-to-detect-undefined-behavior/">How to Use Miri to Detect Undefined Behavior — Rust FAQ</a></li>

</ul>
</details>

**标签**: `#Rust`, `#FFI`, `#Miri`, `#Safety`, `#Undefined Behavior`

---

<a id="item-16"></a>
## [Siri 的未来：私有推理为何不够隐私](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/) ⭐️ 7.0/10

一篇技术文章指出，苹果 Siri 当前采用的私有推理方法可能无法提供足够的隐私保证。作者认为，即使使用了同态加密等技术，用户数据仍有可能被推断或泄露。 该批评直接挑战了苹果在 AI 领域强调的隐私保护承诺，可能影响用户对 Siri 及苹果生态的信任。若私有推理缺陷被证实，将推动整个行业重新评估隐私保护技术的有效性。 文章分析的重点是私有推理（Private Inference）与同态加密（Homomorphic Encryption）在实际部署中的局限性，例如模型权重泄露或侧信道攻击。苹果已在 iOS 18 中引入同态加密用于 Live Caller ID Lookup 等功能，但文章认为这不足以杜绝隐私风险。

rss · Lobsters · Jun 14, 03:50

**背景**: 私有推理（Private Inference）是一种隐私保护机器学习技术，允许服务器在不暴露用户输入数据或模型参数的情况下执行推理。同态加密是该领域的关键工具之一，可直接对密文进行计算。苹果于 2024 年开源了 Swift 同态加密库，并在 Siri 等场景中探索应用，但技术文章指出其隐私保证可能弱于预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/homomorphic-encryption">Combining Machine Learning and Homomorphic Encryption in the Apple Ecosystem - Apple Machine Learning Research</a></li>
<li><a href="https://www.forbes.com/sites/davidbirch/2024/12/06/witchcraft-or-mathematics-apples-new-encryption-tool-is-important/">Witchcraft Or Mathematics, Apple’s New Encryption Tool Is Important</a></li>

</ul>
</details>

**标签**: `#privacy`, `#inference`, `#Apple`, `#Siri`, `#cryptography`

---