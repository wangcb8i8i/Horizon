---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> From 31 items, 14 important content pieces were selected

---

1. [谷歌发布 Gemini 3.8 Flash 及网络安全专用版](#item-1) ⭐️ 9.0/10
2. [调查：三网站生成 21.5 万 AI“最佳软件”页面，Perplexity 引以为据](#item-2) ⭐️ 8.0/10
3. [无需完整依赖类型即可表达依赖 if 表达式](#item-3) ⭐️ 8.0/10
4. [从零实现 FMA，发现 C 与 Rust 标准库中的舍入 Bug](#item-4) ⭐️ 8.0/10
5. [Meta 发布 Muse Spark 1.3：登顶 DeepSWE，极致性价比](#item-5) ⭐️ 7.0/10
6. [谷歌胜诉，广告技术业务免遭强制拆分](#item-6) ⭐️ 7.0/10
7. [Mistral 训练数据退出机制引发信任争议](#item-7) ⭐️ 7.0/10
8. [Poisson 圆盘采样图解：Bridson 算法及其应用](#item-8) ⭐️ 7.0/10
9. [静态分配，恒定工作量：系统编程探索](#item-9) ⭐️ 7.0/10
10. [Go 团队推出 goroutine 泄漏分析工具](#item-10) ⭐️ 7.0/10
11. [PostgreSQL 正则扩展 pg_tre 与 pg_re2 发布](#item-11) ⭐️ 7.0/10
12. [CTTI 指数级膨胀，RTTI 线性扩展](#item-12) ⭐️ 7.0/10
13. [用 ImHex 逆向未知文件格式：作者实战指南](#item-13) ⭐️ 7.0/10
14. [追踪 np.add：从 Python 到底层 C 实现的完整调用链](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 3.8 Flash 及网络安全专用版](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 9.0/10

谷歌宣布推出 Gemini 3.8 Flash 和 3.8 Flash Cyber，这是 Gemini 3 模型家族的最新迭代，在软件工程和智能体知识工作流方面带来性能提升，并支持可定制的推理强度（高、中、低）。其中 3.8 Flash Cyber 专为网络安全防御者设计，可通过 Fairwind 项目供受信任的防御者使用。 此次发布意义重大，因为 Gemini 3.8 Flash 以与 3.7 Flash 相同的低价提供了接近 Opus 5 级别的智能表现（Artificial Analysis 显示智能评分为 59），并在 HTML/JavaScript 生成上表现突出，可能进一步拉低高质量 AI 应用的成本门槛。专门的网络安全版本则表明谷歌正将 AI 能力深入应用于自动化漏洞发现与修复，对安全行业格局可能产生深远影响。 据社区用户测试，从提示词到生成一个完整的 HTML 作品仅需约 13 秒、花费 1.8 美分，速度与成本优势明显。模型继续支持可调节的思考强度（high/medium/low），但部分用户反馈 3.8 在低思考强度下相比 3.7 存在回归。此外，Gemini 系列仍保持独特的多模态能力，能直接接受音频和视频输入，而 OpenAI 和 Anthropic 的旗舰模型仍仅支持图像输入。

hackernews · bratao · Sep 2, 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553)

**背景**: Gemini 3 Flash 系列是谷歌面向高频、低成本场景推出的轻量级模型，在保持较强推理能力的同时优化速度和成本。这类模型常用于智能体工作流、代码生成、多媒体分析等任务。与完整版旗舰模型不同，Flash 版本通常在参数量或推理深度上有所精简，但通过可调节的思考强度来平衡质量、成本和延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3 . 8 Flash and 3 . 8 Flash Cyber</a></li>
<li><a href="https://cybersecuritynews.com/gemini-3-8-flash-cyber/">Google Launches Gemini 3 . 8 Flash Cyber to Find Vulnerabilities and...</a></li>

</ul>
</details>

**社区讨论**: 社区整体反馈积极，用户 simonw 特别称赞其速度和 HTML/JavaScript 生成能力，并以极低成本快速产出了令人印象深刻的网页作品；mattlondon 指出该模型在 deepswe 基准上排名第一，且智能评分与 Opus 5 Medium 相当，但对实际使用体验持保留态度。也有用户如 jampa 在旅行规划等真实场景中认为它优于此前版本，但 simonw 同时注意到 3.8 在低思考强度上相比 3.7 可能有所退步。

**标签**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#model release`

---

<a id="item-2"></a>
## [调查：三网站生成 21.5 万 AI“最佳软件”页面，Perplexity 引以为据](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

一项调查发现，三个网站利用程序化 SEO 生成了超过 215,128 个针对 AI 的“最佳软件”推荐页面，而 Perplexity 等 AI 搜索工具会在答案中引用这些页面。这揭示了 AI 搜索生态中被机器批量制造内容渗透的严重程度。 该问题意味着用户在使用 Perplexity 等 AI 搜索工具时，获得的结果可能被低质量内容农场操纵，而非基于真实可靠的信息。这会侵蚀用户对 AI 推荐和整个搜索生态的信任。 这些页面通常采用自动化方式大规模生成，专门为迎合 AI 爬虫和生成引擎的引用偏好而设计，即所谓 AEO。社区用户也反映，Claude、Codex 等模型在搜索时常常引用了由 AI 生成或企业自建的对比页面，模型普遍缺乏对信息来源动机的审视。

hackernews · jakobgreenfeld · Sep 2, 13:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**背景**: Perplexity 是一家提供 AI 答案引擎的公司，它利用大型语言模型并结合实时网络搜索来回答用户问题。内容农场则是指批量生产低质量在线内容的机构，随着 AI 工具普及，这类内容的生产速度和规模大幅提升。程序化 SEO 是用技术手段自动化、规模化生成网页以获取搜索流量的做法，正被这类内容农场用于制造大量看似权威的推荐页面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perplexity_AI">Perplexity AI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_farm">Content farm - Wikipedia</a></li>
<li><a href="https://www.forbes.com/sites/bernardmarr/2023/05/16/the-danger-of-ai-content-farms/">The Danger Of AI Content Farms</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍表达了对 AI 推荐可靠性的担忧。有用户指出大语言模型更偏爱自己生成的文本，并提到 Claude 在搜索时经常引用 AI 生成的网站；还有人分享 Perplexity 优化响应速度后结果质量明显下降，链接和参考经常是垃圾。另有用户认为模型对信息来源动机缺乏怀疑，这是可被利用的缺陷，但窗口期终将过去。

**标签**: `#AI search`, `#Content farms`, `#LLM reliability`, `#Perplexity`, `#SEO manipulation`

---

<a id="item-3"></a>
## [无需完整依赖类型即可表达依赖 if 表达式](https://haskellforall.com/2026/09/dependent-if-expressions) ⭐️ 8.0/10

Gabriella439 在博文中探索了一种在 Haskell 中模拟“依赖 if 表达式”的新技术，使类型能够依据运行时条件分支，而无须引入完整的依赖类型系统。该文提出了一种在现有 Haskell 类型级编程能力之内的编码方式，为类型系统扩展提供了新思路。 这一工作填补了普通 Haskell 类型级编程与未来完整依赖类型（Dependent Haskell）之间的空白，有助于开发者在当前 GHC 中表达更精细的不变量。对于经常利用类型系统保证程序安全的函数式编程社区来说，这是一项有实用价值的探索。 由于新闻正文未完整公开，尚无法确定其具体编码细节；不过基于相关文献，这类技术通常依赖 DataKinds、TypeFamilies、GADTs 或单例（singletons）等扩展来部分模拟依赖条件。作者 Gabriella439 是 Haskell 社区中知名的技术作家，其建议一般基于已被验证的类型级编程技术。

rss · Lobsters · Sep 2, 17:52

**背景**: 依赖类型允许类型依赖于具体值，例如长度索引列表的 append 操作返回的列表长度是输入长度的函数；完整的依赖类型虽然在 Haskell 中尚未实现，但可通过“伪造（faking）”技术达到类似效果。这种技术将数据类型复制到类型层面，用类型构造器和类型类模拟对应的值构造器与类型约束，从而表达依赖 if 等条件类型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cambridge.org/core/journals/journal-of-functional-programming/article/faking-it-simulating-dependent-types-in-haskell/A904B84CA962F2D75578445B703F199A">Faking it Simulating dependent types in Haskell</a></li>
<li><a href="https://wiki.haskell.org/Dependent_type">dependent type - HaskellWiki</a></li>

</ul>
</details>

**标签**: `#Haskell`, `#dependent types`, `#type-level programming`, `#functional programming`

---

<a id="item-4"></a>
## [从零实现 FMA，发现 C 与 Rust 标准库中的舍入 Bug](https://shnatsel.github.io/implementing-fma-finding-bugs-in-std/) ⭐️ 8.0/10

开发者 shnatsel 通过详细实现一次融合乘加（FMA），发现 C 和 Rust 标准库中的 fma 实现存在细微缺陷。这些缺陷会导致特定浮点输入下计算结果未能正确舍入。 FMA 是数值计算中的基础操作，标准库实现如果存在缺陷，可能让大量依赖它的应用产生难以察觉的精度损失。这项发现也提醒人们，即便是被广泛使用的 C 和 Rust 标准库，仍需要在极端浮点边界条件下做充分验证。 融合乘加要求对 a×b+c 的无限精度中间结果只做一次舍入，软件实现需要精确追踪 round 和 sticky 位，因此很难正确实现。该文章揭示的缺陷不满足 IEEE 754 对正确舍入的要求，也印证了“许多系统数学库的 fma 实现存在 bug”这一长期认知。

rss · Lobsters · Sep 2, 16:19

**背景**: FMA（融合乘加）是一种浮点运算指令，它在一次操作中计算 a×b+c，并且只对中间结果做一次舍入，从而避免分步乘法和加法带来的双重舍入误差。该指令在现代 CPU（如 x86-64 的 FMA3、ARM）和 GPU 中广泛支持，常用于矩阵乘法、点积等数值密集计算。由于不同硬件对 FMA 的支持情况不同，有时需要通过软件方式实现 fma，而正确舍入的软件实现需要精细的位级算法，因而容易出现缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multiply–accumulate_operation">Multiply–accumulate operation - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/28630864/how-is-fma-implemented">floating point - How is fma () implemented - Stack Overflow</a></li>

</ul>
</details>

**标签**: `#FMA`, `#floating-point`, `#Rust`, `#C`, `#standard library`, `#bug discovery`

---

<a id="item-5"></a>
## [Meta 发布 Muse Spark 1.3：登顶 DeepSWE，极致性价比](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 7.0/10

Meta 正式发布 Muse Spark 1.3，在 DeepSWE 基准上取得 75.4 分，成为当前最高分。相较 1.2 版本，新版在长周期编码、上下文跟踪和工具使用上表现更稳定，质量提升明显。 这显示低成本开放模型在真实软件工程任务上已接近前沿水平，将加剧 AI 模型的价格竞争。Meta 同时推出的“contributor”付费档位以明确的数据训练权益换取低价，可能成为行业透明度与定价模式的新标杆。 Muse Spark 1.3 针对长周期编码工作流调优，能在单一长线程中跟踪上下文和先前结果，处理混乱或冲突输入并在需要时主动提问。其低价格档位（如 muse-spark-1.3-contributor）以允许 Meta 使用数据训练为条件，据实测生成一张 SVG 仅需约 4.2 美分。

hackernews · bvaldivielso · Sep 2, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**背景**: Muse Spark 是 Meta Superintelligence Labs（MSL）推出的多模态大语言模型系列，2026 年首次发布，面向编程、推理与 AI 辅助场景。DeepSWE 是 2026 年出现的软件工程基准，为规避数据污染而完全从零编写任务，要求模型在真实开源仓库中解决长期未修复问题。本次评测中，Muse Spark 1.3 的 75.4 分击败了此前 Google Gemini 3.8 Flash 数小时前创下的纪录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-spark-1-3">Introducing Muse Spark 1.3 | Meta AI Research</a></li>
<li><a href="https://deepswe.datacurve.ai/">DeepSWE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Muse_Spark">Muse Spark - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 开发者普遍认可 1.3 版本的质量与成本优势，例如 Simon Willison 实测生成 SVG 仅花费 4.2 美分，且成品优于 1.2 版（后者还会擅自添加动画）。不少评论称赞 Meta 将“是否允许用你的数据训练”与价格挂钩的做法透明，也有用户指出该模式恰好揭示了 token 训练数据的真实价值；与此同时，部分评论未忘提及 Meta 面临未成年人社交成瘾的诉讼。

**标签**: `#AI`, `#Meta`, `#LLM`, `#Muse Spark`, `#Benchmarks`

---

<a id="item-6"></a>
## [谷歌胜诉，广告技术业务免遭强制拆分](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) ⭐️ 7.0/10

美国政府对谷歌广告技术业务提起的反垄断诉讼于 2026 年 9 月 2 日以谷歌胜诉告终，法院拒绝了强制谷歌出售其广告技术业务的请求。这意味着谷歌避免了一场可能改变数字广告市场格局的业务拆分。 这一判决对大型科技公司的反垄断执法产生深远影响，尤其是针对通过拆分来恢复市场竞争的救济方式。谷歌得以继续保留其整合了广告买卖全链条的广告技术业务，监管机构未来采取类似拆分行动将面临更大阻力。 据报道，谷歌广告技术业务去年的收入约为 300 亿美元，约占母公司 Alphabet 总收入的 8%，但分析师估计其对利润的贡献不足 1%，且该业务收入已连续 16 个季度下滑。有评论因此认为这是一个“没人关心的业务”。

hackernews · donohoe · Sep 2, 14:46 · [社区讨论](https://news.ycombinator.com/item?id=49537131)

**背景**: 广告技术（ad tech）是指帮助广告主、发布商和中介机构购买、销售、投放和分析数字广告的软件与工具，例如需求方平台（DSP）和供应方平台（SSP）等。在反垄断执法中，拆分（divestiture）是一种常见的补救措施，要求企业出售部分资产或业务单元以恢复市场竞争。美国司法部此前指控谷歌在广告技术领域存在垄断行为，因而寻求让谷歌剥离相关业务，但本次判决未支持这一拆分请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://advertising.amazon.com/library/guides/what-is-adtech">What is AdTech? A Beginner's Guide | Amazon Ads</a></li>
<li><a href="https://business.linkedin.com/advertise/resources/marketing-terms/what-is-adtech">What is AdTech? The fundamental guide</a></li>
<li><a href="https://uslawexplained.com/divestiture">Divestiture: The Ultimate Guide to Corporate Splits and ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体对判决结果不满，认为大型科技公司过于轻易地规避了重大反垄断执法。有观点指出企业合并容易而拆分极难，立法应使二者难度对等；也有人质疑该业务收入占比低、拆分意义有限；还有人提议通过对垄断企业累进征税来促使企业自行拆分，避免长期诉讼。

**标签**: `#antitrust`, `#google`, `#adtech`, `#regulation`, `#big tech`

---

<a id="item-7"></a>
## [Mistral 训练数据退出机制引发信任争议](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) ⭐️ 7.0/10

Mistral 官方帮助文档发布“Can I opt out of my input or output data being used for training”页面，说明用户对输入/输出数据用于训练的选择权。该页面在社区引发讨论，多名用户对 AI 企业能否真正遵守退出（opt-out）承诺表示怀疑。 该新闻反映了企业用户对 AI 训练数据隐私的普遍担忧，尤其是欧盟企业选择本土 AI 供应商时的信任问题。若用户无法确信退出机制已被严格执行，可能影响 Mistral 等 AI 平台在企业市场的采用。 有用户指出，Mistral 的 Pro 和 Team 套餐默认开启训练数据共享，且团队设置曾允许集中禁用训练，但后续更新后这些选项被更改，Team 套餐也变为默认开启。社区讨论中还有人提到 GitHub Copilot 等服务的类似“撤毯”行为（如默认开启训练）。

hackernews · teekert · Sep 2, 12:30 · [社区讨论](https://news.ycombinator.com/item?id=49535284)

**背景**: 大型语言模型（LLM）常使用用户输入与输出来改进模型性能，“退出”（opt-out）机制即用户要求平台不将自己的数据用于训练。Mistral AI 是一家法国 AI 研究实验室，开发开源与商用大模型，并面向企业提供平台服务，因此在欧洲用户中有一定市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mistral_AI">Mistral AI - Wikipedia</a></li>
<li><a href="https://mistral.ai/">Frontier AI LLMs, assistants, agents, services | Mistral</a></li>

</ul>
</details>

**社区讨论**: 评论区整体情绪以怀疑为主，多名用户认为 AI 公司不会真正尊重退出选择，甚至可能绕过协议收集数据。也有用户分享自己转向更注重隐私的替代服务，并批评新闻标题具误导性，称原文仅是帮助文档中的常见问题。

**标签**: `#AI`, `#privacy`, `#data-training`, `#Mistral`, `#opt-out`

---

<a id="item-8"></a>
## [Poisson 圆盘采样图解：Bridson 算法及其应用](https://stripeacross.com/posts/poisson-disk-sampling/) ⭐️ 7.0/10

这篇文章以可视化方式深入讲解了 Poisson 圆盘采样的原理，重点介绍 Robert Bridson 提出的快速算法及其在图形学与程序化生成中的典型应用。文章在社区获得较高评分，引发了关于算法实现细节的讨论。 Poisson 圆盘采样生成的蓝噪声分布广泛用于抗锯齿、纹理合成、物体摆放与随机地图生成等场景，理解其核心算法有助于开发者在质量与性能之间做出更优取舍。这篇文章降低了理解门槛，对图形学和程序化内容生成相关从业者具有实用参考价值。 文章详细说明了 Bridson 算法如何借助活动列表（active list）与环形（annulus）采样，在近似线性时间内生成满足最小间距约束的采样点。有读者指出，由于算法依赖活动列表，直接移植到着色器逐像素执行存在困难，实际中可用网格哈希加抖动的替代方案。

hackernews · vismit2000 · Sep 2, 13:47 · [社区讨论](https://news.ycombinator.com/item?id=49536177)

**背景**: Poisson 圆盘采样是一种随机采样方法，要求任意两点之间的距离不小于指定半径，从而获得空间上均匀且带随机性的蓝噪声点集。Bridson 算法是其中广为推荐的快速实现，它利用背景网格划分空间，只需检查相邻单元即可加速候选点的验证；这类采样常被用于超采样抗锯齿和纹理生成等方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Poisson_disk_sampling">Poisson disk sampling</a></li>
<li><a href="https://www.jasondavies.com/poisson-disc/">Poisson-Disc Sampling - Jason Davies</a></li>

</ul>
</details>

**社区讨论**: 评论区整体反馈积极，有用户称其为“神奇的算法”。讨论集中于实现细节：一位听众提到未能找到逐像素着色器实现，因为 Bridson 算法需要活动列表，于是改用网格哈希加抖动；也有人对文中可视化里 p、q 两个点位置的理解提出困惑，并分享了相关的调试界面和可交互示例链接。

**标签**: `#algorithms`, `#procedural generation`, `#graphics`, `#sampling`

---

<a id="item-9"></a>
## [静态分配，恒定工作量：系统编程探索](https://matklad.github.io/2026/09/02/static-allocation-constant-work.html) ⭐️ 7.0/10

系统程序员 matklad 于 2026 年 9 月 2 日发表技术文章《Static Allocation, Constant Work》，探讨静态分配与恒定工作量（O(1)）相结合的编程技术。文章以 orders 切片为例，展示了先使用 @memset(orders, undefined) 清空，再将切片交由用位集追踪空闲对象的池（pool）管理的具体做法。 作为被广泛认可的系统程序员，matklad 的这篇文章对关心高吞吐、低延迟内存管理的开发者有较强参考价值。它所讨论的静态分配与 O(1) 对象回收策略，可能影响嵌入式系统、数据库、游戏引擎和语言工具链等场景下的资源管理设计。 文中描述的方法包括用 @memset 将切片置为 undefined，再通过内存池托管待回收对象，同时用一个位集跟踪哪些对象空闲。这体现了以固定内存布局和固定计算量实现资源复用的设计思路，规避了运行时动态分配可能引入的开销。

rss · Lobsters · Sep 2, 18:19

**背景**: 静态内存分配指在编译期就确定数据对象所需存储量的分配方式，它与程序运行时才分配内存的动态分配相反。'恒定工作量'（constant work）是算法分析中的概念，通常对应大 O 表示法中的 O(1)，表示操作耗时不会随输入规模增大而增加。将两者结合，可以让系统在运行前确定内存布局并确保关键操作始终在常数时间内完成，从而减少不可预测的延迟与堆碎片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Static_variable">Static variable - Wikipedia</a></li>
<li><a href="https://matklad.github.io/2026/09/02/static-allocation-constant-work.html">Static Allocation, Constant Work</a></li>

</ul>
</details>

**标签**: `#static-allocation`, `#systems-programming`, `#performance`

---

<a id="item-10"></a>
## [Go 团队推出 goroutine 泄漏分析工具](https://go.dev/blog/goroutine-leak-profiles) ⭐️ 7.0/10

Go 团队在官方博客中介绍了 goroutine 泄漏分析（leak profiles），这是一种帮助开发者检测和调试 goroutine 泄漏的新方法。通过该分析，开发者能更准确地识别真正泄漏的 goroutine，而不仅仅是暂时阻塞的。 这对所有 Go 开发者都很重要，因为 goroutine 泄漏是并发编程中常见的难题，可能导致内存泄漏和性能下降。该技术提供了一种系统化的方式来发现低数量、难以察觉的泄漏问题，填补了现有 profiling 工具的空白。 传统的 goroutine profile 无法区分真正泄漏的 goroutine 与因高并发流量而临时阻塞的 goroutine，而泄漏分析专门针对长期存在、不退出且非预期的 goroutine。此外，它能够捕捉到数量很少、可能多年未被发现的泄漏情况。

rss · Lobsters · Sep 2, 18:50

**背景**: 在 Go 语言中，goroutine 是轻量级并发执行单元。当 goroutine 因等待永不满足的条件（如未收到值的通道接收或死循环）而永久无法退出时，就发生了 goroutine 泄漏，导致内存无法释放。Go 提供了诸如 runtime/pprof 等 API 来检查活动 goroutine 及其堆栈，从而帮助开发者定位问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/blog/goroutine-leak-profiles">Goroutine Leak Profiles - The Go Programming Language</a></li>
<li><a href="https://github.com/DataDog/go-profiler-notes/blob/main/goroutine.md">go-profiler-notes/goroutine.md at main · DataDog/go ... - GitHub</a></li>

</ul>
</details>

**标签**: `#Go`, `#profiling`, `#goroutines`, `#debugging`, `#runtime`

---

<a id="item-11"></a>
## [PostgreSQL 正则扩展 pg_tre 与 pg_re2 发布](https://www.depesz.com/2026/08/25/new-things-for-regular-expressions-in-postgresql-pg_tre-and-pg_re2/) ⭐️ 7.0/10

Depesz 发文介绍了 PostgreSQL 生态中两个新的正则表达式扩展：pg_tre 和 pg_re2。pg_tre 是一个基于 TRE 正则库、支持近似（模糊）匹配的原生索引访问方法，面向 PostgreSQL 18+；pg_re2 则是由 ClickHouse 团队开发的扩展，将 RE2 驱动的快速正则表达式函数引入 PostgreSQL。 这两个扩展显著增强了 PostgreSQL 在正则表达式方面的能力，分别解决了模糊匹配索引和高速正则处理的需求。对于需要在数据库内进行复杂文本检索、数据清洗或近似匹配的开发者来说，这些功能可以简化架构并提升查询性能。 pg_tre 要求 PostgreSQL 18 及以上版本，需要在 postgresql.conf 中设置 shared_preload_libraries = 'pg_tre'，它允许通过 tre_pattern 显式指定编辑距离（如 k=0 精确匹配、k=1 容忍一个字符错误），并可结合 pgvector 作为混合过滤条件。pg_re2 要求 PostgreSQL 13 或更高版本，提供与 ClickHouse 兼容的 RE2 正则函数，并支持与 pg_clickhouse 的推送下推集成。

rss · Lobsters · Sep 2, 12:59

**背景**: PostgreSQL 内置的 SIMILAR TO 和 POSIX 正则表达式功能相对基础，缺少专门的近似匹配索引和 RE2 这类保证线性时间执行的正则引擎。pg_tre 通过编辑距离衡量索引内容与正则表达式的相似度，工作方式类似文本向量索引；而 pg_re2 将 ClickHouse 中成熟的正则函数移植到 Postgres，使数据库内的高性能正则处理成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codeberg.org/gregburd/pg_tre">gregburd/pg_tre: A PostgreSQL module that provides a new index type based on TRE REGEX library which supports approximate (fuzzy) matching. The index can function much like a vector index in that the edit distance is in effect how similar indexed content is to the provided regular expression. - Codeberg.org</a></li>
<li><a href="https://clickhouse.com/blog/introducing-pg_re2-regex-in-postgres">Introducing pg_re2, fast, RE2-powered regular expressions in ...</a></li>
<li><a href="https://www.postgresql.org/about/news/pg_tre-111-released-an-approximate-regex-index-am-for-postgresql-18-3305/">PostgreSQL: pg_tre 1.1.1 released -- an approximate-REGEX index AM for PostgreSQL 18+</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#regular expressions`, `#extensions`, `#pg_tre`, `#pg_re2`

---

<a id="item-12"></a>
## [CTTI 指数级膨胀，RTTI 线性扩展](https://www.gingerbill.org/article/2026/09/02/ctti-is-exponential-rtti-is-linear/) ⭐️ 7.0/10

一篇题为《CTTI 是指数级的，RTTI 是线性的》的技术文章指出，编译期类型信息（CTTI）的规模可能呈指数级增长，而运行时类型信息（RTTI）则呈线性增长。文章对比了两种类型信息机制在扩展性上的本质差异。 这一分析对语言设计者和编译器开发者具有参考价值，因为它揭示了 CTTI 在复杂模板元编程场景下可能带来的编译时间和二进制体积灾难。理解这一差异有助于在编译期反射与运行时反射之间做出更合理的工程取舍，影响 C++等静态类型语言的元编程实践。 CTTI 通常依赖模板实例化和编译器内建函数（如__PRETTY_FUNCTION__）来提取类型信息，每次模板展开都可能生成新的类型组合，导致指数级膨胀。RTTI 则通过为每个多态类关联一个 type_info 对象，其内存和查询开销随类型数量线性增长，且仅在多态场景下触发。

rss · Lobsters · Sep 2, 21:35

**背景**: 编译期类型信息（CTTI）指在编译阶段获取、操作类型特征的技术，常见于 C++元编程库（如 boost::type_index、ctti）。运行时类型信息（RTTI）是 C++等语言在程序运行时识别对象真实类型的能力，核心包括 dynamic_cast 和 typeid 操作符。由于 CTTI 在深层模板实例化中会产生组合爆炸，而 RTTI 按类简单注册，两者的扩展性因此呈现指数与线性的对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Manu343726/ctti">GitHub - Manu343726/ctti: Compile Time Type Information for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Run-time_type_information">Run-time type information - Wikipedia</a></li>

</ul>
</details>

**标签**: `#type-information`, `#compilers`, `#programming-languages`, `#reflection`, `#performance`

---

<a id="item-13"></a>
## [用 ImHex 逆向未知文件格式：作者实战指南](https://werwolv.net/posts/file_format_reverse_engineering/) ⭐️ 7.0/10

这篇文章由 ImHex 的作者 WerWolv 撰写，是一份关于如何利用 ImHex 逆向分析未知文件格式的实操指南。文章结合 ImHex 的自定义模式语言与可视化功能，展示了从零开始识别二进制文件中数据结构的方法。 逆向未知文件格式是安全研究、数据恢复和软件逆向等领域的核心技能，而这份指南的直接来源是工具作者本人，因此带有独特的设计视角和实用技巧。对于长期使用二进制编辑器和模式语言的开发者来说，它提供了可借鉴的工作流程和思路。 ImHex 是一款跨平台、免费开源的高级十六进制编辑器，支持 Windows、macOS、Linux 以及浏览器运行。其独创的类 C 风格模式语言可定义结构体、数组、指针、枚举、位域等数据类型，并支持根据 MIME 类型或魔数自动加载解析规则，帮助用户高亮和解读文件内容。

rss · Lobsters · Sep 2, 22:30

**背景**: 在没有专用解析器时，分析未知二进制文件通常需要借助十六进制编辑器和手动比对的方式逐字节猜测结构，效率很低。ImHex 提供了一种可编程的解析环境，使用者可以用模式语言描述格式规则，让工具自动识别数据布局、字段类型和边界，从而加速逆向过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ImHex">ImHex - Wikipedia</a></li>
<li><a href="https://github.com/WerWolv/ImHex">GitHub - WerWolv/ImHex: A Hex Editor for Reverse Engineers ... ImHex Next-Gen Hex Editor for Binary & Memory Analysis ImHex Web - Free Online Hex Editor for Reverse Engineers ImHex - Modern, Free and Open Source Hex Editor for Reverse ... ImHex - Wikipedia Hex Editor - WerWolv's Documentation Page</a></li>

</ul>
</details>

**标签**: `#reverse engineering`, `#file formats`, `#hex editor`, `#binary analysis`, `#ImHex`

---

<a id="item-14"></a>
## [追踪 np.add：从 Python 到底层 C 实现的完整调用链](https://blog.veitheller.de/numpy.html) ⭐️ 7.0/10

博客作者 Veit Heller 发表了一篇技术深潜文章，详细追踪了 np.add 从 Python 层调用到 NumPy 底层 C 实现的完整执行路径。文章剖析了 Python/C API 的对象调用过程和 ufunc 的分派机制，揭示了 NumPy 加法运算内部的各个步骤。 这类底层解析为关注 Python 性能的开发者提供了实用参考，帮助他们理解 NumPy 运算为何高效以及 Python 与 C 扩展之间的边界开销。对希望研究 NumPy 内部实现或参与开源的读者也具有较高价值。 文章属于教学式代码追踪而非新成果，内容结构围绕 Python 调用协议、NumPy ufunc 对象以及底层基于 dtype 的计算循环展开。它假设读者已了解 NumPy 基本用法，并适合对 C 语言和 CPython 有一定基础的人阅读。

rss · Lobsters · Sep 2, 14:25

**背景**: NumPy 的通用函数（ufunc）是用于在数组上执行逐元素运算的快速向量化函数，例如 np.add 就是其中一个实例。ufunc 由 C 实现，支持广播和自动类型处理，Python 中的调用会通过 Python/C API 进入 C 层，再由 NumPy 根据输入数据的 dtype 选择对应的内部循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://numpy.org/doc/stable/user/basics.ufuncs.html">Universal functions ( ufunc ) basics — NumPy v2.5 Manual</a></li>
<li><a href="https://deepwiki.com/numpy/numpy/2.3-universal-functions-(ufuncs)">Universal Functions ( ufuncs ) | numpy / numpy | DeepWiki</a></li>
<li><a href="https://docs.python.org/3/c-api/index.html">Python/C API reference manual — Python 3.14.7 documentation</a></li>

</ul>
</details>

**标签**: `#numpy`, `#python`, `#internals`, `#c`, `#systems`

---