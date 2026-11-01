# Security Policy · 安全策略

[English](#english) · [简体中文](#简体中文)

---

## English

### Reporting a vulnerability

**Do not open a public issue for security problems.**

Use GitHub's private advisory flow: **Security → Report a vulnerability**.
We acknowledge within 48 hours and aim to ship a fix or mitigation within 7 days for
issues affecting the client, and within 24 hours for anything that could expose
credentials or hosted-service data.

Please include: affected version, reproduction steps, and the impact you believe it has.
We will credit you in the advisory unless you ask us not to.

### Scope

| In scope | Out of scope |
|:--|:--|
| `cli/`, `sdk/` source | The hosted service's infrastructure (report separately) |
| `teams/` schema validation and parser | Rate limiting or quota complaints |
| Supply-chain issues in our dependency tree | Findings from automated scanners with no PoC |
| Anything that could leak a token or key | Social engineering of maintainers |

### Secrets: the one rule that gets a PR closed instantly

This repository must contain **zero** credentials. That includes:

- ❌ API keys, tokens, session cookies, JWTs — in any file, any branch, any commit
- ❌ `.env`, `.env.*`, `credentials.json`, `*.pem`, `*.key`
- ❌ Internal hostnames, private IPs, database connection strings
- ❌ Any example config that would work if pasted verbatim

Examples must use obvious placeholders:

```yaml
# ✅ correct
token: ${SD_TOKEN}

# ❌ wrong — even if it is a "test" key
token: <paste-a-real-key-here>
```

If you commit a secret by accident: revoke it first, then tell us. Do not try to
rewrite history quietly — we rotate on disclosure anyway, and a clean rewrite wastes
the reviewer's time.

A pre-commit hook and a CI secret scan both run on every PR. They will catch most of
this. They will not catch a key you base64-encoded "temporarily".

---

## 简体中文

### 漏洞报告

**安全问题请不要开公开 Issue。**

走 GitHub 私有通道：**Security → Report a vulnerability**。
我们 48 小时内确认；影响客户端的，7 天内给出修复或缓解；可能泄露凭据或托管服务数据的，24 小时内响应。

请附：受影响版本、复现步骤、你认为的影响面。除你要求匿名外，我们会在公告中署名致谢。

### 范围

| 在范围内 | 不在范围内 |
|:--|:--|
| `cli/`、`sdk/` 源码 | 托管服务的基础设施（请另行报告） |
| `teams/` 的 schema 校验与解析 | 限流、配额相关投诉 |
| 依赖树的供应链问题 | 无 PoC 的自动化扫描结果 |
| 任何可能导致 token 或密钥泄露的问题 | 对维护者的社工 |

### 密钥：唯一一条会让 PR 立刻被关闭的规则

本仓库必须**不含任何凭据**，包括：

- ❌ API Key、token、session cookie、JWT —— 任何文件、任何分支、任何提交
- ❌ `.env`、`.env.*`、`credentials.json`、`*.pem`、`*.key`
- ❌ 内网主机名、私有 IP、数据库连接串
- ❌ 任何「照抄就能用」的示例配置

示例一律使用明显的占位符：

```yaml
# ✅ 正确
token: ${SD_TOKEN}

# ❌ 错误 —— 哪怕它是「测试用」的 Key
token: <把真实 key 粘贴到这里>
```

如果误提交了密钥：**先吊销，再告知我们**。不要试图悄悄改写历史——反正我们要轮换，干净的改写只会浪费审查时间。

每个 PR 都会跑 pre-commit 钩子和 CI 密钥扫描。它们能挡住大部分情况，挡不住你「临时」base64 一下的那个 Key。
