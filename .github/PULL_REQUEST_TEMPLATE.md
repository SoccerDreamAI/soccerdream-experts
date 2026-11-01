<!--
English first, then 简体中文. Fill in EVERY section. A PR containing only "fix"
will be closed with a link back to CONTRIBUTING.md.

英文在前，简体中文在后。**每一栏都要填**。只写「修复」的 PR 会被关闭并附回贡献指南。
-->

## What this changes / 本 PR 改了什么

<!-- One or two sentences. The diff shows *what*; explain *why*. -->
<!-- 一到两句。diff 已经说明了「改了什么」，这里解释「为什么」。 -->

## Why it matters / 为什么值得改

<!-- What breaks, or what gets worse, if this is not merged? -->
<!-- 不合并的话，什么东西会坏、会变差？ -->

## Type of change / 变更类型

- [ ] New persona / 新增人设 (`agents/`)
- [ ] Persona change / 修改人设 (`agents/`)
- [ ] Team config / 团队配置 (`teams/`)
- [ ] Client or schema / 客户端或 schema (`cli/`, `sdk/`)
- [ ] Docs only / 仅文档
- [ ] Tooling or CI / 工具链或 CI

## How it was verified / 如何验证

<!--
Paste the output of the commands you ran. "It works" is not verification.

贴出你实际跑的命令输出。「能跑」不算验证。
-->

```bash
$ make lint
$ make test
```

## Persona checklist / 人设专用自查

<!-- Skip if this PR does not touch agents/. / 不涉及 agents/ 可跳过。 -->

- [ ] All four sections present and in order: `Prior`, `Method`, `Evidence standard`, `Refusal`
      四段齐全且顺序正确：`Prior`、`Method`、`Evidence standard`、`Refusal`
- [ ] The `Prior` is a specific bias, not "be careful and consider many factors"
      `Prior` 是一条具体的偏好，不是「要谨慎、要多方面考虑」
- [ ] `Refusal` is written as a rule, not a preference
      `Refusal` 写成规则，不是倾向
- [ ] Body is under 400 words / 正文 400 字以内
- [ ] No real fixtures, real odds, or real team names in examples
      示例中不含真实赛事、真实赔率或真实球队名

## Safety checklist / 安全自查

- [ ] No credentials, tokens, keys, or `.env` files in this diff
      本 diff 不含任何凭据、token、密钥或 `.env` 文件
- [ ] No internal hostnames, private IPs, or connection strings
      不含内网主机名、私有 IP 或连接串
- [ ] This PR does not introduce a selection, tip, stake, or recommendation
      本 PR 不引入选项、建议、下注金额或推荐
- [ ] This PR does not make conflicting reads averaged together
      本 PR 不引入「对冲突结果取平均」

## Related issue / 关联 Issue

<!-- Use `Closes #123` on its own line to auto-close. / 单独一行写 `Closes #123` 可自动关闭。 -->

Closes #
