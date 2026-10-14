# Problem Family: <family name>

## Definition

用一句话定义这类问题。

```text
当 <condition> 时，代码容易发生 <failure mode>。
```

## Verified examples

| Evidence ID | Repo / Module | Root cause | Fix pattern |
|---|---|---|---|
|  |  |  |  |

只有至少 2 个已验证案例时才把状态设为 confirmed；否则使用 tentative。

## Common signals

```text
code smell:
log pattern:
metric pattern:
review pattern:
```

## Reusable prevention

### Test template

```text
Given:
When:
Then:
```

### Static / CI check

```text
rule:
tool:
scope:
```

### Review checklist

- [ ] 
- [ ] 

## Design-level action

如果反复出现，不要继续只做局部 patch，考虑：

```text
API redesign:
state machine redesign:
schema validation:
type-level prevention:
ownership change:
```

## Status

```text
family status: tentative | confirmed | resolved-by-design
last updated:
```

不足两个已验证案例时保持 tentative。需要比较多个已验证记录时，用下面的提示：

```text
以下是多个已验证问题：

<evidence records>

请归纳重复出现的根因家族、典型代码模式、可复用测试模板、适合静态检查的部分，以及哪些问题说明设计本身需要调整。
不要根据单例建立家族；否则标记为 tentative。
```
