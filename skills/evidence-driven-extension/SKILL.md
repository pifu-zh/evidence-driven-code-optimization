---
name: evidence-driven-extension
description: >-
  Add behavior with evidence. Use for a new API, rule, task type, or
  integration. Require the user-visible behavior, non-goals, at least two
  compared designs, and tests for the chosen design before implementation.
---

# Evidence-Driven Extension

证据出现之前不改代码。必要证据是用户可见行为、非目标、至少两个设计的比较，以及所选设计的测试。

## 输入

- 目标：新行为可测试、可回滚、可演进。
- 边界：允许改哪些模块；不允许改哪些公共 API。
- 非目标没写清时，停。

## 问题卡

```bash
python3 scripts/new_investigation.py --kind extension --slug your-problem-name
```

写下用户可见行为、非目标、允许修改的范围、禁止修改的范围。

## 候选

少于两个设计时，不实现。比较实现复杂度、耦合、可测试性、回滚难度和后续演进成本。

不允许无证据下结论。每个设计必须有验证方式。证据不足时必须明说。向模型要设计时使用：

```text
你是严格的软件设计助手。

任务：
为一个新功能设计最小可验证实现方案。

现有架构：
<relevant architecture>

需求：
<requirement>

非目标：
<non-goals>

允许修改：
<allowed modules>

不允许修改：
<forbidden modules / public APIs>

请输出：

1. 用户可见行为定义。
2. 关键接口或数据模型草案。
3. 至少 2 个设计候选，并比较：
   - 实现复杂度；
   - 对现有耦合的影响；
   - 可测试性；
   - 回滚难度；
   - 后续演进成本。
4. 每个候选的最小测试集。
5. 推荐方案及理由。
6. 推荐方案的第一步最小 PR 应该包含什么、不包含什么。
7. 明确列出暂不处理的边界情况。
```

## 最终 patch

第一步只包含所选设计里测试覆盖的最小切片。每个行为变化有测试。有回滚方式。不提前加入配置、持久化或并发。

## 验证

跑 formatter、linter、type check、测试和 build。再跑所选设计的测试，以及兼容性测试。

用 `CHECKLISTS/acceptance-checklist.md` 做 review。

## 归档

留下被拒绝的设计、第一步包含和不包含的内容、测试和后续演进项。
