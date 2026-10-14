# 性能

证据出现之前不改代码。必要证据是数字目标、固定 benchmark、至少 3 次采样，以及 before/after profile。

## 输入

- 目标：达到明确的性能预算，例如 P95、CPU、allocations 或 DB query count。
- 边界：数据正确性不变；对外 API 不变，除非明确允许。
- “变快”不是目标。

## 问题卡

```bash
python3 scripts/new_investigation.py --kind performance --slug your-problem-name
```

先固定数据集、输入规模、并发、预热、测量次数、采样指标、硬件或容器限制、依赖版本。

记录 P50、P95、P99、CPU time、wall time、allocations、GC、DB query count、IO wait、lock contention。

## 先测量

没有 baseline 和 profile 时，只收集它们，不改代码。把目标代码、benchmark 命令、profile、最近变更、不变量和约束交给分析。

## 候选

使用同目录的 `PROMPT.md`。每个候选要预测某个指标变化多少。证据还兼容多个原因时保留落选候选。profile 已经钉死热点时，不要编造额外候选。

一次实验只改一件事。不用缓存、预热或数据倾斜解释未达成的预测。

## 最终 patch

只包含必要修改。正确性测试仍然通过。有回滚方式。不把开销转嫁到相邻场景。

## 验证

跑 formatter、linter、type check、测试和 build。再跑 before、after、至少 3 次采样、P95 和 P99、目标场景和相邻场景。

用 `CHECKLISTS/acceptance-checklist.md` 做 review。benchmark 必须可复现。

## 归档

留下协议、baseline、after、profile、候选、被拒绝方案和后续动作。至少两个已验证案例才更新 `TEMPLATES/problem-family-card.md`。
