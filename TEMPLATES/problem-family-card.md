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
