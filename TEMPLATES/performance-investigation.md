# Performance Investigation: <short title>

## Status

```text
state: investigating
target: <optimize latency / reduce allocations / reduce DB load>
confidence: low | medium | high
```

## Performance goal

不要写“变快”。

写：

```text
场景：
输入规模：
并发：
当前 P95：
目标 P95：
当前 allocations：
目标 allocations：
CPU / 内存 / IO 预算：
不允许退化的指标：
```

## Benchmark protocol

```text
硬件 / 容器：
运行时版本：
依赖版本：
数据集：
输入生成方式：
预热策略：
重复次数：
采样窗口：
统计口径：
执行命令：
```

## Baseline

| Metric | Value |
|---|---|
| P50 |  |
| P95 |  |
| P99 |  |
| CPU time |  |
| wall time |  |
| allocations |  |
| GC pause |  |
| DB query count |  |
| IO wait |  |
| error rate |  |

## Profile evidence

记录 profile 结论和原始文件位置。

| Profile | Observed hotspot | Artifact |
|---|---|---|
| CPU flamegraph |  |  |
| allocation profile |  |  |
| DB profile |  |  |
| lock / contention |  |  |

## Candidate causes

### Hypothesis 1

```text
假设：
代码位置：
为什么能解释 profile：
预期收益：
改动风险：
验证成本：
可证伪预测：
最小实验：
状态：untested / confirmed / rejected / inconclusive
```

## Experiments

| Experiment | Patch | Prediction | Result | Decision |
|---|---|---|---|---|
|  |  |  |  |  |

## Final result

| Metric | Before | After | Delta | Target | Pass |
|---|---:|---:|---:|---:|---|
| P50 |  |  |  |  |  |
| P95 |  |  |  |  |  |
| P99 |  |  |  |  |  |
| CPU time |  |  |  |  |  |
| allocations |  |  |  |  |  |

## Regression check

检查相邻场景：

```text
场景 A：
场景 B：
冷启动：
小数据量：
大数据量：
高并发：
异常路径：
```

## Decision

```text
decision: accepted | rejected | blocked
reason:
follow-ups:
```
