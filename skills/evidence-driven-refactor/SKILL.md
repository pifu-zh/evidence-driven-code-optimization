---
name: evidence-driven-refactor
description: >-
  Change structure only when evidence shows behavior stays locked. Use for
  public API changes, state-model migrations, or storage and framework
  replacements. Require behavior-lock tests, compatibility tests, and a
  rollback before editing.
---

# Evidence-Driven Refactor

证据出现之前不改代码。必要证据是锁定当前行为的测试、兼容性测试和回滚方案。

## 输入

- 目标：结构变化后，已有行为保持不变。
- 边界：允许动哪些模块；哪些公共 API、数据格式和并发语义不能变。
- 只为看起来现代而重构，停。

## 问题卡

写下要搬动的模块、必须保持的行为、禁止改变的接口，以及回滚步骤。

先写行为锁定测试。测试必须能在错误的新结构上失败。没有这些测试时，不开始搬动。

## 候选

一次只决定一个结构变化。不把行为修改混进同一次 patch。

不允许无证据下结论。每个结构变化必须有验证方式。证据不足时必须明说。向模型要方案时使用：

```text
你是严格的结构迁移助手。

目标：
在不改变已有行为的前提下，完成一次最小的结构搬动。

要保持的行为：
<behavior locked by tests>

允许搬动：
<modules>

不允许改变：
<public APIs / formats / concurrency>

现有锁定测试：
<commands and results>

约束：
- 没有行为锁定测试时，不要开始搬动。
- 不要在同一次 patch 里改变用户可见行为。
- 不要顺手改无关代码。
- 如果信息不足，请明确说明还缺什么证据。

请输出：

1. 这次搬动包含什么、不包含什么。
2. 哪些现有测试锁定了必须保持的行为。
3. 一个可证伪预测：哪条测试会在错误的新结构上失败。
4. 回滚步骤。
5. 兼容性风险。
```

## 最终 patch

只包含这次搬动。公共接口变化写明。回滚不需要考古。不用 broad catch、retry 或 sleep 掩盖行为变化。不削弱断言。

## 验证

跑 formatter、linter、type check、unit tests、integration tests、行为锁定测试、兼容性测试和 build。

用 `CHECKLISTS/acceptance-checklist.md` 做 review。确认没有新的用户可见行为。

## 归档

留下被锁定的行为、这次结构决定、回滚方式和后续动作。
