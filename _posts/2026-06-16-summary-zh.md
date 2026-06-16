---
layout: default
title: "Horizon Summary: 2026-06-16 (ZH)"
date: 2026-06-16
lang: zh
---

> From 36 items, 19 important content pieces were selected

---

1. [LinkedIn 招聘任务藏 npm 后门](#item-1) ⭐️ 9.0/10
2. [Iroh 1.0：应用层点对点网络库正式发布](#item-2) ⭐️ 8.0/10
3. [本地模型替代 Claude/GPT 编程的实践分享](#item-3) ⭐️ 8.0/10
4. [Hetzner 大幅上调云服务器价格](#item-4) ⭐️ 8.0/10
5. [福克斯拟收购 Roku，引发媒体整合担忧](#item-5) ⭐️ 8.0/10
6. [《指挥官基恩》引擎白皮书揭示早期 PC 游戏技术突破](#item-6) ⭐️ 8.0/10
7. [Salesforce 斥资 36 亿美元收购 AI 客服公司 Fin](#item-7) ⭐️ 8.0/10
8. [Rust 与 C/C++内存安全 CVE 差异分析](#item-8) ⭐️ 8.0/10
9. [Diplomat：为 Rust 库生成多语言 FFI 绑定](#item-9) ⭐️ 8.0/10
10. [用 C++26 静态反射在编译时解析 JSON](#item-10) ⭐️ 8.0/10
11. [Clojure 优化后性能接近 C](#item-11) ⭐️ 8.0/10
12. [家庭实验室 AI 开发平台分享引发社区共鸣](#item-12) ⭐️ 7.0/10
13. [美国电池制造业产出再创新高，但与中国差距悬殊](#item-13) ⭐️ 7.0/10
14. [TimescaleDB 时间序列数据压缩解析](#item-14) ⭐️ 7.0/10
15. [排版系统 Typst 0.15 发布](#item-15) ⭐️ 7.0/10
16. [通过 HTTPS DNS 记录节省 TLS 连接往返](#item-16) ⭐️ 7.0/10
17. [用户抗议 AMD 移除消费级 CPU 内存加密](#item-17) ⭐️ 7.0/10
18. [裸机启动 Linux：最小化启动技术](#item-18) ⭐️ 7.0/10
19. [PostgreSQL 唯一可扩展删除操作是 DROP TABLE](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LinkedIn 招聘任务藏 npm 后门](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

一名开发者收到 LinkedIn 上某加密初创公司招聘人员的面试任务，要求审查一个 GitHub 仓库中的 npm 依赖问题。该仓库的依赖项中隐藏着后门，通过 npm 的 prepare 脚本在安装依赖时自动执行恶意代码，实现远程命令执行。 这标志着一种新型的供应链攻击向量，利用招聘流程传播恶意软件，对开发者安全构成严重威胁。同时暴露了平台（GitHub、LinkedIn）对举报的响应不足，可能助长类似攻击。 后门代码隐藏在注释墙中，npm 的 prepare 脚本在 npm install 后自动运行，因此仅执行依赖安装即可触发后门。该后门会执行从攻击者服务器接收到的任意命令。

hackernews · lwhsiao · Jun 15, 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48546294)

**背景**: 软件供应链攻击是指攻击者通过渗透软件开发生命周期中的某个环节来植入恶意代码。npm 是 JavaScript 的包管理器，广泛用于前端和后端项目。攻击者常利用“依赖混淆”（dependency confusion）技术，创建与内部包同名的公共包，或在合法包中植入恶意代码。本文展示的正是通过面试任务诱导开发者安装恶意依赖的攻击手法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
<li><a href="https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/">What is a supply chain attack?</a></li>
<li><a href="https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610">Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies | by Alex Birsan | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍认为该攻击手法非常危险，因为它与常见的面试任务几乎无异，开发者容易放松警惕。有评论质疑这是否构成犯罪，并呼吁建立网络犯罪报告机制。还有用户指出，该攻击者可能使用了同一个域名针对多个目标，相关讨论已在 Reddit 上出现。

**标签**: `#supply chain security`, `#npm`, `#backdoor`, `#LinkedIn`, `#recruitment scam`

---

<a id="item-2"></a>
## [Iroh 1.0：应用层点对点网络库正式发布](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 正式发布，这是一个基于 Rust 的模块化网络栈，提供点对点连接库，支持自定义传输协议，并采用“应用层的 Tailscale”心智模型。 Iroh 允许开发者构建去中心化应用，无需依赖传统网络层（如 VPN）即可实现设备间直接通信，降低了点对点应用的门槛，对隐私保护和分布式网络有重要影响。 Iroh 默认支持 IPv4、IPv6 和中继传输，但新增了自定义传输接口，允许开发者实现如 WebRTC、BLE 等任意传输协议。其使用加密密钥对（dial keys）作为端点标识，替代传统 IP 地址。

hackernews · Lobsters · Jun 15, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48542480)

**背景**: 点对点（P2P）网络允许设备直接通信而不依赖中央服务器，但常受限于 NAT 和防火墙。Tailscale 是一种基于 WireGuard 的 VPN 工具，在网络层实现设备互联。Iroh 则在应用层（通过 QUIC 协议）实现类似功能，开发者可直接嵌入应用，用户无需额外账号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/n0-computer/iroh">GitHub - n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. · GitHub</a></li>
<li><a href="https://blog.lambdaclass.com/the-wisdom-of-iroh/">The Wisdom of Iroh - LambdaClass Blog</a></li>

</ul>
</details>

**社区讨论**: 社区中，开发者 apitman 将 Iroh 比作“应用层的 Tailscale”，强调其易用性；Iroh 核心开发者 rklaehn 解释了自定义传输的设计动机，以应对多样化的传输需求。也有用户如 Thaxll 质疑其必要性，认为现有 IP/DNS 已足够，而 coldblues 看好去中心化网络前景。

**标签**: `#p2p`, `#networking`, `#iroh`, `#decentralized`

---

<a id="item-3"></a>
## [本地模型替代 Claude/GPT 编程的实践分享](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.0/10

Hacker News 上多位用户报告成功使用本地大语言模型（如 Qwen 和 Gemma）替代 Claude 或 GPT 作为日常编码工具，并分享了详细的硬件配置和性能数据。 这表明本地模型在编码任务上的能力已接近云端前沿模型，为注重隐私、成本的开发者提供了可行替代方案，可能改变 AI 编程助手的格局。 常用设置包括在配备双 RTX 3090 显卡、128GB 内存的硬件上运行 Qwen3.6-35B 或 Gemma-4-26B 模型，推理速度可达约 150 token/秒，但质量约为 8-12 个月前的边缘模型水平。

hackernews · cloudking · Jun 15, 14:46

**背景**: Claude 和 GPT 是云端 AI 编程助手，依赖远程服务器，用户需付费并担心数据隐私。本地模型如 Qwen（阿里通义千问系列）和 Gemma（Google 开源模型）可在本地硬件上运行，完全离线，保护隐私且免费，但需要高性能显卡和大内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Qwen_language_model">Qwen (language model)</a></li>
<li><a href="https://grokipedia.com/page/gemma_language_model">Gemma (language model)</a></li>

</ul>
</details>

**社区讨论**: 社区整体持积极态度，多位用户证实了本地模型的可行性，但指出其智能程度略逊于 Claude 或 Codex，偶尔仍需回退到云端模型。也有观点认为，追求最新模型的机会成本较高。

**标签**: `#local LLM`, `#coding assistant`, `#Qwen`, `#Gemma`, `#AI tooling`

---

<a id="item-4"></a>
## [Hetzner 大幅上调云服务器价格](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 8.0/10

德国云服务商 Hetzner 宣布对其云服务器产品进行大规模价格调整，部分实例价格涨幅高达 3 倍。 这标志着 AI 热潮导致的硬件成本飙升已蔓延至中小型云服务商，可能推动更多用户转向大型超大规模云厂商或自建基础设施。 新价格对比旧价格涨幅显著，例如 CX22 实例月费从约 3.49 欧元涨至 9.99 欧元；Hetzner 称调整是由于硬件采购成本（如 RAM 和 SSD）急剧上升。

hackernews · tuhtah · Jun 15, 13:19 · [社区讨论](https://news.ycombinator.com/item?id=48540844)

**背景**: Hetzner 是欧洲知名的平价云服务提供商，以低价 VPS 和专用服务器吸引大量开发者。近两年由于 AI 训练需求爆发，全球内存和存储芯片供不应求，导致服务器硬件成本大幅上涨。

**社区讨论**: 社区普遍对 3 倍涨幅感到震惊，认为这削弱了 Hetzner“低价”定位；部分用户指出这是硬件稀缺的必然结果，也有人质疑 Hetzner 此前定价是否过低。

**标签**: `#Hetzner`, `#cloud pricing`, `#AI boom`, `#hardware costs`

---

<a id="item-5"></a>
## [福克斯拟收购 Roku，引发媒体整合担忧](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

据报道，福克斯公司正在与流媒体硬件制造商 Roku 进行收购谈判，可能达成一项重大交易。 这一收购若完成，将使福克斯直接控制大量美国客厅的流媒体硬件入口，可能加剧媒体垂直整合和反垄断问题，并影响数百万用户的观看体验。 Roku 在美国家庭中的渗透率估计在 30%至 50%之间，其平台已从纯硬件销售转向内置广告和内容合作，此次收购可能进一步改变其服务中立性。

hackernews · thm · Jun 15, 12:50 · [社区讨论](https://news.ycombinator.com/item?id=48540499)

**背景**: Roku 是美国最大的流媒体播放器品牌之一，提供硬件和操作系统，允许用户访问各类流媒体应用。福克斯是一家大型媒体内容公司，拥有新闻、体育和娱乐资产。若收购成功，福克斯可能优先推广自家内容，或改变 Roku 的开放生态。

**社区讨论**: 社区用户普遍持悲观态度，认为媒体公司不应被允许直接拥有电视硬件入口，担心 Roku 的服务中立性受损并出现内容偏袒。一些用户已开始转向 Nvidia Shield 等替代设备。

**标签**: `#acquisition`, `#streaming`, `#roku`, `#fox`, `#media`

---

<a id="item-6"></a>
## [《指挥官基恩》引擎白皮书揭示早期 PC 游戏技术突破](https://forgottenbytes.net/commander_keen.html) ⭐️ 8.0/10

发布了关于《指挥官基恩》游戏引擎技术创新的白皮书，详细记录了 John Carmack 发明的自适应瓦片刷新（adaptive tile refresh）等关键突破。 该白皮书展示了 1990 年代初 PC 游戏如何通过巧妙的编程技巧克服硬件限制实现主机级别的平滑滚动，对理解游戏引擎发展史和早期 PC 游戏编程智慧具有重要价值。 自适应瓦片刷新技术仅重绘屏幕新暴露的部分，而非整个画面，从而在 MS-DOS 系统上实现了类似 NES 游戏的流畅横向卷轴效果。这项技术由 John Carmack 创造，并在《指挥官基恩》系列中首次应用。

hackernews · mfiguiere · Jun 15, 17:52 · [社区讨论](https://news.ycombinator.com/item?id=48544781)

**背景**: 1990 年代初的 PC 缺乏硬件精灵和专用图形加速器，其 CPU 性能虽不弱，但逐帧重绘整个屏幕会导致严重卡顿。相比之下，任天堂 SNES 等家用游戏机拥有专用硬件来高效渲染精灵和滚动背景。自适应瓦片刷新通过只更新变化区域，使 PC 能实现类似的平滑滚动效果，为后续如《毁灭战士》等动作游戏奠定了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Adaptive_tile_refresh">Adaptive tile refresh - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Commander_Keen">Commander Keen - Wikipedia</a></li>
<li><a href="https://www.howtogeek.com/704727/30-years-of-vorticons-how-commander-keen-changed-pc-gaming/">30 Years of Vorticons: How Commander Keen Changed PC Gaming</a></li>

</ul>
</details>

**社区讨论**: 社区用户对白皮书表示赞赏，并推荐《Masters of Doom》一书以了解 id Software 历史。有用户指出，需结合当时硬件差异来理解 PC 为何需要特殊技巧，而用户 LarsDu88 则提到该白皮书风格类似 Fabien Sanglard 的作品。部分用户希望看到更多关于 Apogee 和 Epic 早期游戏引擎的分析。

**标签**: `#retro gaming`, `#game engine`, `#Commander Keen`, `#id Software`, `#technical history`

---

<a id="item-7"></a>
## [Salesforce 斥资 36 亿美元收购 AI 客服公司 Fin](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL) ⭐️ 8.0/10

Salesforce 于 2026 年 6 月 15 日签署最终协议，以约 36 亿美元收购 AI 客户支持平台 Fin（前身为 Intercom）。 此次收购凸显 AI 客服领域的激烈竞争，Salesforce 旨在对抗由前联席 CEO Bret Taylor 创立的 Sierra（估值 158 亿美元），并防止独立 AI 客服代理成为 CRM 之外的第三方控制点。 Fin 拥有超过 3 万家企业客户，包括 Anthropic、Clay 等；收购发生在 Fin 从 Intercom 更名仅一个月后，反映了市场的快速演变。

hackernews · colesantiago · Jun 15, 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48540126)

**背景**: 传统客服平台如 Intercom 提供即时通讯和自动化支持，而新一代 AI 客服代理利用大语言模型自主解决问题。Salesforce 是全球领先的 CRM 软件提供商，正通过收购加速 AI 战略布局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fin.ai/">Fin AI</a></li>
<li><a href="https://www.reddit.com/r/CustomerSuccess/comments/1qwjjes/feeling_hopeless_with_fin_ai_of_intercom/">Feeling hopeless with Fin AI of Intercom : r/CustomerSuccess</a></li>
<li><a href="https://www.linkedin.com/company/fin">Fin - LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 评论对 AI 客服体验褒贬不一：有用户认为执行得当的 AI（如 Starlink 客服）优于 95%的人工客服；但另一部分用户批评 AI 常编造理由拒绝帮助。部分评论指出 Intercom 等传统平台的价值可能因企业自训 AI 代理而下降。

**标签**: `#acquisition`, `#AI`, `#customer support`, `#Salesforce`, `#SaaS`

---

<a id="item-8"></a>
## [Rust 与 C/C++内存安全 CVE 差异分析](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html) ⭐️ 8.0/10

一篇技术博客分析了 Rust 和 C/C++中内存安全相关 CVE（常见漏洞与暴露）的本质差异，并质疑直接比较原始 CVE 数量的有效性。 该分析有助于纠正社区中过度依赖 CVE 计数来评判语言安全性的倾向，促使开发者更关注漏洞类型和根本原因，而非简单数字。 博客指出，C/C++中任何空指针解引用都可能被记为 CVE，而 Rust 的 Option<T>类型可明确处理 None 值，因此两者上报的 CVE 性质不同；此外，Rust 中 unsafe 代码和意外 panic 也可能产生新的安全风险。

hackernews · nicoburns · Jun 15, 16:11 · [社区讨论](https://news.ycombinator.com/item?id=48543392)

**背景**: 内存安全漏洞如缓冲区溢出是软件安全的主要威胁，CVE 系统为已知漏洞提供标准标识。Rust 通过所有权和借用检查在编译时防止内存错误，但 unsafe 块仍可能引入问题，而 C/C++则完全依赖开发者手动管理内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 用户 john_strinlai 认为 CVE 数量是最无用的指标，提议忽略仅比较数量的言论；cesaref 建议 C 函数应增加非空断言；bawolff 指出 Rust 的 Option<T>与 C 的空指针不可比；fweimer 担心 Rust 的类型安全瑕疵可能被标记为 CVE，增加开发者负担。

**标签**: `#Rust`, `#C++`, `#memory safety`, `#CVEs`, `#software security`

---

<a id="item-9"></a>
## [Diplomat：为 Rust 库生成多语言 FFI 绑定](http://manishearth.github.io/blog/2026/06/14/diplomat-multi-language-ffi-for-rust-libraries/) ⭐️ 8.0/10

Diplomat 是一种新工具，可自动从 Rust 库生成面向 C、C++ 和 JavaScript 等语言的高层级 FFI 绑定，显著降低多语言互操作的门槛。 该工具解决了 Rust 生态中长期存在的 FFI 编写繁琐、易出错的问题，使 Rust 库能更轻松地被其他语言调用，从而扩大 Rust 在跨语言项目中的适用性。 Diplomat 最初由 Manish 于 2021 年为 ICU4X 项目设计，支持单向 FFI（即仅从其他语言调用 Rust），并自动生成类型安全的高层级 API。

rss · Lobsters · Jun 15, 05:53

**背景**: FFI（外部函数接口）是让一种编程语言调用另一种语言编写的函数的技术。传统上，为 Rust 库提供多语言绑定需要手动编写大量样板代码，且容易出错。Diplomat 通过定义 Rust API 注解，自动生成对应语言的绑定代码，大大简化了这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rust-diplomat/diplomat">GitHub - rust - diplomat / diplomat : Rust tool for generating FFI ...</a></li>
<li><a href="https://manishearth.github.io/blog/2026/06/14/diplomat-multi-language-ffi-for-rust-libraries/">Diplomat : Multi-language FFI for Rust Libraries - In Pursuit of Laziness</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foreign_function_interface">Foreign function interface - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Rust`, `#FFI`, `#multi-language`, `#libraries`, `#interoperability`

---

<a id="item-10"></a>
## [用 C++26 静态反射在编译时解析 JSON](https://lemire.me/blog/2026/06/14/parsing-json-at-compile-time-with-c26-static-reflection/) ⭐️ 8.0/10

文章探讨了如何利用 C++26 新引入的静态反射功能，在编译时直接解析 JSON 字符串，生成类型安全的数据结构。 该技术实现了零运行时开销的 JSON 解析，显著提升性能，同时通过编译期类型检查增强代码安全性，展示了 C++26 静态反射的实际应用价值。 该方法依赖 C++26 静态反射在编译期对 JSON 结构进行内省和类型匹配，要求 JSON 内容在编译时已知；解析结果直接映射为 C++类型，避免了运行时动态解析的开销。

rss · Lobsters · Jun 15, 06:07

**背景**: C++26 标准正式引入了静态反射机制，允许程序员在编译期查询类型的成员、布局等信息，从而进行元编程。编译时 JSON 解析是这一特性的一种应用，将原本运行时的解析工作提前到编译阶段，适用于配置文件、固定数据等场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.infoq.com/news/2025/06/cpp-26-feature-complete/">C++26 Draft Finalized with Static Reflection, Contracts, and Sender/Receiver Types - InfoQ</a></li>
<li><a href="https://medium.com/@massimiliano.bastia92/c-static-reflection-an-overview-of-the-metaprogramming-paradigm-shift-4cc2ca49a2c6">C++ Static Reflection: An Overview of the Metaprogramming Paradigm Shift | by Massimiliano Bastia | Medium</a></li>

</ul>
</details>

**标签**: `#C++`, `#JSON`, `#compile-time`, `#static reflection`, `#programming`

---

<a id="item-11"></a>
## [Clojure 优化后性能接近 C](https://ertu.dev/posts/4_clojure-reaching-c-performance/) ⭐️ 8.0/10

一篇技术博客文章展示了通过类型提示、原始类型和避免反射等优化手段，Clojure 代码的性能可以接近 C 语言的水平。 该文章挑战了 Clojure 作为动态函数式语言天生性能较慢的偏见，表明在 JVM 上也能达到接近系统级语言的效率，对性能敏感的 Clojure 开发者具有重要参考价值。 文章具体使用了 Clojure 的`^long`类型提示、`long-array`原始数组以及避免装箱操作等技术，将计算密集型任务的运行时间从数秒降至接近 C 的水平（文中以斐波那契数列计算为例）。

rss · Lobsters · Jun 15, 04:44

**背景**: Clojure 是一种运行在 JVM 上的动态函数式 Lisp 方言，默认使用不可变数据和装箱类型，这在某些场景下会导致性能开销。通常，动态语言（如 Python、Ruby）比静态编译语言（如 C、Rust）慢得多，但通过合适的优化技巧，可以大幅缩小差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Clojure_(programming_language)">Clojure (programming language)</a></li>
<li><a href="https://clojure.org/">Clojure</a></li>

</ul>
</details>

**标签**: `#Clojure`, `#performance`, `#optimization`, `#JVM`, `#programming languages`

---

<a id="item-12"></a>
## [家庭实验室 AI 开发平台分享引发社区共鸣](https://rsgm.dev/post/ai-dev-platform/) ⭐️ 7.0/10

一位开发者详细介绍了其自建的家庭实验室 AI 开发平台设置，包括使用 opencode 作为 AI 编码助手并与 Forgejo 集成，这一分享在社区中获得了 228 个赞和 42 条评论。 该分享反映了自托管 AI 开发环境的趋势，开发者们积极交流实践经验，促进了开源 AI 工具链和本地化工作流的普及与优化。 该平台的核心组件包括 opencode AI 编码助手和 Forgejo 版本控制系统，评论中还提到了使用 n8n、k3s 等工具实现自动化工作流，以及通过 Forgejo 动作运行器调用 opencode 的能力。

hackernews · rsgm · Jun 15, 15:09 · [社区讨论](https://news.ycombinator.com/item?id=48542433)

**背景**: 家庭实验室（homelab）AI 开发平台是指个人或小型团队在自有的硬件上搭建的端到端 AI 开发环境，通常涵盖代码编辑、模型推理、自动化流水线等功能。这类设置依赖开源工具，旨在提供灵活、低成本且高度可控的实验环境。

**社区讨论**: 社区反响热烈，许多开发者分享了类似的工作流，例如将 opencode 集成到 Forgejo 动作运行器中，或使用 n8n 和 k3s 构建自动化平台。也有用户讨论了资源限制和测试效率等实际挑战，整体氛围积极且富有建设性。

**标签**: `#homelab`, `#AI development`, `#self-hosting`, `#dev platform`, `#open source`

---

<a id="item-13"></a>
## [美国电池制造业产出再创新高，但与中国差距悬殊](https://fred.stlouisfed.org/series/IPG33591S) ⭐️ 7.0/10

据 FRED 数据显示，美国电池制造业产出持续打破历史纪录，但社区评论揭示 2025 年美国电池产能仅为 70 GWh，而中国高达 1755 GWh，差距显著。 这一对比凸显美国在电池供应链上的弱势，影响电动汽车普及、能源存储及国家安全。尽管美国产出增长，但与中国差距巨大，亟需加快产能建设。 社区评论引用 2025 年数据：美国电池产能 70 GWh，中国 1755 GWh，欧洲 252 GWh，且不包括小型电池生产。另有评论提及比亚迪刀片电池 2.0 等最新技术。

hackernews · epistasis · Jun 15, 20:28 · [社区讨论](https://news.ycombinator.com/item?id=48546616)

**背景**: 电池制造业产出是衡量电池生产能力的关键指标，对电动汽车和可再生能源存储至关重要。近年来美国通过《通胀削减法案》等政策扶持本土电池产业，但中国凭借先发优势和规模效应占据主导地位。

**社区讨论**: 社区评论总体认可美国产出增长，但普遍担忧与中国差距巨大。有用户质疑美国电池产出增长与电动汽车普及率不成比例，也有用户认为这对国家安全是积极信号，但追赶任务艰巨。

**标签**: `#battery manufacturing`, `#energy storage`, `#US-China competition`, `#manufacturing output`, `#electric vehicles`

---

<a id="item-14"></a>
## [TimescaleDB 时间序列数据压缩解析](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 7.0/10

TimescaleDB 通过 Hypercore 引擎实现了列式存储与类型感知压缩，对时间序列数据可达到高达 98%的压缩率。 该技术显著降低时间序列数据的存储成本，同时保持 PostgreSQL 的查询性能，对物联网、监控等海量时序场景至关重要。 压缩算法针对不同数据类型采用 delta-of-delta、simple8b、游程编码等方法，并利用列式存储减少扫描数据量。

hackernews · lkanwoqwp · Jun 15, 17:29 · [社区讨论](https://news.ycombinator.com/item?id=48544451)

**背景**: 时间序列数据通常随时间高频采集，具有重复模式。列式存储按列而非行组织数据，便于压缩和聚合查询。TimescaleDB 作为 PostgreSQL 扩展，兼顾 OLTP 与 OLAP。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Column_storage">Column storage</a></li>
<li><a href="https://www.tigerdata.com/blog/time-series-compression-algorithms-explained">Time-series compression algorithms, explained | Tiger Data</a></li>

</ul>
</details>

**社区讨论**: 社区讨论聚焦于压缩对查询性能的实际影响，有用户指出“up to”措辞夸张，也有用户对比了 Swinging-Door 等有损压缩算法，认为 TimescaleDB 的无损压缩更适合 IoT 场景。

**标签**: `#timescaledb`, `#compression`, `#time-series`, `#postgresql`, `#database`

---

<a id="item-15"></a>
## [排版系统 Typst 0.15 发布](https://typst.app/blog/2026/typst-0.15/) ⭐️ 7.0/10

Typst 0.15 版本正式发布，带来了大量新特性和改进，包括性能优化、语法增强和文档功能扩展。 作为 LaTeX 的现代替代品，Typst 以易用性和强大功能受到关注，此次大版本更新进一步巩固了其作为开源排版工具的地位，可能吸引更多用户从传统系统迁移。 具体更新内容涵盖编译器优化、新的标记命令以及更完善的错误提示，官方发布日志提供了完整变更列表。

rss · Lobsters · Jun 15, 17:14

**背景**: Typst 是一个开源排版系统，基于标记语言，旨在提供与 LaTeX 相当的排版能力，同时学习曲线更平缓。它支持复杂数学公式、文档自动化、书籍排版等场景，目前托管在 GitHub 上，采用 Apache 2.0 许可证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Typst">Typst - Wikipedia</a></li>
<li><a href="https://github.com/typst/typst">GitHub - typst/typst: A markup-based typesetting system that is powerful and easy to learn. · GitHub</a></li>
<li><a href="https://typst.app/">Typst: The new foundation for documents</a></li>

</ul>
</details>

**标签**: `#typesetting`, `#Typst`, `#open source`, `#release`

---

<a id="item-16"></a>
## [通过 HTTPS DNS 记录节省 TLS 连接往返](https://savearoundtrip.com/) ⭐️ 7.0/10

一篇名为 savearoundtrip 的文章提出，通过在 DNS 中发布 HTTPS 记录，浏览器可以在首次连接时直接使用 HTTP/3，从而避免一次 TLS 往返。 该提案有助于减少网页加载延迟，提升用户体验，尤其对首次访问的优化有重要意义。若被采纳，可能成为 Web 性能优化的新标准实践。 HTTPS DNS 记录（基于 SVCB）可以提前告知浏览器服务器支持的协议和参数，避免传统的 ALPN 协商带来的额外往返。该方案仅需在 DNS 配置中添加一条记录，无需修改现有 TLS 协议。

rss · Lobsters · Jun 15, 18:36

**背景**: 传统的 TLS 连接需要一次额外的往返（round trip）来协商应用层协议（如 HTTP/1.1 或 HTTP/2）。HTTPS DNS 记录是一种新的 DNS 资源记录类型，它允许域名所有者提前公布服务端的协议能力，使得浏览器在第一次连接时就能直接使用最优协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://savearoundtrip.com/">savearoundtrip: publish an HTTPS DNS record, skip a round trip</a></li>
<li><a href="https://gcore.com/docs/dns/dns-records/what-is-an-https-record-and-how-is-it-configured">What is an HTTPS record and how is it configured? - Gcore Docs</a></li>
<li><a href="https://hosting.nl/en/support/wat-is-een-https-dns-record-en-hoe-voeg-je-een-http-dns-record-toe/">Add an HTTPS DNS record (and what is it really) | Hosting.NL</a></li>

</ul>
</details>

**标签**: `#DNS`, `#HTTPS`, `#web performance`, `#TLS optimization`

---

<a id="item-17"></a>
## [用户抗议 AMD 移除消费级 CPU 内存加密](https://arstechnica.com/security/2026/06/users-cry-foul-after-amd-stripped-memory-crypto-from-its-consumer-cpus/) ⭐️ 7.0/10

AMD 从其消费级 CPU 中移除了内存加密功能，这一变化引发了用户的强烈不满和抗议。 内存加密是保护数据免受物理攻击的关键安全特性，移除该功能将使用户数据更容易在内存被盗或冷启动攻击时泄露，对个人和企业用户的安全构成威胁。 目前尚不清楚 AMD 具体移除了哪一项内存加密技术（如 SME 或 TSME），但该决定影响了所有使用相关消费级 CPU 的用户。AMD 官方尚未对此变动发表详细声明。

rss · Lobsters · Jun 15, 20:03

**背景**: 内存加密是一种在 CPU 与 RAM 之间实时加密数据的技术，可防止攻击者通过物理手段读取内存内容。AMD 的 Secure Memory Encryption（SME）和 Transparent SME（TSME）此前主要应用于 EPYC 服务器处理器，部分消费级 CPU 也曾支持该功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/developer/sev.html">AMD Secure Encrypted Virtualization (SEV) | AMD</a></li>
<li><a href="https://blog.cloudflare.com/securing-memory-at-epyc-scale/">Securing Memory at EPYC Scale | The Cloudflare Blog</a></li>

</ul>
</details>

**标签**: `#security`, `#AMD`, `#hardware`, `#cryptography`, `#CPU`

---

<a id="item-18"></a>
## [裸机启动 Linux：最小化启动技术](https://nick.zoic.org/art/boot-naked-linux/) ⭐️ 7.0/10

一篇文章详细探讨了如何从零开始构建最小 Linux 启动环境，跳过传统引导加载程序，直接使用内核 EFI 存根和极简 initramfs 来引导系统。 对于系统程序员和嵌入式开发者，理解这种最小化启动方法有助于深入掌握 Linux 启动流程，优化启动速度，并简化定制系统的构建。 文章可能涉及 Linux 内核的 EFI 启动存根（stub）、initramfs 手动构建以及启动协议中的关键字段（如魔数 0xAA55）。最小化启动常用于资源受限或需要快速启动的场景。

rss · Lobsters · Jun 15, 17:43

**背景**: Linux 启动传统上依赖于引导加载程序（如 GRUB 或 systemd-boot）来加载内核和 initramfs（初始内存文件系统）。initramfs 包含启动所需的驱动和工具。通过使用内核的 EFI 存根，可以直接从 UEFI 固件启动内核，省去 bootloader。最小化启动意味着仅包含必要组件，以获得极小的启动映像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linux_startup_process">Booting process of Linux - Wikipedia</a></li>
<li><a href="https://wiki.archlinux.org/title/Minimal_initramfs">mkinitcpio/ Minimal initramfs - ArchWiki</a></li>
<li><a href="https://www.kernel.org/doc/html/v6.1/x86/boot.html">1. The Linux/x86 Boot Protocol — The Linux Kernel documentation</a></li>

</ul>
</details>

**标签**: `#Linux`, `#booting`, `#systems programming`, `#kernel`

---

<a id="item-19"></a>
## [PostgreSQL 唯一可扩展删除操作是 DROP TABLE](https://planetscale.com/blog/the-only-scalable-delete) ⭐️ 7.0/10

PlanetScale 发表文章指出，在 PostgreSQL 中，对于大规模数据删除，唯一可扩展的操作是 DROP TABLE，因为普通 DELETE 操作受 MVCC 机制影响，会产生大量死元组并导致 VACUUM 性能问题。 该观点揭示了 PostgreSQL 在大数据量场景下删除操作的性能瓶颈，对数据库架构设计和运维策略有重要指导意义，尤其适用于需要定期清理大量数据的高并发系统。 PostgreSQL 的 MVCC 机制使 DELETE 操作仅为逻辑标记，实际数据回收依赖 VACUUM；随着表增大和碎片化，VACUUM 效率显著下降；而 DROP TABLE 直接释放整个表的存储空间，无需逐行清理。

rss · Lobsters · Jun 15, 05:55

**背景**: PostgreSQL 使用多版本并发控制（MVCC）处理并发事务，每个更新或删除操作都会创建新行版本，旧版本保留用于其他事务。未清理的死元组会占用空间并影响性能，因此数据库需要自动或手动执行 VACUUM 来回收空间。VACUUM 的触发基于阈值（默认 50 行+20%变化量），大表可能需要调优。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://planetscale.com/blog/the-only-scalable-delete">The only scalable delete in Postgres is DROP TABLE — PlanetScale</a></li>
<li><a href="https://www.postgresql.org/docs/7.1/mvcc.html">PostgreSQL: Documentation: 7.1: Multi-Version Concurrency Control</a></li>
<li><a href="https://www.postgresql.org/docs/current/routine-vacuuming.html">PostgreSQL: Documentation: 18: 24.1. Routine Vacuuming</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#database`, `#scalability`, `#data deletion`

---