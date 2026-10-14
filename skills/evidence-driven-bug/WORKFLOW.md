# 功能 / 正确性

证据出现之前不改代码。必要证据是最小复现，以及一个在旧实现上会失败的测试。

## 输入

- 目标：错误行为消失，现有行为不被破坏。
- 边界：允许改哪些模块；不允许改哪些公共 API；是否允许迁移、格式或并发语义变化。
- 并发或 IO 问题还要有压力测试或确定性重放。

## 问题卡

```bash
python3 scripts/new_investigation.py --kind bug --slug your-problem-name
```

写下症状、影响范围、触发条件、相关模块、期望行为、当前行为、日志或 trace、已排除原因。

## 先复现

```text
Given 已知状态和输入
When 执行目标函数 / API / 状态迁移
Then 结果不符合 spec
```

不能稳定复现时，先补观测：输入、状态快照、trace id、关键分支日志、时间戳、随机种子、环境变量、依赖版本。信息不够就继续收集，不修代码。

## 候选

使用同目录的 `PROMPT.md`。每个候选要有根因、代码位置、它为何解释现有证据、可证伪预测、验证实验、风险、候选 patch 思路。

证据还兼容多个原因时，保留每个检验过的候选，包括 `rejected` 和 `inconclusive`。失败测试已经钉死原因时，不要编造额外候选。

一次实验只改一件事。不顺手重构，不改无关风格。

## 最终 patch

只包含必要修改。每个行为变化有测试。公共接口变化写明。有回滚方式。不隐藏根因。不用 broad catch、retry 或 sleep 掩盖问题。不削弱断言。

## 验证

跑 formatter、linter、type check、unit tests、integration tests、相关回归和 build。再跑 failing test、边界、兼容性；涉及并发时跑 stress 或 race detector。

用 `CHECKLISTS/acceptance-checklist.md` 做 review。测试必须能在旧实现上失败。

## 归档

留下问题卡、根因、候选、被拒绝方案、patch、测试、review 和后续动作。至少两个已验证案例才更新 `TEMPLATES/problem-family-card.md`。
