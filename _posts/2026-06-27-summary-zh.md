---
layout: default
title: "Horizon Summary: 2026-06-27 (ZH)"
date: 2026-06-27
lang: zh
---

> From 32 items, 14 important content pieces were selected

---

1. [DeepSeek 开源 DSpark 推测解码方法，加速 LLM 推理](#item-1) ⭐️ 9.0/10
2. [公网摄像头活地图引发大规模隐私担忧](#item-2) ⭐️ 8.0/10
3. [数据中的可疑间断点分析](#item-3) ⭐️ 8.0/10
4. [Reddit 反垃圾系统内部机制揭秘](#item-4) ⭐️ 8.0/10
5. [数据访问模式如何让 CPU 变慢](#item-5) ⭐️ 8.0/10
6. [Prism：带有类型化效果的不纯函数式语言](#item-6) ⭐️ 8.0/10
7. [UEFI CA 即将到期，影响 Secure Boot](#item-7) ⭐️ 8.0/10
8. [pg_plan_advice：帮助 PostgreSQL 选择最佳查询计划](#item-8) ⭐️ 8.0/10
9. [扎克伯格对举报人的法律战](#item-9) ⭐️ 7.0/10
10. [Linux 7.2 优化匿名管道性能，提升 Shell 管道速度](#item-10) ⭐️ 7.0/10
11. [Go 缓存分片锁基准测试](#item-11) ⭐️ 7.0/10
12. [AI 学会 RF 芯片设计的“黑暗艺术”](#item-12) ⭐️ 7.0/10
13. [AI 时代的数学家：身份与工作的重塑](#item-13) ⭐️ 7.0/10
14. [Token 级对比 Transformer 与混合模型](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DeepSeek 开源 DSpark 推测解码方法，加速 LLM 推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) ⭐️ 9.0/10

DeepSeek 发布了关于推测解码（Speculative Decoding）的 DSpark 论文，并已在 Hugging Face 上提供集成该模块的模型。 这一创新显著降低了大模型推理的延迟和成本，使开源社区能够更高效地部署 LLM，同时也展示了中国实验室在 AI 研究方面的领先实力。 DSpark 基于推测解码框架，利用小型草稿模型快速生成候选令牌，再由目标模型并行验证，保持输出分布不变的同时将推理速度提升约 2-3 倍。

hackernews · aurenvale · Jun 27, 09:18 · [社区讨论](https://news.ycombinator.com/item?id=48696585)

**背景**: 推测解码是一种推理优化技术，类比 CPU 的推测执行：小型草稿模型预测多个令牌序列，大型目标模型在一次前向传播中验证这些序列，通过拒绝采样保证输出质量与标准解码一致。该技术无需修改模型架构，可直接集成到现有系统中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf">DeepSpec/DSpark_paper.pdf at main · deepseek-ai/DeepSpec</a></li>
<li><a href="https://arxiv.org/abs/2211.17192">[2211.17192] Fast Inference from Transformers via Speculative Decoding</a></li>

</ul>
</details>

**社区讨论**: 社区普遍赞誉 DeepSeek 的开放创新精神，认为其比美国实验室更愿意分享细节；用户实际使用反馈显示成本大幅降低（如 1.5B 令牌花费 40 美元），并期待该技术能集成到本地推理工具如 DwarfStar 中。有网友对比了 2022 年的推测解码论文，询问 DSpark 的改进之处。

**标签**: `#AI/ML`, `#speculative decoding`, `#LLM inference`, `#DeepSeek`, `#open research`

---

<a id="item-2"></a>
## [公网摄像头活地图引发大规模隐私担忧](https://ipcrawl.com/) ⭐️ 8.0/10

一个名为 IP Crawl 的网站通过 IP 爬虫技术，发现并公开展示了全球范围内大量连接到公共互联网的开放式网络摄像头的实时画面。 该网站使得任何人都可以未经授权查看他人私人空间或公共场所的实时监控画面，严重侵犯隐私，并暴露了物联网设备普遍存在的安全配置薄弱问题。 网站允许用户按地理位置、标签等筛选和浏览摄像头，每个摄像头对应一个实时 URL；这些摄像头通常因用户未更改默认密码或未开启防火墙而被直接暴露在公网上。

hackernews · arm32 · Jun 27, 19:09 · [社区讨论](https://news.ycombinator.com/item?id=48700834)

**背景**: 许多廉价网络摄像头为了易用性，出厂时默认关闭安全功能，用户往往不了解如何设置防火墙或更改默认凭据。攻击者或爬虫可以通过扫描特定 IP 段或使用 Shodan 等搜索引擎发现此类设备，IP Crawl 正是利用类似技术系统化收集并展示这些摄像头。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ipcrawl.com/">IP Crawl — open webcam catalog</a></li>
<li><a href="https://asimily.com/blog/iot-security-cameras-are-vulnerable-cyberattacks/">IoT Security Cameras are Vulnerable to Cyberattacks</a></li>
<li><a href="https://www.guidepointsecurity.com/blog/iot-camera-security-evolving-threats/">IoT Camera Security: The Fixable Threat You Might Not See Coming | GuidePoint Security</a></li>

</ul>
</details>

**社区讨论**: 大部分评论者感到不安和震惊，指出这些摄像头可能位于卧室等私密空间，侵犯隐私行为类似于“用望远镜偷窥邻居”。有人回忆十年前已有类似网站，但问题至今未改善，反映了物联网安全的长期困境。

**标签**: `#privacy`, `#security`, `#IoT`, `#webcams`, `#internet exposure`

---

<a id="item-3"></a>
## [数据中的可疑间断点分析](https://danluu.com/discontinuities/) ⭐️ 8.0/10

文章分析了马拉松完赛时间在整半小时和整 15 分钟处出现聚集以及税收政策中的“断崖效应”等数据间断现象，揭示了人类行为和政策的深层模式。 这些发现对数据分析和政策设计具有重要启示，帮助识别统计偏差和政策缺陷，从而改进数据解读和公共政策。 马拉松数据来自 970 多万次完赛记录，显示每半小时和每 15 分钟处有明显间断点，原因是跑者接近整时间时会加速；税收断崖效应则导致某些收入区间有效税率超过 60%。

hackernews · tosh · Jun 27, 13:32 · [社区讨论](https://news.ycombinator.com/item?id=48698151)

**背景**: 数据间断点是指数据分布中出现的异常跳跃或聚集，通常由人为目标驱动行为或制度规则（如税收门槛）引起。本文通过真实案例说明如何识别这些间断点及其背后的机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danluu.com/discontinuities/">Suspicious discontinuities</a></li>
<li><a href="https://www.ncsl.org/human-services/addressing-benefits-cliffs">Addressing Benefits Cliffs</a></li>

</ul>
</details>

**社区讨论**: 社区评论生动有趣，有用户分享了亲身经历解释马拉松数据，也有用户补充了英国和印度税收断崖的具体例子，进一步印证了文章观点。

**标签**: `#data analysis`, `#statistics`, `#policy`, `#behavioral economics`, `#hn-discussion`

---

<a id="item-4"></a>
## [Reddit 反垃圾系统内部机制揭秘](https://lyra.horse/blog/2026/06/reddit-spam-internals/) ⭐️ 8.0/10

一位 Reddit 版主在查看被自动删除的垃圾内容时，意外发现了 Reddit 反垃圾系统的内部工作原理，并在博客中详细披露了其采用的机器学习和启发式技术。 这是罕见地直接曝光大型平台核心反垃圾系统的技术细节，对关注系统安全、机器学习应用及社区治理的读者具有重要参考价值，也可能促使 Reddit 调整其内部策略。 作者是通过版主后台的“已移除垃圾”通知，看到了原本不应公开的系统内部标记和分类信息，从而推断出反垃圾机制。具体技术包括基于内容的特征提取、用户行为模式分析以及机器学习模型等。

rss · Lobsters · Jun 27, 15:10

**背景**: Reddit 是全球知名的社交新闻聚合和讨论平台，面临大量垃圾内容（如广告、恶意链接）的挑战。其反垃圾系统结合了规则引擎、用户举报和机器学习模型，但具体实现一直保密。版主通常只能看到最终结果（帖子被删除），而无法了解判决依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lyra.horse/blog/2026/06/reddit-spam-internals/">A peek into Reddit's anti-spam internals Ʊ lyra's epic blog</a></li>

</ul>
</details>

**标签**: `#Reddit`, `#anti-spam`, `#machine learning`, `#systems`, `#security`

---

<a id="item-5"></a>
## [数据访问模式如何让 CPU 变慢](https://blog.weineng.me/posts/slowest_add/) ⭐️ 8.0/10

一篇技术文章详细分析了特定数据访问模式（如随机访问或非连续访问）如何导致 CPU 缓存频繁未命中，从而大幅降低程序性能。 该分析对性能敏感的软件开发（如游戏引擎、数据库和实时系统）具有重要指导意义，帮助开发者优化内存布局以提升整体效率。 文章可能结合基准测试说明，当数据访问不按顺序或跨度过大时，CPU 每次只能利用缓存行中的少量数据，导致缓存带宽浪费和额外的内存延迟。

rss · Lobsters · Jun 27, 14:18

**背景**: CPU 缓存是位于处理器核心附近的高速存储器，用于临时存储频繁使用的数据以加速访问。当 CPU 需要的数据不在缓存中时（即缓存未命中），它必须从较慢的主存中加载，造成数十甚至数百个周期的延迟。数据访问模式（如顺序访问、步长访问或随机访问）决定了缓存行（通常 64 字节）的利用效率，良好的模式能显著提升性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CPU_cache">CPU cache - Wikipedia</a></li>
<li><a href="https://www.abhik.ai/concepts/memory/cpu-cache-lines">CPU Cache Lines: The Complete Guide with Interactive Simulator | Abhik Sarkar</a></li>
<li><a href="https://redis.io/glossary/cache-miss/">Understanding Cache Misses: Definitions, Types, and Impact</a></li>

</ul>
</details>

**标签**: `#CPU`, `#performance`, `#data access patterns`, `#optimization`, `#systems`

---

<a id="item-6"></a>
## [Prism：带有类型化效果的不纯函数式语言](https://www.stephendiehl.com/posts/prism/) ⭐️ 8.0/10

Stephen Diehl 发布了 Prism 语言的设计，这是一种不纯函数式语言，其类型系统集成了类型化效果（typed effects），允许程序员显式管理副作用。 该设计为函数式编程中副作用管理提供了新的平衡点，可能影响编程语言研究与实践，特别是那些需要在纯函数式严格性与实际开发灵活性之间取得折中的场景。 Prism 允许不纯度（如可变状态或 I/O）通过类型系统中的效果标记进行追踪和控制，与纯函数式语言（如 Haskell）依赖单子管理副作用不同，Prism 采用更直接的效果类型系统。

rss · Lobsters · Jun 27, 19:39

**背景**: 函数式编程通常强调纯函数——无副作用且引用透明。然而，实际程序需要副作用（如输入输出、状态修改）。类型化效果系统将副作用纳入类型签名，使得编译器可以静态检查并限制副作用传播。Effekt 和 Koka 等语言已探索此类设计，Prism 则在不纯函数式范式下实现该理念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Effect_system">Effect system - Wikipedia</a></li>
<li><a href="https://effekt-lang.org/">Effekt Language: Home</a></li>

</ul>
</details>

**标签**: `#programming languages`, `#functional programming`, `#type systems`, `#effects`

---

<a id="item-7"></a>
## [UEFI CA 即将到期，影响 Secure Boot](https://blog.einval.com/2026/06/27#its_dead_jim) ⭐️ 8.0/10

2011 年发布的 UEFI 证书颁发机构（CA）将于 2026 年 6 月 27 日到期，这将影响使用 Secure Boot 的系统启动安全。 此次证书到期可能导致大量设备无法验证启动加载程序，影响 Windows 和 Linux 系统的安全启动，需要用户和企业及时更新固件。 所有使用 2011 年 UEFI CA 签名的启动加载程序（如 Linux Shim）都将失效，未更新固件的设备将失去启动时恶意软件检测能力。

rss · Lobsters · Jun 27, 22:42

**背景**: UEFI 安全启动（Secure Boot）是一种固件安全功能，通过验证启动加载程序的数字签名来防止恶意软件在系统启动时加载。Microsoft 作为 UEFI CA，颁发了用于签名的证书，该证书将在 2026 年 6 月 27 日到期。为了维持安全启动功能，设备需要安装新的 2023 年证书。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trellix.com/blogs/platform/navigating-microsoft-uefi-cert-transition-encrypted-devices/">Navigating the Microsoft UEFI Certificate Transition for Encrypted...</a></li>
<li><a href="https://blog.sonnes.cloud/secure-boot-what-it-is-and-how-to-update-secure-boot-keys/">Secure Boot – What it is and how to update Secure... - Sonne´s Cloud</a></li>
<li><a href="https://www.techtimes.com/articles/318848/20260622/secure-boot-2011-certificates-expire-wednesday-unupdated-devices-lose-bootkit-revocation-forever.htm">Secure Boot 2011 Certificates Expire Wednesday: Unupdated...</a></li>

</ul>
</details>

**标签**: `#UEFI`, `#Secure Boot`, `#Certificate Expiry`, `#Infrastructure`

---

<a id="item-8"></a>
## [pg_plan_advice：帮助 PostgreSQL 选择最佳查询计划](https://www.postgresql.org/docs/19/pgplanadvice.html) ⭐️ 8.0/10

PostgreSQL 19 引入了一个新的贡献模块 pg_plan_advice，它允许用户通过一种特殊的“计划建议”迷你语言来描述、重现和修改关键的规划器决策，从而帮助查询规划器生成更优的执行计划。 该模块直接解决了 PostgreSQL 查询性能优化的常见痛点，为数据库管理员和开发人员提供了一种无需修改 SQL 语句即可干预查询计划的手段，有望显著提升复杂查询的性能。 pg_plan_advice 使用 GUC 设置和 EXPLAIN (PLAN_ADVICE)工作流来生成和应用计划建议，而不是像 Oracle 或 MySQL 那样在 SQL 注释中嵌入提示。它提供了一种结构化的方式来控制规划器行为。

rss · Lobsters · Jun 27, 19:31

**背景**: PostgreSQL 的查询优化器基于统计信息为查询选择执行计划，但有时由于统计不准确或复杂查询逻辑，可能选到次优计划。传统上，用户难以直接干预规划器决策。pg_plan_advice 正是为了填补这一空白而设计的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/19/pgplanadvice.html">PostgreSQL : Documentation: 19: F.30. pg _ plan _ advice — help the...</a></li>
<li><a href="https://neon.com/postgresql/postgresql-19/pg-plan-advice">PostgreSQL 19 pg _ plan _ advice - Query Plan Hints for PostgreSQL</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#query planning`, `#database optimization`, `#performance`

---

<a id="item-9"></a>
## [扎克伯格对举报人的法律战](https://pluralistic.net/2026/06/27/zuckerstreisand-2/) ⭐️ 7.0/10

Meta 公司针对前员工 Sarah Wynn-Williams 的回忆录发起了一场激进的诉讼，试图阻止其出版。文章分析认为，此举可能隐藏着更深的动机，即防止更严重的爆料曝光。 这一事件反映了大型科技公司利用法律手段压制举报人的趋势，可能对内部举报文化和言论自由产生寒蝉效应。同时，它揭示了 Meta 高层如 Joel Kaplan 在其中的角色，引发对科技巨头权力滥用的担忧。 文章提到，Meta 执行副总裁 Joel Kaplan 曾因策划向难民营提供付费互联网服务而失败，并因在员工昏迷期间对其评价“不回应”而受到批评。此外，Kaplan 还卷入了一场政变相关事件。

hackernews · HotGarbage · Jun 27, 14:38 · [社区讨论](https://news.ycombinator.com/item?id=48698684)

**背景**: 举报人是指揭露组织内部不当行为的个人，通常面临法律报复。Meta（原 Facebook）多次因隐私和安全问题受到批评。本新闻中的诉讼针对的是回忆录，而非直接机密泄露，因此显得不同寻常。

**社区讨论**: 社区评论中，用户猜测 Meta 的动机可能不仅仅是震慑，还可能是为了掩盖更严重的秘密。有用户指出扎克伯格在私人棋类游戏中作弊，认为其行为源于自负和报复心理。还有用户建议潜在举报人使用承诺方案（commitment scheme）来保护证据的可信度。

**标签**: `#whistleblowing`, `#Meta`, `#tech ethics`, `#litigation`, `#Hacker News`

---

<a id="item-10"></a>
## [Linux 7.2 优化匿名管道性能，提升 Shell 管道速度](https://www.phoronix.com/news/Linux-72-Faster-Anon-Pipe-Write) ⭐️ 7.0/10

Linux 内核 7.2 版本改进了匿名/未命名管道的写入性能，从而提高了 Shell 管道的执行效率。 这项优化直接影响日常使用 shell 管道的用户和脚本，能减少进程间通信的开销，提升整体系统响应速度。 该改进针对匿名管道的写操作进行了内核级优化，具体可能涉及缓冲区管理和调度策略的调整，但未公开详细技术实现。

rss · Lobsters · Jun 27, 14:29

**背景**: 匿名管道（Anonymous Pipe）是操作系统中一种单向进程间通信（IPC）机制，常用于 shell 中的管道操作符“|”，将一个程序的输出直接传递给另一个程序。Linux 内核的管道实现基于内核缓冲区，优化写入性能可以降低延迟和 CPU 占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anonymous_pipe">Anonymous pipe</a></li>

</ul>
</details>

**标签**: `#linux`, `#kernel`, `#performance`, `#pipes`, `#shell`

---

<a id="item-11"></a>
## [Go 缓存分片锁基准测试](https://strebkov.dev/posts/shard-your-locks/) ⭐️ 7.0/10

一篇博文对六种 Go 缓存实现进行了基准测试，以展示分片锁在减少锁竞争、提升并发性能方面的优势。 该测试为高并发 Go 服务在选择缓存方案时提供了数据支撑，有助于开发者通过简单的分片锁技术显著提升吞吐量。 测试对比了全局锁、读写锁以及不同分片数（如 16、64 个分片）的缓存实现，并展示了在 8 核机器上分片锁可带来数倍的性能提升。

rss · Lobsters · Jun 27, 12:40

**背景**: 在高并发场景下，多个协程同时访问同一个缓存会导致锁竞争，严重降低性能。分片锁（sharded locks）将缓存数据划分为多个独立区域（即分片），每个分片有自己的锁，从而将竞争分散到多个锁上，减少等待时间。这种设计在工业级系统（如 ConcurrentHashMap）中已被广泛验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yuxu.ge/blog/hephaestus/2026-02-25-sharded-locking-strategy-en.html">Beyond Global Locks: Sharded Locking Strategies in Rust</a></li>

</ul>
</details>

**标签**: `#Go`, `#caching`, `#concurrency`, `#performance`, `#benchmarking`

---

<a id="item-12"></a>
## [AI 学会 RF 芯片设计的“黑暗艺术”](https://spectrum.ieee.org/ai-radio-chip-design) ⭐️ 7.0/10

研究人员利用强化学习和扩散模型，让 AI 自动设计射频（RF）芯片，将传统需要数月的手工设计过程缩短至数小时。 这一突破将极大加速 5G、雷达等无线通信系统的开发周期，降低对稀缺 RF 芯片设计专家的依赖，推动硬件设计自动化进入新阶段。 AI 生成的电路结构往往出人意料但效率极高，已成功应用于实际 RF 集成电路（RFIC）设计，并经过仿真验证。

rss · Lobsters · Jun 27, 18:03

**背景**: RF 芯片设计涉及高频模拟电路与电磁场复杂交互，长期以来依赖少数资深工程师凭经验和直觉进行手工调优，因此被称为“黑暗艺术”。传统设计流程包含大量试错迭代，周期长且成本高昂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/ai-radio-chip-design">AI Learns the “Dark Art” of RFIC Design - IEEE Spectrum</a></li>
<li><a href="https://thinkrobotics.com/blogs/learn/radio-frequency-chips-the-backbone-of-iot-communication">Radio Frequency Chips : The Backbone of IoT Communication</a></li>
<li><a href="https://www.meegle.com/en_us/topics/chip-design/chip-design-for-rf-applications">Chip Design For RF Applications</a></li>

</ul>
</details>

**标签**: `#AI`, `#chip design`, `#RF`, `#machine learning`, `#hardware design`

---

<a id="item-13"></a>
## [AI 时代的数学家：身份与工作的重塑](https://spectrum.ieee.org/ai-in-mathematics) ⭐️ 7.0/10

IEEE Spectrum 发表文章，探讨随着 AI（如 DeepMind 的 AlphaProof）在数学定理证明上取得突破，数学家的传统角色和工作内涵正面临重新定义。 这一讨论触及人类在数学创造中的独特价值、AI 对数学本质的影响，以及未来数学教育和科研方向的根本问题。 文章提及自动定理证明（ATP）技术的进步，特别是 DeepMind 的 AlphaProof 在 2024 年成功解决了多个长期未解的数学问题，展示了 AI 在数学推理上的强大能力。

rss · Lobsters · Jun 27, 00:27

**背景**: 自动定理证明是计算机科学的一个分支，旨在用程序自动生成数学证明。近年，AI 结合形式化验证工具（如 Lean）显著提升了证明能力，使 AI 不仅能辅助计算，还能参与发现和验证定理。这促使数学家反思自身工作的核心——从证明发现转向更高层次的抽象与创造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://dev.to/monuminu/how-deepmind-alphaproof-nexus-cracks-56-year-old-math-agentic-llm-loops-and-lean-formal-45ei">How DeepMind AlphaProof Nexus Cracks 56-Year-Old Math ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#philosophy of science`

---

<a id="item-14"></a>
## [Token 级对比 Transformer 与混合模型](https://arxiv.org/pdf/2606.20936) ⭐️ 7.0/10

一篇 arXiv 预印本论文在 token 级别上系统比较了标准 Transformer 架构与混合模型（如 LSTM-Transformer 和 CNN-Transformer）的性能差异。 这种细粒度的对比有助于研究人员理解不同架构在处理序列数据时对局部与全局依赖关系的捕获能力，从而为未来模型设计和优化提供指导。 论文可能分析了多种混合模型变体，并在自然语言处理或时间序列预测等任务上评估了 token 级别的准确率、计算效率等指标。

rss · Lobsters · Jun 27, 15:16

**背景**: Transformer 通过自注意力机制擅长捕获长距离依赖，但计算复杂度较高；混合模型结合 CNN 或 LSTM 的局部特征提取能力与 Transformer 的全局建模能力，旨在平衡性能与效率。Token 级别评估关注模型对每个输入单元（如词或子词）的理解，是衡量细粒度表现的重要方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41598-024-55483-x">Advanced hybrid LSTM-transformer architecture for real-time ...</a></li>
<li><a href="https://medium.com/@savindufernando/the-rise-of-hybrid-cnn-transformer-architectures-5e101986f51d">The Rise of Hybrid CNN-Transformer Architectures - Medium</a></li>
<li><a href="https://arxiv.org/abs/2508.05468">TASE: Token Awareness and Structured Evaluation for ... GitHub - MantisAI/nervaluate: Full named-entity (i.e., not ... Demystifying evals for AI agents \ Anthropic Token-level Data Selection for Safe LLM Fine-tuning Evaluating Chunking Strategies for Retrieval | Chroma Evaluation Methods | python-yyds/GPT-NER | DeepWiki</a></li>

</ul>
</details>

**标签**: `#transformers`, `#hybrid models`, `#token-level`, `#AI research`, `#architecture comparison`

---