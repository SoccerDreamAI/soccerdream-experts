# 参与贡献

[English](CONTRIBUTING.md) · 简体中文

谢谢你愿意改进这个项目。这里读完约两分钟，能省掉一轮返工。

## 最快的贡献方式：写一个人设

人设（`agents/*.md`）是杠杆最高、也最好审的贡献。
好的人设是**窄的**、**敢唱反调的**——它应该带着一个会让它偶尔出错的先验偏好，以及一条把它约束在边界内的拒答规则。

契约见 [`agents/_schema.md`](agents/_schema.md)。看完复制一个现有人设，改一个点就够。

### 什么样的人设能被合并

| ✅ 会合并 | ❌ 会被打回 |
|:--|:--|
| 有明确领域 + 明确先验 | 「一个什么都懂的聪明分析师」 |
| 说明「什么证据能改变它的看法」 | 复述显而易见的话 |
| 有拒答规则（明确不回答什么） | 什么都很自信地回答 |
| 给出推理路径，而不是结论 | 把结论焊死在里面 |
| 400 字以内 | 2000 字的气氛描写 |

## 我们不会合并的内容

- 任何产出**投注建议、下注金额、「推荐选项」**的人设。本项目是分析框架，请保持这一点
- 任何**对冲突结果取平均**的改动。分歧只升级，不中和
- 真实比赛数据、真实赔率快照、任何从实时数据源爬取的内容
- 任何形式的硬编码凭据，见 [SECURITY.md](SECURITY.md)
- 图方便新增的依赖。每一个都要在 PR 描述里给出理由

## 工作流

```bash
# 1. fork 后克隆你自己的仓库
git clone git@github.com:<you>/soccerdream-experts.git
cd soccerdream-experts

# 2. 开分支 —— 绝不在 main 上改
git checkout -b persona/add-injury-context-reader

# 3. 改完先在本地校验
make lint          # schema + markdown + 密钥扫描
make test          # 单元测试

# 4. 按下面的格式提交
git commit -m "feat(agents): add injury-context reader persona"

# 5. 推送并对着 main 开 PR
git push origin persona/add-injury-context-reader
```

`make lint` 和 `make test` 跟 CI 跑的是同一套命令。本地过了，CI 基本就会过。
如果 CI 挂了而你在本地复现不出来，直接在 PR 里说明，我们来看。

## 分支命名

```
persona/<短标识>      新增或修改人设
team/<短标识>         新增或修改团队配置
fix/<短标识>          修 bug
docs/<短标识>         仅文档
chore/<短标识>        工具链、CI、依赖
```

## 提交格式

采用 Conventional Commits。标题用祈使句、不超过 72 字符、不加句号。

```
<type>(<scope>): <subject>

[可选正文 —— 解释「为什么」，不要解释「改了什么」，diff 已经说明改了啥]

[可选脚注 —— Refs #123, BREAKING CHANGE: ...]
```

type：`feat`、`fix`、`docs`、`refactor`、`test`、`chore`、`perf`
scope：`agents`、`teams`、`cli`、`sdk`、`docs`、`ci`

合格：

```
feat(agents): add injury-context reader persona

现有人设都在加权近期状态，但忽略了确认缺阵。这个人设先看名单，
名单未确认时明确拒绝发言。
```

不合格：

```
改了点东西
```

## 合并请求

模板里的每一栏都要填。只写「修复」两个字的 PR 会被直接关闭，并附回本文链接。
如果你的 PR 关闭了某个 Issue，单独一行写 `Closes #123`。

一周内你会收到三种结果之一：**合并**、**要求修改**（会写清改哪里）、**拒绝**（会给理由）。
我们不会让 PR 无声地挂着——超过一周没动静，直接在帖子里 ping。

## 语言

- 代码、注释、提交信息、人设正文：**英文**
- 文档可以提交任意语言；`*.zh-CN.md` 镜像由我们维护
- PR 讨论：都可以，你用什么语言我们就用什么语言回

## 行为准则

对事直接，对人宽容。欢迎围绕设计争论，不接受人身轻慢。见 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。
