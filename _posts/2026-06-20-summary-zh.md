---
layout: default
title: "Horizon Summary: 2026-06-20 (ZH)"
date: 2026-06-20
lang: zh
---

> From 29 items, 14 important content pieces were selected

---

1. [Project Valhalla 十年磨一剑：值类型登陆 JDK 28](#item-1) ⭐️ 9.0/10
2. [挪威禁止小学使用人工智能](#item-2) ⭐️ 8.0/10
3. [现代汽车全面收购波士顿动力](#item-3) ⭐️ 8.0/10
4. [业余爱好者用 AI 工具或破译线形文字 A](#item-4) ⭐️ 8.0/10
5. [Godot 4.7 发布：灯光、摄像机、动作](#item-5) ⭐️ 8.0/10
6. [Bevy 0.19 发布，Rust 游戏引擎新版本](#item-6) ⭐️ 8.0/10
7. [SMPTE 宣布免费开放其媒体技术标准库](#item-7) ⭐️ 8.0/10
8. [《毁灭战士》作曲家鲍比·普林斯去世](#item-8) ⭐️ 7.0/10
9. [ATProto 中不存在“实例”概念](#item-9) ⭐️ 7.0/10
10. [Google Workspace 被指阻止 Firefox 访问](#item-10) ⭐️ 7.0/10
11. [法院记录应免费开放](#item-11) ⭐️ 7.0/10
12. [新法案旨在阻止政府施压平台审查合法言论](#item-12) ⭐️ 7.0/10
13. [开源 CAD 内核 Fornjot 宣布关闭](#item-13) ⭐️ 7.0/10
14. [定义 Well-Known URI 的实用指南](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Project Valhalla 十年磨一剑：值类型登陆 JDK 28](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 9.0/10

经过长达十年的研发，Project Valhalla 终于将值类型（Value Types）带到了 JDK 28 中，具体通过 JEP 401 实现。这使得 JVM 能够直接存储值而非对象引用，大幅提升内存密度和性能。 这是 Java/JVM 发展史上的里程碑，标志着 Java 在保持面向对象模型的同时，获得了接近 C 语言的数据处理效率。所有 Java 开发者都能从中受益，尤其是在高性能计算和大数据处理领域。 值类型（内联类）没有对象头，数组可扁平化连续存储，但超过 64 位的值类型在堆扁平化方面存在限制。JDK 28 已提供预览版，实测显示通过值对象优化可获得近 3 倍的加速效果。

hackernews · Lobsters · Jun 19, 06:35 · [社区讨论](https://news.ycombinator.com/item?id=48595511)

**背景**: Project Valhalla 是 OpenJDK 于 2014 年启动的实验性项目，旨在为 Java 引入值类型以解决引用类型的内存和性能开销。值类型类似于 C#中的 struct，但需要与 Java 的泛型系统完全集成。该项目由 Brian Goetz 领导，经历了多次设计调整，最终在 JDK 28 中交付。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://www.baeldung.com/java-valhalla-project">Java Valhalla Project | Baeldung</a></li>
<li><a href="https://inside.java/2025/10/27/try-jep-401-value-classes/">Try Out JEP 401 Value Classes and Objects - Inside.java</a></li>

</ul>
</details>

**社区讨论**: 社区评论中有人质疑文章关于 64 位堆扁平化限制的描述，认为前后矛盾；也有人批评 Java 的 null 处理不够简化，导致模型复杂。但多数评论认可 Valhalla 的价值，并指出 Java 在近年已取得巨大进步，不应以过去的印象评判。

**标签**: `#Java`, `#JVM`, `#Project Valhalla`, `#Value Types`, `#Performance`

---

<a id="item-2"></a>
## [挪威禁止小学使用人工智能](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/) ⭐️ 8.0/10

挪威政府宣布，小学（6 至 13 岁）原则上禁止使用人工智能，初中生（14 至 16 岁）可在教师监督下谨慎使用。 这一政策是首个国家级对 AI 在教育领域的严格限制，可能影响其他国家制定类似法规，并引发关于 AI 对儿童学习影响的讨论。 禁令覆盖 1 至 7 年级（6-13 岁），作为一般规则不鼓励使用 AI；8 至 10 年级（14-16 岁）可在教师指导下采用 AI 工具。该政策旨在保护基础读写能力培养。

hackernews · ilreb · Jun 19, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48600093)

**背景**: AI 工具如 ChatGPT 能生成文本、代码等内容，但可能干扰儿童学习基础技能。教育界担忧学生过度依赖 AI 会削弱独立思考能力，且难以有效监管作业真实性。

**社区讨论**: 多数评论支持禁令，认为 13 岁以下儿童应专注读写基础，类比“学算术前不应使用计算器”。部分用户质疑执行难度，指出 AI 已对教师和学生造成负面影响，但无外力禁止下难以控制。

**标签**: `#AI regulation`, `#education`, `#Norway`, `#policy`, `#generative AI`

---

<a id="item-3"></a>
## [现代汽车全面收购波士顿动力](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/) ⭐️ 8.0/10

现代汽车通过行使 2020 年收购协议中的看跌期权，从软银手中购入了波士顿动力剩余约 9%的股份，从而实现了对这家机器人公司的 100%控股。 此次收购巩固了现代汽车在机器人领域的战略布局，可能加速通用机器人技术的商业化，尤其针对韩国劳动力人口下降（预计到 2040 年减少 25%）带来的自动化需求。这也表明人形机器人（如 Atlas）与专用机器人（如 Spot）的商业化路线之争仍在持续。 2020 年 12 月现代汽车以 8.8 亿美元收购了波士顿动力 80%的股份，当时估值约 11 亿美元；软银此次出售剩余股份价值约 3.25 亿美元。波士顿动力已实现 Spot 机器人的商业部署（超过 1500 台），而 Atlas 人形机器人仍处于研发阶段。

hackernews · ck2 · Jun 19, 16:28 · [社区讨论](https://news.ycombinator.com/item?id=48600312)

**背景**: 波士顿动力以开发高动态机器人闻名，包括四足机器人 Spot 和双足人形机器人 Atlas。Spot 是其首款商用机器人，最初为国防承包商，2019 年向企业客户开放。现代汽车集团作为全球汽车制造商，正寻求在制造自动化和通用机器人领域拓展业务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Atlas_(robot)">Atlas ( robot ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Boston_Dynamics">Boston Dynamics - Wikipedia</a></li>
<li><a href="https://bostondynamics.com/products/spot/">Spot | Boston Dynamics</a></li>

</ul>
</details>

**社区讨论**: 讨论中，有观点质疑人形机器人相比专用机器人的效率优势，认为人类形态并非最优设计；但也有评论指出，鉴于韩国严重的人口老龄化，通用机器人可能比汽车制造自动化更具战略意义。另有用户对收购细节提出疑问，确认这是购买剩余股份。

**标签**: `#robotics`, `#acquisition`, `#Boston Dynamics`, `#Hyundai`, `#SoftBank`

---

<a id="item-4"></a>
## [业余爱好者用 AI 工具或破译线形文字 A](https://aiclambake.com/clamtakes/linear-a/) ⭐️ 8.0/10

一名 AI 工程师兼业余爱好者 Tom Di Mino 声称使用 Claude Code 等 AI 工具破解了未破译的线形文字 A（Linear A）脚本，已翻译超过 300 个单词，其工作正由罗格斯大学和剑桥大学的语言学专家审核。 如果验证属实，这将是历史语言学领域的重大突破，因为线形文字 A 自 1900 年发现以来一直未被破译，且其破解可能揭示米诺斯文明的语言、文化和宗教实践，弥补古代史一大空白。 Di Mino 利用 Claude Code 构建了一套 Python 脚本，用于查询、交叉引用和组织数字化语料库（来自 GORILA 和 SigLA 数据库），实现了此前手动难以完成的系统化假设检验；他基于最常用的“奠酒公式”进行翻译，其方法还解决了线形文字 B 的一些遗留问题。

hackernews · Kosturdistan · Jun 19, 16:04 · [社区讨论](https://news.ycombinator.com/item?id=48600107)

**背景**: 线形文字 A 是米诺斯文明（约公元前 1800-1450 年）使用的一种音节文字，主要见于克里特岛的宫殿和宗教泥板。目前已知语料仅约 7500 个字符，分散在约 1500 处铭文中，且多为简短片段。其继承者线形文字 B 已于 20 世纪 50 年代被破译（记录早期希腊语），但线形文字 A 的语言至今未知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear_A">Linear A - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linear_A_script">Linear A script</a></li>

</ul>
</details>

**社区讨论**: 社区整体持谨慎乐观态度，认为 Di Mino 的工作因有专家审核和实际成果（如翻译 300+词、解决线形文字 B 问题）而比以往声称更可信；评论也强调其关键创新在于用 AI 工具（Claude Code）构建自动化分析管线，而非将 AI 作为“黑箱”直接输出结果。

**标签**: `#Linear A`, `#decipherment`, `#AI-assisted research`, `#linguistics`, `#Claude Code`

---

<a id="item-5"></a>
## [Godot 4.7 发布：灯光、摄像机、动作](https://godotengine.org/releases/4.7/) ⭐️ 8.0/10

Godot 4.7 版本正式发布，带来了新的光照系统、摄像机改进和动作相关功能。该版本旨在为游戏开发者提供更强大的工具和更流畅的工作流程。 作为流行的开源游戏引擎，Godot 4.7 的发布将进一步巩固其在独立游戏开发领域的地位。新功能有望降低开发门槛，提升游戏品质，特别对 2D 和 3D 游戏创作产生积极影响。 具体更新包括改进的光照渲染管线、新的摄像机节点以及动画系统优化。Godot 4.7 还修复了多个社区报告的 bug，并提升了性能。

rss · Lobsters · Jun 19, 08:26

**背景**: Godot 是一款免费开源的游戏引擎，支持 2D 和 3D 游戏开发，并可在多平台导出。它采用 MIT 许可证，拥有活跃的社区和插件生态。本次 4.7 版本是继 4.6 之后的一次重要增量更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Godot_(game_engine)">Godot (game engine)</a></li>
<li><a href="https://godotengine.org/">Godot Engine - Free and open source 2D and 3D game engine</a></li>

</ul>
</details>

**标签**: `#godot`, `#game development`, `#open source`, `#release`

---

<a id="item-6"></a>
## [Bevy 0.19 发布，Rust 游戏引擎新版本](https://bevy.org/news/bevy-0-19/) ⭐️ 8.0/10

Bevy 0.19 版本正式发布，带来了新功能和性能改进，例如对 ECS 系统的优化和更好的编译速度。 Bevy 是 Rust 生态中重要的游戏引擎，此次更新增强了 Rust 游戏开发的能力，推动了数据驱动游戏引擎的发展。 该版本优化了实体组件系统（ECS），提升了运行时性能，并改进了开发者体验，具体变更可参考官方发布说明。

rss · Lobsters · Jun 19, 21:41

**背景**: Bevy 是一个使用 Rust 语言编写的数据驱动游戏引擎，其核心是自研的实体组件系统（ECS），实现了大规模并行和缓存友好的设计。Bevy 旨在简化游戏开发流程，同时保持高性能和生产力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bevy.org/">Bevy Engine</a></li>
<li><a href="https://github.com/bevyengine/bevy">bevyengine/ bevy : A refreshingly simple data-driven game engine built...</a></li>

</ul>
</details>

**标签**: `#Rust`, `#game engine`, `#Bevy`, `#open source`

---

<a id="item-7"></a>
## [SMPTE 宣布免费开放其媒体技术标准库](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community) ⭐️ 8.0/10

SMPTE（电影与电视工程师协会）宣布即日起将其全部技术标准库向全球免费开放，无需付费即可获取 800 余项标准文档。 此举消除了获取标准的经济门槛，将加速媒体技术领域的创新与互操作性，惠及全球开发者、工程师和影视制作机构。 免费开放的标准涵盖时间码、数字电影、视频压缩等关键领域，用户需在 SMPTE 网站注册后即可浏览和下载。

rss · Lobsters · Jun 19, 21:19

**背景**: SMPTE 成立于 1916 年，是国际公认的媒体技术标准制定组织，其标准此前通常需要付费获取。免费开放有助于推动行业标准化共识的形成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SMPTE">SMPTE</a></li>

</ul>
</details>

**标签**: `#standards`, `#media`, `#video`, `#SMPTE`, `#open access`

---

<a id="item-8"></a>
## [《毁灭战士》作曲家鲍比·普林斯去世](https://www.legacy.com/legacy/robert-bobby-prince-lll) ⭐️ 7.0/10

经典游戏《毁灭战士》《德军总部 3D》和《毁灭公爵 3D》的作曲家鲍比·普林斯（Bobby Prince）逝世，享年未知。 鲍比·普林斯的音乐定义了 90 年代第一人称射击游戏的听觉体验，对游戏文化和音乐历史产生了深远影响。 普林斯的作品包括《毁灭战士》系列中标志性的 MIDI 配乐，上个月美国国会图书馆将《毁灭战士》原声带列入国家录音登记册。

hackernews · pgrote · Jun 19, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=48602352)

**背景**: 鲍比·普林斯是游戏音乐领域的先驱，其作曲风格融合了金属与电子元素，极大增强了游戏的沉浸感。他的逝世让无数玩家和同行缅怀。

**社区讨论**: 社区评论充满敬意，玩家们分享了经典曲目链接并称赞其音乐在游戏氛围中的重要性，有人幽默调侃地狱也聘请他配乐，并提及国会图书馆的认可。

**标签**: `#gaming`, `#music`, `#composer`, `#DOOM`, `#Wolfenstein 3D`

---

<a id="item-9"></a>
## [ATProto 中不存在“实例”概念](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 7.0/10

Dan Abramov 撰文澄清 ATProto（Bluesky 协议）中不存在“实例”这一概念，指出这是一种类别错误，并用 RSS 和 email 的类比解释其架构。 该文章有助于纠正对 ATProto 的常见误解，明确其与 Mastodon/ActivityPub 的架构差异，对理解去中心化社交网络的多样性至关重要。 文章强调 ATProto 将中继（Relay）、应用视图（AppView）和个人数据服务器（PDS）分离，而“实例”是 Mastodon 等联邦式网络的概念。

hackernews · danabramov · Jun 19, 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48599515)

**背景**: ATProto 是 Bluesky 开发的一种去中心化社交协议，旨在实现用户数据的可移植性和可扩展性。在 Mastodon 中，“实例”指独立服务器，用户通过加入不同实例互动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/overview">Protocol Overview - AT Protocol</a></li>

</ul>
</details>

**社区讨论**: 评论中存在不同观点：有人批评类比不准确，认为 RSS 和 email 的中立性更强；也有人称赞 ATProto 的架构设计优雅，解决了性能扩展问题。

**标签**: `#ATProto`, `#decentralized protocols`, `#Bluesky`, `#architecture`, `#ActivityPub`

---

<a id="item-10"></a>
## [Google Workspace 被指阻止 Firefox 访问](https://tales.fromprod.com/2026/169/google-workspace-threatening-to-block-firefox.html) ⭐️ 7.0/10

一篇博客文章称 Google Workspace 可能阻止 Firefox 浏览器访问，但社区评论澄清这是企业管理员可配置的策略，并非 Google 全局变更。 此事引发了对浏览器兼容性和企业 IT 控制权的讨论，但实际影响有限，仅影响特定企业环境中的用户。 博客作者表示未配置 IAP 或上下文感知访问，但使用的是 Workspace Business Plus 版本；社区指出该限制来自 Google 的上下文感知访问产品，仅适用于 Enterprise 版。

hackernews · birdculture · Jun 19, 16:30 · [社区讨论](https://news.ycombinator.com/item?id=48600345)

**背景**: User-Agent 是一个 HTTP 标头，用于标识客户端软件。企业 IT 管理员可以通过 Google Workspace 的上下文感知访问功能，基于浏览器 User-Agent 设置访问策略，从而限制某些浏览器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/User-Agent_header">User-Agent header</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent">User - Agent header - HTTP | MDN</a></li>

</ul>
</details>

**社区讨论**: 社区多数评论认为这是企业策略而非 Google 强制变更，作者澄清未配置相关功能；讨论还涉及功能检测与用户代理检测的优劣，部分用户支持转向功能检测。

**标签**: `#Google Workspace`, `#Firefox`, `#browser compatibility`, `#corporate IT policy`, `#user-agent`

---

<a id="item-11"></a>
## [法院记录应免费开放](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free) ⭐️ 7.0/10

电子前沿基金会（EFF）呼吁法院记录应免费向公众开放，指出当前联邦法院系统 PACER 每页收费 1 美元，而爱达荷州州法院每页收费高达 10 美元，严重阻碍了公众获取司法信息。 法院记录是公共法律文件，收取高额费用违背了司法透明原则，不仅影响普通公民维护自身权利，也阻碍了法律研究和技术创新（如 AI 训练数据的获取）。 PACER 是联邦法院的电子公共访问系统，每页文档收费 0.10 美元（上限 3 美元），但实际按页计费常导致高昂费用；而州级法院如爱达荷州每页收费 10 美元，更显不合理。CourtListener 平台及其 Recap 插件允许用户自愿共享已付费的 PACER 文档，以降低公共获取成本。

hackernews · hn_acker · Jun 19, 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600946)

**背景**: PACER（Public Access to Court Electronic Records）是美国联邦法院的电子记录系统，自 1988 年建立以来一直依靠用户收费维持运营，但近年来批评声不断，认为其应当免费。尽管法律允许收取“合理费用”，但实际收费远超成本，且存在技术陈旧、搜索功能有限等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://upsolve.org/learn/pacer-guide/">PACER Guide: How To Get Your Court Notices Without an Attorney</a></li>
<li><a href="https://mo-casenet.us/pacer/">PACER - Mo-Casenet.us</a></li>
<li><a href="https://pacer.uscourts.gov/">Public Access to Court Electronic Records | PACER : Federal Court ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持免费开放，强调法律规定公众有权免费阅读法律文件；用户 jacobmarble 指出州级（爱达荷州）每页 10 美元远高于联邦系统；cdolan 肯定了 CourtListener 和 Recap 的临时作用；treebeard901 认为收费是政府故意限制权利的手段；user3939382 引用汉谟拉比法典，强调司法裁决即法律，必须可免费获取。

**标签**: `#legal-tech`, `#open-access`, `#government-transparency`, `#PACER`, `#public-records`

---

<a id="item-12"></a>
## [新法案旨在阻止政府施压平台审查合法言论](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech) ⭐️ 7.0/10

美国参议员 Ted Cruz 和 Ron Wyden 提出一项两党法案（JAWBONE），旨在禁止政府机构通过非正式施压要求在线平台删除合法言论。电子前沿基金会（EFF）公开支持该法案。 该法案若通过，将填补当前法律空白，限制政府以“劝诫”方式绕开程序侵犯言论自由。它直接保护了如 ICEBlock 等应用开发者及普通用户的言论权利，是维护网络自由的重要立法进展。 法案全称为“Justice Against Weaponized Bureaucratic Overreach to Networked Expression”（JAWBONE），由共和党参议员 Cruz 与民主党参议员 Wyden 联合发起。EFF 此前曾代表 ICEBlock 应用在法庭上对抗政府要求平台下架其内容的施压行为。

hackernews · hn_acker · Jun 19, 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600950)

**背景**: 政府机构有时会通过非正式方式（如信件、电话）向社交媒体公司施压，要求删除或限制某些内容，这种做法被称为“jawboning”。由于缺乏法律监督，这种压力可能侵犯受第一修正案保护的言论自由。EFF 等组织长期推动立法，要求政府行为透明并遵循正当程序。

**社区讨论**: 社区评论中对法案的缩写名称 JAWBONE 表示赞赏，但也有用户质疑共和党参议员 Cruz 的真实动机，认为他可能只支持有利保守派的审查案件。部分评论批评标题党，并强调该法案是两党合作成果，且得到 EFF 支持，应当获得更多关注。

**标签**: `#policy`, `#free speech`, `#government censorship`, `#EFF`

---

<a id="item-13"></a>
## [开源 CAD 内核 Fornjot 宣布关闭](https://fornjot.app/blog/shutting-down-fornjot/) ⭐️ 7.0/10

Fornjot 项目宣布关闭，这是一个用 Rust 语言编写的开源边界表示（b-rep）CAD 内核。开发者 Hanno Braun 在博客中表示将停止维护。 Fornjot 是 Rust 生态中少数专注于 CAD 内核的项目，其关闭对 Rust 在 CAD 领域的探索是一个打击，也引发了对开源 CAD 项目可持续性的思考。 Fornjot 是一个早期阶段、实验性项目，最新版本为 2023 年 12 月发布的 v0.48.0。关闭可能源于开发者精力不足或缺乏足够的社区贡献。

rss · Lobsters · Jun 19, 11:28

**背景**: Fornjot 采用边界表示法（b-rep），该方法通过存储几何体的边界（如面、边、顶点）来描述三维形状。它是用 Rust 重写的少数 CAD 内核之一，旨在探索 Rust 在工程软件中的潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fornjot.app/">Fornjot</a></li>
<li><a href="https://github.com/hannobraun/fornjot">GitHub - hannobraun/fornjot: Early-stage b-rep CAD kernel, written in the Rust programming language. · GitHub</a></li>
<li><a href="https://users.rust-lang.org/t/fornjot-v0-48-0-open-source-b-rep-cad-kernel-in-rust/103982">Fornjot v0.48.0 - open source b-rep CAD kernel in Rust - announcements - The Rust Programming Language Forum</a></li>

</ul>
</details>

**标签**: `#Rust`, `#CAD`, `#open-source`, `#project-shutdown`

---

<a id="item-14"></a>
## [定义 Well-Known URI 的实用指南](https://mnot.net/blog/2026/well_known_uris) ⭐️ 7.0/10

Mark Nottingham 发表了一篇技术文章，详细阐述了定义 Well-Known URI 时应遵循的指南和常见陷阱。该文章为 API 和协议设计者提供了实践建议。 这篇文章对于希望使用/.well-known/路径部署标准化资源的 Web 开发者和标准制定者至关重要，能够帮助他们避免常见错误，确保 URI 的一致性和互操作性。 文章可能涵盖了选择路径前缀、注册流程以及处理不同 HTTP 方法等方面的注意事项。文中还引用了 Lobste.rs 上的社区讨论，反映了技术社群对该话题的关注。

rss · Lobsters · Jun 19, 12:29

**背景**: Well-Known URI 指以/.well-known/开头的路径前缀，由 IETF 在 RFC 8615 中标准化。它们用于在 Web 服务器上提供标准化的服务发现和信息资源，例如 ACME 挑战和 OAuth 元数据。定义新的 Well-Known URI 需要遵循注册程序并确保路径的唯一性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Well-known_URI">Well-known URI - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc8615">RFC 8615 - Well-Known Uniform Resource Identifiers (URIs)</a></li>

</ul>
</details>

**标签**: `#web standards`, `#URIs`, `#HTTP`, `#API design`

---