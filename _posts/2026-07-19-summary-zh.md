---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> From 32 items, 13 important content pieces were selected

---

1. [阿里发布 2.4 万亿参数开源模型 Qwen 3.8](#item-1) ⭐️ 9.0/10
2. [用 1600 美元 ESP32 替代 12 万美元保龄球计分系统](#item-2) ⭐️ 8.0/10
3. [AI 建议使准确率降低 3 倍但信心倍增](#item-3) ⭐️ 8.0/10
4. [Minecraft Java 版快照 26.3.4 采用 SDL3](#item-4) ⭐️ 8.0/10
5. [Claude Code 改用 Rust 重写的 Bun 运行时](#item-5) ⭐️ 8.0/10
6. [数学家仍未找到最快乘法算法](#item-6) ⭐️ 8.0/10
7. [OpenAI 将 Codex 上下文窗口从 372k 缩小至 272k](#item-7) ⭐️ 7.0/10
8. [卖出 2500 台 MIDI 录音机：硬件没那么难](#item-8) ⭐️ 7.0/10
9. [Moonshot AI 因 Kimi K3 需求火爆暂停新订阅](#item-9) ⭐️ 7.0/10
10. [家庭服务器的报废与重生](#item-10) ⭐️ 7.0/10
11. [并行编程的禅意](#item-11) ⭐️ 7.0/10
12. [使用 Lean 进行形式化验证的入门教程](#item-12) ⭐️ 7.0/10
13. [Linux 调度器研究：指标的重要性](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [阿里发布 2.4 万亿参数开源模型 Qwen 3.8](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) ⭐️ 9.0/10

阿里巴巴宣布推出 Qwen 3.8，一个拥有 2.4 万亿参数的开源权重大语言模型，旨在与 Moonshot AI 的 Kimi K3（2.8 万亿参数）竞争。 此举标志着中国 AI 巨头在开源大模型领域展开激烈竞争，将推动模型性能提升和本地化部署，惠及开发者和企业用户。 Qwen 3.8 的参数规模为 2.4T，小于 Kimi K3 的 2.8T，但阿里巴巴强调其开放权重（open weights）特性，允许用户本地运行和微调。

hackernews · nh43215rgb · Jul 19, 08:44 · [社区讨论](https://news.ycombinator.com/item?id=48966120)

**背景**: 开源权重模型（open-weights LLM）是指模型权重公开可下载，用户可在自有硬件上部署和定制，相比闭源 API 更注重隐私和成本控制。参数数量（如 2.4T）衡量模型规模，通常越大能力越强，但硬件需求也更高。Qwen 系列是阿里巴巴开发的千问模型家族，Qwen 3.8 是其最新版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onyx.app/self-hosted-llm-leaderboard">Best Self-Hosted LLM Leaderboard 2026 | Open-Weight Model ...</a></li>
<li><a href="https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html">China's Moonshot AI unveils Kimi K3 that rivals OpenAI, Anthropic</a></li>
<li><a href="https://www.geeky-gadgets.com/moonshot-ai-kimi-k3-review/">Kimi K3 Open Source AI Rivals GPT 5.6 Sol with 2.8T ...</a></li>

</ul>
</details>

**社区讨论**: 社区对此反应积极，有用户期待较小尺寸版本以便本地运行，但也有用户批评 Qwen 3.7 Pro 在编程任务中表现不佳且成本高，认为 DeepSeek V4 Pro 更优。

**标签**: `#LLM`, `#open-weights`, `#Alibaba Qwen`, `#AI competition`, `#large language model`

---

<a id="item-2"></a>
## [用 1600 美元 ESP32 替代 12 万美元保龄球计分系统](https://news.ycombinator.com/item?id=48968606) ⭐️ 8.0/10

一位前 SRE 购买了一座废弃的保龄球中心，并自制了一套基于 ESP32 的开源计分系统 OpenLaneLink，将原本 6 位数的商业系统成本降至约每对球道 200 美元。 此举展示了用现代开源硬件和软件大幅降低传统工业设备成本的可行性，挑战了供应商锁定和高昂维护费的模式，可能激励更多小型场馆自行改造。 系统采用 ESP32 和 ESPNow 形成星形拓扑无线网络，以 RS485 作为无线干扰时的有线回退，树莓派作为中央网关运行 Redis 和状态机，上层用 React/WebSocket 构建用户界面。

hackernews · section33 · Jul 19, 14:41

**背景**: 保龄球中心的自动计分系统通常由专用厂商（如 Brunswick、AMF）提供，整套更换费高达 8 万至 12 万美元，且配件昂贵、定制困难。ESP32 是廉价低功耗微控制器，支持 Wi-Fi 和蓝牙，适合物联网应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48968606">Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_scorer">Automatic scorer - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区反响热烈，多位有类似经历的读者分享了自己改造旧设备（如机械保龄球道、机床）的经验，一致认同用现代嵌入技术替代老旧昂贵系统的巨大潜力。有人提议用 DMX 控制灯光特效，进一步扩展功能。

**标签**: `#embedded systems`, `#hardware hacking`, `#cost reduction`, `#retrofitting`, `#ESP32`

---

<a id="item-3"></a>
## [AI 建议使准确率降低 3 倍但信心倍增](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study) ⭐️ 8.0/10

一项研究发现，当人们使用 AI 建议时，回答准确率降低约 3 倍，但自信心却提升约 2 倍。该研究揭示了人类过度依赖 AI 可能带来的认知偏差。 这一发现值得警惕，因为它表明人们可能在不知不觉中因 AI 建议而变得更自信，但判断力却显著下降。这对教育、专业决策和日常信息处理领域有深远影响，提醒我们需要更谨慎地评估 AI 辅助的可靠性。 研究涉及参与者被要求回答一系列问题，其中部分问题 AI 会给出错误答案，但参与者无法区分正确与错误建议。结果表明，即使 AI 错了，人们也更倾向于接受其建议，且随后对自己答案的信心反而增加。

hackernews · rbanffy · Jul 19, 21:18 · [社区讨论](https://news.ycombinator.com/item?id=48971738)

**背景**: 随着大型语言模型的普及，越来越多的人依赖 AI 获取信息和解答疑惑。然而，AI 并非总是正确，且其输出往往带有误导性。这项研究关注的是人类与 AI 交互中的“过度依赖”现象——即人们倾向于高估 AI 正确性，并因此削弱自身批判性思维。

**社区讨论**: 社区评论中，有用户批评研究方法，认为研究设计的本质是让参与者面对已知会出错的 AI，这并非 AI 特有的问题；也有人悲观地认为，即使 AI 变得更智能，人们仍会选择能强化自身错误信念的“谄媚答案”。此外，有教师提出让学生先获得 AI 回答再批判其错误的创新教学方式。

**标签**: `#AI`, `#critical thinking`, `#human-AI interaction`, `#overconfidence`, `#study`

---

<a id="item-4"></a>
## [Minecraft Java 版快照 26.3.4 采用 SDL3](https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4) ⭐️ 8.0/10

Minecraft: Java Edition 的快照 26.3.4 将底层图形和输入库从 SDL2 升级到了 SDL3，以改善跨平台的窗口管理和输入处理。 这次升级意味着 Minecraft 将获得更稳定和现代的跨平台支持，同时 SDL3 的采用也可能推动其他游戏项目跟进迁移，对游戏开发生态有积极影响。 新版使用了社区贡献的 LWJGL 绑定（由 GTNH 模组包团队成员编写），但也存在已知问题：在 Windows 多显示器设置下独占全屏可能崩溃，以及在 Wayland 下进入独占全屏会崩溃。

hackernews · ObviouslyFlamer · Jul 19, 11:48 · [社区讨论](https://news.ycombinator.com/item?id=48967256)

**背景**: SDL（Simple DirectMedia Layer）是一个跨平台的多媒体库，用于处理视频、音频、输入等，广泛用于游戏开发。SDL3 于 2025 年 1 月正式发布，相比 SDL2 带来了更简化的 API 和改进的硬件加速支持。Minecraft Java 版之前使用 SDL2，此次升级是为了跟上库的发展并获得更好性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer">Simple DirectMedia Layer - Wikipedia</a></li>
<li><a href="https://wiki.libsdl.org/">SDL Wiki: SDL3/FrontPage</a></li>

</ul>
</details>

**社区讨论**: 社区对这次升级普遍表示关注和认可，有评论指出 LWJGL 绑定由 GTNH 模组包团队贡献，实现了“原版→模组→原版”的循环。也有人对已知的崩溃问题表示担忧，希望正式版前能修复。还有用户对 Minecraft 越来越像一个游戏引擎而非单纯游戏表示惊叹。

**标签**: `#Minecraft`, `#SDL3`, `#game development`, `#cross-platform`, `#rendering`

---

<a id="item-5"></a>
## [Claude Code 改用 Rust 重写的 Bun 运行时](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/) ⭐️ 8.0/10

Anthropic 旗下的 Claude Code 现在使用 Bun 作为 JavaScript 运行时，而 Bun 已被从 Zig 语言重写为 Rust 语言。 这一变化涉及两个重大决策：Claude Code 选择第三方运行时以及 Bun 核心语言的迁移，引发了关于技术选型、工程管理和开源治理的广泛讨论。 Claude Code 是一个基于 React 的终端 UI 应用，选择 Bun 是因为性能优势；Bun 的重写合并了一个超过 100 万行代码的 Pull Request，且在短短一个月内完成。

hackernews · tosh · Jul 19, 10:03 · [社区讨论](https://news.ycombinator.com/item?id=48966569)

**背景**: Bun 是一个 JavaScript 运行时，最初用 Zig 编写（一种需要手动管理内存的系统语言）。Rust 同样是一种系统语言，但通过所有权机制自动管理内存。Claude Code 是 Anthropic 的 AI 编程工具。这次重写引发了社区对工程质量和沟通方式的争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有开发者质疑为何一个 TUI 应用需要依赖 JavaScript 运行时，也有人支持 Rust 的自动内存管理能减少内存错误。但多数人批评项目负责人的沟通方式不当，认为 Bun 的治理不透明且重写过程过于激进。

**标签**: `#bun`, `#rust`, `#claude code`, `#rewrite`, `#javascript runtime`

---

<a id="item-6"></a>
## [数学家仍未找到最快乘法算法](https://www.scientificamerican.com/article/mathematicians-still-dont-know-the-fastest-way-to-multiply-numbers/) ⭐️ 8.0/10

《科学美国人》发表文章指出，寻找两个整数相乘的最快算法仍是未解决的开放问题。尽管已有多种快速算法，但最优复杂度尚未确定。 乘法是计算的基础操作，其效率直接影响计算机科学、密码学和数值计算等领域。这个问题的解决可能带来算法理论的重大突破和实践性能提升。 目前最快的理论算法是 2019 年 Harvey 和 van der Hoeven 提出的 O(n log n)算法，但因常数过大无法实际使用。实际中常用 Schönhage-Strassen 算法（复杂度 O(n log n log log n)）。

rss · Lobsters · Jul 19, 07:50

**背景**: 乘法算法从小学的 O(n²)方法，发展到 1960 年 Karatsuba 的 O(n^1.58)、1971 年 Schönhage-Strassen，以及 2007 年 Fürer 的改进。核心思路包括分治和快速傅里叶变换（FFT）。问题在于是否存在真正最优的复杂度下界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication">Computational complexity of matrix multiplication - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Karatsuba_algorithm">Karatsuba algorithm</a></li>

</ul>
</details>

**标签**: `#algorithms`, `#computational complexity`, `#mathematics`, `#open problem`

---

<a id="item-7"></a>
## [OpenAI 将 Codex 上下文窗口从 372k 缩小至 272k](https://github.com/openai/codex/pull/33972/files) ⭐️ 7.0/10

OpenAI 通过 GitHub 提交将 Codex 模型的上下文大小从 372k 标记减少到 272k，相当于减少约 10 万 token。这一改动引发了社区关于上下文压缩利弊的广泛讨论。 上下文窗口大小直接影响 AI 代码生成的质量和细节保留能力。此举可能导致模型在处理长文档或复杂任务时丢失关键信息，进而影响开发者的使用体验和模型选择偏好。 上下文压缩是一种通过删除低信号 token 来减少窗口的技术，但不像摘要那样保留全部细节。社区评论指出，超过 50% 的上下文使用后模型质量下降明显，而压缩后的内容可能遗漏重要细节。

hackernews · AmazingTurtle · Jul 19, 07:54 · [社区讨论](https://news.ycombinator.com/item?id=48965850)

**背景**: 大型语言模型的上下文窗口是指模型一次能处理的 token 数量上限。为了在有限窗口内容纳更多信息，一些系统采用上下文压缩（context compaction）技术，即删除不重要的 token 以腾出空间。这种策略虽然降低了计算开销，但也可能牺牲信息的完整性和准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://www.morphllm.com/context-compaction">Context Compaction: Delete Noise, Keep Signal | Technical Guide</a></li>

</ul>
</details>

**社区讨论**: 社区对此意见不一。部分用户认为压缩会导致细节丢失，尤其在需要精细讨论的场景下表现不佳，因此更倾向于使用 Anthropic 等提供长上下文的模型。另一些用户则认为，过长的上下文会降低模型智能，建议将对话分段，每段控制在 300k 以内，并手动清除旧上下文以获得更好效果。

**标签**: `#OpenAI`, `#Codex`, `#context window`, `#AI models`, `#code generation`

---

<a id="item-8"></a>
## [卖出 2500 台 MIDI 录音机：硬件没那么难](https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard) ⭐️ 7.0/10

作者分享了他销售 2500 台 MIDI 录音机（JamCorder）的经验，并提出了“硬件并不难”的观点，挑战了常见的“硬件很难”论调。 该观点为硬件创业者提供了新的思路，表明通过简化设计和合理规划，硬件产品开发并非不可逾越的障碍，可能激励更多人进入硬件领域。 作者强调其产品仅使用 25 个元件的 PCB 和两个注塑件，认为硬件难度取决于产品本身的复杂性，而非硬件固有的特性。

hackernews · chipweinberger · Jul 19, 10:34 · [社区讨论](https://news.ycombinator.com/item?id=48966713)

**背景**: MIDI 录音机是一种记录乐器数字接口（MIDI）数据的设备，常用于音乐创作和演出。传统上，硬件开发被认为比软件开发更困难，涉及供应链、制造、物流等复杂环节。

**社区讨论**: 评论中，用户 JimsonYang 认为“硬件很难”是风投的说法，关注规模、物流和现金流等挑战；skippyfish 列举了硬件扩展和用户端问题的困难；starky 则指出硬件难度取决于产品复杂度，简单产品并不难。整体观点分化，有人认同作者，也有人强调硬件的固有挑战。

**标签**: `#hardware`, `#MIDI`, `#entrepreneurship`, `#product development`

---

<a id="item-9"></a>
## [Moonshot AI 因 Kimi K3 需求火爆暂停新订阅](https://twitter.com/kimi_moonshot/status/2078855608565207130) ⭐️ 7.0/10

Moonshot AI 于近日宣布，由于旗下 Kimi K3 模型需求在 48 小时内逼近容量极限，为保障现有订阅用户的体验，公司决定暂时停止接受新订阅，并将计算资源优先分配给现有用户。 这一举措反映出 Kimi K3 作为一款 2.8 万亿参数的开源模型，在市场上获得了极高的关注度和需求，同时也体现了 Moonshot AI 以用户为中心、不盲目追求增长的战略，可能成为 AI 行业客户运营的新标杆。 Kimi K3 是 Moonshot AI 于 2026 年 7 月发布的最新大语言模型，采用 Kimi Delta 注意力机制和注意力残差结构，原生支持视觉能力，上下文窗口达 100 万 tokens。此次暂停仅针对新订阅用户，已有订阅用户不受任何影响。

hackernews · serialx · Jul 19, 16:02 · [社区讨论](https://news.ycombinator.com/item?id=48969291)

**背景**: Moonshot AI 是一家成立于 2023 年的中国人工智能公司，由清华大学校友创立，专注于开发先进的大语言模型以实现通用人工智能。其 Kimi 系列聊天机器人以超长上下文支持著称，K3 是该系列的最新旗舰模型，也是全球首个开源的超 3T 参数级别模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://openlm.ai/kimi-k3/">Kimi K3 - openlm.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍赞扬 Moonshot AI 优先保障现有用户的做法，认为这是客户导向的体现。但也有用户反映，在试用中遇到了配额限制问题——例如有用户付费后因 K3 单日配额用尽而无法完成任务。部分技术讨论则聚焦于 K3 大量采用 RNN/线性注意力层（是全注意力层的三倍），认为这种架构可能对长上下文任务极为有利。

**标签**: `#Moonshot AI`, `#Kimi K3`, `#subscription`, `#demand`, `#AI`

---

<a id="item-10"></a>
## [家庭服务器的报废与重生](https://sgt.hootr.club/blog/home-server-rebirth/) ⭐️ 7.0/10

一篇博客文章记录了作者家庭服务器因 SD 卡损坏而故障，随后重建的过程。社区评论建议使用 Intel NUC 等迷你 PC 或 NVMe SSD 来避免 SD 卡损坏问题。 许多家庭服务器爱好者依赖 Raspberry Pi 和 SD 卡，但 SD 卡容易损坏，导致数据丢失。本文和社区讨论提供了实用的替代方案，有助于提升家庭服务器的稳定性和可靠性。 作者可能仍在使用 Raspberry Pi，但社区强调使用 USB 或 NVMe SSD 启动可以避免 SD 卡损坏。此外，有评论提到现代 Rockchip SBC 已配备 NVMe 插槽。

hackernews · Lobsters · Jul 19, 10:44 · [社区讨论](https://news.ycombinator.com/item?id=48966769)

**背景**: Raspberry Pi 是流行的单板计算机，常用于家庭服务器。其 SD 卡作为存储介质容易因频繁读写或电源故障而损坏。Intel NUC 是一种小型迷你 PC，具有更强的性能和稳定性，常被推荐作为 Raspberry Pi 的替代品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=ce_xaNk9fIk">What Can You Do with an Intel NUC ? - YouTube</a></li>
<li><a href="https://www.coolblue.be/en/advice/what-is-a-barebone.html">What's a barebone? - Coolblue - anything for a smile</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍认同 Raspberry Pi 的 SD 卡损坏问题，并分享了多种解决方案，如使用 USB 3.0 闪存盘、Argon One 外壳加 SATA SSD，或直接采用带有 NVMe 插槽的 Rockchip SBC。用户“arjie”分享了通过预置多张 SD 卡并定期更换的经验，显示长期运行的可行性。总体而言，讨论实用且具有建设性。

**标签**: `#home-server`, `#raspberry-pi`, `#self-hosting`, `#hardware`, `#SSDs`

---

<a id="item-11"></a>
## [并行编程的禅意](https://smolnero.com/posts/the-zen-of-parallel-programming) ⭐️ 7.0/10

本文从哲学视角探讨了并行编程，可能提供了相关见解和最佳实践。 在多核处理器时代，并行编程至关重要，这类哲学思考有助于开发者建立正确的并发思维，提升软件性能与可靠性。 文章发布于 smolnero.com，并在 lobste.rs 上有评论链接，表明社区对此话题有讨论。

rss · Lobsters · Jul 19, 20:19

**背景**: 并行编程指同时执行多个计算任务，常用于提升程序性能。与串行编程不同，它面临竞态条件、死锁等复杂问题，需要深入理解并发模型。

**标签**: `#parallel programming`, `#concurrency`, `#software engineering`, `#best practices`, `#programming philosophy`

---

<a id="item-12"></a>
## [使用 Lean 进行形式化验证的入门教程](https://hashcloak.com/blog/tutorial-introduction-to-formal-verification-with-lean-(part-1)) ⭐️ 7.0/10

本教程系列的第一部分介绍了形式化验证的基本概念以及如何使用 Lean 定理证明器进行验证。 形式化验证能极大提高关键系统的可靠性，而 Lean 作为开源证明助手，此教程降低了学习门槛，有助于推广形式化方法在软件开发中的应用。 该教程是系列的第一部分，适合初学者；后续部分可能涵盖更高级的定理证明技术。Lean 基于演算结构且支持函数式编程。

rss · Lobsters · Jul 19, 17:35

**背景**: 形式化验证是运用数学方法严格证明系统满足特定规格的过程，常用于密码协议、操作系统等关键领域。Lean 是一个开源的交互式定理证明器和编程语言，由微软研究院发起，正逐步成为主流的形式化验证工具之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#Lean`, `#theorem proving`, `#software correctness`

---

<a id="item-13"></a>
## [Linux 调度器研究：指标的重要性](https://pradyun.net/blog/metrics_matter.html) ⭐️ 7.0/10

一篇技术文章深入探讨了 Linux 调度器的工作原理，并强调了性能指标在分析调度行为中的关键作用。 对于系统工程师和开发者而言，理解调度器行为并正确使用性能指标，有助于优化系统性能和资源利用率。 文章可能涉及 CFS 和 EEVDF 等调度器，并指出仅凭单一指标（如平均负载）可能误导性能分析。

rss · Lobsters · Jul 19, 00:45

**背景**: Linux 内核使用多种调度算法（如 CFS 和 EEVDF）来管理进程的 CPU 时间分配。性能指标（如 CPU 使用率、等待时间）用于监控和调优系统。但选择错误的指标可能导致错误结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.kernel.org/scheduler/index.html">Scheduler — The Linux Kernel documentation</a></li>
<li><a href="https://linuxvox.com/blog/what-scheduling-algorithms-does-linux-kernel-use/">Linux Kernel Scheduling Algorithms Explained: A Guide for OS ...</a></li>

</ul>
</details>

**标签**: `#Linux`, `#schedulers`, `#performance`, `#systems`, `#metrics`

---