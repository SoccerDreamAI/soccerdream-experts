# NOTICE — Licensing, Scope & Ownership

[English](#english) · [简体中文](#简体中文)

---

## English

### 0. Ownership

Copyright © 2026 SoccerDream AI. All rights reserved except as expressly granted below.

The Licensed Work — every persona, the orchestration schema, the documentation, the assets
and the marks — is the property of SoccerDream AI. Nothing in this repository transfers
ownership. A licence to use is not a licence to claim authorship: publishing a copy while
presenting it as your own work, or under our name, is outside every grant on this page.

If you find this repository, or substantial parts of it, republished elsewhere without
attribution, report it to the address in `TRADEMARK.md`. We hold the copyright and can act
on it; the same file is honest about what we cannot enforce.

### 1. Source-available, not open source

"Open source" has a specific meaning (OSI Definition): anyone may use, modify, and
redistribute the software **for any purpose**, including commercially. This repository
deliberately does not grant that. We use *source-available* throughout, and we ask you to
use the same word when describing it. Calling it "open source" is not a small inaccuracy —
it is the one inaccuracy that turns a reader against the project.

### 2. What is licensed, and how

| Scope | Paths | License | Commercial use |
|:--|:--|:--|:--|
| **Client code** | `cli/`, `sdk/`, `scripts/` | BUSL-1.1 | ❌ license required |
| **Orchestration** | `teams/` (files **and** schema) | BUSL-1.1 | ❌ license required |
| **Personas** | `agents/` (files **and** structure) | BUSL-1.1 | ❌ license required |
| **Prose docs** | `docs/**/*.md`, root `*.md` | CC BY-NC-SA 4.0 | ❌ non-commercial only |
| **Brand** | `docs/assets/`, logos, names | All rights reserved | ❌ not licensed |

Personas are licensed under BUSL rather than a Creative Commons license **on purpose**.
CC licenses are irrevocable, and their "non-commercial" boundary is genuinely ambiguous for
a company using them internally — which produces disputes we would rather not have.
One license, one enforcement path.

### 3. Additional Use Grant — what you may do for free

BUSL-1.1 as published permits **no production use** without a commercial license. That is
too strict for this project, so we grant more:

> **You may use the Licensed Work in production, free of charge, for:**
> **(a)** internal evaluation, up to thirty (30) consecutive days per organisation;
> **(b)** academic research and teaching, at a non-profit institution;
> **(c)** personal projects with no commercial intent.
>
> **Everything else requires a commercial license.** In particular: any paid product, any
> hosted or SaaS offering, any client deliverable, and any internal use continuing past the
> evaluation window.

This grant exists because a license nobody can try is a license nobody buys.

### 4. What is deliberately absent

Not part of this repository, and not licensed by it:

- Training prompts and evolved prompt wording
- Evaluation weights, calibration parameters, scoring internals
- Live data feed adapters, normalization rules, history store
- Model routing, cost accounting, key management

Nothing in this repository is obfuscated. The closed layers are **absent**, not hidden.
Reconstructing them is outside the scope of the grant.

### 5. Ownership of your outputs

**You own what your team produces.** Reports, conclusions, diffs, and any artifact generated
by a configuration you wrote are yours. We claim no ownership, no license, and no right to
reuse them.

We state this explicitly because it is the first question every commercial evaluator asks,
and because the answer is genuinely in your favour.

### 6. Contributions

Contributions are accepted under the terms in [CLA.md](CLA.md). In short: you keep your
copyright, and you grant us a perpetual, irrevocable, worldwide, royalty-free right to use,
**sublicense, and relicense** your contribution.

The relicense grant is not boilerplate. Without it we could not (a) sell a commercial
license covering contributed code, or (b) convert this project to Apache-2.0 on the Change
Date. A contribution accepted without it would silently fragment the license.

### 7. Trademarks

"SoccerDream", the SoccerDream mark, and the expert-team naming convention are trademarks.
No license above grants trademark rights.

**Forks must rename.** If you fork and publish, remove the name and marks from your repo,
your package names, and your UI. Presenting a fork as the official project is a trademark
violation regardless of what the code license says.

### 8. No warranty, no advice

Provided "as is", without warranty of any kind, express or implied. This project is a
research and analysis framework. **It provides no betting advice, tips, predictions of
outcomes, or recommendations, and it promises no result of any kind.** No output should be
treated as a forecast of a real-world event. Nothing here is intended for anyone under 18.

### 9. Commercial licensing

For any use outside the Additional Use Grant — including internal commercial use beyond the
evaluation window, SaaS deployment, or embedding in a paid product — contact the maintainers.
Two business days.

---

## 简体中文

### 0. 权属

版权所有 © 2026 SoccerDream AI。除下文明确授予的权利外，保留一切权利。

本许可作品——全部人设、编排 schema、文档、素材与标识——均为 SoccerDream AI 的财产。
本仓库中的任何内容均不构成所有权转让。**使用权不是署名权**：把本仓库内容或其实质部分
复制后署他人之名、或以本项目名义对外发布，不在本页任何授予范围之内。

如发现本仓库或其实质部分被无署名转载，请按 `TRADEMARK.md` 中的地址告知。我们持有著作权，
可以据此主张权利；同一份文件也写清了我们追究不到什么。

### 1. 源码可见，不是开源

「开源」有明确含义（OSI 定义）：任何人可**为任何目的**（含商业目的）使用、修改、再分发。
本仓库刻意不授予该权利。全文统一使用*源码可见（source-available）*，也请你在介绍本项目时
使用同样的措辞。把它称作「开源」不是一个小误差——它恰好是那个会让读者转而反对你的误差。

### 2. 各部分的许可

| 范围 | 路径 | 许可证 | 可否商用 |
|:--|:--|:--|:--|
| **客户端代码** | `cli/`、`sdk/`、`scripts/` | BUSL-1.1 | ❌ 需授权 |
| **编排** | `teams/`（文件**与** schema） | BUSL-1.1 | ❌ 需授权 |
| **人设** | `agents/`（文件**与**结构） | BUSL-1.1 | ❌ 需授权 |
| **文字文档** | `docs/**/*.md`、根目录 `*.md` | CC BY-NC-SA 4.0 | ❌ 仅限非商业 |
| **品牌** | `docs/assets/`、标识、名称 | 保留所有权利 | ❌ 不授权 |

人设采用 BUSL 而**不是** Creative Commons，是刻意的决定。CC 许可**不可撤销**，且其
「非商业」边界在公司内部使用场景下确实模糊——这会制造我们并不想参与的争议。
**一个许可证，一条执法路径。**

### 3. 附加使用授权 —— 你可以免费做什么

BUSL-1.1 原文规定：无商业授权则**不得用于生产**。对本项目而言这太严，所以我们额外放开：

> **以下生产用途免费：**
> **（a）** 内部评估——每个组织最长连续 30 天；
> **（b）** 学术研究与教学——非营利机构；
> **（c）** 无商业意图的个人项目。
>
> **其余一律需要商业授权。** 具体包括：任何付费产品、任何托管或 SaaS 服务、
> 任何交付给客户的项目，以及任何超出评估窗口的内部使用。

这条授权的理由是：**没人能试用的许可，就是没人会买的许可。**

### 4. 刻意不提供的部分

不属于本仓库，也不由本仓库许可：

- 训练词与进化后的提示词措辞
- 评估权重、校准参数、打分明细
- 实时数据适配器、归一化规则、历史库
- 模型路由、成本核算、密钥管理

本仓库没有任何东西被混淆。闭源部分是**缺席**，不是**隐藏**。重建上述内容不在授权范围内。

### 5. 你产出物的所有权

**你的团队产出的东西归你。** 由你编写的配置所生成的报告、结论、diff 以及任何产物，
所有权归你。我们不主张所有权、不主张许可、不主张复用权。

我们把这条显式写出来，因为这是每个商业评估者最先问的问题，
而且这个答案确实对你有利。

### 6. 关于贡献

贡献按 [CLA.md](CLA.md) 的条款接收。简言之：你保留著作权，并授予我们一项永久、
不可撤销、全球范围、免版税的权利，可**再许可（sublicense）与重新许可（relicense）**你的贡献。

这项 relicense 授权不是套话。没有它，我们既无法（a）把含贡献代码的部分纳入商业授权包，
也无法（b）在 Change Date 把本项目转为 Apache-2.0。缺了它的贡献，会悄悄地把许可证撕成两半。

### 7. 商标

「SoccerDream」、SoccerDream 标识及专家团命名体系为商标。上述任何许可均不授予商标权。

**Fork 必须改名。** 如果你 fork 并对外发布，请从仓库名、包名、界面中移除本名称与标识。
把 fork 表现为官方项目，无论代码许可怎么写，都构成商标侵权。

### 8. 无担保、不构成建议

按「现状」提供，不附带任何明示或默示担保。本项目为研究与分析框架。
**不提供任何投注建议、提示、结果预测或推荐，也不承诺任何结果。**
任何输出均不应被视为对现实赛果的预判。本项目不面向 18 岁以下人士。

### 9. 商业授权

超出附加使用授权范围的任何使用——含超出评估窗口的内部商业使用、SaaS 部署、
嵌入付费产品——请联系维护者。两个工作日内回复。
