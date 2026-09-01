---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> From 34 items, 13 important content pieces were selected

---

1. [任意用户进程可提权至 root 的严重漏洞](#item-1) ⭐️ 9.0/10
2. [谷歌已从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](#item-2) ⭐️ 8.0/10
3. [AI 时代最安全的工作或许是写作](#item-3) ⭐️ 8.0/10
4. [curl 维护者公开讨论 CVE 认定分歧](#item-4) ⭐️ 8.0/10
5. [利用 AD CS RPC 端点从 IIS AppPool 提权至 SYSTEM](#item-5) ⭐️ 8.0/10
6. [安防摄像头变身自动鸟类识别系统](#item-6) ⭐️ 7.0/10
7. [ChatGPT Work 工具与技能参考站点上线](#item-7) ⭐️ 7.0/10
8. [NAT 是否是互联网中心化的“原罪”？](#item-8) ⭐️ 7.0/10
9. [AI 播客：Gemini 3.7 Flash、Jalapeño 芯片与无人机袭击](#item-9) ⭐️ 7.0/10
10. [可引导构建：原理与意义解析](#item-10) ⭐️ 7.0/10
11. [Kale：一种转换安全的电子表格系统](#item-11) ⭐️ 7.0/10
12. [Cargo 调度器性能改进探讨](#item-12) ⭐️ 7.0/10
13. [Rootless Docker 及其隐藏的安全权衡](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [任意用户进程可提权至 root 的严重漏洞](https://www.vesto.me/2026/08/31/any-process-escalate-root.html) ⭐️ 9.0/10

一篇安全披露报告指出，存在一种漏洞可让任意用户进程将权限提升至 root。该消息在 Lobsters 上引发讨论，但目前披露中未提供具体技术细节。 此漏洞影响系统安全根基，任何本地用户都可能借此获得完全控制权，属于严重级别的安全事件。企业和开发者应密切关注官方补丁或缓解措施。 消息源仅给出链接指向 Lobsters 评论，未包含漏洞的详细技术分析。目前尚未明确受影响的系统或软件版本，需等待进一步披露。

rss · Lobsters · Aug 31, 13:46

**背景**: 权限提升（privilege escalation）是攻击者从低权限账户获取更高权限的过程，root 是 Unix/Linux 系统中的超级管理员账户。此类漏洞一旦被利用，攻击者可完全控制系统，因此通常被视为最高危的安全问题。

**标签**: `#security`, `#vulnerability`, `#privilege escalation`, `#root`

---

<a id="item-2"></a>
## [谷歌已从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已按计划从 Chrome 网上应用店移除所有 Manifest V2（MV2）扩展，包括广受欢迎的广告拦截器 uBlock Origin。这一变化意味着这些扩展无法再被新用户安装，已安装用户也收不到更新。 这影响数百万依赖广告拦截的用户，尤其是那些需要保护自己免受恶意广告侵害的普通用户。许多用户因此考虑转向 Firefox 或其他浏览器，也引发了对谷歌在浏览器市场垄断地位的讨论。 根据谷歌的时间表，2026 年 7 月 8 日所有剩余 MV2 扩展将从商店移除，但在 Chrome 138 或更早版本上已安装的 MV2 扩展仍保留但无法更新。MV3 移除了实时请求检查能力并限制了规则数量，从而削弱了广告拦截器的功能。

hackernews · twapi · Aug 31, 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V2 是 Chrome 扩展的旧版规范，允许扩展拥有长期运行的后台页面和强大的网络请求拦截能力。Manifest V3 是谷歌推出的新版规范，旨在提高扩展的安全性、隐私性和性能，但限制了广告拦截等功能的实现方式。uBlock Origin 因依赖 MV2 的 API 而无法在 MV3 下提供同等保护，其开发者推出了功能受限的 uBlock Origin Lite。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
<li><a href="https://factually.co/fact-checks/technology/manifest-v3-ad-blockers-ublock-origin-brave-firefox-2026-4d29ee">How Manifest V 3 Changed Ad Blockers: uBlock Origin, Br...</a></li>

</ul>
</details>

**社区讨论**: 评论普遍表达了对谷歌此举的不满和对 Firefox 的支持。用户 beloch 指出广告拦截已变成安全问题，因为恶意广告可能诱骗年老用户安装流氓软件；Night_Thastus 表示将继续使用 Firefox，反对谷歌对互联网的单方面控制；还有用户回忆 Chrome 曾获得赞誉，但现在推荐大家使用 Firefox。

**标签**: `#Chrome`, `#Extensions`, `#Ad Blocking`, `#uBlock Origin`, `#Manifest V3`

---

<a id="item-3"></a>
## [AI 时代最安全的工作或许是写作](http://muratbuffalo.blogspot.com/2026/08/the-safest-job-from-ai-may-be-writing.html) ⭐️ 8.0/10

Muratbuffalo 博客发表文章称，写作可能是最不受 AI 影响的工作，因为熟练写作需要 LLM 所缺乏的意图性。该观点引发激烈讨论，文章获得 138 条评论，社区反响热烈。 这一论点挑战了 AI 将全面取代创意工作的普遍假设，并促使人们重新审视 AI 对写作行业就业的真实影响。对记者、翻译、技术写作者等文字工作者而言，这关乎他们的职业前景与生存压力。 讨论中出现了不少反例，指出 LLM 虽无法媲美顶级人类写作，但足以胜任大量低端文字工作，包括新闻、翻译、企业通讯和校对等。作者强调的“意图性”成为争论焦点，许多人认为这种高标准在现实商业环境中并不被市场优先考虑。

hackernews · ilreb · Aug 31, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=49512856)

**背景**: 大型语言模型（LLM）是经过海量文本训练的人工智能模型，能够生成、总结、翻译和分析文本。这类模型的输出本质上是基于统计概率的词语组合，而非出于人类那样的表达意图。正因如此，一些人认为写作中的刻意选词、复杂思想和细腻表达是 AI 难以复制的，但这也并不能保证所有写作岗位都安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论区的观点分歧明显。有人强烈反驳，认为无关 LLM 能否写出顶级文字，关键在于普通写作工作（如新闻、翻译、技术写作）才是多数人糊口的来源，而 AI 正在夺走这些岗位。也有评论者认同作者的核心逻辑，指出 LLM 缺乏意图性，人类在表达细微差别时仍有优势，但市场需求并不总是为这种差异买单。

**标签**: `#AI`, `#writing`, `#LLMs`, `#future of work`, `#job market`

---

<a id="item-4"></a>
## [curl 维护者公开讨论 CVE 认定分歧](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/) ⭐️ 8.0/10

curl 项目维护者 Daniel Stenberg 在 2026 年 6 月 24 日发表了一篇题为“a CVE dispute”的博客文章，公开讨论了一起与 CVE（通用漏洞披露）相关的争议。文章主要围绕漏洞处理方式和技术判断上的分歧展开，并附有指向 Lobsters 评论区讨论的链接。 这一讨论折射出开源安全生态中 CVE 编号认定、报告流程和修复责任等常见矛盾。由于 curl 被全球数百万开发者和软件项目广泛依赖，此类争议的处理方式和最终结论可能影响大量下游用户对安全公告的信任与响应策略。 博客正文内容较为简短，仅包含指向 Lobsters 评论区的链接，具体争议的技术细节未在摘要中展开。从标题和摘要可以推断，分歧可能涉及漏洞严重性评估、披露时机或协调流程等技术判断问题。

rss · Lobsters · Aug 31, 10:38

**背景**: curl 是一个广泛使用的开源命令行工具和库，用于通过 URL 传输数据，几乎所有主流操作系统和编程环境都内置或依赖它。CVE（Common Vulnerabilities and Exposures）是公开披露安全漏洞的标准化编号体系，维护者与安全研究者之间常因漏洞是否构成实际风险、严重性评分或披露时间表产生分歧，这类“CVE 争议”在开源社区中并不罕见。

**标签**: `#curl`, `#security`, `#CVE`, `#open-source`, `#vulnerabilities`

---

<a id="item-5"></a>
## [利用 AD CS RPC 端点从 IIS AppPool 提权至 SYSTEM](https://www.mannulinux.org/2026/08/Privilege-escalation-from-IIS-AppPool-to-NT-AuthoritySYSTEM-via-AD-CS-RPC-endpoint.html) ⭐️ 8.0/10

这篇文章提出了一种通过 Active Directory 证书服务（AD CS）的 RPC 端点实现权限提升的新方法，使攻击者能够从 IIS AppPool 账户直接提升至 NT Authority/SYSTEM 权限。 该攻击路径为 Web 应用初始访问提供了通向系统最高权限的捷径，对 Windows 服务器的安全评估和 AD CS 加固具有重要参考价值，可能影响大量使用 IIS 和 AD CS 的企业环境。 攻击很可能利用了 IIS AppPool 默认具备的 SeImpersonatePrivilege 权限，并结合 AD CS RPC 接口中的特定操作来窃取或模拟 SYSTEM 令牌。文章可能提供了详细的步骤或概念验证代码，但具体利用的 RPC 方法尚需阅读原文确认。

rss · Lobsters · Aug 31, 12:36

**背景**: IIS AppPool 是 IIS Web 服务器中隔离 Web 应用的进程池，通常以低权限账户（如 IIS APPPOOL\DefaultAppPool）运行，但常被授予 SeImpersonatePrivilege 等特权。Active Directory 证书服务（AD CS）是 Windows Server 中负责颁发和管理数字证书的角色，其 RPC 端点用于证书注册、续订等管理操作。此前已有多个利用 AD CS 的已知攻击（如 PetitPotam 和 ESC 系列），本文探索了通过其 RPC 端点进行本地提权的新路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://petitpotam.com/systems-and-services-vulnerable-to-petitpotam-exploitation/">Systems and Services Vulnerable to PetitPotam Exploitation</a></li>
<li><a href="https://www.hackingarticles.in/windows-privilege-escalation-seimpersonateprivilege/">Windows Privilege Escalation: SeImpersonate Privilege</a></li>

</ul>
</details>

**标签**: `#security`, `#privilege-escalation`, `#IIS`, `#AD-CS`, `#Windows`

---

<a id="item-6"></a>
## [安防摄像头变身自动鸟类识别系统](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 7.0/10

一位博主撰文介绍如何借助 BirdNET-Go，将现有安防摄像头改造成自动鸟类识别系统。该系统利用摄像头自带的音频流进行实时鸟声识别，并已在社区引发广泛讨论和实践。 这一项目展示了将人工智能技术与现有智能家居硬件结合的可行路径，降低了鸟类监测和公民科学参与的门槛。对鸟类爱好者、DIY 爱好者和生态研究者而言，它提供了一种低成本的自动化监测方案。 技术实现依赖摄像头支持的 RTSP 音视频流，BirdNET-Go 可在树莓派等低功耗设备上本地运行 24/7。需要注意的是，部分摄像头麦克风采样率仅为 16kHz，而 BirdNET 期望 48kHz 音频，画质与音质不佳时可能需要外接麦克风。

hackernews · speckx · Aug 31, 16:47 · [社区讨论](https://news.ycombinator.com/item?id=49511856)

**背景**: BirdNET 是康奈尔大学开发的 AI 鸟声识别工具，可通过鸟鸣识别物种。BirdNET-Go 是其社区驱动的自托管实现，支持本地多模型推理，无需联网即可持续分析环境声音。安防摄像头通常具备网络音频流能力，因此可作为现成的音频采集源，配合 BirdNET-Go 实现无人值守的自动鸟类监测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tphakala/birdnet-go">GitHub - tphakala/birdnet-go: Self-hosted realtime soundscape analyser for birds, bats and other wildlife. Multi-model local AI inference, runs 24/7 on a Raspberry Pi. · GitHub</a></li>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://birdnet.cornell.edu/app/">BirdNET App – Identify Birds by Sound</a></li>

</ul>
</details>

**社区讨论**: 社区反响积极，多位用户分享了相似尝试。例如有用户用 Unifi 门铃摄像头配合 BirdNET-Go 成功运行，也有用户指出 Aqara 摄像头存在风噪和采样率限制，不得不外接麦克风。还有人将系统便携化并加装墨水屏显示统计信息，同时指出了界面渲染的细节问题，整体氛围务实且乐于互助。

**标签**: `#birdnet`, `#security cameras`, `#ai`, `#edge computing`, `#raspberry pi`

---

<a id="item-7"></a>
## [ChatGPT Work 工具与技能参考站点上线](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 7.0/10

一个记录 ChatGPT Work 工具和技能的参考站点上线，重点展示了通过 Playwright 控制浏览器的方法，该方法利用 Node.js REPL 启动浏览器实例并获取操作指令。 该站点为开发者提供了实用的 AI 工具工作流参考，尤其展示了如何将 Playwright 集成到 ChatGPT Work 中，有助于提升自动化效率，也反映了 AI 代理工具生态的快速发展。 最值得注意的技能是控制浏览器，它指示 ChatGPT Work 通过 Node.js REPL 运行`nodeRepl.write(await browser.documentation())`来获取完整的浏览器使用说明。

hackernews · ijidak · Aug 31, 14:07 · [社区讨论](https://news.ycombinator.com/item?id=49510000)

**背景**: ChatGPT Work 是 OpenAI 于 2026 年 7 月推出的 AI 代理，可基于连接的应用和文件创建演示文稿、电子表格等文档。Playwright 是微软开发的开源浏览器自动化库，支持 Chromium、Firefox 和 WebKit，常用于网页测试和抓取。该参考站点将两者结合，展示了 AI 代理如何利用此类工具执行网页操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChatGPT">ChatGPT - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Playwright_(software)">Playwright (software) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论中，simonw 认为最有意思的是控制浏览器的技能，通过 Playwright 和 Node.js REPL 指令实现；darepublic 担心这些工具会降低速度并浪费 token；satvikpendem 质疑它和 Codex 的区别；enraged_camel 则注意到 AI 生成的网站外观有趋同现象。

**标签**: `#ChatGPT Work`, `#AI tools`, `#browser automation`, `#reference`, `#Playwright`

---

<a id="item-8"></a>
## [NAT 是否是互联网中心化的“原罪”？](https://dreamstation.systems/personal/ntppost.html) ⭐️ 7.0/10

一篇题为《互联网中心化与 NAT 的原罪》的文章指出，NAT（网络地址转换）通过削弱个人运行服务器的能力，成为互联网中心化的重要推手。该文在 Hacker News 上引发热议，Linux NAT 实现者 RustyRussell 也参与讨论，并承认自己的设计决策带来了公共端点丧失的后果。 这场讨论揭示了看似中立的 NAT 技术如何悄然改变了互联网的端到端模型，使普通用户从“拥有公共端点的参与者”沦为“只能访问云端的内容消费者”。它对网络中立性、去中心化运动以及 IPv6 的推广具有重要启示，也促使人们重新审视互联网架构设计中的权衡取舍。 RustyRussell 坦言，他在 Linux 中实现的 NAT 系统为了将更多连接挤进单一 IP 地址而避免端口预留，只要远端地址能区分连接即可；这导致来自其他地址的入站流量无法路由，用户不再拥有公共端点。讨论中还区分了普通 NAT 与运营商级 NAT（CGNAT），认为真正的“原罪”是后者，因为它严格限制了被运营商级 NAT（CGNAT）用户的自由。

hackernews · robinpie · Aug 31, 02:23 · [社区讨论](https://news.ycombinator.com/item?id=49504905)

**背景**: NAT（网络地址转换）是一种在数据包传输过程中修改 IP 地址信息的机制，最初用于缓解 IPv4 地址枯竭问题，让大量私有设备共享少量公网 IP。传统互联网设计遵循“端到端原则”，即网络只负责传输，功能由端节点实现；NAT 的出现打破了这一模型，在路由器上引入状态，使得外部无法主动发起连接到内网设备，从而改变了互联网的开放架构。这篇文章正是基于这一背景，将 NAT 视为互联网中心化的早期诱因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Network_address_translation">Network address translation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_principle">End - to - end principle - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论中，RustyRussell 以 NAT 实现者的身份表达了歉意，承认当时只想着解决具体问题而忽略了公共端点的价值；有人感叹 NAT 让“客户端-服务器”模式变得理所当然，成为对开放互联网的挽歌。但也有反驳观点认为普通 NAT 可控且能保护不安全设备，真正的“原罪”是运营商级 NAT（CGNAT）；还有人指出互联网设计者将现实世界的安全假设错误地套用到了网络空间。

**标签**: `#NAT`, `#networking`, `#internet centralization`, `#client-server`, `#IPv4`

---

<a id="item-9"></a>
## [AI 播客：Gemini 3.7 Flash、Jalapeño 芯片与无人机袭击](https://lastweekin.ai/p/lwiai-podcast-255-gemini-37-jalapeno) ⭐️ 7.0/10

本期播客讨论了谷歌发布的 Gemini 3.7 Flash 模型、OpenAI 与博通合作推出的 Jalapeño 推理芯片，以及一起完全由 AI 引导的无人机袭击事件。 Gemini 3.7 Flash 是谷歌最新的高性价比模型，Jalapeño 芯片则代表了 OpenAI 自研硬件的突破，这两者都可能重塑 AI 产业格局；而 AI 自主执行军事行动的事件引发了对伦理与监管的严重关切。 Gemini 3.7 Flash 在文档处理（GDP.pdf 基准 34.0% vs 22.0%）和自动化工作流（AutomationBench 30.4% vs 17.0%）上明显优于前代 3.6 Flash。Jalapeño 是 OpenAI 首款自研推理 ASIC 芯片，功耗约 700W，采用 2,048 芯片的 pod 设计。

rss · Last Week in AI · Aug 31, 08:20

**背景**: Gemini 是 Google DeepMind 开发的多模态大语言模型家族，包含 Pro、Flash 等版本，Flash 系列主打低延迟与高吞吐。Jalapeño 是 OpenAI 与博通联合设计的专用推理加速器，而非通用 GPU，旨在提升推理性能与能效。播客《Last Week in AI》每周汇总 AI 领域的重要新闻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash">Gemini 3.7 Flash | Gemini Enterprise Agent Platform | Google Cloud Documentation</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/openai-s-jalapeno-ai-chip-explained-performance-power-why-it-matters-2026">OpenAI's Jalapeño AI Chip Explained: Performance, Power & Why It...</a></li>

</ul>
</details>

**标签**: `#AI`, `#podcast`, `#Gemini`, `#inference`, `#drones`

---

<a id="item-10"></a>
## [可引导构建：原理与意义解析](https://lwn.net/Articles/1088279/) ⭐️ 7.0/10

LWN 发布了一篇题为《Bootstrappable builds: how and why》的技术文章，系统讲解了可引导构建的动机、方法与意义。这是一篇解释性文章，而非发布新版本或新工具的公告。 可引导构建是软件供应链安全与可复现构建领域的重要议题，能显著降低对预编译工具链的信任依赖。该文章有助于开发者理解和应用可引导构建，从而提升构建过程的可验证性并减少供应链攻击风险。 可引导构建通常通过寻找能用源码构建的旧版本编译器，再逐步编译出新版本编译器来实现。其核心理念是在可复现构建的基础上，进一步确保构建所需的整个工具链都能从源码引导构建，从而缩短信任链。

rss · Lobsters · Aug 31, 17:03

**背景**: 可复现构建是一组软件开发实践，旨在从源代码到二进制代码建立一条可独立验证的路径。可引导构建则将这一理念向前推进一步，要求构建目标二进制时所需的工具也能从源码引导构建，类似于用大量原子搭建房屋。结合独立的、周期性的源码审计，这些方法能有效减少构建流程中被植入后门的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bootstrappable_builds">Bootstrappable builds - Wikipedia</a></li>
<li><a href="https://lwn.net/Articles/841797/">Bootstrappable builds [LWN.net]</a></li>
<li><a href="https://reproducible-builds.org/">Reproducible Builds — a set of software development practices that create an independently-verifiable path from source to binary code</a></li>

</ul>
</details>

**标签**: `#bootstrappable builds`, `#reproducible builds`, `#software supply chain`, `#toolchain`

---

<a id="item-11"></a>
## [Kale：一种转换安全的电子表格系统](https://arxiv.org/abs/2608.26345) ⭐️ 7.0/10

该论文介绍了 Kale，一个通过限制引用类型来消除电子表格中结构变换（如插入、删除或重排行列）所导致公式引用错误的风险的原型系统。论文还描述了一项用户研究，展示了该系统的有效性。 电子表格广泛应用于数据处理，但传统系统中行列操作常使公式引用出错，影响可靠性。Kale 提供了一种确保引用数据在结构变换后仍然正确的机制，对最终用户编程和数据转换领域具有潜在影响。 Kale 的核心安全属性是“通过结构变换保留引用数据”，即当行列被插入、移除或重排时，引用受影响单元格的公式仍指向相同的数据。系统通过限制可表达的引用来实现这一保证，从根源上避免一类常见错误。

rss · Lobsters · Aug 31, 18:32

**背景**: 传统电子表格如 Excel 和 Google Sheets 在行列操作时会自动更新公式引用，但有时会产生非预期结果，导致数据错误。Kale 是来自 Michael Coblenz 等人（共 14 位作者）的研究原型，于 2026 年 8 月 26 日提交至 arXiv，旨在为电子表格提供形式化的安全保障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.26345">[2608.26345] Kale: A Transformation-Safe Spreadsheet System</a></li>
<li><a href="https://arxiv.org/html/2608.26345v1">Kale: A Transformation-Safe Spreadsheet System</a></li>
<li><a href="https://arxivtldr.org/abs/2608.26345">TL;DR: Kale: A Transformation-Safe Spreadsheet System | ArXiv TLDR</a></li>

</ul>
</details>

**标签**: `#spreadsheets`, `#data transformation`, `#programming languages`, `#formal methods`, `#systems`

---

<a id="item-12"></a>
## [Cargo 调度器性能改进探讨](https://spirali.github.io/blog/cargo-scheduler/) ⭐️ 7.0/10

一篇技术博客对 Cargo 的作业调度器进行了深入分析，指出了潜在的改进方向，以提升构建性能。文章引发了关于 Rust 构建系统优化可能性的讨论。 如果调度器得到改进，Rust 项目的编译时间有望显著缩短，尤其对大型项目而言。该分析关注 Rust 生态的核心构建工具，可能影响开发者日常开发效率。 Cargo 使用与 GNU make 类似的 jobserver 协议来协调并发进程，调度策略决定了并行任务的分配效率。博客可能探讨了现有调度算法的局限性，并提出了替代方案。

rss · Lobsters · Aug 31, 10:50

**背景**: Cargo 是 Rust 的官方构建系统和包管理器，负责编译项目并管理依赖。构建过程中，Cargo 会调度多个并行任务来加速编译，而作业调度器（scheduler）决定任务执行的顺序和资源分配。并行任务调度是计算机科学中的经典优化问题，目标是减少总完成时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://packages.ecosyste.ms/registries/crates.io/packages/jobserver">jobserver | crates.io | Ecosyste.ms: Packages</a></li>
<li><a href="https://en.wikipedia.org/wiki/Parallel_task_scheduling">Parallel task scheduling - Wikipedia</a></li>

</ul>
</details>

**标签**: `#rust`, `#cargo`, `#build-systems`, `#scheduling`, `#performance`

---

<a id="item-13"></a>
## [Rootless Docker 及其隐藏的安全权衡](https://www.kenmuse.com/blog/rootless-docker-and-its-hidden-security-trade-offs/) ⭐️ 7.0/10

本文探讨了以 rootless 模式运行 Docker 所带来的安全收益，以及与之相伴的、容易被忽视的权衡取舍。文章还指出了该模式在实际部署中可能遇到的功能限制。 对于 DevOps 和安全工程人员而言，rootless Docker 常被视为降低容器逃逸风险的重要手段，但其在端口绑定、网络模式等方面的限制可能影响生产环境的可用性。理解这些隐藏成本有助于团队在安全与功能性之间做出更明智的决策。 Rootless 模式通过用户命名空间将容器内的非 root 用户映射到宿主机的非特权用户，从而避免 Docker 守护进程以 root 身份运行。该模式下无法绑定 1024 以下的特权端口，且部分网络模式（如 host 网络）和存储驱动受到限制或不可用。

rss · Lobsters · Aug 31, 03:12

**背景**: Docker 传统上要求守护进程以 root 权限运行，容器中 root 用户的权限在宿主机上也具有高权限，增加了安全风险。Rootless 模式利用了 Linux 用户命名空间功能，使容器内的 UID/GID 与宿主机隔离，从而降低提权攻击的可能性。然而，这一机制也引入了性能和兼容性方面的代价，例如需要额外配置和部分功能不可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://liudonghua123.github.io/docker-docs/engine/security/rootless/">Run the Docker daemon as a non-root user ( Rootless mode )</a></li>
<li><a href="https://access.redhat.com/articles/5946151">Understanding user namespaces with rootless containers - Red Hat Customer Portal</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-01-06-docker-rootless-mode/view">How to Run Docker Without Root ( Rootless Mode )</a></li>

</ul>
</details>

**标签**: `#docker`, `#security`, `#containerization`, `#rootless`, `#devops`

---