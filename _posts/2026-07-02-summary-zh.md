---
layout: default
title: "Horizon Summary: 2026-07-02 (ZH)"
date: 2026-07-02
lang: zh
---

> From 34 items, 16 important content pieces were selected

---

1. [PostgreSQL 19 引入 io_uring 内核异步读](#item-1) ⭐️ 9.0/10
2. [crustc：将整个 rustc 编译器翻译为 C 语言](#item-2) ⭐️ 9.0/10
3. [电沉积自组装分子提升钙钛矿光伏性能](#item-3) ⭐️ 9.0/10
4. [弗吉尼亚州禁止出售地理位置数据](#item-4) ⭐️ 8.0/10
5. [Linux 6.9 导致 LUKS 挂起时未擦除加密密钥](#item-5) ⭐️ 8.0/10
6. [Podman v6.0.0 发布，网络能力大幅提升](#item-6) ⭐️ 8.0/10
7. [如何向陌生人有效求助](#item-7) ⭐️ 8.0/10
8. [自托管照片管理应用 Immich 3.0 正式发布](#item-8) ⭐️ 8.0/10
9. [西班牙下令将 Palantir 列入黑名单](#item-9) ⭐️ 8.0/10
10. [谷歌开源零知识证明技术，推动隐私年龄验证](#item-10) ⭐️ 8.0/10
11. [Hanami 3.0 与 Hanakai 项目宣布](#item-11) ⭐️ 8.0/10
12. [PeerTube：去中心化视频平台，挑战 YouTube](#item-12) ⭐️ 7.0/10
13. [JavaScript ECS 与 OOP 内存访问对比分析](#item-13) ⭐️ 7.0/10
14. [防止认证令牌被盗的方法探讨](#item-14) ⭐️ 7.0/10
15. [新型 PamStealer macOS 恶意软件采用高级隐蔽技术](#item-15) ⭐️ 7.0/10
16. [美国国家科学院新院长承诺加倍投入研究](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [PostgreSQL 19 引入 io_uring 内核异步读](https://dev.to/franckpachot/iouring-buffered-reads-in-postgresql-19-iouring-mcn) ⭐️ 9.0/10

PostgreSQL 19 开始支持使用 Linux 内核的 io_uring 接口进行异步读操作，取代传统的同步或 AIO 方式。 这将显著提升数据库的 I/O 效率，特别是高并发场景下的读取性能，减少系统调用开销和上下文切换。 io_uring 通过共享内存环在用户态和内核态之间高效传递 I/O 请求和完成事件，PostgreSQL 19 利用它实现了真正的内核级异步缓冲读取。

rss · Lobsters · Jul 2, 12:46

**背景**: io_uring 是 Linux 5.1 引入的高性能异步 I/O 框架，解决了传统 read/write 和 AIO 接口的性能瓶颈。传统方式需要频繁系统调用，而 io_uring 支持批量提交和完成，大幅降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io_uring - Wikipedia</a></li>
<li><a href="https://man7.org/linux/man-pages/man7/io_uring.7.html">io_uring (7) — Linux manual page</a></li>
<li><a href="https://deepwiki.com/torvalds/linux/5.1-io_uring-asynchronous-io">io_uring Asynchronous I/O | torvalds/linux | DeepWiki</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#io_uring`, `#async I/O`, `#databases`, `#Linux kernel`

---

<a id="item-2"></a>
## [crustc：将整个 rustc 编译器翻译为 C 语言](https://github.com/FractalFir/crustc) ⭐️ 9.0/10

FractalFir 的 crustc 项目成功将 Rust 编译器 rustc 的全部源码翻译成了 C 语言代码。这是一个将 Rust 编译器完整移植到 C 的开源实现。 该项目可能显著提升 Rust 编译器的可移植性，使得 rustc 能在更多平台（包括缺乏 Rust 原生支持的平台）上自举，对 Rust 生态的跨平台发展有重要价值。 翻译工作覆盖了 rustc 的完整代码库，生成的 C 代码旨在保持与原 Rust 编译器的行为一致。该项目开源在 GitHub 上，供社区进一步验证和改进。

rss · Lobsters · Jul 2, 23:19

**背景**: rustc 是 Rust 编程语言的官方编译器，通常使用 Rust 自身编写，因此需要已有的 Rust 编译器来编译新版本（即自举）。将 rustc 翻译为 C 可以打破这种依赖，让 Rust 在尚未有 Rust 编译器的新平台上也能构建。

**标签**: `#rust`, `#compiler`, `#translation`, `#C`

---

<a id="item-3"></a>
## [电沉积自组装分子提升钙钛矿光伏性能](https://www.nature.com/articles/s41586-026-10844-6) ⭐️ 9.0/10

一项发表在《自然》杂志上的研究提出，通过电沉积方法制备自组装分子（SAMs），能够显著提升钙钛矿太阳能电池的性能和稳定性。 该方法解决了 SAMs 在钙钛矿光伏中容易脱离和钝化效果不足的关键问题，有望推动钙钛矿太阳能电池的商业化进程并降低制造成本。 该研究针对传统涂覆法导致的 SAMs 分布不均和附着力差等挑战，利用电沉积技术实现了更均匀、更牢固的 SAMs 层，从而增强了界面钝化效果。

rss · Nature · Jul 2, 00:00

**背景**: 自组装分子（SAMs）是钙钛矿太阳能电池中常用的界面修饰材料，可减少缺陷并提高效率。电沉积作为一种可控的薄膜制备技术，相比传统溶液涂覆能提供更好的均匀性和附着力，近年来在光伏领域受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onlinelibrary.wiley.com/doi/full/10.1002/ifm2.8">Self-assembled monolayers for perovskite solar cells</a></li>

</ul>
</details>

**标签**: `#perovskite photovoltaics`, `#electrodeposition`, `#self-assembled molecules`, `#solar energy`, `#materials science`

---

<a id="item-4"></a>
## [弗吉尼亚州禁止出售地理位置数据](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) ⭐️ 8.0/10

弗吉尼亚州通过立法禁止出售地理位置数据，这是美国各州在隐私保护领域的一项重要举措，主要针对数据经纪人买卖消费者位置信息的行为。 该法律能有效防止地理位置数据被滥用于追踪敏感行为（如访问医疗机构）或影响保险定价，对消费者隐私保护具有里程碑意义，可能推动其他州跟进类似立法。 法律明确禁止数据经纪人出售地理位置数据，但执法面临跨州公司管辖权等挑战，例如在特拉华州注册但在弗吉尼亚州收集数据的公司可能难以监管。

hackernews · toomuchtodo · Jul 2, 21:03 · [社区讨论](https://news.ycombinator.com/item?id=48767347)

**背景**: 地理位置数据指能够定位设备或个人的信息，数据经纪人专门从公开记录或私有渠道收集并出售此类数据。美国联邦层面缺乏统一隐私法规，各州正自行立法填补空白，弗吉尼亚州此法案是继加州之后的重要尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_broker">Data broker</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geolocation_database">Geolocation database</a></li>

</ul>
</details>

**社区讨论**: 评论中多数支持该法律，但担忧执行难度；同时引用实际案例说明地理位置数据被用于反堕胎广告和车险定价等滥用行为，强调立法需有真正效力。

**标签**: `#privacy`, `#geolocation`, `#legislation`, `#data protection`, `#Virginia`

---

<a id="item-5"></a>
## [Linux 6.9 导致 LUKS 挂起时未擦除加密密钥](https://mathstodon.xyz/@iblech/116769502749142438) ⭐️ 8.0/10

自 Linux 6.9 内核版本以来，`cryptsetup luksSuspend` 操作在挂起时不再从内存中擦除磁盘加密主密钥，导致加密密钥在挂起后仍然保留在内存中。这是一个安全回归漏洞。 该漏洞破坏了 LUKS 磁盘加密的核心安全假设，即挂起时应清除密钥以防止物理访问攻击。影响所有使用 LUKS 并依赖 `luksSuspend` 保护密钥的用户，特别是使用 Debian 等发行版中已集成该功能的系统。 该回归影响 Linux 6.9 及后续内核版本，但可能仅直接影响那些集成 `luksSuspend` 的发行版（如 Debian 的 `debian-luks-suspend` 脚本）。 `cryptsetup` 的 `luksSuspend` 本应在挂起前擦除密钥，但内核变更导致该行为失效。

hackernews · Lobsters · Jul 2, 15:25 · [社区讨论](https://news.ycombinator.com/item?id=48763035)

**背景**: LUKS (Linux Unified Key Setup) 是 Linux 上常用的磁盘加密标准，使用主密钥加密数据。 `luksSuspend` 命令用于临时挂起加密设备，它会将主密钥从内存中清除并阻止 I/O 操作，从而在系统挂起（待机）时保护密钥。该功能通常由发行版通过脚本在系统挂起前自动调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.man7.org/linux//man-pages/man8/cryptsetup-luksSuspend.8.html">cryptsetup-luksSuspend (8) - Linux manual page - man7.org</a></li>
<li><a href="https://man.archlinux.org/man/core/cryptsetup/cryptsetup-luksSuspend.8.en">cryptsetup-luksSuspend (8) — Arch manual pages</a></li>
<li><a href="https://github.com/nailfarmer/debian-luks-suspend/">GitHub - nailfarmer/debian-luks-suspend: Lock encrypted root ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有用户指出该回归可能仅影响 Debian 等集成了 `luksSuspend` 的发行版，并非内核官方支持的功能，标题有误导性。其他用户指出挂起后无需重新输入密码本身就说明密钥仍在内存中，而部分用户认为只要在出售设备时擦除数据，该漏洞影响不大。总体来看，社区对漏洞严重性存在分歧，但普遍认为这是一个难以发现的安全回归。

**标签**: `#linux`, `#security`, `#luks`, `#encryption`, `#kernel`

---

<a id="item-6"></a>
## [Podman v6.0.0 发布，网络能力大幅提升](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 8.0/10

Podman v6.0.0 版本正式发布，带来了新的网络功能和多项改进，进一步增强了其作为容器运行时的竞争力。 Podman 作为 Docker 的主要竞争对手，其重大版本更新对容器生态系统具有重要意义，尤其是网络能力的提升有助于吸引更多用户从 Docker 迁移，推动无守护进程架构的普及。 新版本在网络方面有显著增强，但社区用户指出 Podman 在与 Docker 的兼容性上仍存在细微差异，可能导致某些 compose 文件或项目出现问题。

hackernews · soheilpro · Jul 2, 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48762098)

**背景**: Podman 是一个无守护进程的容器运行时，与依赖中央守护进程的 Docker 不同，它通过直接与容器运行时交互来提高安全性和效率。Podman 支持 rootless 容器和 systemd 集成，最近还引入了 Quadlet 功能，可以像 systemd 服务一样管理容器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/devops/what-is-a-podman-container/">What is a Podman Container ? - GeeksforGeeks</a></li>
<li><a href="https://linuxize.com/post/podman-vs-docker/">Podman vs Docker: Differences and Migration Guide - Linuxize</a></li>
<li><a href="https://devops-daily.com/comparisons/podman-vs-docker">Podman vs Docker: Feature Comparison, Pros/Cons, and Verdict</a></li>

</ul>
</details>

**社区讨论**: 社区总体对 Podman 持正面态度，许多用户称赞其易用性和无守护进程架构，例如有用户表示从 Docker 切换到 Podman 完全无痛。但也有用户提醒与 Docker 的兼容性并非完美，项目维护者可能会收到因 Podman 差异导致的投诉。

**标签**: `#podman`, `#containers`, `#devops`, `#open-source`, `#docker-competitor`

---

<a id="item-7"></a>
## [如何向陌生人有效求助](https://pradyuprasad.com/writings/how-to-ask-for-help/) ⭐️ 8.0/10

作者 Pradyut Prasad 发表了一篇实用指南，详细阐述了如何向不认识的人请求帮助，核心方法包括展示事先努力、保持简洁以及准确评估他人帮忙的意愿。 这篇文章对于软件工程师及其他专业人士来说极具价值，因为它提供了具体可操作的沟通策略，能够提高求助成功率，从而促进职业发展和知识交流。 文中强调“事先努力”不在于花费大量时间，而在于针对性地展示你已尽力自行解决问题；同时，求助者往往高估或低估他人被请求的频率，需要对求助目标群体的意愿有更准确的认识。

hackernews · FigurativeVoid · Jul 2, 13:19 · [社区讨论](https://news.ycombinator.com/item?id=48761118)

**背景**: 在职场或开源社区中，向陌生人寻求帮助是常见需求，但很多人因为请求方式不当而被忽视。这篇文章基于作者的经验和社区讨论，提炼出几条关键原则，帮助读者更有效地获得支持。

**社区讨论**: 评论区中，用户 jackconsidine 分享了自己的教训：第一次花费很多时间手写感谢信却没有回应，第二次简短邮件反而有效。FinnLobsien 强调展现自己正在努力解决问题的态度比措辞更重要。shalmanese 指出人们对他人帮助意愿的估算经常偏差几个数量级。Aurornis 补充说，事先努力需要深入而非表面化，比如不能只靠单篇博客或 AI 生成代码来装点门面。

**标签**: `#professional-advice`, `#communication`, `#hacker-news`, `#career`, `#networking`

---

<a id="item-8"></a>
## [自托管照片管理应用 Immich 3.0 正式发布](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

Immich 3.0 版本已正式发布，这是一款自托管的 Google Photos 和 Apple Photos 替代品，受到了社区的广泛关注和讨论。 此版本标志着该项目的重大里程碑，对于注重隐私和希望完全控制自己照片数据的用户来说，Immich 提供了一个强大的开源解决方案。 虽然具体更新细节未在公告中详细列出，但社区讨论表明用户对新版本的性能、功能改进以及 iOS 照片同步问题修复充满期待。

hackernews · hashier · Jul 2, 14:13 · [社区讨论](https://news.ycombinator.com/item?id=48761944)

**背景**: Immich 是一个开源的、自托管的照片和视频备份解决方案，允许用户在自己的服务器上管理媒体文件，无需依赖第三方云服务。它提供类似 Google Photos 的浏览、搜索和组织功能，同时确保用户隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://immich.app/">Immich</a></li>
<li><a href="https://grokipedia.com/page/Immich">Immich</a></li>

</ul>
</details>

**社区讨论**: 社区评论整体积极，多数用户称赞 Immich 是 Google Photos 的理想替代品，并分享了使用体验。部分用户提到 iOS 同步问题曾是痛点，希望新版本有所改善；也有用户出于加密考虑选择了其他方案如 Ente，但仍认可 Immich 的价值。

**标签**: `#self-hosting`, `#photo management`, `#privacy`, `#open-source`, `#immich`

---

<a id="item-9"></a>
## [西班牙下令将 Palantir 列入黑名单](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv) ⭐️ 8.0/10

西班牙政府下令将美国科技巨头 Palantir 列入黑名单，禁止公共和私营公司与其合作。该决定引发了对数据安全和政治动机的广泛讨论。 此举反映了欧洲国家加强技术主权和数据隐私保护的趋势，可能影响其他国家的类似决策。Palantir 曾因涉及监控和隐私争议而备受批评，西班牙的行动可能重塑欧美科技合作格局。 黑名单的具体实施细节尚未公布，但表明西班牙正逐步减少对外国科技公司的依赖。Palantir 的主要产品包括 Gotham 和 Foundry，用于政府情报和企业数据分析。

hackernews · mgh2 · Jul 2, 15:02 · [社区讨论](https://news.ycombinator.com/item?id=48762725)

**背景**: Palantir Technologies 是一家美国上市公司，由彼得·蒂尔等人创立，专注于数据集成和分析软件。其客户包括美国国防部、警察部门以及多家企业。Palantir 因其在政府监控和预测性警务中的作用而受到批评。技术主权是指国家自主掌握关键技术的政治理念，欧洲多国正在推动这一议程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Palantir">Palantir</a></li>
<li><a href="https://en.wikipedia.org/wiki/Technological_sovereignty">Technological sovereignty - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，部分用户表示赞赏（如 milanito1985 认为西班牙方向正确，_ink_考虑移居），但也有质疑（如 Dibby053 怀疑动机是贿赂而非安全），同时有用户支持各国效仿（localdeclan）或强烈反对 Palantir（madhacker）。整体情绪复杂，观点分化。

**标签**: `#Palantir`, `#Spain`, `#data privacy`, `#tech sovereignty`, `#government contracts`

---

<a id="item-10"></a>
## [谷歌开源零知识证明技术，推动隐私年龄验证](https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/) ⭐️ 8.0/10

谷歌宣布开放其零知识证明（ZKP）技术，旨在实现隐私保护的年龄验证方案。该技术允许用户在证明年龄达标的同时不泄露具体生日或其他个人信息。 此举有望平衡日益严格的年龄验证法规与用户隐私保护需求，为在线年龄验证提供一种更安全、更具隐私性的替代方案，对社交媒体、成人内容网站等需年龄验证的平台影响深远。 谷歌开放的 ZKP 技术基于非交互式零知识证明，无需反复交互即可完成验证，降低延迟。该方案可集成至现有年龄保证系统，支持移动端 API 调用，但需依赖可信设置环节。

rss · Lobsters · Jul 2, 13:31

**背景**: 零知识证明是一种密码学协议，允许一方（证明者）向另一方（验证者）证明某个断言为真，而不泄露任何额外信息。年龄保证技术通常通过身份证扫描或面部年龄估计等方式实现，但这些方法常涉及隐私泄露风险。谷歌此次开源旨在推广更安全的认证方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>
<li><a href="https://en.wikipedia.org/wiki/Age_assurance">Age assurance</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#privacy`, `#age assurance`, `#cryptography`

---

<a id="item-11"></a>
## [Hanami 3.0 与 Hanakai 项目宣布](https://www.bounga.org/ruby/2026/07/03/hanakai-and-hanami-3-0/) ⭐️ 8.0/10

Hanami 3.0 正式发布，同时 Dry 和 Rom 项目合并为新的 Hanakai 项目，标志着 Ruby 生态系统的一次重大整合。 Hanami 3.0 作为全栈 Ruby 框架的重大版本更新，有望提升开发者生产力和应用性能；Hanakai 项目整合了三个成熟工具库，将进一步简化 Ruby 应用开发。 Hanami 框架以低内存消耗（比其他框架少 60%）和快速响应著称，Hanakai 项目旨在提供更一致、更易维护的开发体验。

rss · Lobsters · Jul 2, 22:22

**背景**: Hanami 是一个全栈 Ruby Web 框架，强调简洁、可维护性和性能。Dry 和 Rom 是 Ruby 社区中分别用于应用架构和数据映射的流行库。三者的合并形成了 Hanakai 项目，统一了工具链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/hanami/hanami">GitHub - hanami/hanami: A flexible framework for maintainable ...</a></li>
<li><a href="https://hanakai.org/blog/2026/05/01/welcome-to-hanakai">Welcome to Hanakai · Hanakai</a></li>
<li><a href="https://hanakai.org/hanami">Hanami · Hanakai</a></li>

</ul>
</details>

**标签**: `#Ruby`, `#Hanami`, `#web framework`, `#release`

---

<a id="item-12"></a>
## [PeerTube：去中心化视频平台，挑战 YouTube](https://github.com/Chocobozzz/PeerTube) ⭐️ 7.0/10

PeerTube 是一个基于 ActivityPub 协议的去中心化、联邦式视频平台，由法国非营利组织 Framasoft 支持开发，旨在替代 YouTube 等集中式视频托管服务。 PeerTube 为内容创作者和观众提供了不依赖单一商业实体的视频分享方式，有助于保护隐私和避免算法操控，但其缺乏盈利模式限制了主流创作者迁移。 PeerTube 利用 WebTorrent 实现 P2P 传输，当视频流行时可减轻服务器负载；作为 Fediverse 的一部分，它可以与 Mastodon 等其他联邦平台互操作。

hackernews · doener · Jul 2, 11:17 · [社区讨论](https://news.ycombinator.com/item?id=48759634)

**背景**: PeerTube 自 2017 年由开发者 Chocobozzz 发起，现由法国非营利组织 Framasoft 维护。它采用 ActivityPub 协议，使不同实例之间可以互相订阅和发现内容，形成联邦式网络。与 YouTube 不同，PeerTube 没有中心化服务器或推荐算法，实例由社区自行托管和审核。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PeerTube">PeerTube - Wikipedia</a></li>
<li><a href="https://github.com/Chocobozzz/PeerTube">GitHub - Chocobozzz/PeerTube: ActivityPub-federated video streaming platform using P2P directly in your web browser · GitHub</a></li>
<li><a href="https://joinpeertube.org/">What is PeerTube ? | JoinPeerTube</a></li>

</ul>
</details>

**社区讨论**: 评论中，专业 YouTuber 指出缺乏盈利模式是最大障碍，因为制作高质量视频成本高昂；其他用户认为 PeerTube 目前内容和受众不足，仅适合开源或隐私相关话题；也有用户表示对于开源项目教程，使用现有实例嵌入视频已足够。总体来看，技术可行但社会采用面临挑战。

**标签**: `#decentralization`, `#federation`, `#open source`, `#video hosting`, `#content creation`

---

<a id="item-13"></a>
## [JavaScript ECS 与 OOP 内存访问对比分析](https://www.dmurph.com/posts/2026/06/ecs_vs_oop_benchmark/ecs_vs_oop_benchmark.html) ⭐️ 7.0/10

文章通过基准测试，深入分析了 JavaScript 中 Entity Component System（ECS）与面向对象编程（OOP）的内存访问模式差异，探讨了 ECS 在 JavaScript 中实现的可行性。 该分析挑战了 JavaScript 不适合高性能数据导向设计的传统观念，为游戏开发、大型应用等场景提供了新的性能优化思路，可能推动 ECS 模式在 JavaScript 生态中的采用。 文章可能详细比较了 ECS 下组件的连续内存布局与 OOP 中对象的分散内存分配，并考察了 V8 引擎等 JavaScript 运行时的内存管理特性对 ECS 效能的限制与机遇。

rss · Lobsters · Jul 2, 04:23

**背景**: Entity Component System（ECS）是一种数据导向的设计模式，它将实体（Entity）视为仅包含 ID 的容器，组件（Component）为纯数据，系统（System）负责处理逻辑。与 OOP 将数据和逻辑封装在对象中不同，ECS 通过将同类组件连续存储来提高缓存命中率，从而提升性能。在 JavaScript 中实现 ECS 面临其动态类型和垃圾回收机制难以控制内存布局的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Entity_component_system">Entity component system - Wikipedia</a></li>
<li><a href="https://pancy.medium.com/entity-component-system-ecs-in-a-frame-and-javascript-f5b7cdba7248">Entity - Component - System ( ECS ) in A-Frame and JavaScript | Medium</a></li>

</ul>
</details>

**标签**: `#ECS`, `#JavaScript`, `#memory`, `#performance`, `#programming`

---

<a id="item-14"></a>
## [防止认证令牌被盗的方法探讨](https://codon.org.uk/~mjg59/blog/p/preventing-token-theft/) ⭐️ 7.0/10

一篇来自资深安全研究员的博客文章，详细讨论了防止认证令牌被盗的多种方法，并引用了社区讨论。 令牌盗窃是绕过 MFA 的常见攻击手段，该文提出的防御措施对于提升 Web 应用安全性具有重要参考价值。 文章可能涵盖了令牌绑定（Token Binding）等技术，该技术将令牌与 TLS 连接绑定，防止令牌被窃取后重放。

rss · Lobsters · Jul 2, 11:02

**背景**: 令牌（Token）是用户登录后系统颁发的凭证，用于后续请求的身份验证。令牌盗窃指攻击者窃取令牌并冒充用户，即使有 MFA 也可能被绕过。令牌绑定是一种通过加密方式将令牌与客户端-服务器 TLS 通道绑定的协议，使被盗令牌在其他连接中无效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.obsidiansecurity.com/blog/token-based-attacks-how-attackers-bypass-mfa">Token-Based Attacks: How Attackers Bypass MFA</a></li>
<li><a href="https://www.kaseya.com/blog/what-is-token-theft/">What is token theft? - Kaseya</a></li>
<li><a href="https://en.wikipedia.org/wiki/Token_Binding">Token Binding</a></li>

</ul>
</details>

**标签**: `#security`, `#token`, `#authentication`, `#best practices`

---

<a id="item-15"></a>
## [新型 PamStealer macOS 恶意软件采用高级隐蔽技术](https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/) ⭐️ 7.0/10

研究人员发现了一种名为 PamStealer 的新型 macOS 恶意软件，它利用 Pluggable Authentication Modules (PAM) 接口在窃取登录密码前进行本地验证，并采用自包含的 JXA dropper 和 Rust 编写的第二阶段载荷。 这一发现对 macOS 安全领域具有重要意义，因为 PamStealer 展示了更高级的隐蔽技术和攻击流程，可能被其他恶意软件作者效仿，从而增加 Mac 用户的感染风险。 PamStealer 通过恶意脚本（.scpt）和脚本编辑器诱饵传播，其独特之处在于使用 PAM 验证密码的正确性后才进行窃取，从而避免触发警报；整个攻击链包括 JXA dropper 和 Rust 编写的载荷，体现了模块化和隐蔽性设计。

rss · Lobsters · Jul 2, 20:16

**背景**: PAM 是 macOS 中用于身份验证的底层框架，允许应用程序验证用户密码。近年来，macOS 恶意软件数量增长，攻击者不断开发新技术绕过安全机制。PamStealer 的出现标志着 macOS 信息窃取恶意软件的发展进入了新阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/">Newly discovered PamStealer isn’t your typical macOS malware</a></li>
<li><a href="https://www.idropnews.com/news/pamstealer-macos-malware-password-verification/265878/">New PamStealer Mac Malware Pre-verifies Stolen Passwords</a></li>

</ul>
</details>

**标签**: `#macOS`, `#malware`, `#cybersecurity`, `#stealth`

---

<a id="item-16"></a>
## [美国国家科学院新院长承诺加倍投入研究](https://www.nature.com/articles/d41586-026-02088-1) ⭐️ 7.0/10

美国国家科学院新任院长尼尔·舒宾(Neil Shubin)于 2026 年 7 月 2 日通过《自然》杂志发表声明，强调将继续大力支持科学研究，并警告忽视科学将导致社会失去未来。 这一表态体现了美国国家科学院对研究投入的坚定承诺，对全球科技政策和研究方向可能产生导向性影响，尤其在当前国际科技竞争加剧的背景下，其立场有助于稳定科研人员和机构的预期。 舒宾在声明中指出“一个丢失科学的社会将丢失未来”，但未公布具体的政策变革或新倡议。该消息发布于 2026 年 7 月 2 日，来源为《自然》杂志。

rss · Nature · Jul 2, 00:00

**背景**: 美国国家科学院是美国科学界最高荣誉机构之一，其主席的发言通常代表科学界对政策的主流看法。舒宾是一位古生物学家，在学界享有声誉，他的上任可能影响未来美国科研经费分配和科学教育方向。

**标签**: `#science policy`, `#National Academy of Sciences`, `#research funding`, `#leadership`

---