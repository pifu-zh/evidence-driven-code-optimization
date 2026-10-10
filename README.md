# Evidence-Driven Code Optimization

**Evidence-Driven Code Optimization** 是一套把 AI 生成候选答案和机器可验证证据分开的代码分析、修复、优化与扩展工作流。它适用于个人项目，也适合作为团队在 AI 辅助编码时的合入纪律。

## 核心原则

> AI 负责生成假设、补丁和反例；  
> 复现、测试、静态检查、benchmark、profile 和 review 负责裁决。

它借鉴 OpenAI `openai/math` 公开材料中的方法论：大量探索、过滤重要结果、聚合成问题家族，并对至少一部分结果做形式化验证。迁移到代码工程时，Lean proof 的位置由这些证据代替：

- 最小复现；
- failing test；
- property test；
- type check；
- static analysis；
- fuzz / stress test；
- reproducible benchmark；
- before/after profile；
- human review。

## 来源

方法论参考：

- [OpenAI: Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/)
- [GitHub: openai/math](https://github.com/openai/math)

本仓库借鉴的是上述公开材料中描述的工程思想：**先大量生成候选，再筛选，再聚合成家族，再用可验证工件确认**。它不是 OpenAI 官方项目，也不代表 OpenAI；没有复制 `openai/math` 中的论文、证明、模型输出或其他内容。

`README.md`、`WORKFLOW.md`、`PROMPTS.md`、模板、检查表、JSON Schema 和脚手架脚本是为软件工程场景独立整理的实现。项目由 [pifu-zh](https://github.com/pifu-zh) 维护，Codex 协助完成了初稿整理。

## 适用场景

适合以下场景：

| 场景 | 典型问题 | 必要证据 |
|---|---|---|
| 功能 / 正确性 bug | 状态机漏迁移、边界条件、折扣计算、权限判断、异步错误被吞掉 | 最小复现 + failing test |
| 性能退化 | 接口 P95 变高、批处理变慢、内存增长、DB QPS 突增 | 固定 benchmark + before/after profile |
| 热路径优化 | 序列化、缓存、查询、渲染、调度、锁竞争 | 目标指标 + 多轮采样 + 相邻场景回归 |
| 大范围重构 | 改公共接口、迁移状态模型、替换存储或框架 | 行为锁定测试 + 兼容性测试 + 回滚方案 |
| 新功能扩展 | 新 API、新规则、新任务类型、新集成 | 行为规范 + 候选设计对比 + 测试集 |
| AI 辅助编码 | 模型直接给 diff，但缺少根因和验证 | 假设、可证伪预测、实验结果、review |

不适合以下场景：

- 没有明确目标的“随便看看能不能优化”；
- 没有 benchmark 的性能改动；
- 没有失败测试的功能修复；
- 只为了看起来现代而做的大重构；
- 只需要一次性脚本、且错误成本极低的探索性实验。

## 目标读者

- 需要定位和修复难复现 bug 的工程师；
- 需要判断 AI 生成补丁是否可靠的工程师；
- 需要优化性能但希望避免凭感觉改代码的团队；
- 希望把重复问题沉淀成检查表、测试模板和静态规则的技术负责人；
- 使用 Codex、Claude、Copilot、Cursor 或其他 AI 工具，但不想让未验证 diff 直接进入 main 的人。

## 仓库结构

```text
README.md                          项目简介、来源、场景和快速用法
WORKFLOW.md                        从问题定义到合入归档的标准流程
PROMPTS.md                         bug、性能、扩展、review 和家族归纳 Prompt
CHECKLISTS/acceptance-checklist.md 合入前检查表
SCHEMA/evidence-record.schema.json evidence.yml 的结构说明
TEMPLATES/bug-investigation.md     功能 / 正确性问题模板
TEMPLATES/performance-investigation.md 性能问题模板
TEMPLATES/evidence-record.md       通用证据记录模板
TEMPLATES/problem-family-card.md   根因家族模板
scripts/new_investigation.py       新建调查记录的脚手架脚本
```

## 用法

## 1. 获取仓库

### 方式 A：作为独立工具包克隆

```bash
git clone https://github.com/pifu-zh/evidence-driven-code-optimization.git
cd evidence-driven-code-optimization
```

适合先学习流程，再手动在自己的项目里使用。

### 方式 B：放进目标仓库

把整个目录复制到你的项目，例如：

```bash
git clone https://github.com/pifu-zh/evidence-driven-code-optimization.git
cp -R evidence-driven-code-optimization /path/to/your-repo/evidence-toolkit
```

建议把 `evidence-toolkit/` 提交进目标仓库，这样团队可以共享模板、Prompt 和检查表。

## 2. 新建一次调查

在你的目标仓库根目录运行：

```bash
python3 /path/to/evidence-driven-code-optimization/scripts/new_investigation.py \
  --kind bug \
  --slug checkout-discount-zero-total
```

支持三类：

```bash
# 功能 / 正确性问题
--kind bug

# 性能问题
--kind performance

# 功能扩展
--kind extension
```

生成结果：

```text
evidence/001-checkout-discount-zero-total/
├── evidence.yml
└── README.md
```

`evidence.yml` 适合工具和长期归档；`README.md` 适合人阅读和 PR 引用。

## 3. 按场景填写

### Bug 场景

1. 写清楚症状、期望行为、当前行为；
2. 写最小复现；
3. 写一个会失败的测试；
4. 用 `PROMPTS.md` 里的 **功能 bug 根因分析** 让 AI 给候选根因；
5. 要求每个根因都有可证伪预测；
6. 做最小实验；
7. 确认根因后再生成最小 patch；
8. 跑回归、边界、兼容性和静态检查；
9. 用 `CHECKLISTS/acceptance-checklist.md` 复核；
10. 归档根因和被拒绝方案。

### 性能场景

1. 把目标写成数字，例如 P95、CPU、allocations、DB query count；
2. 固定数据集、并发、硬件、预热和采样方式；
3. 记录 baseline；
4. 收集 CPU、allocation、DB、IO 或 lock profile；
5. 用 **性能问题根因分析** Prompt 给 AI；
6. 每个假设必须预测某个指标会变化多少；
7. 做最小实验；
8. 比较 before/after，不只看平均值；
9. 检查相邻场景是否退化；
10. 合入后保留 benchmark artifact。

### 功能扩展场景

1. 写清用户可见行为和非目标；
2. 明确允许和不允许修改的模块；
3. 用 **功能扩展设计** Prompt 比较至少两个设计；
4. 给推荐方案定义最小测试集；
5. 拆出第一个最小 PR；
6. 每个行为变化都补测试；
7. 保留后续演进项。

## 4. 用 Prompt 和检查表约束 AI

不要让流程退化成：

```text
AI 给 patch → 直接合入
```

应保持：

```text
问题定义 → 复现 / profile → AI 候选假设 → 可证伪实验 → 最小 patch → 自动验证 → review → 合入
```

当 AI 给出建议时，追问：

```text
你预测修改后哪个测试会转绿？
你预测修改后哪个 benchmark 指标会下降多少？
如果预测不成立，怎么排除这个假设？
```

## 5. 提交 PR 时引用证据

建议在 PR 描述里加入：

```markdown
Evidence record: evidence/001-checkout-discount-zero-total/README.md

Root cause:
Discount was applied after clamping, so a discount larger than subtotal produced a negative total.

Verification:
- Added `cart-discount-boundary.test.js`.
- Old implementation failed the new test.
- New implementation passes unit, integration, typecheck, lint, and build.
```

性能 PR 则额外写：

```markdown
Benchmark:
- before: P95 842ms, allocations 184MB
- after: P95 407ms, allocations 93MB
- artifact: evidence/001-search-api-high-p95/benchmark.json
```

## 最重要的一条规则

如果 AI 给出的方案很合理，但没有证据，它仍然只是候选方案。

## License

Apache License 2.0。详见 [LICENSE](LICENSE)。
