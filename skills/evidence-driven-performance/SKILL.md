---
name: evidence-driven-performance
description: >-
  Investigate performance regressions and hot paths with evidence. Use for
  latency, P95, throughput, allocations, memory growth, or slow batch jobs.
  Stop when there is no numeric target, fixed benchmark, repeated samples, or
  before/after profile.
---

# Evidence-Driven Performance

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

每个候选要预测某个指标变化多少。证据还兼容多个原因时保留落选候选。profile 已经钉死热点时，不要编造额外候选。

一次实验只改一件事。不用缓存、预热或数据倾斜解释未达成的预测。

不允许无证据下结论。每个假设必须可证伪。每个修改必须有验证方式。证据不足时必须明说。向模型要候选时使用：

```text
你是严格的性能工程助手。

目标：
根据 profile 和 benchmark 证据找出主要性能根因，而不是给出泛泛优化建议。

目标代码：
<paths>

性能目标：
<perf budget / SLA>

当前 benchmark：
<before benchmark summary>

环境：
<hardware, runtime, container limits, dataset, concurrency>

Profile 数据：
<CPU / allocation / IO / DB / GC / lock summary>

相关约束：
- 数据正确性不能变。
- 对外 API 不能变，除非明确允许。
- 禁止用 benchmark 噪声解释未达成的性能预测。
- 证据不足时必须说明。
- profile 已经钉死热点时，不要编造额外候选。

请输出：

1. 证据仍然兼容的候选性能根因。热点已经钉死时，说明为什么没有其他候选。
2. 按预期收益 / 改动风险 / 验证成本排序。
3. 每个根因对应具体代码位置。
4. 每个根因解释为什么它能解释 profile 现象。
5. 每个根因给出一个可证伪性能预测。
   例如：
   - P95 下降 20% 以上；
   - allocations 下降 40% 以上；
   - DB query count 从 500 降到 1。
6. 每个根因给出最小实验设计。
7. 对最优先假设给出最小实验 patch。
8. 明确列出可能导致结果无效的因素，例如缓存、预热、数据倾斜、JIT、网络抖动。
```

## 最终 patch

只包含必要修改。正确性测试仍然通过。有回滚方式。不把开销转嫁到相邻场景。

## 验证

跑 formatter、linter、type check、测试和 build。再跑 before、after、至少 3 次采样、P95 和 P99、目标场景和相邻场景。

用 `CHECKLISTS/acceptance-checklist.md` 做 review。benchmark 必须可复现。

## 归档

留下协议、baseline、after、profile、候选、被拒绝方案和后续动作。至少两个已验证案例才更新 `TEMPLATES/problem-family-card.md`。
