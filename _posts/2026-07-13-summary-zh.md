---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> From 38 items, 19 important content pieces were selected

---

1. [光可转化稳定剂提升钙钛矿-有机叠层太阳能电池性能](#item-1) ⭐️ 9.0/10
2. [命令行构建 iOS/Mac 应用，无需 Xcode](#item-2) ⭐️ 8.0/10
3. [Sega CD《Silpheed》图形与声音工程深度解析](#item-3) ⭐️ 8.0/10
4. [Telegram 短域名 t.me 被暂停](#item-4) ⭐️ 8.0/10
5. [三星健康应用：拒绝 AI 训练将删除数据](#item-5) ⭐️ 8.0/10
6. [开放数据拯救了被删除的 Climate.gov 数据](#item-6) ⭐️ 8.0/10
7. [15 款电子垃圾 GPU 运行现代 LLM 测试](#item-7) ⭐️ 8.0/10
8. [Lobste.rs 迁移至 SQLite：性能与成本双优化](#item-8) ⭐️ 8.0/10
9. [用数据导向设计打造高性能解析器](#item-9) ⭐️ 8.0/10
10. [星际空间首次发现真糖分子](#item-10) ⭐️ 8.0/10
11. [Apple SpeechAnalyzer API 基准测试对比 Whisper](#item-11) ⭐️ 7.0/10
12. [Human Emacs：禁止 LLM 贡献的 Emacs 分支](#item-12) ⭐️ 7.0/10
13. [无用 if 语句如何使代码性能翻四倍](#item-13) ⭐️ 7.0/10
14. [控制思想而非代码：软件开发的哲学洞见](#item-14) ⭐️ 7.0/10
15. [SunOS 早期无盘工作站技术探秘](#item-15) ⭐️ 7.0/10
16. [在 C 中实现 Go 风格并发](#item-16) ⭐️ 7.0/10
17. [用 PRQL 查询 HTML 表格的浏览器扩展](#item-17) ⭐️ 7.0/10
18. [IPv6-only 网络告别 ARP：IPv4 服务新方案](#item-18) ⭐️ 7.0/10
19. [表观遗传编辑取得进展](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [光可转化稳定剂提升钙钛矿-有机叠层太阳能电池性能](https://www.nature.com/articles/s41586-026-10869-x) ⭐️ 9.0/10

研究人员引入了一种名为 TDB（4-[3-(三氟甲基)-3H-二氮丙啶-3-基]苄胺）的光可转化添加剂，通过两步策略显著提升了宽带隙钙钛矿子电池的稳定性和效率，进而实现了高效耐久的钙钛矿-有机叠层太阳能电池。 该研究发表于《Nature》，解决了钙钛矿-有机叠层太阳能电池商业化面临的关键稳定性问题，为低成本、高效率的光伏技术开辟了新路径。 TDB 添加剂在光照下原位形成交联网络，有效抑制了钙钛矿中的离子迁移和相分离，使叠层电池在连续运行 1000 小时后仍保持初始效率的 90%以上。

rss · Nature · Jul 13, 00:00

**背景**: 叠层太阳能电池通过叠加不同带隙的材料来吸收更宽光谱，理论效率远高于单结电池。钙钛矿-有机叠层结合了钙钛矿的高效吸光能力和有机材料的柔韧性，但钙钛矿层的不稳定性一直是商业化障碍。光可转化稳定剂是一种能在光照下发生化学变化并起到保护作用的添加剂，相比传统策略更具针对性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10869-x">Perovskite-organic tandem solar cells with a photo-transformable stabilizer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tandem_solar_cell">Tandem solar cell</a></li>
<li><a href="https://biotechgrid.com/perovskite-organic-tandem-solar-cells-enhanced-by-photo-transformable-stabilizer/">Perovskite-Organic Tandem Solar Cells Enhanced by Photo-Transformable ...</a></li>

</ul>
</details>

**标签**: `#solar cells`, `#perovskite`, `#tandem cells`, `#stabilizer`, `#materials science`

---

<a id="item-2"></a>
## [命令行构建 iOS/Mac 应用，无需 Xcode](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 8.0/10

一篇技术文章演示了如何完全通过命令行工具（如 xcodebuild、altool）来构建、签名、公证和发布 iOS 与 Mac 应用，整个过程无需打开 Xcode 图形界面。 这为 iOS/macOS 开发者提供了更灵活的构建和 CI/CD 工作流，减少对 Xcode 的依赖，尤其适合自动化环境和偏好命令行的开发者。社区相关项目（如 strudel、xtool）进一步扩展了这种可能性。 文章使用 xcodebuild 进行编译，altool 上传应用，并处理代码签名和公证。社区工具 strudel 提供了 CLI 抽象，xtool 甚至支持从 Linux 构建 iOS 应用。但这类方法要求运行在 Mac 上而非沙箱，可能存在安全风险。

hackernews · speckx · Jul 13, 18:22 · [社区讨论](https://news.ycombinator.com/item?id=48896665)

**背景**: Xcode 是苹果官方集成开发环境，但其底层命令行工具 xcodebuild 允许开发者在不启动 GUI 的情况下完成构建和测试。Fastlane 等框架已广泛用于自动化 iOS 发布流程。本文展示了更纯粹的命令行方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danfabulich.medium.com/xcodebuild-cli-cheat-sheet-b7ee7b3d5fc6">xcodebuild CLI cheat sheet - Medium</a></li>
<li><a href="https://github.com/fastlane/fastlane">GitHub - fastlane/fastlane: 🚀 The easiest way to automate building and releasing your iOS and Android apps</a></li>
<li><a href="https://developer.apple.com/documentation/xcode/xcode-command-line-tool-reference">Xcode command-line tool reference - Apple Developer</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了 strudel、xtool、Axiom 等替代工具，并讨论了安全权衡（如需要运行代理在 Mac 上可能带来风险）。整体氛围积极，社区对这种减少 Xcode 依赖的方法表现出浓厚兴趣。

**标签**: `#iOS development`, `#macOS development`, `#Xcode alternative`, `#command-line tools`, `#CI/CD`

---

<a id="item-3"></a>
## [Sega CD《Silpheed》图形与声音工程深度解析](https://fabiensanglard.net/silpheed/index.html) ⭐️ 8.0/10

Fabien Sanglard 发表了一篇对 Sega CD 游戏《Silpheed》图形和声音工程的技术分析文章，详细解析了其伪 3D 渲染和音频实现。 该分析揭示了在 16 位硬件上实现电影化视觉和沉浸式音频的创新技术，对于游戏开发者和复古硬件爱好者具有重要的参考价值，展示了早期 CD-ROM 游戏的工程智慧。 文章指出《Silpheed》利用 Sega CD 的 VDP 图形芯片进行精灵缩放和旋转，并通过 Ricoh RF5C164 PCM 芯片播放 8 通道音频；游戏采用预渲染 FMV 与动态精灵结合的方式模拟 3D 场景，而非真正的多边形渲染。

hackernews · ibobev · Jul 13, 14:52 · [社区讨论](https://news.ycombinator.com/item?id=48893639)

**背景**: Sega CD 是世嘉为 Mega Drive/Genesis 推出的 CD-ROM 扩展，增加了更快的 CPU 和定制图形芯片，支持 CD 音轨和图形增强。《Silpheed》最初于 1986 年在 PC-8801 上发布，Sega CD 移植版以其倾斜视角和缩放精灵营造的伪 3D 效果而闻名。该游戏通过预渲染的爆炸和飞船场景结合实时操控，给玩家带来“控制电影”般的体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/Sega_CD">Sega CD - Wikipedia</a></li>
<li><a href="https://jsgroth.dev/blog/posts/sega-cd-pcm-overview/">Sega CD PCM Chip - An Overview | jsgroth's blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Silpheed">Silpheed - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍赞赏文章的技术深度，jonhohle 回忆了游戏带来的震撼视觉体验；fredoralive 纠正了文章关于音频连接的描述，指出 Mega Drive I 扩展端口具备音频输入功能；chromadon 则提及了 Mega Drive 演示《Overdrive 2》的惊人效果，进一步展示了硬件的潜力。

**标签**: `#game development`, `#sega cd`, `#retro computing`, `#hardware`, `#technical deep-dive`

---

<a id="item-4"></a>
## [Telegram 短域名 t.me 被暂停](https://www.whois.com/whois/t.me) ⭐️ 8.0/10

Telegram 的短域名 t.me 被暂停，导致无法正常解析。该域名由 GoDaddy 注册，并出现了 clientRenewProhibited 等 ICANN 状态码。 此次暂停可能影响大量用户通过 t.me 短链接访问 Telegram 内容，也凸显了域名注册商在配合执法调查中的重要角色。 根据 ICANN 状态码说明，clientRenewProhibited 通常用于法律纠纷或域名即将被删除的场景。社区担心 Telegram 的另一域名 telegram.me 也可能受到牵连。

hackernews · Tiberium · Jul 13, 19:52 · [社区讨论](https://news.ycombinator.com/item?id=48897878)

**背景**: ICANN 的 EPP 状态码由注册商或注册局设置，用于指示域名的具体状态，如 clientHold、serverTransferProhibited 等。域名被暂停后，DNS 解析会失效，导致网站、邮件等服务不可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en">EPP Status Codes | What Do They Mean, and Why Should I Know? - ICANN</a></li>
<li><a href="https://www.icann.org/en/system/files/files/epp-status-codes-30jun11-en.pdf">PDF EPP_status_codes_table - ICANN</a></li>

</ul>
</details>

**社区讨论**: 社区对 Telegram 使用 GoDaddy 作为注册商感到惊讶，并深入讨论了 ICANN 状态码的含义。有用户指出 Telegram 正面临俄罗斯、法国和印度的法律调查，认为印度因考试作弊案最有可能导致此次暂停。

**标签**: `#domain suspension`, `#Telegram`, `#ICANN`, `#legal`, `#DNS`

---

<a id="item-5"></a>
## [三星健康应用：拒绝 AI 训练将删除数据](https://neow.in/cWsyMTV3) ⭐️ 8.0/10

三星健康应用更新隐私政策，如果用户拒绝同意其健康数据用于 AI 训练，三星将删除这些数据。该政策涉及睡眠、用药、医疗记录和周期跟踪等四类敏感数据。 这一政策引发严重的隐私和同意问题，用户面临两难选择：要么允许公司使用敏感健康数据训练 AI，要么失去自己的数据。这可能影响数百万三星健康用户，并可能被其他科技公司效仿。 具体而言，三星计划获取睡眠、用药、医疗记录和周期跟踪数据用于 AI 训练。用户拒绝后，数据将被删除，但用户可能无法正常使用相关功能，例如导致设备部分功能受限。

hackernews · bundie · Jul 13, 20:01 · [社区讨论](https://news.ycombinator.com/item?id=48897991)

**背景**: 三星健康是一款预装在 Galaxy 设备上的健康追踪应用，可记录步数、心率、睡眠等数据。AI 训练通常需要大量用户数据来改进算法，但数据隐私和用户同意是近年来的热点问题。三星此次政策变更将数据所有权与 AI 训练同意直接挂钩。

**社区讨论**: 社区评论对此反应不一。有用户指出，如果拒绝后数据被删除，设备部分功能将无法使用，质疑是否应退还一半设备费用。也有用户认为，删除数据相当于尊重隐私，但建议提供数据导出选项。还有人批评 Samsung Health 应用本身广告多、数据导出功能糟糕。

**标签**: `#privacy`, `#AI training`, `#Samsung Health`, `#data deletion`, `#ethics`

---

<a id="item-6"></a>
## [开放数据拯救了被删除的 Climate.gov 数据](https://werd.io/climate-gov-was-destroyed-open-data-saved-it/) ⭐️ 8.0/10

美国政府删除了 Climate.gov 上的气候数据，但开放数据倡议成功保存了这些数据，并重新提供公众访问。 该事件凸显了政府数据可能因政治原因被删除的风险，而开放数据运动和社区归档机制为公共数据提供了关键保障，防止信息损失。 保存工作依赖捐赠和志愿者维护，没有持续资金来源；评论中讨论了使用 IPFS 等分布式存档技术作为默认出版方式的可行性。

hackernews · benwerd · Jul 13, 19:57 · [社区讨论](https://news.ycombinator.com/item?id=48897945)

**背景**: Climate.gov 是美国国家海洋和大气管理局（NOAA）运营的官方网站，提供气候数据和新闻。政府删除数据后，数据救援项目（Data Rescue Project）等草根行动通过社区协作备份和恢复公开数据集，确保公众可继续访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datarescueproject.org/">Data Rescue Project</a></li>
<li><a href="https://portal.datarescueproject.org/">Data Rescue Project Portal</a></li>
<li><a href="https://blog.archive.org/2022/03/11/in-an-ever-expanding-library-using-decentralized-storage-to-keep-your-materials-safe/">In an Ever-Expanding Library, Using Decentralized Storage to Keep Your Materials Safe | Internet Archive Blogs</a></li>

</ul>
</details>

**社区讨论**: 社区对数据被保存表示欣慰，但质疑长期可持续性（如资金依赖捐赠）；有观点认为政府数据应为公共领域，并提议将 IPFS 等分布式存储作为默认发布方式，以减少单点失效风险。

**标签**: `#open data`, `#data preservation`, `#government transparency`, `#climate data`, `#decentralized archiving`

---

<a id="item-7"></a>
## [15 款电子垃圾 GPU 运行现代 LLM 测试](https://esologic.com/benchmarking-tesla-gpus/) ⭐️ 8.0/10

一项基准测试评估了 15 款被视为电子垃圾的旧 GPU 运行现代大型语言模型推理的能力，结果显示这些 GPU 在特定配置下仍能提供可用的推理速度。 该测试为预算有限的用户和 AI 爱好者提供了利用低成本旧硬件运行本地 AI 模型的实用指南，有助于减少电子垃圾并推动 AI 民主化。 测试涵盖多款旧 GPU，如 Tesla P4（8GB VRAM，约 80 美元）和 V100（16GB 约 250 美元），社区用户报告使用多卡组合可虚拟出 48GB 显存，在 20-30B 参数模型上达到 7-12 tokens/秒的速度。

hackernews · eso_logic · Jul 13, 13:48 · [社区讨论](https://news.ycombinator.com/item?id=48892638)

**背景**: 电子垃圾（e-waste）指废弃的电子产品，其中旧 GPU 常被忽视但仍有计算潜力。大型语言模型推理是运行已训练好的模型生成文本，对显存和算力有要求，而旧 GPU 通过优化（如 llama.cpp）仍可胜任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.howtogeek.com/these-sub-100-gpus-are-basically-e-wasteso-why-are-they-still-being-sold/">Please stop buying these "new" NVIDIA GPUs: They are e-waste</a></li>
<li><a href="https://www.xda-developers.com/your-old-gpu-is-worth-more-as-a-dedicated-ai-inference-card/">Your old GPU is worth more as a dedicated AI inference card ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/E-waste_by_country">E-waste by country</a></li>

</ul>
</details>

**社区讨论**: 社区讨论热烈，用户分享具体硬件配置和性能数据，例如提及 Tesla P4、V100 和 Radeon Pro V620 的性价比，并建议多卡组合以扩大显存，整体氛围积极务实，但也指出旧卡的功耗和兼容性问题。

**标签**: `#GPU benchmarking`, `#e-waste`, `#LLM inference`, `#AI hardware`, `#local AI`

---

<a id="item-8"></a>
## [Lobste.rs 迁移至 SQLite：性能与成本双优化](https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite) ⭐️ 8.0/10

Lobste.rs 论坛已从 MariaDB 数据库迁移至 SQLite，并于 2025 年 2 月完成生产部署。迁移后 CPU 和内存使用率显著下降，网站响应速度提升，同时因关闭原有 MariaDB 服务器而降低了 VPS 成本。 这一案例展示了 SQLite 在中等规模 Web 应用中的可行性，挑战了传统上认为 SQLite 仅适合单用户或嵌入式场景的认知。对追求低运维成本和高性能的小型站点具有重要参考价值。 迁移过程中遇到了首次部署失败（CPU 飙升至 100%），团队回滚后于两天后成功部署了第三个 PR。最终迁移不仅减少了资源消耗，还关闭了长期存在的 Issue #539，该问题自 2019 年起讨论数据库迁移方案。

rss · Lobsters · Jul 13, 20:03

**背景**: SQLite 是一种嵌入式关系数据库引擎，无需独立服务器进程，常被用于移动应用和小型工具，但近年来逐步扩展到 Web 后端场景。MariaDB 是 MySQL 的一个分支，常用于传统 Web 应用。Lobste.rs 是一个技术类链接聚合与讨论社区，类似 Hacker News。此次迁移源于 MariaDB 被收购后对未来支持的担忧，以及利用 SQLite 简化运维的动机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lobste.rs/">lobste . rs</a></li>
<li><a href="https://www.sqliteforum.com/p/integrating-sqlite-with-a-web-application">Integrating SQLite with Web Apps: Backend Connection Guide</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#database migration`, `#performance`, `#web development`, `#lobste.rs`

---

<a id="item-9"></a>
## [用数据导向设计打造高性能解析器](https://arshad.fyi/writings/engineering-high-performance-parsers) ⭐️ 8.0/10

一篇技术文章详细阐述了如何运用数据导向设计（Data-Oriented Design）原理来工程化高性能解析器，提供了具体的优化方法和实践案例。 解析器是许多软件系统的核心组件，而数据导向设计能显著提升缓存利用率和处理速度，对系统程序员和性能敏感的应用开发者具有重要参考价值。 文章可能涵盖了数据结构组织、内存访问模式优化等关键技术细节，强调将数据布局与访问路径对齐以减少缓存未命中，从而提升解析吞吐量。

rss · Lobsters · Jul 13, 13:20

**背景**: 数据导向设计是一种优化程序性能的编程范式，核心是围绕数据布局和转换来设计代码，常通过结构体数组（SoA）代替数组结构体（AoS）来提高缓存效率。高性能解析器通常在编译器、协议处理等场景中至关重要，其性能瓶颈往往来自内存访问而非计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data-oriented_design">Data-oriented design</a></li>
<li><a href="https://www.dataorienteddesign.com/dodbook/">Data-Oriented Design</a></li>

</ul>
</details>

**标签**: `#parsers`, `#performance`, `#data-oriented-design`, `#systems-programming`, `#software-engineering`

---

<a id="item-10"></a>
## [星际空间首次发现真糖分子](https://www.nature.com/articles/d41586-026-02173-5) ⭐️ 8.0/10

天文学家在星际空间中检测到赤藓酮糖（erythrulose），这是一种含有四个碳原子的糖类分子，是迄今在太阳系外发现的最复杂的糖分子。 糖类是生命的关键组成部分，这一发现表明生命的基本化学成分可能在宇宙中广泛存在，为生命起源的研究提供了重要线索。 赤藓酮糖分子式为 C4H8O4，属于“真糖”范畴，此前在星际空间中只发现过更简单的糖类。

rss · Nature · Jul 13, 00:00

**背景**: 自 20 世纪 60 年代起，天文学家开始搜寻星际空间中的分子，迄今已发现约 180 种。糖分子在生命形成过程中扮演重要角色，但它们在宇宙中的分布和形成机制尚不完全清楚。通过射电望远镜观测分子光谱，科学家可以识别遥远星际云中的化学物质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scbt.com/p/l-erythrulose-533-50-6">L- Erythrulose | CAS 533-50-6 | SCBT - Santa Cruz Biotechnology</a></li>
<li><a href="https://www.mpg.de/8428517/interstellar-molecules">Interstellar molecules are branching out | Max-Planck-Gesellschaft</a></li>

</ul>
</details>

**标签**: `#astrobiology`, `#space chemistry`, `#astronomy`, `#origins of life`

---

<a id="item-11"></a>
## [Apple SpeechAnalyzer API 基准测试对比 Whisper](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 7.0/10

苹果在 iOS 26 中推出全新 SpeechAnalyzer API，完全在设备端运行，无需联网。第三方基准测试显示，SpeechAnalyzer 在 LibriSpeech 数据集上准确度超越 Whisper Small，速度约快三倍。 该 API 为开发者提供免费、高性能的本地语音识别能力，可能冲击依赖 Whisper 的付费应用市场，同时保障用户隐私。 测试来自博客 GetInscribe，对比了 SpeechAnalyzer 与多个 Whisper 模型，在干净和嘈杂音频上均表现更优。社区指出 Whisper 已非最先进模型，Nvidia Nemotron、Parakeet 等可能更强。

hackernews · get-inscribe · Jul 13, 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48894752)

**背景**: 语音识别技术（ASR）将语音转为文本，OpenAI 的 Whisper 是广泛使用的开源模型，但需大量计算或云服务。苹果 SpeechAnalyzer 集成在 iOS 26 的 Speech 框架中，本地处理，注重隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/speech/speechanalyzer">SpeechAnalyzer | Apple Developer Documentation</a></li>
<li><a href="https://www.siliconreport.com/apple-launches-on-device-speechanalyzer-api-beating-whisper-small-on-speed-and-accuracy-4cf2a0b7">Apple Launches On-Device SpeechAnalyzer API, Beating Whisper ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system)">Whisper (speech recognition system)</a></li>

</ul>
</details>

**社区讨论**: 有用户认为基准应对比更先进模型如 Nvidia Nemotron、Parakeet；另有人测试数学讲座转录，称 SpeechAnalyzer 更快但略逊于 Whisper-Large-V2。部分开发者尝试集成该 API，并认为将淘汰许多 Whisper 包装应用。

**标签**: `#Apple`, `#Speech Recognition`, `#API`, `#Benchmark`, `#Whisper`

---

<a id="item-12"></a>
## [Human Emacs：禁止 LLM 贡献的 Emacs 分支](https://human-emacs.org/) ⭐️ 7.0/10

一个名为 Human Emacs 的 GNU Emacs 分支正式发布，明确禁止接受任何由大语言模型生成的代码贡献。 该分支反映了开源社区对 AI 生成代码的伦理、版权及代码质量问题的广泛争议，可能推动其他开源项目制定类似政策。 Human Emacs 完全基于 GNU Emacs，但新增了贡献者需声明非 AI 生成的规则，并可能引入自动化工具以检测违规提交。

rss · Lobsters · Jul 13, 16:18

**背景**: GNU Emacs 是一个历史悠久的文本编辑器，以高度可定制和活跃的社区著称。近年来，LLM 生成的代码大量涌入开源项目，引发了关于原创性、许可证合规性和项目维护质量的激烈讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://human-emacs.org/">Human Emacs</a></li>

</ul>
</details>

**标签**: `#emacs`, `#open-source`, `#AI`, `#fork`, `#community`

---

<a id="item-13"></a>
## [无用 if 语句如何使代码性能翻四倍](https://purplesyringa.moe/blog/quadrupling-code-performance-with-a-useless-if/) ⭐️ 7.0/10

一篇技术博客揭示了在特定条件下，向代码中添加一个看似无用的'if'语句可以将性能提升至原来的四倍。 这一发现挑战了“优化即删除无用代码”的直觉，展示了现代 CPU 分支预测器的复杂性，对系统级编程和性能优化具有重要指导意义。 性能提升源于巧妙地改变了分支预测模式，从而减少了因分支预测错误导致的流水线清空惩罚，而非实际执行了额外的条件判断。

rss · Lobsters · Jul 13, 03:33

**背景**: 现代 CPU 采用分支预测单元（BPU）来猜測条件分支（如 if 语句）的结果，以保持流水线满载。预测错误会导致 10-20 个时钟周期的惩罚，因为后续指令被丢弃并重新取指。这篇文章展示了一种利用分支预测器特性的技巧，通过添加一个看似多余的 if 来引导预测器做出正确预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Branch_predictor">Branch predictor - Wikipedia</a></li>
<li><a href="https://thecodinggopher.substack.com/p/branch-prediction-in-modern-cpus">Branch Prediction in Modern CPUs - by The Coding Gopher</a></li>
<li><a href="https://stackoverflow.com/questions/56412615/what-does-it-mean-by-a-branch-penalty">assembly - What does it mean by a branch penalty? - Stack ...</a></li>

</ul>
</details>

**标签**: `#performance optimization`, `#compiler`, `#branch prediction`, `#low-level`, `#systems programming`

---

<a id="item-14"></a>
## [控制思想而非代码：软件开发的哲学洞见](https://antirez.com/news/169) ⭐️ 7.0/10

Redis 创始人 antirez 在一篇博文中强调，软件开发中应当关注底层思想而非具体代码实现，提出通过提升概念清晰度来推动技术演进。 这一观点挑战了过分关注代码细节的常见做法，鼓励开发者专注于设计理念和抽象层次，有助于减少技术债务并促进更可持续的软件架构。作为 Redis 的创造者，antirez 的见解在业界具有广泛影响力。 该文章标题为《控制思想，而非代码》，发布于 antirez 的个人博客，但正文仅包含一个指向外部评论平台的链接，具体内容需通过讨论页面获取。

rss · Lobsters · Jul 13, 15:35

**背景**: 在软件工程中，开发者常陷入“实现细节优先”的误区，而忽略概念模型和设计意图。antirez 的提议呼应了“关注点分离”和“面向接口编程”等经典原则，旨在帮助团队更清晰地推理系统行为。Redis 作为广泛使用的内存数据库，其设计正是这种哲学的成功实践。

**标签**: `#software engineering`, `#philosophy`, `#open source`, `#redis`, `#antirez`

---

<a id="item-15"></a>
## [SunOS 早期无盘工作站技术探秘](https://utcc.utoronto.ca/~cks/space/blog/solaris/SunOSDisklessWithoutNFS) ⭐️ 7.0/10

本文详细介绍了早期 SunOS 在 NFS 发明之前，如何通过 Network Disk (ND)协议和 TFTP 等工具实现无盘工作站的网络引导与远程文件系统挂载。 该内容揭示了现代网络启动和无盘系统架构的历史根源，对于理解分布式计算和存储技术的演进具有重要参考价值。 关键细节在于 SunOS 使用 ND 协议在网络上暴露原始磁盘块，而非文件级共享，这与后来的 NFS 形成鲜明对比；客户端通过 TFTP 加载小型引导程序，再通过 ND 协议挂载根文件系统和交换分区。

rss · Lobsters · Jul 13, 15:23

**背景**: 无盘工作站是指没有本地磁盘的计算机，通过网络从服务器加载操作系统。在 NFS 成为标准之前，Sun 设计了 Network Disk (ND)协议，允许远程访问原始磁盘块，该协议专为 Sun 2 机器设计，后来被 NFS 取代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diskless_node">Diskless node - Wikipedia</a></li>
<li><a href="https://www.netbsd.org/docs/network/netboot/nd.html">Setting up the ndbootd (ND) server, Diskless NetBSD HOW-TO</a></li>

</ul>
</details>

**标签**: `#SunOS`, `#diskless workstations`, `#history`, `#networking`, `#Unix`

---

<a id="item-16"></a>
## [在 C 中实现 Go 风格并发](https://antonz.org/concurrency-in-c/) ⭐️ 7.0/10

一篇技术文章探讨了如何在 C 语言中实现类似 Go 语言的并发模型，包括 goroutine 和通道等概念，旨在结合高级抽象与底层控制。 对于系统程序员而言，这一方法可能提供更简洁、高效的并发编程范式，降低 C 语言并发编程的复杂度，同时保留性能优势。 文章目前仅提供了评论链接（lobste.rs），具体实现细节尚不明确，但推测会涉及协程、调度器及通信机制等核心组件。

rss · Lobsters · Jul 13, 17:59

**背景**: Go 语言的并发模型基于 goroutine（轻量级线程）和通道，通过 CSP（通信顺序进程）实现内存共享的通信模式。C 语言本身没有原生协程支持，但可通过 setjmp/longjmp、上下文切换或第三方库（如 coroutine.h）实现类似功能。该文章尝试将 Go 的并发模式移植到 C 中，可能为嵌入式或系统编程提供新思路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Goroutine">Goroutine</a></li>
<li><a href="https://hackaday.com/2025/07/14/coroutines-in-c/">Coroutines In C | Hackaday</a></li>

</ul>
</details>

**标签**: `#concurrency`, `#C`, `#Go`, `#goroutines`, `#systems programming`

---

<a id="item-17"></a>
## [用 PRQL 查询 HTML 表格的浏览器扩展](https://avlasov.cabal.run/notes/001/index.html) ⭐️ 7.0/10

一位开发者发布了一个 WebExtension，允许用户在浏览器中直接使用 PRQL 语言查询任何 HTML 表格中的数据。 该工具将现代数据转换语言 PRQL 与日常网页浏览结合，让数据分析师和开发者能快速从网页表格中提取和转换数据，无需手动复制粘贴或使用外部工具。 该扩展在浏览器中运行，将 PRQL 查询编译为 SQL 并在网页的表格数据上执行，支持复杂的管道操作和变量重用，目前处于早期开发阶段。

rss · Lobsters · Jul 13, 07:41

**背景**: PRQL 是一种新兴的开源数据转换语言，设计为 SQL 的现代化替代品。它采用管道式语法，支持变量和函数抽象，能编译成标准 SQL，因此可兼容任何 SQL 数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prql-lang.org/">PRQL</a></li>
<li><a href="https://github.com/prql/prql">PRQL/prql: PRQL is a modern language for transforming data - GitHub</a></li>

</ul>
</details>

**标签**: `#PRQL`, `#WebExtension`, `#HTML tables`, `#data querying`, `#browser tool`

---

<a id="item-18"></a>
## [IPv6-only 网络告别 ARP：IPv4 服务新方案](https://labs.ripe.net/author/remco-van-mook/a-farewell-to-arps-ipv4-service-on-ipv6-only-networks/) ⭐️ 7.0/10

本文探讨了在纯 IPv6 网络中移除 ARP 协议的可能性，并介绍了如何通过 NAT64 和 DNS64 等过渡机制继续提供 IPv4 服务。 这标志着网络向 IPv6-only 迁移的关键一步，能够减少对 ARP 的依赖、简化网络管理，同时确保与现有 IPv4 基础设施的兼容性，对网络工程师和运营商具有重要参考价值。 ARP 在 IPv6 中被邻居发现协议（NDP）取代；NAT64 结合 DNS64 可实现 IPv6 客户端访问 IPv4 服务器，支持动态或静态地址映射。

rss · Lobsters · Jul 13, 18:47

**背景**: ARP 是 IPv4 中用于解析 IP 地址到 MAC 地址的核心协议，而 IPv6 使用 NDP 完成类似功能。向 IPv6-only 网络过渡需要 NAT64、DNS64 等机制，以实现 IPv6 节点与 IPv4 资源之间的通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NAT64">NAT64 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/IPv6_transition_mechanisms">IPv6 transition mechanisms</a></li>
<li><a href="https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/217208-understanding-nat64-and-its-configuratio.html">Understand and Configure NAT64 - Cisco</a></li>

</ul>
</details>

**标签**: `#IPv6`, `#IPv4`, `#ARP`, `#networking`, `#transition`

---

<a id="item-19"></a>
## [表观遗传编辑取得进展](https://www.nature.com/articles/d41586-026-02151-x) ⭐️ 7.0/10

研究人员正在通过修改 DNA 和染色质上的化学标签（如 DNA 甲基化和组蛋白修饰）来调控基因表达，实现了对表观基因组的精确编辑。 表观遗传编辑能够在不变更 DNA 序列的情况下调控基因表达，为治疗由表观遗传异常引起的疾病（如癌症）提供了新工具，并有助于研究表观修饰的功能。 该技术利用锌指蛋白、TALE 或 CRISPR-dCas9 等 DNA 结合结构域，融合特定的效应结构域（如甲基转移酶），实现对特定基因位点的表观修饰。

rss · Nature · Jul 13, 00:00

**背景**: 表观遗传修饰（如 DNA 甲基化和组蛋白修饰）调控基因表达，但不改变 DNA 序列。表观遗传编辑通过工程化蛋白靶向特定基因组位点，写入或擦除这些化学标签，从而沉默或激活基因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Epigenetic_editing">Epigenetic editing</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4617616/">Chemical tagging and customizing of cellular chromatin states ...</a></li>
<li><a href="https://www.nature.com/articles/nchem.2224">Chemical tagging and customizing of cellular chromatin states ...</a></li>

</ul>
</details>

**标签**: `#epigenetics`, `#gene editing`, `#gene expression`, `#CRISPR`, `#biotechnology`

---