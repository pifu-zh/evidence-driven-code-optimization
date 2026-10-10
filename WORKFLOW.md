# 标准流程

## 0. 输入

任何调查开始前，先确定三件事：

1. **目标**
   - bug：让错误行为消失且不破坏现有行为；
   - performance：达到明确性能预算；
   - extension：新行为可测试、可回滚、可演进。

2. **边界**
   - 允许改哪些模块；
   - 不允许改哪些公共 API；
   - 是否允许迁移、格式变化、并发语义变化。

3. **验收证据**
   - 功能问题至少需要 failing test；
   - 性能问题至少需要 reproducible benchmark；
   - 并发/IO 问题至少需要压力或确定性重放证据。

## 1. 建立问题卡

新建调查记录：

```bash
python3 scripts/new_investigation.py --kind bug --slug your-problem-name
```

填写：

- 症状；
- 影响范围；
- 触发条件；
- 相关模块；
- 期望行为；
- 当前行为；
- 日志 / trace / screenshot；
- 已排除原因。

## 2. 先复现，再分析

### 功能 / 正确性问题

优先写一个最小的 failing test：

```text
Given 已知状态和输入
When 执行目标函数 / API / 状态迁移
Then 结果不符合 spec
```

如果无法稳定复现，先补观测点：

- 输入 payload；
- 状态快照；
- trace id；
- 关键分支日志；
- 时间戳和时钟来源；
- 随机种子；
- 环境变量；
- 依赖版本。

### 性能问题

先固定 benchmark：

- 数据集；
- 输入规模；
- 并发数；
- 预热次数；
- 测量次数；
- 采样指标；
- 硬件 / 容器限制；
- 依赖版本。

至少记录：

- P50 / P95 / P99；
- CPU time；
- wall time；
- allocations；
- GC；
- DB query count；
- IO wait；
- lock contention。

## 3. 收集 profile 或失败证据

不要先让 AI 猜方案。

先给 AI 这些事实：

```text
目标代码
复现命令
failing test 输出
stack trace
profile 数据
最近相关变更
不变量
约束
```

如果信息不足，第一步是收集信息，不是修代码。

## 4. 让 AI 生成候选假设

每个候选假设必须有：

1. 根因解释；
2. 对应代码位置；
3. 为什么它解释现有证据；
4. 可证伪预测；
5. 验证实验；
6. 风险和影响面；
7. 候选 patch 思路。

禁止接受这种输出：

> “这里可能有问题，建议改成另一种写法。”

必须追问：

```text
你预测修改后哪个测试会转绿？
你预测修改后哪个 benchmark 指标会下降多少？
如果预测不成立，怎么排除这个假设？
```

## 5. 做最小实验

每个实验只验证一件事。

推荐顺序：

1. 写失败测试或补充观测；
2. 做最小 patch；
3. 只改目标路径；
4. 不顺手重构；
5. 不修改无关风格；
6. 运行完整验证；
7. 记录结果。

实验输出只有三种：

| 状态 | 含义 |
|---|---|
| confirmed | 预测成立，可以继续 |
| rejected | 预测不成立，记录并放弃 |
| inconclusive | 证据不足，继续收集或设计更好的实验 |

## 6. 生成最终 patch

最终 patch 必须满足：

- 只包含必要修改；
- 每个行为变化有测试覆盖；
- 公共接口变化显式说明；
- 有回滚方式；
- 不隐藏根因；
- 不用 broad catch / retry / sleep 掩盖问题；
- 不通过降低测试强度让 CI 通过。

## 7. 自动验证

### 所有改动必须跑

- formatter；
- linter；
- type check；
- unit tests；
- integration tests；
- relevant regression tests；
- build。

### 功能问题额外跑

- failing test；
- property test；
- boundary tests；
- backwards compatibility tests。

### 性能问题额外跑

- before benchmark；
- after benchmark；
- 至少 3 次或多轮采样；
- P95 / P99，不只看平均值；
- 目标场景；
- 相邻场景，确认没有退化。

### 并发 / 异步 / IO 问题额外跑

- stress test；
- race detector；
- timeout / retry chaos test；
- deterministic replay，如果可用。

## 8. 人工 review

review 不只是看代码风格，重点看：

1. 是否真的处理根因；
2. 是否引入新状态或新耦合；
3. 测试是否会在旧实现上失败；
4. benchmark 是否可复现；
5. 失败路径是否被覆盖；
6. 是否影响 API 兼容性；
7. 是否需要在 runbook / docs / migration 中更新。

## 9. 归档

合入后补齐：

```text
问题卡
根因
候选方案
被拒绝方案
最终 patch
测试
benchmark / profile
review 结论
根因家族
后续动作
```

然后更新 `problem-family-card.md`。
