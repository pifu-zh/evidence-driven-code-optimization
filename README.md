# Evidence-Driven Code Optimization

AI 可以提出假设、补丁和反例。复现、测试、静态检查、benchmark、profile 和 review 负责裁决。没有证据的方案仍然只是候选。

方法论启发来自 [OpenAI 的数学进展说明](https://openai.com/index/sharing-ai-progress-in-mathematics/) 和 [openai/math](https://github.com/openai/math)。本仓库不是 OpenAI 官方项目。文档和脚本由 [pifu-zh](https://github.com/pifu-zh) 为代码场景整理，Codex 协助起草。

## 用法

在仓库根目录安装四个 skill：

```bash
python3 setup.py install
```

技能会装到 `~/.cursor/skills/` 和 `~/.codex/skills/`。

在目标项目里新建调查记录：

```bash
python3 /path/to/evidence-driven-code-optimization/scripts/new_investigation.py \
  --kind bug \
  --slug checkout-discount-zero-total
```

`--kind` 可以是 `bug`、`performance` 或 `extension`。然后按对应 skill 的 `SKILL.md` 做。

## 使用场景

| Skill | 场景 | 改代码前必须有 |
|---|---|---|
| `evidence-driven-bug` | 结果错误、边界、权限、被吞掉的错误 | 最小复现，以及会在旧实现上失败的测试 |
| `evidence-driven-performance` | P95、吞吐、内存、热路径 | 数字目标、固定 benchmark、至少 3 次采样、前后 profile |
| `evidence-driven-refactor` | 改接口、状态模型、存储或框架 | 行为锁定测试、兼容性测试、回滚方案 |
| `evidence-driven-extension` | 新 API、新规则、新集成 | 用户可见行为、非目标、至少两个设计、所选设计的测试 |

不使用这些 skill 的情况：没有目标的优化、没有 benchmark 的性能改动、没有失败测试的功能修复、只为看起来现代的重构、错误成本极低的一次性脚本。

## 示例

功能。折扣大于小计时总价变成负数。先写测试证明旧实现会失败，再改把折扣放在截断之前的那一行。

```text
Evidence: evidence/001-checkout-discount-zero-total/README.md
Old implementation failed cart-discount-boundary.
New implementation passes the same test.
```

性能。搜索接口 P95 是 842ms，目标低于 500ms。先固定数据集和并发，记下 before profile，再改被 profile 钉住的那一处。

```text
before: P95 842ms
after: P95 407ms
artifact: evidence/001-search-api-high-p95/benchmark.json
```

重构。把订单状态从字符串改成枚举之前，先用现有非法迁移测试锁住行为，并写下如何回滚。

扩展。要加“预订单”时，先写清它不是退款，再比较“新状态”和“独立单据”两个设计，只实现测试覆盖的那一刀。

## License

Apache License 2.0。详见 [LICENSE](LICENSE)。
