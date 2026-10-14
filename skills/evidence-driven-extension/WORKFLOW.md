# 新功能

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

使用同目录的 `PROMPT.md`。少于两个设计时，不实现。比较实现复杂度、耦合、可测试性、回滚难度和后续演进成本。

## 最终 patch

第一步只包含所选设计里测试覆盖的最小切片。每个行为变化有测试。有回滚方式。不提前加入配置、持久化或并发。

## 验证

跑 formatter、linter、type check、测试和 build。再跑所选设计的测试，以及兼容性测试。

用 `CHECKLISTS/acceptance-checklist.md` 做 review。

## 归档

留下被拒绝的设计、第一步包含和不包含的内容、测试和后续演进项。
