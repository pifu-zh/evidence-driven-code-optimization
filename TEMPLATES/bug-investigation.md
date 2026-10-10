# Bug Investigation: <short title>

## Status

```text
state: investigating
impact: < blocker / major / minor / internal >
confidence: low | medium | high
```

## Symptom

描述用户可见或系统可见的错误行为。

## Expected

写清楚规范，而不是只写“应该正确”。

## Actual

写清楚当前输出、状态变化或错误。

## Reproduction

```bash
# 最小复现命令
```

```text
Input:
Expected:
Actual:
Frequency:
Environment:
```

如果还不能稳定复现，列出缺少的信息。

## Evidence

| 证据 | 结论 | 位置 |
|---|---|---|
| failing test | 证明行为错误 | path/to/test |
| log | 显示异常分支 | artifact link |
| trace | 显示调用链 | artifact link |

## Candidate root causes

### Hypothesis 1

```text
假设：
代码位置：
为什么能解释证据：
可证伪预测：
验证实验：
状态：untested / confirmed / rejected / inconclusive
```

## Verified root cause

只有在实验确认后才填写这里。

```text
根因：
确认实验：
为什么其他假设被排除：
```

## Minimal fix

```text
改动范围：
patch link:
不做什么：
回滚方式：
```

## Tests

```text
旧实现必须失败的测试：
新实现必须通过的测试：
回归测试：
property / fuzz test：
```

## Decision

```text
decision: accepted | rejected | blocked
reason:
follow-ups:
```
