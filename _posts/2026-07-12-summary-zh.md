---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> From 27 items, 14 important content pieces were selected

---

1. [Chromium 148 中 Math.tanh 可被用于操作系统指纹识别](#item-1) ⭐️ 8.0/10
2. [研究显示 Claude Code token 开销远高于 OpenCode](#item-2) ⭐️ 8.0/10
3. [陶哲轩谈用 LLM 编码代理构建应用](#item-3) ⭐️ 8.0/10
4. [爱尔兰数据中心耗电占全国 23%](#item-4) ⭐️ 8.0/10
5. [我热爱 LLM，我厌恶炒作](#item-5) ⭐️ 8.0/10
6. [电影特效到 CGI 的转型与 LLM 影响软件开发类比](#item-6) ⭐️ 8.0/10
7. [慢软件：高延迟系统设计的辩护](#item-7) ⭐️ 8.0/10
8. [黑客利用 SQL 注入攻破苹果系统实现远程代码执行](#item-8) ⭐️ 8.0/10
9. [Tiny Emulators：引脚级模块化 8 位模拟器](#item-9) ⭐️ 7.0/10
10. [迁移 AI 代理至 GPT-5.6：速度快 2.2 倍，成本低 27%](#item-10) ⭐️ 7.0/10
11. [Rust arena 内存管理解决三年旧问题](#item-11) ⭐️ 7.0/10
12. [InfiniteDiffusion：融合扩散模型与程序化生成的地形算法](#item-12) ⭐️ 7.0/10
13. [EF Core 11 提升拆分查询性能](#item-13) ⭐️ 7.0/10
14. [Motorola MR2600 路由器存在未认证远程代码执行漏洞](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Chromium 148 中 Math.tanh 可被用于操作系统指纹识别](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 8.0/10

Chromium 148 的 Math.tanh 函数实现依赖于底层操作系统，不同 OS 返回不同结果，从而可以被用于浏览器指纹识别，识别用户所使用的操作系统。 这是一个新的浏览器指纹识别向量，能绕过传统的用户代理检测，进一步威胁用户隐私。它表明即使是浏览器内置的 JavaScript 数学函数也可能成为追踪手段，需要浏览器厂商和隐私工具重视并采取对策。 V8 引擎对大多数数学函数使用自带的 llvm-libc 库，但 Math.tanh 直接调用宿主操作系统的数学库（如 macOS 的 libsystem_m、Linux 的 glibc、Windows 的 UCRT），导致结果出现系统间差异。此外，CSS 三角函数和 Web Audio 的 FFT 实现也同样存在操作系统依赖性。

hackernews · joahnn_s · Jul 12, 21:12 · [社区讨论](https://news.ycombinator.com/item?id=48884853)

**背景**: 浏览器指纹识别是通过收集浏览器版本、屏幕分辨率、已安装字体、时区等特征来唯一标识用户的技术，常用于广告追踪和反欺诈。JavaScript 的 Math 函数精度在标准中定义为“实现相关”，因此不同浏览器、不同操作系统上的相同计算可能产生微小差异，这为指纹识别提供了可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scrapfly.dev/posts/browser-math-os-fingerprint/">Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev</a></li>
<li><a href="https://news.ycombinator.com/item?id=48884853">Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS | Hacker News</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math">Math - JavaScript - MDN Web Docs</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出，该技术可能更有效地识别浏览器版本范围而非仅操作系统，但大多数用户不会伪造用户代理，因此实用性有限。有观点认为这篇文章是 Scrapfly 公司利用 AI 分析指纹技术以推广其反爬服务；也有评论呼吁推动正确舍入的数学函数来消除此类指纹差异。

**标签**: `#fingerprinting`, `#browser security`, `#privacy`, `#JavaScript`, `#Chromium`

---

<a id="item-2"></a>
## [研究显示 Claude Code token 开销远高于 OpenCode](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 8.0/10

一项实证研究发现，Claude Code 每次请求平均发送约 33,000 个 token，而 OpenCode 仅发送约 7,000 个 token，表明 Claude Code 的系统提示和缓存策略导致更高的 token 消耗。 token 开销直接影响使用成本，对于依赖 API 调用的大规模开发团队，这一差距可能导致显著的费用差异，并促使开发者重新评估编码代理的效率和经济性。 研究者在 Claude Code 和 OpenCode 与 Anthropic 端点之间添加日志记录，捕获所有请求和返回的 usage 块，排除了特殊情况的干扰后，确认 Claude Code 因更大的系统提示和低效的缓存策略而消耗更多 token。

hackernews · systima · Jul 12, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: Claude Code 是 Anthropic 推出的终端编码代理工具，能够理解代码库、编辑文件并运行命令。OpenCode 是一个开源编码代理，支持在终端、IDE 或桌面使用。两者都连接 Anthropic 的语言模型，但架构和优化策略不同，导致 token 使用效率差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/claude-code?ref=contraption.co">Claude Code : Deep Coding at Terminal Velocity \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有人指出子代理（sub agents）会大量消耗 token，而 Claude Code 的缓存策略可能被设计为增加用量以鼓励订阅；另一些人强调，除了初始提示大小，工具质量和减少往返调用同样重要，单纯比较 token 数量可能不够全面。

**标签**: `#AI agents`, `#token usage`, `#Claude Code`, `#OpenCode`, `#cost efficiency`

---

<a id="item-3"></a>
## [陶哲轩谈用 LLM 编码代理构建应用](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 8.0/10

著名数学家陶哲轩在博客中分享了他使用基于 LLM 的编码代理（如 Claude）制作数据可视化和交互式应用的经验，并讨论了这类工具的潜力和局限性。 这展示了 LLM 编码代理正在降低软件创建的门槛，使非专业程序员也能快速构建定制化工具，可能对教育、科研和日常工作产生深远影响。 陶哲轩指出，LLM 生成的代码适合作为论文补充的非关键部分，但不宜用于核心任务；他同时强调，用户仍需具备一定的审查能力以规避风险。

hackernews · subset · Jul 12, 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48880170)

**背景**: LLM 编码代理是一种结合大语言模型生成能力与迭代调试的自动化开发工具，它通过编译、运行反馈不断改进代码。这类工具近年因“氛围编程”（Vibe Coding）概念而流行，允许用户用自然语言描述需求并快速获得可运行程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/llm-based-coding-agents">LLM - Based Coding Agents</a></li>
<li><a href="https://arxiv.org/pdf/2510.12399">A Survey of Vibe Coding with Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 社区评论整体积极，认为 LLM 编码代理显著提升了教学效率（如快速生成 8 位计算机模拟器）和软件开发普及度。也有调侃称“菲尔兹奖得主也开始像普通人一样向 LLM 求助”，同时认可平衡视角：这是有用的工具，但需要谨慎对待其输出。

**标签**: `#AI`, `#coding agents`, `#LLMs`, `#software development`, `#education`

---

<a id="item-4"></a>
## [爱尔兰数据中心耗电占全国 23%](https://www.theregister.com/on-prem/2026/07/11/irish-datacenters-now-guzzle-23-of-the-countrys-electricity/5270013) ⭐️ 8.0/10

最新数据显示，爱尔兰的数据中心现消耗该国约 23%的电力，这一比例较往年显著上升。 该数据引发了对数据中心经济价值与能源负担之间平衡的广泛讨论，可能影响全球科技公司的选址决策和国家的能源政策。 数据中心虽带来就业和经济活动，但同时也推高了居民电价（近年上涨约 40%），且爱尔兰宽带费用在欧洲属于较高水平。

hackernews · Bender · Jul 12, 20:16 · [社区讨论](https://news.ycombinator.com/item?id=48884322)

**背景**: 数据中心需要大量电力运行服务器和冷却系统。爱尔兰凭借低企业税和凉爽气候吸引了众多科技巨头建设数据中心，但电力需求激增已对电网造成压力。

**社区讨论**: 评论中有人认为数据中心创造了价值，不应一味批评；也有人担忧电价上涨和基础设施压力；另有用户将爱尔兰与加州对比，指出加州数据中心人均耗电更高但批评较少。

**标签**: `#energy`, `#datacenters`, `#infrastructure`, `#Ireland`, `#electricity`

---

<a id="item-5"></a>
## [我热爱 LLM，我厌恶炒作](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

George Hotz 发表博客文章，表达对大型语言模型（LLM）的喜爱，同时批评围绕 AI 的过度炒作。他提出 AI 确实创造价值，但前沿实验室可能无法捕获这些价值。 作为 AI 领域知名人物，Hotz 的观点有助于平衡当前对 AI 的过度乐观，提醒关注价值分配和开源力量。文章引发关于 AI 估值、生产力提升和开源未来的深入讨论。 Hotz 认为前沿实验室的估值过高，因为价值可能流向用户而非开发者。他观察到生产力提升并未转化为公开可见的软件创新，而是被用于私有定制化项目。

hackernews · therepanic · Jul 12, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**背景**: 大型语言模型（LLM）是能够理解和生成人类语言的人工智能系统，如 GPT 系列。近年来，LLM 引发巨大炒作，部分公司估值极高。开源 LLM（如 Llama）的兴起使个人和小团队也能构建定制解决方案。

**社区讨论**: 社区评论普遍认同 Hotz 的观点，认为前沿实验室难以捕获 AI 创造的价值。有用户指出生产力提升体现在私有 homelab 项目中，并担忧开源生态的平衡可能被打破。也有用户提到模型迭代（如 Sonnet 4）正在加速进步，对 ASI 时间线持不确定态度。

**标签**: `#LLMs`, `#AI Hype`, `#Open Source`, `#Productivity`

---

<a id="item-6"></a>
## [电影特效到 CGI 的转型与 LLM 影响软件开发类比](https://fabiensanglard.net/extinct/index.html) ⭐️ 8.0/10

文章将电影行业从实际特效转向 CGI 的过程，类比于软件工程中从手写代码转向使用大型语言模型（LLM）的趋势。作者认为，拒绝 LLM 的开发者将因产出不足而落后，但阅读和理解代码的能力仍然重要。 这个类比引发了对技术采用中不可逆变革的深入讨论，提醒开发者 LLM 可能像 CGI 改变电影制作一样，根本性地改变软件开发流程、技能要求和行业结构。 电影行业转向 CGI 的部分原因是非工会化的数字特效公司能降低成本，但如今人们又开始怀念实际特效的质感。类似地，软件开发中使用 LLM 虽能提高生产率，但也可能带来质量下降或技能贬值的问题，甚至可能出现反弹。

hackernews · zdw · Jul 12, 15:17 · [社区讨论](https://news.ycombinator.com/item?id=48881830)

**背景**: 实际特效指使用物理模型、微缩景观等实景技术，而 CGI 通过数字手段创建视觉效果。类似地，传统软件开发中每一行代码都由人类编写，而 LLM（如 GPT-4）能自动生成代码片段。电影工业中，CGI 曾降低成本和时间，但如今部分创作者和观众重新认可实际特效的独特价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sei.cmu.edu/blog/application-of-large-language-models-llms-in-software-engineering-overblown-hype-or-disruptive-change/">Application of Large Language Models (LLMs) in Software Engineering: Overblown Hype or Disruptive Change? | CMU Software Engineering Institute</a></li>
<li><a href="https://www.researchgate.net/publication/375989472_THE_EVOLUTION_OF_VISUAL_EFFECTS_IN_CINEMA_A_JOURNEY_FROM_PRACTICAL_EFFECTS_TO_CGI">(PDF) the evolution of visual effects in cinema: a journey from...</a></li>
<li><a href="https://www.studiobinder.com/blog/what-is-cgi-meaning-definition/">What is CGI ? How CGI Works in Movies and Animation</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体上认可这个类比，但指出更深层次：电影业转向 CGI 部分因非工会化降低成本，而 CGI 泛滥后又引发对实际特效的回归。一些开发者质疑“生产率落后”的说法，认为软件工程中很少以代码量评价绩效。还有评论强调使用 LLM 需反复迭代 PR 来保证质量，实际提速有限，并讨论了工作乐趣与效率之间的矛盾。

**标签**: `#technology adoption`, `#LLMs`, `#software engineering`, `#industry trends`, `#AI impact`

---

<a id="item-7"></a>
## [慢软件：高延迟系统设计的辩护](https://www.sigops.org/2026/slow-software-the-case-for-high-latency-systems-development/) ⭐️ 8.0/10

ACM SIGOPS 发表一篇观点文章，主张高延迟系统具有被忽略的优势，应当作为一种有意的设计选择。 该文章挑战了系统设计领域长期追求低延迟的主流范式，可能引发对延迟取舍的重新思考，影响软件架构师和开发者的设计决策。 文章来自 ACM SIGOPS 这一权威组织，标题为《Slow Software: The Case for High-latency Systems Development》，但其正文内容尚未公开，仅提供 Lobste.rs 评论链接。

rss · Lobsters · Jul 12, 16:47

**背景**: 在系统设计中，延迟是指数据从发送到接收所需的时间，高延迟意味着显著延迟。通常，工程师会尽力降低延迟以提升用户体验，但高延迟在某些场景下（如批处理、节能、容错）可能带来好处。SIGOPS 是计算机操作系统领域的顶级学术团体，其发表的观点文章通常具有很强的影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SIGOPS">SIGOPS</a></li>
<li><a href="https://www.geeksforgeeks.org/system-design/high-latency-vs-low-latency-system-design/">High Latency vs Low Latency | System Design - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#systems design`, `#latency`, `#software engineering`, `#opinion`, `#SIGOPS`

---

<a id="item-8"></a>
## [黑客利用 SQL 注入攻破苹果系统实现远程代码执行](https://projectdiscovery.io/blog/hacking-apple-with-sql-injection) ⭐️ 8.0/10

一名安全研究员公开了如何通过 SQL 注入漏洞，成功从苹果公司系统中获取远程代码执行权限。 这一发现表明即便是大型科技公司也可能存在严重 Web 安全漏洞，攻击者可能利用此类漏洞获取敏感数据或完全控制服务器。 该漏洞链从 SQL 注入开始，结合其他攻击技术最终实现了远程代码执行。目前苹果公司已修复该漏洞。

rss · Lobsters · Jul 12, 10:50

**背景**: SQL 注入是一种常见 Web 漏洞，攻击者通过在输入框中插入恶意 SQL 语句，能操纵数据库。远程代码执行（RCE）则允许攻击者在服务器上运行任意命令，是最严重的漏洞之一。

**标签**: `#security`, `#sql-injection`, `#apple`, `#remote-code-execution`, `#web-security`

---

<a id="item-9"></a>
## [Tiny Emulators：引脚级模块化 8 位模拟器](https://floooh.github.io/tiny8bit-preview/index.html) ⭐️ 7.0/10

Andre Weissflog 的 Tiny Emulators 项目展示了一种适用于 8 位系统的引脚级模块化模拟方法，允许在浏览器中运行多个 8 位计算机的软件。 这种方法通过自包含模块和明确定义的接口实现了高度灵活性，为模拟器设计和互操作性带来新思路，对复古计算爱好者和模拟器开发者有重要参考价值。 该模拟器基于 WebAssembly 在浏览器中运行，支持 KC85/2/3/4、Amstrad CPC 等多种 8 位计算机，但部分游戏音量大且项目已有 8 年历史。

hackernews · naves · Jul 12, 20:23 · [社区讨论](https://news.ycombinator.com/item?id=48884395)

**背景**: 引脚级模拟是一种精确模拟硬件的方法，通过模拟芯片上每个引脚的电平变化和时序来保持兼容性。传统模拟通常只模拟指令集或内存映射，而引脚级模拟更细致但性能开销大。Tiny Emulators 正是采用这种模型，将组件视为独立模块并通过引脚交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://floooh.github.io/tiny8bit/">Tiny Emulators</a></li>
<li><a href="https://blog.adafruit.com/2025/04/28/the-tiny-emulators-allows-8-bit-gameplay-in-browser/">The Tiny Emulators allows 8-bit gameplay in browser</a></li>
<li><a href="https://8bitnews.io/article/tiny-emulators">Tiny Emulators</a></li>

</ul>
</details>

**社区讨论**: 评论普遍赞赏其设计，Lerc 认为引脚级模拟的模块化接口是互操作性中未被充分探索的领域；infinite_spin 提醒部分游戏音量较大；gabrielsroka 指出项目已有 8 年历史。

**标签**: `#emulation`, `#retrocomputing`, `#modular design`, `#8-bit`, `#hobbyist`

---

<a id="item-10"></a>
## [迁移 AI 代理至 GPT-5.6：速度快 2.2 倍，成本低 27%](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6) ⭐️ 7.0/10

Ploy 公司将其生产环境中的 AI 代理从 Opus 模型迁移至 GPT-5.6 系列的 Sol 和 Luna 模型，实现了 2.2 倍的构建速度和 27%的成本降低。 这一迁移展示了 GPT-5.6 在实际生产环境中的显著性能提升和成本效益，为其他企业在模型选择与迁移时提供了具体参考，验证了模型升级对业务的实际价值。 Ploy 的 AI 代理负责构建和编辑营销网站，迁移后在分类任务上也有改进。但 Sol 模型成本较高，因此仅用于核心编排，而 Luna 模型用于实际工具调用，一次 Sol 的开销可运行五次 Luna。

hackernews · brryant · Jul 12, 17:13 · [社区讨论](https://news.ycombinator.com/item?id=48882716)

**背景**: GPT-5.6 是 OpenAI 于 2026 年 7 月发布的模型系列，包含 Sol（旗舰推理）、Terra（通用）和 Luna（轻量快速）三个版本，分别针对不同复杂度的任务。企业常需根据成本与性能权衡选择适合的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>
<li><a href="https://kie.ai/gpt-5-6">OpenAI GPT - 5 . 6 API: Frontier Reasoning and Agentic Coding... | Kie.ai</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有用户认为原文的 LLM 写作风格不佳，但也有用户表示自己迁移到 GPT-5.6 后获得了类似改进。部分评论强调了模型路由策略的重要性，认为将 Sol 用于关键任务、Luna 用于高频调用可平衡成本与效果。

**标签**: `#AI agents`, `#GPT-5.6`, `#performance optimization`, `#cost reduction`, `#production migration`

---

<a id="item-11"></a>
## [Rust arena 内存管理解决三年旧问题](https://giacomocavalieri.me/writing/gleam-rust-arenas) ⭐️ 7.0/10

一篇技术文章详细介绍了如何使用 Rust 中的 arena 分配器来解决一个存在三年的内存管理问题，展示了一种巧妙的内存管理技巧。 这一案例展示了 arena 分配在解决长期内存问题中的实际价值，对 Rust 社区和系统编程领域具有启发意义。它提供了一种高效的内存管理策略，可能被更多项目采纳。 Arena 分配器通过预先分配一大块连续内存并线性分配对象，最后统一释放，从而减少分配和释放的开销。Rust 中的 arena 常用于管理同生命周期对象，并支持通过指针比较实现快速相等性判断。

rss · Lobsters · Jul 12, 18:58

**背景**: 内存管理中的 arena 分配是一种策略，它预先分配一大块连续内存，在该区域内顺序分配对象，然后一次性释放整个区域。与传统 malloc/free 相比，arena 分配减少了大量小操作，特别适合管理具有相同生命周期的对象。Rust 的编译器 rustc 内部就广泛使用了 arena 来管理内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@syntaxSavage/arena-allocation-in-rust-fast-memory-for-short-lived-objects-2e55a89257d6">Arena Allocation in Rust: Fast Memory for Short-Lived Objects | by SyntaxSavage | Medium</a></li>
<li><a href="https://rustc-dev-guide.rust-lang.org/memory.html">Memory management in rustc - Rust Compiler Development Guide</a></li>

</ul>
</details>

**标签**: `#Rust`, `#arenas`, `#memory management`

---

<a id="item-12"></a>
## [InfiniteDiffusion：融合扩散模型与程序化生成的地形算法](https://xandergos.github.io/terrain-diffusion/) ⭐️ 7.0/10

InfiniteDiffusion 是一种无需训练的算法，它重新设计了扩散模型的采样过程，实现了惰性和无边界生成，从而将扩散模型的高保真度与程序化噪声的实用性（如无缝无限范围、种子一致性和常数时间生成）结合起来。 该研究对游戏开发和 AI 领域具有重要意义，因为它弥合了 AI 生成内容的高保真度与程序化生成的实用效率之间的鸿沟，有望革新开放世界地形的生成方式。 该算法无需额外训练，可直接应用于现有扩散模型；它支持生成无缝衔接的无限大地形，且每次生成结果可通过种子复现，时间开销恒定，类似传统 Perlin 噪声但质量更高。

rss · Lobsters · Jul 12, 19:56

**背景**: 传统程序化地形生成依赖于 Perlin 噪声等数学函数，虽然快速且可无限扩展，但缺乏真实感；而扩散模型能生成高保真图像，但通常需要大量计算且难以扩展到任意大的场景。InfiniteDiffusion 将两者的优势结合，提供了一种实用且高质量的解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.08309">[2512.08309] InfiniteDiffusion: Bridging Learned Fidelity and Procedural Utility for Open-World Terrain Generation</a></li>
<li><a href="https://xandergos.github.io/terrain-diffusion/">InfiniteDiffusion</a></li>
<li><a href="https://github.com/xandergos/terrain-diffusion">GitHub - xandergos/ terrain -diffusion: Procedural generation with...</a></li>

</ul>
</details>

**标签**: `#diffusion-models`, `#procedural-generation`, `#terrain-generation`, `#game-development`, `#ai`

---

<a id="item-13"></a>
## [EF Core 11 提升拆分查询性能](https://steven-giesel.com/blogPost/d4401fd0-805a-4703-9d9e-5fe3b57c25ea) ⭐️ 7.0/10

EF Core 11 引入了针对拆分查询的性能优化，使得使用 AsSplitQuery() 方法时查询执行更快。 这一改进直接提升了 EF Core 在处理包含多个集合加载的复杂查询时的效率，减少了因多次数据库往返带来的延迟，尤其有益于数据密集型应用。 拆分查询通过将单个大型 JOIN 查询分解为多个较小 SQL 查询来避免笛卡尔乘积问题，但此前存在额外的性能开销；EF Core 11 优化了这一过程，使拆分查询整体速度更快。

rss · Lobsters · Jul 12, 14:02

**背景**: Entity Framework Core（EF Core）是 .NET 平台的对象关系映射（ORM）框架。当查询包含多个导航属性（如包含多个子集合）时，EF Core 默认使用单个 JOIN 查询，可能导致数据重复（笛卡尔乘积）和性能下降。拆分查询通过使用 AsSplitQuery() 方法，为每个集合执行单独的 SQL 查询，但过去会带来额外的数据库往返开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/ef/core/querying/single-split-queries">Single vs. Split Queries - EF Core | Microsoft Learn</a></li>
<li><a href="https://dev.to/stevsharp/optimize-ef-core-queries-with-assplitquery-20on">🚀 Optimize EF Core Queries with AsSplitQuery() - DEV Community</a></li>

</ul>
</details>

**标签**: `#Entity Framework`, `#C#`, `#Performance`, `#.NET`, `#Database`

---

<a id="item-14"></a>
## [Motorola MR2600 路由器存在未认证远程代码执行漏洞](https://mrbruh.com/motorola/) ⭐️ 7.0/10

安全研究员披露了 Motorola MR2600 路由器中的一个未认证远程代码执行漏洞，攻击者无需身份验证即可完全控制设备。 该漏洞影响广泛使用的家用路由器，可能被恶意利用发起网络攻击或窃取隐私，凸显了 IoT 设备安全性的薄弱环节。 漏洞详情及 PoC（概念验证代码）已在个人博客上公开，但官方尚未发布固件更新修复该问题。

rss · Lobsters · Jul 12, 14:03

**背景**: 远程代码执行（RCE）漏洞允许攻击者在目标设备上运行任意代码，未认证意味着无需登录凭据即可触发。此类漏洞在路由器等物联网设备中尤为危险，因为它们常被用作网络攻击的跳板。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.motorola.com/us/en/p/motoaccessories/motohome/modems---routers/motorolamr2600">motorola mr2600 | MOTOROLAMR2600 | motorola</a></li>
<li><a href="https://www.amazon.com/MOTOROLA-AC2600-Gigabit-Extended-MR2600/dp/B07CDQNHRX">Amazon.com: Motorola MR2600 Smart WiFi Router with Range Boost | Easy Plug and Play Setup | Up to 64 Devices | Dual Band Gigabit Speeds | Live Chat Support : Electronics</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#RCE`, `#IoT`, `#router`

---