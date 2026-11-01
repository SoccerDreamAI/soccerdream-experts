# Why the license looks like this

[English](#english) · [简体中文](#简体中文)

Most source-available projects pick a license by vibe and then spend three years explaining
it. Here is the reasoning, so you can disagree with the reasoning rather than the outcome.

---

## English

### Why not just use MIT

MIT grants everyone the right to use this commercially, forever, with no obligation beyond
attribution. That is a fine choice for a library. It is a bad choice for a project whose
value is the configuration inside it: the moment we ship MIT, someone repackages `agents/`
and `teams/` as a paid product, and we have no recourse and no argument.

The people who would do that are not villains. They are behaving rationally under the
license we handed them.

### Why not a Creative Commons license for the personas

This was the first instinct, and it is wrong for a specific reason: **CC licenses are
irrevocable and their "non-commercial" boundary is genuinely ambiguous for internal
corporate use.** A company running these personas for an internal tool can make a
defensible argument that it is not "commercial". You then either litigate an ambiguity or
let it stand — both worse than a single clear rule.

Personas are also machine-parsed configuration, not prose. CC was designed for creative
works. Applying it to a file a program reads and validates is a category error that
produces strange questions, like whether a schema change is a "derivative work".

**So: BUSL for anything the runtime consumes, CC BY-NC-SA for the prose.** Two licenses,
each in the domain it was designed for, with one enforcement path.

### Why BUSL-1.1 rather than a custom license

BUSL has three properties that matter here:

1. **It is a known quantity.** Procurement teams have seen it. A custom license triggers a
   legal review that takes weeks and usually ends in "no".
2. **It has a Change Date.** Every version converts to Apache-2.0 after four years. This
   answers the "what if you disappear" objection honestly, instead of with a promise.
3. **It has an Additional Use Grant slot.** This is the important one — see below.

### The Additional Use Grant is a business decision, not a legal one

BUSL's default permits **no production use** without a commercial license. Taken literally,
that means an engineer cannot run this on a real workload before their legal team has
signed something. In practice they close the tab.

We grant three exceptions — 30-day internal evaluation, academic use, personal
non-commercial use — because **a license nobody can try is a license nobody buys.** The
evaluation window is long enough for a proof of concept and short enough that it cannot
substitute for a commercial license in production.

If you fork this for your own project, this is the field worth thinking hardest about.
Everything else is convention.

### Why the CLA demands relicense rights

The project is three things at once: source-available today, Apache-2.0 after the Change
Date, and commercially licensable in between. All three depend on the same ability — **to
apply a different license to the same code later.**

An inbound-equals-outbound contribution (the common "by submitting, you agree to license
under the repo's license" wording) does not grant that. A contributor's lines would stay
under BUSL forever, which means the Change Date would be a lie for a portion of the
codebase, and a commercial license could not cover contributed work.

So contributors grant sublicense and relicense rights explicitly, in [CLA.md](../CLA.md).
This is stricter than most projects, and it is stated plainly rather than buried — a
contributor who declines is told why, before spending an evening on a pull request.

### Why outputs belong to the user

The first question every commercial evaluator asks is "who owns what this thing produces".
The answer here is: you do. We claim nothing.

This is not generosity. A framework whose output ownership is unclear cannot be adopted
inside a company, because nobody wants to explain to their legal team why the vendor might
own the analysis. Clarifying it costs us nothing and removes the single most common
blocker.

### What we accept as the cost

- Some developers will skip the repo because "source-available" is a hyphenated word they
  do not trust. That is the correct trade: the ones who stay understand what they are
  getting.
- Some forks will violate the license. Enforcement is expensive and we will not pursue most
  of them. The license is a boundary marker, not a police force.
- A stricter CLA means fewer drive-by contributions. The contributions we do get are worth
  more.

---

## 简体中文

大多数「源码可见」项目的许可证是凭感觉选的，然后用三年时间去解释它。
这里把推理过程写出来，方便你反对推理，而不是反对结论。

### 为什么不用 MIT

MIT 授予任何人永久、可商用的权利，除署名外没有任何义务。对库来说是好事；
对本项目来说不是——本项目的价值就在里面的配置。一旦发 MIT，明天就有人把
`agents/` 和 `teams/` 打包成付费产品销售，而我们既无救济手段，也无话可说。

会这么做的人不是坏人。在我们给出的许可证下，那是理性行为。

### 为什么人设不用 Creative Commons

这是第一反应，但它是错的，原因很具体：**CC 许可不可撤销，而它的「非商业」边界
在公司内部使用场景下确实模糊。** 一家公司把这些人设用于内部工具，完全可以主张
自己「非商业」。然后你要么去打一场关于模糊条款的官司，要么认了——两个都比
一条清晰的规则更糟。

而且人设是被程序解析的配置，不是散文。CC 是为创作作品设计的。把它套在一个
会被程序读取和校验的文件上，属于范畴错误，会衍生出很奇怪的问题，比如
「改 schema 算不算衍生作品」。

**所以：运行时会读取的东西走 BUSL，散文走 CC BY-NC-SA。** 两个许可证，各自待在自己
被设计出来的领域，执法路径只有一条。

### 为什么用 BUSL-1.1 而不是自拟许可

BUSL 有三个恰好合用的性质：

1. **它是已知量。** 采购和法务见过它。自拟许可会触发一轮长达数周的法律审查，
   而结论通常是「不行」。
2. **它有 Change Date。** 每个版本四年后自动转为 Apache-2.0。这回答了
   「你们要是倒闭了怎么办」这个合理的疑问——用条款回答，而不是用承诺。
3. **它有一个 Additional Use Grant 的位置。** 这条最重要，见下。

### Additional Use Grant 是商业决策，不是法律决策

BUSL 默认**不允许任何生产使用**。字面执行的结果是：工程师在法务签字之前，
不能拿它跑任何真实负载。现实中他们会直接关掉标签页。

我们开了三个口子——30 天内部评估、学术使用、个人非商业使用——因为
**没人能试用的许可，就是没人会买的许可。** 评估窗口长到够做概念验证，
又短到不能替代生产环境的商业授权。

如果你要 fork 出自己的项目，这是唯一值得认真想一想的字段。其余都是惯例。

### 为什么 CLA 必须要求 relicense 权利

本项目同时是三样东西：今天是源码可见，Change Date 后是 Apache-2.0，中间可商业授权。
三者依赖同一件事——**以后能给同一份代码换许可证。**

「提交即视为按本仓库许可证授权」这种常见的 inbound=outbound 写法，不授予这项权利。
贡献者写的那些行会永远停在 BUSL 下，于是 Change Date 对一部分代码而言是句谎话，
商业授权包也覆盖不了贡献代码。

所以贡献者在 [CLA.md](../CLA.md) 里显式授予 sublicense 与 relicense 权利。
这比多数项目严格，所以我们把它写在明面上而不是埋起来——不同意的贡献者会在
花一晚上写 PR 之前就知道原因。

### 为什么产出物归用户

每个商业评估者问的第一个问题都是「这东西产出的结果归谁」。这里的答案是：归你。
我们不主张任何权利。

这不是慷慨。一个产出物权属不清的框架，在公司内部是推不动的——没人想向法务解释
为什么供应商可能拥有那份分析报告。把这件事说清楚对我们零成本，却移除了最常见的那个阻碍。

### 我们接受的代价

- 有些开发者会因为「源码可见」是个带连字符的、他们不信任的词而划走。
  这个交换是对的：留下来的人知道自己拿的是什么。
- 有些 fork 会违反许可。执法很贵，我们不会去追大多数。许可证是界碑，不是警察。
- 更严的 CLA 意味着更少的随手贡献。但我们收到的那些，价值更高。
