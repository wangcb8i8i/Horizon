---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> From 33 items, 27 important content pieces were selected

---

1. [美国科学陷入混乱危机](#item-1) ⭐️ 9.0/10
2. [OpenBSD PPP 协议栈 27 年认证绕过漏洞](#item-2) ⭐️ 9.0/10
3. [Lore：Epic Games 开源版本控制，瞄准游戏开发](#item-3) ⭐️ 8.0/10
4. [美国暂缓将 DeepSeek 列入黑名单，超 100 家中国公司被列为安全风险](#item-4) ⭐️ 8.0/10
5. [OpenAI 财务泄露：年亏损数十亿美元](#item-5) ⭐️ 8.0/10
6. [GLM-5.2 成 Artificial Analysis 领先开源模型](#item-6) ⭐️ 8.0/10
7. [Tesco 因 Broadcom 滥用行为迁移 4 万个 VMware 工作负载](#item-7) ⭐️ 8.0/10
8. [RFC 10008 定义新的 HTTP QUERY 方法，解决 GET 带请求体问题](#item-8) ⭐️ 8.0/10
9. [人类连接：AI 无法复制的竞争护城河](#item-9) ⭐️ 8.0/10
10. [Adam (YC W25) 发布开源 AI CAD 平台 CADAM](#item-10) ⭐️ 7.0/10
11. [机器人赛跑：Claude vs Grok vs DeepSeek 成本效率大比拼](#item-11) ⭐️ 7.0/10
12. [8 位像素风格实时棒球直播网站](#item-12) ⭐️ 7.0/10
13. [大众封锁 GrapheneOS 用户，引隐私争议](#item-13) ⭐️ 7.0/10
14. [与人对话思考胜过独自思考](#item-14) ⭐️ 7.0/10
15. [Bubbles：独立博客版的 Hacker News](#item-15) ⭐️ 7.0/10
16. [Photobucket 索要 5 美元才让用户取回照片](#item-16) ⭐️ 7.0/10
17. [MicroUI：基于 ANSI C 的微型即时模式 UI 库](#item-17) ⭐️ 7.0/10
18. [仅凭 ID 即可 Rickroll 整个 FIFA 世界杯](#item-18) ⭐️ 7.0/10
19. [Pull Requests 如同免费小狗](#item-19) ⭐️ 7.0/10
20. [Oklch 颜色空间实用指南：面向普通开发者](#item-20) ⭐️ 7.0/10
21. [Google Manifest V3 对广告拦截器的影响](#item-21) ⭐️ 7.0/10
22. [用 Rust 智能框架提升预算 AI 模型性能](#item-22) ⭐️ 7.0/10
23. [简化 GHC 升级的实用策略](#item-23) ⭐️ 7.0/10
24. [《指挥官基恩》游戏引擎架构白皮书分析](#item-24) ⭐️ 7.0/10
25. [R 核心团队荣获 2026 年 Rousseeuw 统计学奖](#item-25) ⭐️ 7.0/10
26. [FMAG：单指令 GPU 虚拟机及工具链](#item-26) ⭐️ 7.0/10
27. [Docker Desktop 网络底层原理](#item-27) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [美国科学陷入混乱危机](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/) ⭐️ 9.0/10

美国科学界正面临资金削减、签证限制和机构不稳定的多重打击，导致大量研究人员离开美国或彻底放弃科研事业。 这一危机将严重削弱美国的科研创新能力和全球领导地位，并可能引发长期的人才流失和科技竞争力下降。 评论中提到的案例包括：一位操作光学陷阱的研究人员因科研环境恶化而计划移民；许多教授的资助枯竭，且因签证限制无法雇佣外国研究生；科研人员普遍感到焦虑，并开始寻找备选出路。

hackernews · presspot · Jun 17, 09:54 · [社区讨论](https://news.ycombinator.com/item?id=48568058)

**背景**: 美国科研长期依赖联邦政府拨款（如国立卫生研究院的 R01 项目）、国际人才流动和稳定的机构支持。近年来，政策变化和预算削减破坏了这一体系，导致科研环境急剧恶化，甚至被视为“科学死亡”。

**社区讨论**: 评论中普遍弥漫着悲观和焦虑情绪。多位用户讲述了自身或身边人被迫离开科研或美国的故事，认为这是系统性崩溃。但也有少数人认为混乱中仍有机遇，比如通过非传统渠道获得资助。

**标签**: `#science policy`, `#research funding`, `#U.S. science crisis`, `#brain drain`

---

<a id="item-2"></a>
## [OpenBSD PPP 协议栈 27 年认证绕过漏洞](https://blog.argus-systems.ai/blog/openbsd-pap-27-year-auth-bypass.html) ⭐️ 9.0/10

研究人员发现 OpenBSD 的 PPP 协议栈中存在一个存在了 27 年的认证绕过漏洞，攻击者可利用该漏洞绕过 PAP（密码认证协议）认证。 该漏洞影响以安全著称的 OpenBSD 操作系统，由于存在时间长达 27 年，可能导致大量设备和网络连接面临未经授权访问的风险。 漏洞位于 PPP 协议栈的 PAP 实现中，可能允许攻击者在无需有效凭证的情况下完成认证；具体细节和利用方式尚未完全公开，但已引起安全社区高度关注。

rss · Lobsters · Jun 17, 05:14

**背景**: PPP（点对点协议）是用于建立拨号或直接连接的标准数据链路层协议，常使用 PAP（密码认证协议）进行用户身份验证。PAP 通过两步握手交换明文密码，安全性较弱。OpenBSD 以其代码审计和安全设计闻名，此漏洞的长期存在凸显了代码遗留问题的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Password_Authentication_Protocol">Password Authentication Protocol - Wikipedia</a></li>
<li><a href="https://man.openbsd.org/OpenBSD-3.9/sppp.4">sppp(4) - OpenBSD manual pages</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#openbsd`, `#authentication`, `#ppp`

---

<a id="item-3"></a>
## [Lore：Epic Games 开源版本控制，瞄准游戏开发](https://lore.org/) ⭐️ 8.0/10

Epic Games 发布了 Lore，一个开源、支持大规模二进制文件和高并发协作的版本控制系统，旨在与 Perforce 竞争。它使用 MIT 许可证，并提供文件锁定、权限管理等游戏开发所需的核心功能。 游戏开发长期依赖 Perforce 处理大文件和二进制资源，但 Perforce 并非开源且管理成本高。Lore 作为开源替代方案，有望降低游戏团队协作门槛，尤其对 Unreal Engine 生态意义重大。 Lore 是 Unreal Editor for Fortnite (UEFN) 的内置版本控制系统，但开源版本目前由于专有压缩格式无法直接与 UEFN 通信。其设计强调可扩展性，支持原子操作和分布式架构，目标是处理大型游戏项目。

hackernews · Lobsters · Jun 17, 14:30 · [社区讨论](https://news.ycombinator.com/item?id=48571081)

**背景**: 版本控制系统（VCS）用于跟踪文件变更，Git 是主流通用 VCS，但在处理大尺寸二进制文件（如纹理、3D 模型）时效率低下，且缺乏文件锁定机制。游戏行业常采用集中式 VCS（如 Perforce），它提供文件锁定、细粒度权限和更好的大文件支持，但需要商业许可证。Lore 由 Epic Games 开发，旨在填补 Git 在游戏开发场景的不足，并提供一个开源、可自托管的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epicgames.github.io/lore/faq/">FAQ - Lore Developer Documentation</a></li>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/ lore : Lore is a next-generation, open source ...</a></li>
<li><a href="https://www.phoronix.com/news/Epic-Games-Lore-VCS">Epic Games Announces Lore Open - Source Version Control System</a></li>

</ul>
</details>

**社区讨论**: 社区普遍对 Lore 表示欢迎，认为它直接挑战了 Perforce 在游戏开发领域的统治地位。许多用户指出 Git 的 UI 和分支操作对非技术人员不友好，而 Perforce 虽功能强大但配置复杂、许可证昂贵。Lore 的开源特性降低了入门成本，但部分评论也提到其与 UEFN 的集成尚不完整，成熟度有待验证。

**标签**: `#version control`, `#game development`, `#open source`, `#scalability`, `#perforce alternative`

---

<a id="item-4"></a>
## [美国暂缓将 DeepSeek 列入黑名单，超 100 家中国公司被列为安全风险](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 8.0/10

美国政府决定推迟将中国 AI 初创公司 DeepSeek 列入贸易黑名单（实体清单），但同时将超过 100 家其他中国公司认定为国家安全风险。 这一决定显示美国对华 AI 政策存在权衡：一方面不愿直接打击表现突出的 DeepSeek，另一方面继续扩大对中国科技企业的限制。它可能影响 DeepSeek 用户（如开发者）的未来使用，并加剧中美技术脱钩趋势。 被列入实体清单意味着美国公司和个人不得向这些企业出售商品或服务，但 DeepSeek 目前暂未被列入。此前另一家中国 AI 公司 Z.ai（智谱）已于 2025 年 1 月被列入清单，但主要依赖美国 GPU 的出口限制早已存在。

hackernews · giuliomagnifico · Jun 17, 03:55 · [社区讨论](https://news.ycombinator.com/item?id=48565498)

**背景**: DeepSeek 是成立于 2023 年的中国 AI 公司，其开源模型（如 DeepSeek-R1）以低成本达到接近顶尖水平，引发了全球关注。美国实体清单是出口管制工具，用于限制外国实体获取美国技术，但不会完全禁止贸易——被禁者仍可购买美国产品，只是无法获得美国供应商的销售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(chatbot)">DeepSeek (chatbot) - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/WhatIs/feature/DeepSeek-explained-Everything-you-need-to-know">DeepSeek explained: Everything you need to know - TechTarget DeepSeek Explained: What Is It and Is It Safe To Use? - ai.nd.edu What is DeepSeek AI? China’s Top AI Chatbot Explained - Beebom DeepSeek (chatbot) - Wikipedia What is DeepSeek, the Chinese AI startup that shook the tech ... What Is DeepSeek? Everything to Know About the New Chinese AI ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论呈现多元观点：有用户表示每天使用 DeepSeek 并担忧未来限制，有人批评美国政策虚伪且难以执行（如“美国防火墙”），也有人指出其他中国 AI 公司早已被列清单且影响有限。部分评论讽刺美国正变得像中国，或认为清单反而提供了投资方向。

**标签**: `#AI regulation`, `#DeepSeek`, `#geopolitics`, `#tech policy`, `#security risks`

---

<a id="item-5"></a>
## [OpenAI 财务泄露：年亏损数十亿美元](https://arstechnica.com/ai/2026/06/leaked-financial-docs-show-openai-is-losing-billions-of-dollars-a-year/) ⭐️ 8.0/10

泄露的财务文件显示，OpenAI 在 2025 年尽管营收达 130 亿美元，但运营亏损高达数十亿美元，其中研发成本是主要支出。 这一财务透明度揭示出 AI 行业领先公司面临的盈利困境，可能影响投资者信心和整个 AI 领域的商业可持续性讨论。 文件显示，OpenAI 营收成本为 75 亿美元，销售和营销支出占相当比例，每付费客户获取成本约 100 美元，而每周活跃用户超 9 亿中仅 5000 万为付费用户。

hackernews · greenchair · Jun 17, 21:31 · [社区讨论](https://news.ycombinator.com/item?id=48577208)

**背景**: OpenAI 起初为非营利组织，后转型为“有限盈利”公司，以吸引投资并推动 AGI 研发。其商业模式依赖高额研发投入和规模化用户增长，但高昂的算力和人才成本导致持续亏损。

**社区讨论**: 社区评论聚焦于成本结构：有观点认为研发成本占比过高，未来应优化推理成本；也有人指出销售成本类似高接触业务，需增长 10 倍才能盈利；还有评论质疑免费用户转付费的难度，以及财务数据细节不足。

**标签**: `#OpenAI`, `#financial analysis`, `#AI industry`, `#business model`, `#startup economics`

---

<a id="item-6"></a>
## [GLM-5.2 成 Artificial Analysis 领先开源模型](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) ⭐️ 8.0/10

GLM-5.2 在 Artificial Analysis 基准测试中成为表现最佳的开源权重模型，其性能接近 Opus 等前沿闭源模型，但成本低得多。 这标志着开源 AI 的重大突破，证明开源模型能以极低价格挑战闭源巨头，可能颠覆行业格局并降低 AI 应用门槛。 GLM-5.2 Max 版本拥有 753B 参数，支持 100 万 token 上下文，在长程任务和复杂推理上较前代 GLM-5.1 有显著提升。

hackernews · himata4113 · Jun 17, 09:12 · [社区讨论](https://news.ycombinator.com/item?id=48567759)

**背景**: GLM 系列由中国智谱 AI（现更名为 Z.ai）开发，自 2025 年 7 月起以 MIT 开源协议发布。Artificial Analysis 是一个独立评测 AI 模型的平台，综合评估智能、速度和成本等维度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.2">GLM-5.2</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://github.com/Z-ai-glm/GLM-5.2">GLM-5.2 Lightweight Installer - GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区讨论热烈，有用户指出 GLM-5.2 在推理效率上仍有提升空间（例如简单任务耗时 15 分钟），但也有用户称赞其以极低成本达到 Opus 级质量，对闭源提供商形成巨大冲击。

**标签**: `#AI`, `#open-source`, `#LLMs`, `#cost efficiency`

---

<a id="item-7"></a>
## [Tesco 因 Broadcom 滥用行为迁移 4 万个 VMware 工作负载](https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/) ⭐️ 8.0/10

英国零售巨头 Tesco 计划在 18 个月内将 4 万个服务器工作负载从 VMware 迁移至其他虚拟化平台，原因是 Broadcom 的定价和许可政策被认为具有滥用性。 这一大规模迁移案例可能引发更多企业效仿，对 VMware 的市场地位构成威胁，同时加速开源替代方案（如 Proxmox）在企业中的采用。 迁移面临数据安全挑战，因为新虚拟化软件与现有备份工具 Veeam 和 Zerto 不兼容，Tesco 需解决兼容性问题。此外，迁移规模巨大，预计耗时 18 个月。

hackernews · Bender · Jun 17, 21:00 · [社区讨论](https://news.ycombinator.com/item?id=48576838)

**背景**: VMware 是业界领先的虚拟化软件，广泛用于企业数据中心。Broadcom 于 2022 年收购 VMware 后更改许可和定价模式，导致许多客户成本激增。Tesco 作为英国最大连锁超市，此举反映了企业应对供应商锁定的典型策略。

**社区讨论**: 社区对迁移规模表示惊讶，并指出 Broadcom 的定价策略已引发普遍不满。有评论认为迁移路径已成熟但工作量巨大，也有人质疑为何需要 18 个月，引发对大规模迁移复杂性的讨论。

**标签**: `#virtualization`, `#enterprise`, `#VMware`, `#Broadcom`, `#migration`

---

<a id="item-8"></a>
## [RFC 10008 定义新的 HTTP QUERY 方法，解决 GET 带请求体问题](https://www.rfc-editor.org/info/rfc10008/) ⭐️ 8.0/10

RFC 10008 正式定义了 HTTP QUERY 方法，这是一种安全且幂等的请求方法，允许在请求体中携带内容，旨在替代带请求体的 GET 请求。 该方法解决了长期以来 GET 请求携带请求体导致的缓存和互操作性问题，为 Web 标准提供了更清晰的语义，可能影响浏览器、缓存代理和 API 设计。 QUERY 方法类似于 POST，但要求幂等性，并可被缓存；缓存键需包含请求体，可能带来实现挑战。该提案经历了多年讨论，最终成为正式 RFC。

hackernews · schappim · Jun 17, 10:51 · [社区讨论](https://news.ycombinator.com/item?id=48568502)

**背景**: HTTP 协议中，GET 方法本不应携带请求体，但实际中部分客户端尝试发送带请求体的 GET，导致历史兼容性问题。QUERY 方法作为新的 HTTP 方法，在保持安全性和幂等性的同时，明确支持请求体，为复杂查询操作提供标准做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://httpwg.org/http-extensions/draft-ietf-httpbis-safe-method-w-body.html">The HTTP QUERY Method</a></li>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008: The HTTP QUERY Method | RFC Editor</a></li>
<li><a href="https://news.ycombinator.com/item?id=48568502">RFC 10008: The new HTTP Query Method | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 社区讨论积极，有评论指出 QUERY 方法命名可能引起混淆，也有人关注缓存键包含请求体的实现难度。部分开发者对 HTML 表单支持 QUERY 表示期待，认为可避免刷新页面时的重新提交警告。总体上，社区认可该方法的必要性，但对其具体实现细节存有疑虑。

**标签**: `#HTTP`, `#RFC`, `#protocol`, `#web standards`, `#caching`

---

<a id="item-9"></a>
## [人类连接：AI 无法复制的竞争护城河](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/) ⭐️ 8.0/10

一篇分析文章指出，真正的人类连接是 AI 无法复制的持久竞争优势，并对比了当前 AI 客服的失败案例。 这提醒企业，在 AI 普及时代，过度依赖自动化可能损害客户关系，而投资人性化服务能成为差异化优势，避免客户流失。 文章以餐厅保留人工预订员为例，说明尽管效率不如在线系统，但人性化沟通能赢得长期忠诚；评论则指出许多企业用 AI 聊天机器人“模拟服务”而非提供实际帮助。

hackernews · speckx · Jun 17, 17:14 · [社区讨论](https://news.ycombinator.com/item?id=48573435)

**背景**: 竞争护城河指企业长期保持优势的能力，如品牌或网络效应。AI 在客服中常被用于降低成本，但可能因缺乏共情和解决问题能力而失败，反而凸显人类情感连接的价值。

**社区讨论**: 讨论中有人质疑“连接”的必要性，认为交易效率更重要；有人讽刺文章可能是 AI 所写；还有人强调服务与产品需并重，且人性化优势在非客户服务类企业中可能不适用。

**标签**: `#human connection`, `#AI limitations`, `#customer service`, `#competitive advantage`, `#business strategy`

---

<a id="item-10"></a>
## [Adam (YC W25) 发布开源 AI CAD 平台 CADAM](https://github.com/Adam-CAD/CADAM) ⭐️ 7.0/10

Adam 团队发布了开源 AI CAD 平台 CADAM，支持通过自然语言或图片生成参数化 3D 模型，输出 OpenSCAD 代码并可直接在浏览器中编辑和导出多种格式。 作为 YC W25 项目，CADAM 将 AI 代码生成能力引入机械设计领域，可能降低 3D 建模门槛，但社区指出 AI 空间推理能力不足，实际工程应用仍有挑战。 CADAM 基于 React（TanStack Start）和 Supabase 后端，采用双模式（参数化/网格）生成模型，参数调整通过正则表达式更新 SCAD 源码，无需 LLM 调用；支持 BOSL2 等库和多种导出格式。

hackernews · zachdive · Jun 17, 16:14 · [社区讨论](https://news.ycombinator.com/item?id=48572553)

**背景**: CAD（计算机辅助设计）是机械工程师用于创建精确 3D 模型的工具，传统上需要手动操作。OpenSCAD 是一种基于代码的 CAD 工具，适合参数化设计。CADAM 试图通过 AI 将自然语言直接转换为可编辑的 CAD 代码，类似“AI 版 TinkerCAD”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tanstack.com/start/latest">TanStack Start</a></li>
<li><a href="https://supabase.com/">Supabase | The Postgres Development Platform.</a></li>

</ul>
</details>

**社区讨论**: 社区反应两极：部分用户认为 AI 能快速生成简单模型，比传统软件更便捷；但许多工程师质疑其可靠性，指出 AI 在空间推理和公差控制上存在根本缺陷，且人工检查 AI 输出往往比直接建模更耗时。

**标签**: `#AI`, `#CAD`, `#open-source`, `#3D modeling`, `#mechanical design`

---

<a id="item-11"></a>
## [机器人赛跑：Claude vs Grok vs DeepSeek 成本效率大比拼](https://openrouter.ai/blog/insights/royale-last-agent-standing/) ⭐️ 7.0/10

OpenRouter 平台发布了一项实验，在模拟跑步机器人游戏中对比 Claude、Grok、DeepSeek 等语言模型的表现和成本，发现 DeepSeek V4 Flash 在成本效率上遥遥领先。 该实验为开发者选择适用于实时控制应用（如机器人）的语言模型提供了量化依据，揭示了高端模型（如 Opus）成本是低端模型的数十倍，直接影响产品落地的经济可行性。 测试未包含 Opus 4.7、GPT-5.5 等前沿模型，因其 30 局游戏成本约 3000 美元，而总实验仅花费 482 美元。社区还指出 Grok 4.1 Fast 被 xAI 静默升级为 Grok 4.3 并提价，引发了信任担忧。

hackernews · Usu · Jun 17, 21:00 · [社区讨论](https://news.ycombinator.com/item?id=48576824)

**背景**: 大型语言模型（LLM）如 Claude（Anthropic 开发）、Grok（xAI 开发）和 DeepSeek（中国公司开发）通过 API 提供文本生成能力。DeepSeek 采用混合专家（MoE）架构，以低推理成本著称；Grok 则与 X 社交平台及特斯拉 Optimus 机器人深度集成。这类模型正被探索用于机器人实时决策等场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2405.04434">DeepSeek -V2: A Strong, Economical, and Efficient</a></li>

</ul>
</details>

**社区讨论**: 有评论戏称若送墨西哥卷饼的机器人用 Grok 可能更容易绕过出口管制；另有人对高端模型的高昂成本表示震惊，认为难以规模盈利。此外，多名用户批评 xAI 将 Grok 4.1 Fast 偷偷替换为 Grok 4.3 并涨价，认为这是不良商业行为。

**标签**: `#LLM`, `#AI`, `#cost-efficiency`, `#model comparison`, `#robotics`

---

<a id="item-12"></a>
## [8 位像素风格实时棒球直播网站](https://ribbie.tv/watch) ⭐️ 7.0/10

用户创建了 ribbie.tv 网站，利用 MLB 实时数据流生成 8 位像素艺术风格的棒球比赛直播，并提供了当日多场比赛的观看链接。 该项目将实时体育数据转化为复古像素艺术，为棒球迷提供了一种新颖且怀旧的观赛方式，展示了数据可视化的创意应用，并引发了社区关于艺术风格和技术实现的积极讨论。 网站已实现真实球场、日夜模式、局间图形和实时计分板等细节，但目前部分图像使用 AI 生成；社区建议采用确定性下采样算法和真正的像素字体以提升视觉效果。

hackernews · brownrout · Jun 17, 16:44 · [社区讨论](https://news.ycombinator.com/item?id=48573012)

**背景**: MLB Statcast 系统自 2015 年起在所有球场部署，能够实时追踪球员位置、球速等数据，为这类可视化项目提供了基础数据源。8 位像素艺术是一种复古数字艺术风格，常唤起对早期电子游戏的怀旧情感。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Statcast">Statcast - Wikipedia</a></li>
<li><a href="https://baseballsavant.mlb.com/league?season=2025">Major League Baseball Statcast , Visuals & Advanced Metrics</a></li>

</ul>
</details>

**社区讨论**: 社区整体对项目表示赞赏，但不少用户批评 AI 生成的艺术不够精致，建议使用真实像素字体和确定性算法；也有用户提出了增加音效、回放功能和基跑者离垒细节等改进意见，还有人分享了类似的物理计分板项目。

**标签**: `#baseball`, `#pixel art`, `#data visualization`, `#sports`, `#web app`

---

<a id="item-13"></a>
## [大众封锁 GrapheneOS 用户，引隐私争议](https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3) ⭐️ 7.0/10

大众汽车封锁了 GrapheneOS 用户对其官方应用和 API 的访问，仅允许通过 Google Play 保护认证的设备使用。 该行为限制了用户选择隐私保护操作系统的自由，并扼杀了社区项目（如 Home Assistant 集成），反映了企业对用户数字权利的侵蚀。 大众 API 被完全锁定，不再支持非 Play 保护认证设备；官方应用被指包含 60% 广告，体验远不如社区集成。

hackernews · microtonal · Jun 17, 15:04 · [社区讨论](https://news.ycombinator.com/item?id=48571526)

**背景**: GrapheneOS 是一款基于 Android 开源项目（AOSP）的开源操作系统，专注于安全和隐私增强。Play 保护认证是 Google 的设备安全验证机制，通常用于确保兼容性和安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍对大众的做法表示失望和愤怒，有用户因此推迟购车，并批评欧盟法规导致汽车过度联网，呼吁行业和政治层面的反思。

**标签**: `#Privacy`, `#GrapheneOS`, `#Volkswagen`, `#Android`, `#API Access`

---

<a id="item-14"></a>
## [与人对话思考胜过独自思考](https://www.thesignalist.io/s/the-dialogue-dividend/) ⭐️ 7.0/10

《The Signalist》上发表了一篇文章，指出向他人大声说出自己的想法比独自思考更有助于理清思路和解决问题。 这一发现强调了协作沟通在认知过程中的关键作用，尤其对需要清晰逻辑的领域（如编程）具有重要启示，可能推动更多团队采用结对编程和橡皮鸭调试等实践。 文章以橡皮鸭调试和结对编程为例，说明将模糊想法转化为结构化语言是提升思维清晰度的核心机制。

hackernews · kodesko · Jun 17, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48569894)

**背景**: 橡皮鸭调试是一种软件调试方法，程序员通过向一只橡皮鸭逐行解释代码来发现错误；结对编程则是两名程序员在同一工作站协作，一人写代码另一人审查。这两种方法都利用了向他人（或模拟他人）表述来强化思考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rubber_duck_debugging">Rubber duck debugging - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pair_programming">Pair programming</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍认同文章核心观点，但强调关键不在于“有听众”，而在于“被迫将模糊想法转化为有结构的句子”，这与写作改善思考的原理类似。有评论提到早期尝试用 LLM 辅助橡皮鸭调试，还有引用爱因斯坦与同事讨论相对论的例子作为佐证。

**标签**: `#cognitive science`, `#productivity`, `#pair programming`, `#rubber duck debugging`, `#communication`

---

<a id="item-15"></a>
## [Bubbles：独立博客版的 Hacker News](https://bubbles.town/) ⭐️ 7.0/10

Bubbles 是一个社区驱动的独立博客聚合器，类似于 Hacker News，但专门聚焦于个人博客。该平台允许用户投票、排序和发现独立博客文章，近期获得了社区高度关注和积极反馈。 Bubbles 的出现反映了独立博客生态的复兴趋势，为远离社交媒体和算法推荐的用户提供了一个更人性化、多样化的内容发现渠道。它可能成为 Hacker News 的有益补充，推动独立博客社区的发展。 Bubbles 支持通过 Mastodon 账号登录（暂无传统邮箱注册），并集成了联邦宇宙（Fediverse）。其排序方式包括 top / new / hot / my，但部分用户建议优化 UI 文案（如将“my”改为“mine”）。

hackernews · headalgorithm · Jun 17, 07:49 · [社区讨论](https://news.ycombinator.com/item?id=48567155)

**背景**: Hacker News 是 Y Combinator 旗下的科技新闻聚合社区，以技术讨论和创业内容为主。近年来，随着社交媒体噪音增加，许多用户开始回归独立博客，寻求更深度、更个性化的阅读体验。Bubbles 正是顺应这一趋势，专注于独立博客的聚合与排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Filter_bubble">Filter bubble - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区总体反响积极，称赞其简洁设计和理念。有用户建议链接应在当前窗口打开而非新标签页，并希望支持邮箱注册以避免依赖社交媒体。此外，作者开源了 RSS 监控引擎，引发了技术栈交流。

**标签**: `#indie blogs`, `#aggregation`, `#community`, `#hacker news alternative`

---

<a id="item-16"></a>
## [Photobucket 索要 5 美元才让用户取回照片](https://www.lutr.dev/want-your-images-back-sure-that-ll-be-5-dollars) ⭐️ 7.0/10

Photobucket 在其账户删除流程中，向用户收取 5 美元订阅费才能下载自己已上传的照片，否则照片将永久丢失。 此事引发了对云存储服务数据可移植性及公司商业道德的广泛讨论，用户可能因无力支付而失去珍贵个人数据，凸显用户权利与平台权力之间的不平衡。 实际上，部分用户发现账户关闭流程中存在隐藏的免费下载选项，但主要界面仍将付费订阅作为首选，造成用户体验混乱。

hackernews · lutr · Jun 17, 13:05 · [社区讨论](https://news.ycombinator.com/item?id=48569954)

**背景**: Photobucket 是一个早期的照片托管平台，曾广泛用于论坛和博客图片外链。该服务多次易主，商业模式失败，近年来通过限制免费账户的功能来试图盈利。数据可移植性是指用户能够将自己的数据从一个服务完整地迁移到另一个服务的能力。

**社区讨论**: 评论中有人指出实际有免费下载路径，但界面设计误导用户；也有人认为这是公司没落后的自救手段，而非纯粹的贪婪。部分用户对比了 Google Photos 等免费导出服务，认为 Photobucket 的做法更加恶劣。

**标签**: `#cloud storage`, `#data portability`, `#user rights`, `#anti-patterns`

---

<a id="item-17"></a>
## [MicroUI：基于 ANSI C 的微型即时模式 UI 库](https://github.com/rxi/microui) ⭐️ 7.0/10

MicroUI 是一个用 ANSI C 编写的微型即时模式图形用户界面库，因其极简设计和可移植性而受到关注。 该库为嵌入式系统和游戏开发提供了一种轻量级 UI 方案，特别适用于资源受限的环境。其即时模式设计简化了 UI 逻辑，降低了学习成本。 MicroUI 仅包含约 1000 行代码，依赖于用户提供的后端渲染函数（如绘制矩形、文本等），因此极易移植到不同平台。社区报告了一个未修复的对齐指针访问错误，可能导致在某些环境（如 Zig）中触发异常。

hackernews · peter_d_sherman · Jun 17, 12:04 · [社区讨论](https://news.ycombinator.com/item?id=48569205)

**背景**: 即时模式 GUI（IMGUI）是一种编程模式，其中用户界面每帧完全重建，控件不持久存储状态。与传统保留模式 GUI 相比，IMGUI 通常更简单、更易调试，适合工具和游戏内界面。ANSI C 保证了代码跨平台兼容性，适合嵌入式系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Immediate_mode_(computer_graphics)">Immediate mode (computer graphics) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区普遍称赞 MicroUI 的简洁性和易用性，认为它是个人小项目的不错选择。但也有用户指出其已基本停止维护，存在指针对齐错误等问题，并且现有 fork 未能彻底解决。

**标签**: `#C`, `#GUI`, `#immediate-mode`, `#library`, `#embedded`

---

<a id="item-18"></a>
## [仅凭 ID 即可 Rickroll 整个 FIFA 世界杯](https://bobdahacker.com/blog/fifa-hack) ⭐️ 7.0/10

一位自称 Bob Da Hacker 的安全研究员声称，他仅利用自己的用户 ID 就能利用一个漏洞，在 FIFA 世界杯赛事中实施大规模 Rickroll 恶作剧。 如果属实，这意味着 FIFA 世界杯的在线系统存在严重的安全漏洞，可能允许攻击者控制比赛现场的大屏幕或广播内容，影响全球数亿观众的观赛体验。 该漏洞类型被推测为不安全的直接对象引用（IDOR），攻击者通过修改 URL 中的 ID 参数绕过权限检查，从而获得对系统高级功能的未授权访问。

rss · Lobsters · Jun 17, 08:31

**背景**: 不安全的直接对象引用（IDOR）是一种常见的 Web 安全漏洞，当应用程序使用用户提供的标识符直接访问内部对象，而未进行适当的权限验证时，攻击者可以篡改标识符获取或修改其他用户的数据。例如，在 URL 中更改用户 ID 就可能访问他人的账户信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Insecure_direct_object_reference">Insecure direct object reference - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/IDOR">Insecure Direct Object Reference ( IDOR ) - Security | MDN</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#FIFA`, `#hacking`, `#rickroll`

---

<a id="item-19"></a>
## [Pull Requests 如同免费小狗](https://www.youtube.com/watch?v=x8_ZZhRL3YU&t=1733s) ⭐️ 7.0/10

SQLite 创始人 Richard Hipp 在演讲中将 pull request 比喻为“免费小狗”，指出接受 pull request 意味着需要长期维护、文档和测试，并非真正免费。 这一观点揭示了开源项目中常见的隐性维护成本，引起开发者对贡献质量和长期责任的反思，对开源社区的管理实践具有重要启发。 Hipp 强调维护者需要为每个 pull request 负责长达数十年，无法轻易丢弃，就像不能遗弃小狗一样。他明确表示不希望接收“免费小狗”，即未经充分考量的贡献。

rss · Lobsters · Jun 17, 13:23

**背景**: Pull request 是开发者向开源项目提交代码修改的常用方式，项目维护者需要审查、测试、合并并长期维护这些代码。开源项目常依赖社区贡献，但维护负担常被低估，Hipp 的比喻正是为此敲响警钟。

**社区讨论**: 社区讨论中，许多开发者对 Hipp 的观点表示强烈认同，认为 pull request 的长期维护成本确实常被忽略，尤其是那些缺乏文档或测试的贡献。也有部分人指出该比喻可能过于极端，但整体上引发了关于贡献者责任与维护者负担的深入反思。

**标签**: `#open source`, `#software maintenance`, `#pull requests`, `#SQLite`

---

<a id="item-20"></a>
## [Oklch 颜色空间实用指南：面向普通开发者](https://hugodaniel.com/posts/color-picking-oklch/) ⭐️ 7.0/10

博主 Hugo Daniel 发布了一篇名为《Color picking Oklch for mortals》的实用指南，详细介绍了如何在 CSS 中使用 Oklch 颜色空间进行感知均匀的颜色选择。 Oklch 已被纳入 CSS Color Level 4 草案并获现代浏览器支持，这篇指南降低了 Web 开发者和设计师使用该先进颜色空间的门槛，有助于创建更具一致性的颜色方案和渐变。 Oklch 是 Oklab 的圆柱形表示，使用明度（L）、色度（C）和色调（h）三个维度，其感知均匀性优于传统的 HSL 和 RGB 颜色空间。部分 Oklch 颜色可能超出 sRGB 色域，需要 fallback 处理。

rss · Lobsters · Jun 17, 10:45

**背景**: 传统颜色空间（如 HSL）在感知上不均匀，导致相同数值间隔的颜色差异在人眼中不一致。Oklab/Oklch 由 Björn Ottosson 于 2020 年提出，基于 CAM16 和 IPT 数据优化，改善了蓝色区域的色相和明度预测，提供更准确的色彩再现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oklab_color_space">Oklab color space</a></li>
<li><a href="https://oklch.org/">OKLCH Color Picker - Modern CSS Color Space Tool</a></li>
<li><a href="https://oklch.com/">OKLCH is a new way to encode colors (like hex, RGBA, or HSL)</a></li>

</ul>
</details>

**标签**: `#color science`, `#web development`, `#CSS`, `#design`

---

<a id="item-21"></a>
## [Google Manifest V3 对广告拦截器的影响](https://arxiv.org/abs/2503.01000) ⭐️ 7.0/10

一篇学术论文详细分析了 Google Chrome 的 Manifest V3 更新如何削弱广告拦截器的有效性。 这一变化影响了数亿用户的浏览体验和隐私保护，因为广告拦截器是用户屏蔽烦人广告和追踪器的主要工具。 论文指出，Manifest V3 强制使用 declarativeNetRequest API，限制了广告拦截器允许的规则数量，并移除了对 webRequest API 的阻塞支持。

rss · Lobsters · Jun 17, 07:30

**背景**: Manifest V3 是 Chrome 扩展平台的新规范，旨在提高安全性、性能和隐私。它用服务工作者替代持久后台页面，并引入 declarativeNetRequest API 来控制网络请求，这限制了广告拦截器的传统工作方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V3 | Chrome for Developers</a></li>

</ul>
</details>

**标签**: `#Manifest V3`, `#ad blockers`, `#browser extensions`, `#Google Chrome`, `#privacy`

---

<a id="item-22"></a>
## [用 Rust 智能框架提升预算 AI 模型性能](https://yogthos.net/posts/2026-06-08-dirge-code.html) ⭐️ 7.0/10

本文介绍了一种使用 Rust 构建的智能框架（harness），可以显著提升预算 AI 模型的运行效率，让低成本模型在性能上超越其规格。 该技术为资源受限场景（如边缘设备或低预算部署）提供了优化方案，可能推动 AI 应用的普及和效率提升，尤其对中小企业或个人开发者意义重大。 该 Rust harness 通过精细的资源管理和并行调度，优化了模型推理路径，减少了不必要的开销。文中还讨论了 Rust 的类型系统和所有权模型如何帮助构建安全高效的 AI 代理框架。

rss · Lobsters · Jun 17, 14:10

**背景**: 预算 AI 模型指那些参数较少、成本较低的模型，适合在有限硬件上运行。Rust 是一门系统编程语言，以内存安全和零成本抽象著称，其编译器特性和所有权模型特别适合构建高性能、可靠的底层工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/majiayu000/harness">GitHub - majiayu000/harness: Rust AI agent orchestration platform with App Server, rules, skills, GC, and observability. · GitHub</a></li>
<li><a href="https://medium.com/@ashbenen/the-compiler-is-the-harness-why-agentic-coding-works-so-well-in-rust-730bca7faf8e">The Compiler Is the Harness: Why Agentic Coding Works So Well in Rust | by Adam Benenson | Medium</a></li>
<li><a href="https://www.subthesis.com/blog/cheap-and-effective-ai-models">Cheap and Effective AI Models: A Complete Guide for 2026 | Subthesis | Subthesis</a></li>

</ul>
</details>

**标签**: `#Rust`, `#AI/ML`, `#performance engineering`, `#model optimization`

---

<a id="item-23"></a>
## [简化 GHC 升级的实用策略](https://blog.haskell.org/making-ghc-upgrades-easy/) ⭐️ 7.0/10

Haskell 官方博客发布了一篇文章，详细介绍了如何通过改进工具和流程来简化 GHC 编译器的升级过程。文章提出了具体方法，旨在降低升级时的冲突和兼容性风险。 GHC 升级是 Haskell 社区的一个常见痛点，简化升级可以显著提升开发者体验和项目维护效率。这篇文章有望推动更流畅的编译器版本迁移，减少社区中因升级停滞导致的生态碎片化。 文章可能涵盖诸如使用 Cabal 文件约束、利用 GHC 的扩展机制或采用多版本测试等策略。具体技术细节需阅读原文，但核心目标是让升级更加可预测和自动化。

rss · Lobsters · Jun 17, 06:47

**背景**: GHC（Glasgow Haskell Compiler）是 Haskell 语言的主要编译器，以强大的优化能力和对 Haskell 2010 标准的支持著称。升级 GHC 时常面临依赖项兼容性问题，以及语言扩展和编译器行为的改变，这迫使项目维护者投入大量精力进行适配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Glasgow_Haskell_Compiler">Glasgow Haskell Compiler - Wikipedia</a></li>
<li><a href="https://www.haskell.org/ghc/">Glasgow Haskell Compiler — The Glasgow Haskell Compiler</a></li>

</ul>
</details>

**标签**: `#Haskell`, `#GHC`, `#compiler`, `#tooling`, `#developer experience`

---

<a id="item-24"></a>
## [《指挥官基恩》游戏引擎架构白皮书分析](https://forgottenbytes.net/commander_keen.html) ⭐️ 7.0/10

一篇名为《Game Engine White Papers: Commander Keen》的技术白皮书发布，详细分析了《指挥官基恩》游戏引擎的架构与自适应块刷新算法。 该白皮书揭示了早期 PC 平台实现流畅卷轴游戏的关键技术突破，对理解游戏引擎发展史以及现代 2D 游戏性能优化具有重要参考价值。 该引擎采用自适应块刷新（adaptive tile refresh）技术，仅重绘屏幕中发生变化的图块，从而在低性能 PC 硬件上实现了平滑的侧向滚动效果；该技术由 John Carmack 于 1990 年首创。

rss · Lobsters · Jun 17, 05:29

**背景**: 《指挥官基恩》是 id Software 前身开发的经典平台游戏系列，其引擎的核心创新在于克服了早期 PC 图形性能的限制。自适应块刷新通过标记图块变更区域来减少重复绘制，这一思路后来也影响了《德军总部 3D》等后续引擎的设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Commander_Keen">Commander Keen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adaptive_tile_refresh">Adaptive tile refresh - Wikipedia</a></li>

</ul>
</details>

**标签**: `#game engines`, `#retro gaming`, `#software architecture`

---

<a id="item-25"></a>
## [R 核心团队荣获 2026 年 Rousseeuw 统计学奖](https://rousseeuwprize.org/2026) ⭐️ 7.0/10

R 核心团队被授予 2026 年 Rousseeuw 统计学奖，该奖项旨在表彰对统计学研究有重大社会影响的创新成果，奖金为 100 万美元。 这是对 R 语言及其核心开发者长期贡献的最高认可之一，凸显了 R 在统计计算和数据科学领域的核心地位，将激励更多开源统计工具的持续发展。 五位 R 核心团队成员代表团队领奖，奖项由 Rousseeuw 基金会设立、比利时国王博杜安基金会管理，每两年颁发一次。R 语言自 1993 年诞生以来已成为全球研究机构、医疗系统和金融行业的标准工具。

rss · Lobsters · Jun 17, 12:20

**背景**: R 是一种用于统计计算和数据可视化的自由开源编程语言，广泛应用于数据挖掘、生物信息学和数据分析。Rousseeuw 统计学奖由统计学家 Peter Rousseeuw 创立，旨在奖励对统计实践产生深远影响的创新，奖金规模与诺贝尔奖相当。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/R_core_team">R core team</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rousseeuw_Prize_for_Statistics">Rousseeuw Prize for Statistics</a></li>
<li><a href="https://www.prweb.com/releases/2026-rousseeuw-prize-for-statistics-awarded-to-r-core-team-for-transforming-statistics-computing-worldwide-302802398.html">2026 Rousseeuw Prize for Statistics Awarded to R Core Team ...</a></li>

</ul>
</details>

**标签**: `#R`, `#Statistics`, `#Award`

---

<a id="item-26"></a>
## [FMAG：单指令 GPU 虚拟机及工具链](https://github.com/jangafx/FMAG) ⭐️ 7.0/10

FMAG 是一个创新的 GPU 虚拟机，它只包含一条指令，从而彻底避免了 GPU 编程中常见的分支发散问题。该项目还提供了配套的工具链，支持开发者使用这一新型架构进行编程。 这一概念挑战了传统 GPU 的 SIMT（单指令多线程）执行模型，可能为某些特定类型的并行计算提供更简单、更高效的解决方案。虽然目前仍是实验性质，但它展示了 GPU 架构设计的新思路，对系统和 GPU 社区具有启发性。 FMAG 虚拟机仅有一条指令，这意味着所有线程在任何时刻都执行完全相同的操作，不存在分支分歧，从而简化了硬件设计和编程模型。项目托管在 GitHub 上，包含完整的实现和文档，但尚未提及性能基准或实际应用场景。

rss · Lobsters · Jun 17, 16:10

**背景**: 传统 GPU 采用 SIMT（单指令多线程）架构，可以同时运行大量线程，但线程遇到条件分支时会产生发散（divergence），导致部分线程闲置，降低效率。为了解决发散问题，编程时需要精心设计分支，或使用掩码操作。FMAG 通过将指令集缩减到一条，使得所有线程永远执行相同操作，从根本上消除了发散，但同时也限制了灵活性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jangafx/FMAG">GitHub - jangafx/FMAG: A single-instruction GPU virtual ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Graphics_processing_unit">Graphics processing unit - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GPU`, `#virtual-machine`, `#toolchain`, `#systems`, `#architecture`

---

<a id="item-27"></a>
## [Docker Desktop 网络底层原理](https://www.docker.com/blog/how-docker-desktop-networking-works-under-the-hood/) ⭐️ 7.0/10

Docker 官方博客发布了一篇深度技术文章，详细解释了 Docker Desktop 在 macOS 和 Windows 上实现容器网络功能的内部机制，包括 VPNkit 组件和网络转换层的工作原理。 这篇文章对于在非 Linux 平台上使用 Docker 的开发者非常关键，因为跨平台网络问题常见且难以排查，理解底层机制有助于更高效地配置网络和调试故障。 文章重点介绍了 VPNkit 如何提供 TCP/IP 堆栈、DNS 服务器（基于 Mirage OCaml）以及 HTTP 代理（基于 Cohttp），并通过虚拟 IP 和 DNS 名称来路由容器流量。

rss · Lobsters · Jun 17, 05:42

**背景**: Docker Desktop 在 macOS 和 Windows 上通过一个轻量级虚拟机运行 Linux 容器，因此其网络需要额外的翻译层才能与宿主机通信。VPNkit 是其中核心的组件，负责处理网络地址转换和协议转发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.docker.com/desktop/features/networking/">Networking on Docker Desktop</a></li>
<li><a href="https://www.docker.com/blog/how-docker-desktop-networking-works-under-the-hood/">How Docker Desktop Networking Works Under the Hood | Docker</a></li>

</ul>
</details>

**标签**: `#Docker`, `#networking`, `#containerization`, `#technical deep-dive`

---