---
layout: default
title: "Horizon Summary: 2026-06-22 (ZH)"
date: 2026-06-22
lang: zh
---

> From 29 items, 15 important content pieces were selected

---

1. [旧工作是否仅因欺诈存在？](#item-1) ⭐️ 8.0/10
2. [宁要重复，不要错误的抽象](#item-2) ⭐️ 8.0/10
3. [AI 时代构建软件的成本仍然不为零](#item-3) ⭐️ 8.0/10
4. [Python 实现 Lisp 解释器经典教程](#item-4) ⭐️ 8.0/10
5. [开发者普遍误解 CORS 机制](#item-5) ⭐️ 8.0/10
6. [AI 正在损害人类技能？早期研究结果令人担忧](#item-6) ⭐️ 8.0/10
7. [苹果内核中 Swift 语言的深度应用分析](#item-7) ⭐️ 8.0/10
8. [Cloudflare 解析 SOCKMAP：基于 BPF 的内核级 TCP 拼接](#item-8) ⭐️ 8.0/10
9. [个人网站 JSON-LD 结构化数据教程](#item-9) ⭐️ 7.0/10
10. [Claude 身份验证引发隐私与市场争议](#item-10) ⭐️ 7.0/10
11. [几何代数批判：一篇引发争议的评论文章](#item-11) ⭐️ 7.0/10
12. [用 APL 语言编写的 3D 体素游戏引擎](#item-12) ⭐️ 7.0/10
13. [优化 SQLx 测试属性重建时间](#item-13) ⭐️ 7.0/10
14. [Loupe：揭示 iOS 原生应用数据访问的隐私工具](#item-14) ⭐️ 7.0/10
15. [远程工作加剧社交隔离](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [旧工作是否仅因欺诈存在？](https://david.newgas.net/did-my-old-job-only-exist-because-of-fraud/) ⭐️ 8.0/10

一篇个人随笔引发了社区讨论，质疑咨询和承包行业中的工作是否因欺诈性计费和实践而得以维持。多名员工分享了亲身经历，包括被篡改工时、承包商被解雇后以更高价重新雇佣等现象。 该讨论揭示了科技和咨询行业中潜在的系统性欺诈问题，可能影响企业成本、员工诚信和行业声誉。这些现象促使从业者反思自己的工作价值和行业道德。 评论者 etothepii 提到，承包商被解雇后通过大型外包商以加价重返原团队；comrade1234 发现自己的工时被经理篡改以消耗政府项目预算；siskiyou 描述了公司 CEO 因 110 亿美元欺诈入狱，而内部员工早有察觉。这些例子表明欺诈可能从高层蔓延至日常操作。

hackernews · advisedwang · Jun 21, 21:40 · [社区讨论](https://news.ycombinator.com/item?id=48622867)

**背景**: 在咨询和外包行业，公司常按工时或项目向客户收费。有些管理者为消耗预算或虚增业绩，会操纵工时记录或进行不正当转包，这在私营和政府项目中均有可能发生。当欺诈成为常态，员工可能不自知地参与其中。

**社区讨论**: 社区讨论总体认可欺诈现象的普遍性，但观点存在分歧。部分人认为此类行为在行业中是公开的秘密，员工应保持警惕；也有评论者如 Zhenya 质疑为何要纠结于此，强调个人只需做好本职工作即可。

**标签**: `#fraud`, `#consulting`, `#tech industry`, `#corporate culture`, `#outsourcing`

---

<a id="item-2"></a>
## [宁要重复，不要错误的抽象](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) ⭐️ 8.0/10

Sandi Metz 在 2016 年发表了一篇经典博文，主张在软件开发中宁可容忍代码重复，也不要过早引入错误的抽象，因为这会导致代码复杂且难以修改。 该观点挑战了“消除重复”的传统教条，提醒开发者警惕过早抽象带来的长期维护成本，对软件设计实践有深远影响。 文章强调，如果强行将看似重复的代码合并成抽象，但该抽象并不符合实际需求，后续重构将更加困难；而保留重复代码反而更灵活。

hackernews · rafaepta · Jun 21, 16:08 · [社区讨论](https://news.ycombinator.com/item?id=48620090)

**背景**: 软件工程中，“Don't Repeat Yourself (DRY)”原则被广泛推崇，但 Metz 指出，当抽象方向错误时，重复代码反而更透明易改。这一观点在社区中引发了关于抽象与复制权衡的持久讨论。

**社区讨论**: 评论中，有用户强调“单一事实来源”原则，认为会影响正确性的重复必须重构；也有用户提到函数式编程和 TypeScript 可以减少此类问题；多数人赞同欠工程化比过工程化更易处理。

**标签**: `#software engineering`, `#abstraction`, `#code duplication`, `#refactoring`, `#design principles`

---

<a id="item-3"></a>
## [AI 时代构建软件的成本仍然不为零](https://brandur.org/minimum-viable-unit) ⭐️ 8.0/10

一篇文章深入探讨了即使有了 AI 辅助，内部构建软件的隐性成本依然存在，认为对于非核心业务，购买现成软件仍比自建更经济。 该观点挑战了 AI 将彻底改变“构建 vs 购买”决策的普遍预期，提醒开发者在拥抱 AI 时要理性评估研发的完整投入，避免盲目自建。 文章特别指出，AI 虽降低了原型搭建的起始成本，但要让软件达到可销售或可用的成熟状态，所需的迭代、维护和打磨工作并未显著减少。

hackernews · brandur · Jun 21, 16:41 · [社区讨论](https://news.ycombinator.com/item?id=48620342)

**背景**: 在软件开发中，“构建 vs 购买”是一个经典决策：企业可以自己开发软件，也可以直接购买第三方产品。随着 AI 代码生成工具（如 GitHub Copilot）的普及，人们一度认为自建成本将趋近于零，但本文通过实际经验论证了这一假设的局限性。

**社区讨论**: 社区评论普遍认同作者观点，多位开发者分享亲身经历：AI 让副项目快速起步，但后续推进的动力和精力投入仍未降低；有评论补充指出，自建成本不为零也意味着第三方竞争者能进入市场压低价格；还有观点强调社区效应使商业软件具备自建难以复制的集体改进优势。

**标签**: `#software engineering`, `#build vs buy`, `#AI`, `#economics`, `#side projects`

---

<a id="item-4"></a>
## [Python 实现 Lisp 解释器经典教程](https://norvig.com/lispy.html) ⭐️ 8.0/10

Peter Norvig 于 2010 年发布的教程《How to Write a (Lisp) Interpreter (In Python)》，详细展示了如何用 Python 构建一个 Lisp 解释器。 该教程是学习解释器设计和 Lisp 语言的经典入门材料，至今仍被广泛引用，对编程语言学习者有极高的教育价值。 教程分为两部分，第一部分实现核心的读取-求值-打印循环（REPL），第二部分扩展了更多功能（如宏）。社区中已有开发者将其移植到 Rust 等语言。

hackernews · tosh · Jun 21, 15:36 · [社区讨论](https://news.ycombinator.com/item?id=48619831)

**背景**: Lisp 是一种历史悠久的编程语言家族，以其括号化的前缀表达式（S 表达式）和代码即数据的特性著称。解释器是直接执行源代码的程序，无需事先编译。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lisp_(programming_language)">Lisp (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Interpreter_(computer_science)">Interpreter (computer science)</a></li>

</ul>
</details>

**社区讨论**: 评论普遍认为这是学习编写编程语言的最佳入门教程之一，不少用户分享了用 Rust 等语言重写的版本，并推荐同作者的其他资源。

**标签**: `#Lisp`, `#interpreter`, `#Python`, `#tutorial`, `#Norvig`

---

<a id="item-5"></a>
## [开发者普遍误解 CORS 机制](https://fosterelli.co/developers-dont-understand-cors) ⭐️ 8.0/10

一篇 2019 年的技术文章指出，大多数开发者并不真正理解跨域资源共享（CORS）的工作原理及其威胁模型。文章引发了大量讨论，社区评论进一步证实了这种普遍误解。 CORS 是现代 Web 安全的基础机制，错误理解会导致严重的安全漏洞。该文章的高热度说明问题普遍存在，正确理解 CORS 对保障 Web 应用安全至关重要。 文章强调，CORS 不能替代服务器端认证，它仅用于浏览器对跨域请求进行额外检查，而许多开发者错误地将其视为访问控制机制。此外，CORS 规范复杂且频繁更新，导致开发者常通过反复试错来配置。

hackernews · toilet · Jun 21, 01:35 · [社区讨论](https://news.ycombinator.com/item?id=48614844)

**背景**: 浏览器默认实施同源策略（Same-Origin Policy, SOP），禁止一个源的脚本访问另一个源的资源。CORS 是一种通过 HTTP 头（如 Access-Control-Allow-Origin）让服务器声明允许特定源访问的机制。但 CORS 并不阻止请求的发送，而是阻止浏览器读取跨域响应，因此必须在服务器端进行适当的验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cross-origin_resource_sharing">Cross-origin resource sharing - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy">Same-origin policy - Security | MDN</a></li>
<li><a href="https://educatedguesswork.org/posts/web-security-model-cors/">Understanding The Web Security Model, Part IV: Cross-Origin Resource Sharing (CORS)</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍认同文章观点，许多开发者表示 CORS 令人困惑且难以正确配置。有评论指出文章本身也存在一些误解，但这反而凸显了 CORS 的复杂性。也有用户推荐 MDN 文档作为权威学习资源，并感叹开发者对威胁模型缺乏整体认识。

**标签**: `#web security`, `#CORS`, `#JavaScript`, `#HTTP`, `#developer education`

---

<a id="item-6"></a>
## [AI 正在损害人类技能？早期研究结果令人担忧](https://www.nature.com/articles/d41586-026-01947-1) ⭐️ 8.0/10

《自然》杂志发表文章，总结了关于人工智能对人类技能影响的初步研究结果，显示 AI 可能正在削弱人们的批判性思维和问题解决能力。 如果 AI 确实使人类依赖外部系统而降低自身认知能力，将深刻影响教育体系、职场竞争力和个体发展，需要社会各界认真审视 AI 的长期代价。 研究指出，频繁使用 AI 工具可能导致“认知卸载”——人们减少独立思考和记忆的练习，从而逐渐丧失这些技能。不过，目前的结果仍是初步的，需要更多纵向研究来确认因果效应。

rss · Lobsters · Jun 21, 10:41

**背景**: 随着 ChatGPT 等生成式 AI 的普及，越来越多的人将任务委托给 AI 完成。学术界和公众开始担忧，这种便利是否会像 GPS 损害方向感一样，削弱人类的核心认知能力。所谓“认知卸载”理论认为，外部工具使用过多会减少大脑相应区域的活跃度，进而导致功能退化。

**标签**: `#AI`, `#human skills`, `#cognitive science`, `#technology impact`, `#research`

---

<a id="item-7"></a>
## [苹果内核中 Swift 语言的深度应用分析](https://blog.calif.io/p/apple-internals-swift-in-the-kernel) ⭐️ 8.0/10

Josh Maine 发表了一篇深度文章，详细分析了 Swift 语言在苹果 XNU 内核中的集成情况，揭示了苹果在新版操作系统中使用 Swift 编写内核部分代码的具体实现。 这表明苹果开始将内存安全的 Swift 语言引入内核开发，是操作系统安全性的重要进步，可能影响未来系统级编程语言的选择。 分析显示，苹果为每个操作系统内核的 Swift 代码分配了独立平台标识，例如 macOS 是 25，iOS 是 26。内核中调用了 Swift 运行时函数如 swift_retain、swift_release 和 swift_dynamicCast 等，但大部分调用来自 swift_dynamicCast 内部。

rss · Lobsters · Jun 21, 08:41

**背景**: XNU 是苹果操作系统（macOS、iOS 等）的内核，传统上使用 C/C++ 编写。Swift 是一种现代、内存安全的编程语言，苹果近年来大力推广。将 Swift 引入内核有助于减少内存安全漏洞，如缓冲区溢出或释放后使用（UAF）等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/apple-internals-swift-in-the-kernel">Apple Internals: Swift in the Kernel - by Josh Maine</a></li>
<li><a href="https://www.osnews.com/story/145352/apple-internals-swift-in-the-kernel/">Apple internals: Swift in the kernel – OSnews</a></li>

</ul>
</details>

**标签**: `#Swift`, `#Kernel`, `#Apple`, `#Systems Programming`, `#Operating Systems`

---

<a id="item-8"></a>
## [Cloudflare 解析 SOCKMAP：基于 BPF 的内核级 TCP 拼接](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/) ⭐️ 8.0/10

Cloudflare 发表博客详细介绍了 SOCKMAP 技术，该技术利用 Linux 内核的 eBPF（扩展伯克利包过滤器）实现高效 TCP 拼接，无需数据复制到用户空间。 SOCKMAP 显著提升了网络代理和负载均衡器的性能，通过在内核层直接转发数据，减少了上下文切换和数据拷贝开销，对高性能网络服务至关重要。 SOCKMAP 从 Linux 4.14 开始引入，由 John Fastabend 在 Cilium 创建，它暴露 Strparser 接口给 eBPF 程序，并支持使用 bpf_sk_redirect_map 等帮助函数进行套接字重定向。

rss · Lobsters · Jun 21, 01:42

**背景**: TCP 拼接是一种将两个 TCP 连接直接在传输层拼接的技术，传统实现需在用户空间拷贝数据。eBPF 则是一种在内核中安全运行沙箱化程序的技术。SOCKMAP 结合两者，允许在内核中执行自定义逻辑来决策数据转发，大幅提升效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/">SOCKMAP - TCP splicing of the future</a></li>
<li><a href="https://docs.kernel.org/bpf/map_sockmap.html">BPF_MAP_TYPE_SOCKMAP and BPF_MAP_TYPE_SOCKHASH — The Linux Kernel documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/TCP_splicing">TCP splicing</a></li>

</ul>
</details>

**标签**: `#SOCKMAP`, `#BPF`, `#TCP splicing`, `#kernel`, `#networking`

---

<a id="item-9"></a>
## [个人网站 JSON-LD 结构化数据教程](https://hawksley.dev/blog/json-ld-explained-for-personal-websites/) ⭐️ 7.0/10

一篇详细教程介绍了如何在个人网站上使用 JSON-LD 来标注数据，从而改善搜索引擎优化（SEO）和富媒体预览效果。 该教程为个人网站所有者提供了一种提升搜索引擎可见性的实用方法，但社区讨论也揭示了在生成式 AI 摘要兴起的背景下，传统 SEO 策略可能面临新挑战。 教程涵盖了 JSON-LD 的基本用法，但评论指出需维护多份元数据的一致性，且部分结构化数据（如评论评分）对个人网站并不适用。

hackernews · ethanhawksley · Jun 21, 18:51 · [社区讨论](https://news.ycombinator.com/item?id=48621517)

**背景**: JSON-LD（JavaScript Object Notation for Linked Data）是一种使用 JSON 编码链接数据的 W3C 标准，它能让网站以结构化方式向搜索引擎描述内容，从而触发富结果（如面包屑导航、星级评分等）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JSON-LD">JSON-LD</a></li>
<li><a href="https://json-ld.org/">JSON - LD - JSON for Linked Data</a></li>

</ul>
</details>

**社区讨论**: 评论中，JdeBP 批评该教程“打上一场战争”，指出 Google 已转向用 LLM 生成摘要代替直接展示网站内容；klodolph 建议参考 Google 官方文档，并强调很多结构化数据类型对个人网站不相关；deftio 和 gomoboo 则分别关注元数据一致性和 SEO 是否真能帮助用户离开搜索页的问题。

**标签**: `#JSON-LD`, `#SEO`, `#semantic web`, `#personal websites`, `#structured data`

---

<a id="item-10"></a>
## [Claude 身份验证引发隐私与市场争议](https://support.claude.com/en/articles/14328960-identity-verification-on-claude) ⭐️ 7.0/10

Anthropic 要求用户通过第三方身份验证服务 Persona 提供政府签发 ID，以继续使用 Claude 高级模型。该政策已于数月前上线，但近期在社区中引发广泛讨论。 这凸显了 AI 服务中隐私与安全之间的紧张关系，同时因美国对高级 AI 模型的出口限制，可能加速国际 LLM 市场的形成，削弱美国 AI 产品的全球竞争力。 Anthropic 明确不会将身份数据用于模型训练，但合作伙伴 Persona 可能使用数据改进其反欺诈模型。此外，若验证失败，用户将被永久锁定，无法再次尝试。

hackernews · bathory · Jun 21, 12:44 · [社区讨论](https://news.ycombinator.com/item?id=48618455)

**背景**: 身份验证是 AI 公司为遵守反洗钱（AML）、了解你的客户（KYC）等法规，以及防止滥用而采取的常见措施。Persona 是一家美国身份验证公司，提供文件分析和生物识别等验证服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Persona_(identity_verification_service)">Persona (identity verification service)</a></li>
<li><a href="https://withpersona.com/">Secure Identity Verification Solutions | Persona</a></li>
<li><a href="https://www.gartner.com/reviews/product/persona">Persona Reviews & Ratings 2026 | Gartner Peer Insights</a></li>

</ul>
</details>

**社区讨论**: 社区讨论呈现两极分化：一方面，非美国用户批评美国政策导致他们无法访问顶级模型，认为付费价值递减；另一方面，用户担忧 Persona 的隐私条款，以及验证失败即永久封锁的严厉后果。

**标签**: `#Claude`, `#identity verification`, `#privacy`, `#Anthropic`, `#AI policy`

---

<a id="item-11"></a>
## [几何代数批判：一篇引发争议的评论文章](https://alexkritchevsky.com/2024/02/28/geometric-algebra.html) ⭐️ 7.0/10

2024 年 2 月，Alex Kritchevsky 发表了一篇题为《反对几何代数》的文章，系统地批评了几何代数（Geometric Algebra）的过度宣传和理论缺陷，认为其缺乏严谨性且实际优势有限。 该文章在数学和物理学社区引发激烈讨论，挑战了几何代数作为统一数学框架的地位，提示研究者应谨慎评估其实际价值，避免被过度推广所迷惑。 文章指出几何代数在量纲分析中存在致命缺陷，因为其丢弃了有意义的单位系统，导致实际计算中难以进行误差检验；此外，许多支持者的论文缺乏理论深度，偏向于工程应用而非严格数学。

hackernews · Hbruz0 · Jun 21, 11:06 · [社区讨论](https://news.ycombinator.com/item?id=48617782)

**背景**: 几何代数（又称 Clifford 代数）是一种将向量、外积等概念统一起来的代数系统，被一些学者倡导为描述物理和几何问题的更好工具，在计算机图形学和机器人学中有应用。然而，其支持者的激进推广方式（如“GA 是万能框架”）一直饱受争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alexkritchevsky.com/2024/02/28/geometric-algebra.html">The Case Against Geometric Algebra</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geometric_algebra">Geometric algebra</a></li>

</ul>
</details>

**社区讨论**: 评论中，有人赞同文章观点，认为 GA 确实存在量纲分析和理论严谨性的问题；但也有用户反驳，指出 GA 在解决具体工程问题时更直观、易用，而文章的批评过分侧重于纯数学角度。

**标签**: `#geometric algebra`, `#mathematics`, `#critique`, `#applied math`, `#physics`

---

<a id="item-12"></a>
## [用 APL 语言编写的 3D 体素游戏引擎](https://github.com/namgyaaal/avoxelgame) ⭐️ 7.0/10

开发者 namgyaaal 发布了一个名为 avoxelgame 的开源项目，这是一个用 APL 语言编写的 3D 体素游戏引擎，展示了 APL 在图形编程中的表达能力。 该项目证明了 APL 这种以极简符号著称的数组编程语言也能用于开发 3D 游戏，挑战了传统上认为游戏开发必须使用 C++或 Rust 等高性能语言的观念，可能激发更多跨语言实验。 引擎支持基本的地形生成和渲染，但项目 README 坦诚地描述为“一个充满 bug 的激情项目”，强调其非商业性质；社区对其性能表现（与 C++/Rust 引擎对比）充满好奇。

hackernews · sph · Jun 21, 08:04 · [社区讨论](https://news.ycombinator.com/item?id=48616713)

**背景**: APL 是一种诞生于 1960 年代的数组编程语言，以使用独特符号实现极简代码而闻名，常用于数学和数据处理。体素游戏引擎则通过三维像素（体素）构建可交互的世界，经典代表如《我的世界》。将 APL 应用于体素渲染属于跨界尝试，旨在探索其符号化表达能否简化游戏逻辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/APL_(programming_language)">APL (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Voxel">Voxel - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对 APL 引擎的创意表示赞赏，认为体素世界的数学结构天然适合 APL 的数组运算；多位用户关注其性能表现，希望看到与 C++/Rust 等传统语言的基准测试。还有评论者肯定项目的诚实定位，认为这种不夸大宣传的“buggy passion project”态度值得提倡。

**标签**: `#APL`, `#game engine`, `#voxel`, `#programming languages`, `#hobby project`

---

<a id="item-13"></a>
## [优化 SQLx 测试属性重建时间](https://kobzol.github.io/rust/2026/06/21/optimizing-sqlx-test-rebuild-time.html) ⭐️ 7.0/10

该博客文章介绍了减少 Rust 中 SQLx 库的 #[sqlx::test] 属性编译重建时间的方法。 这对于使用 SQLx 进行数据库测试的 Rust 开发者很重要，因为它可以减少测试编译等待时间，提高开发效率。 文章可能涉及缓存、增量编译或避免冗余工作等内容，但具体细节未提供。

rss · Lobsters · Jun 21, 18:53

**背景**: SQLx 是 Rust 的异步 SQL 工具包，支持编译时检查查询。#[sqlx::test] 属性在每个测试前自动创建数据库并运行迁移，然后提供连接池。这会导致每次测试编译时都需要处理数据库设置相关的代码，可能增加重建时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kobzol.github.io/rust/2026/06/21/optimizing-sqlx-test-rebuild-time.html">Optimizing #[ sqlx :: test ] rebuild time | Kobzol’s blog</a></li>
<li><a href="https://docs.rs/sqlx/latest/sqlx/">sqlx - Rust</a></li>
<li><a href="https://github.com/launchbadge/sqlx">GitHub - transact-rs/sqlx: 🧰 The Rust SQL Toolkit. An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.</a></li>

</ul>
</details>

**标签**: `#Rust`, `#SQLx`, `#compile-time`, `#optimization`, `#testing`

---

<a id="item-14"></a>
## [Loupe：揭示 iOS 原生应用数据访问的隐私工具](https://github.com/mysk-research/loupe) ⭐️ 7.0/10

Loupe 是一款开源的 iOS 应用，它通过调用与第三方应用相同的公共 iOS API，向用户展示原生应用能够访问的原始数据，并解释这些数据可能如何被用于设备指纹识别。 该应用有助于提高用户对 iOS 设备隐私泄露风险的认知，让用户了解即使不提供姓名、邮箱或位置，应用也能通过设备特征识别用户，从而影响用户权限授予行为和开发者隐私实践。 Loupe 读取的公共 API 包括 Wi-Fi 名称、已安装应用列表、设备型号等，这些信息组合可用于生成唯一设备标识符。该应用已在 App Store 上架，源代码托管在 GitHub 上。

rss · Lobsters · Jun 21, 21:01

**背景**: iOS 应用沙盒机制限制应用访问其他应用的数据和系统资源，但应用可以请求权限访问某些信息，如相机、位置等。设备指纹识别是一种无需用户身份即可跨应用跟踪用户的技术，通过收集硬件、软件和配置特征来唯一识别设备。Loupe 正是利用这些公开 API 来演示隐私风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/guide/security/security-of-runtime-process-sec15bfe098e/web">Security of runtime process in iOS, iPadOS, and visionOS - Apple Support</a></li>
<li><a href="https://techplanet.today/post/loupe-the-ios-app-exposing-what-your-iphone-quietly-reveals-about-you">Loupe : The iOS App Exposing What Your iPhone ... | TechPlanet</a></li>

</ul>
</details>

**标签**: `#privacy`, `#iOS`, `#security`, `#app development`

---

<a id="item-15"></a>
## [远程工作加剧社交隔离](https://www.science.org/doi/10.1126/science.aec7671) ⭐️ 7.0/10

一项发表在《科学》期刊上的研究指出，远程工作会导致员工社交隔离感增加。 该发现对软件工程等行业普遍推行的远程工作模式提出警示，企业需关注员工心理健康和团队凝聚力。 该研究由权威期刊《科学》发布，但具体样本规模和方法未在摘要中详细说明。

rss · Lobsters · Jun 21, 17:01

**背景**: 远程工作自疫情以来广泛普及，但长期缺乏面对面互动可能削弱归属感。社交隔离是指个体与外界联系减少，可能引发孤独、焦虑等问题。

**标签**: `#remote work`, `#social isolation`, `#workplace culture`, `#research`

---