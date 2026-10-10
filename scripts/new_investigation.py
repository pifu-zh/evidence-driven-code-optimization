#!/usr/bin/env python3
import argparse
import datetime as dt
import re
from pathlib import Path


KIND_TEMPLATES = {
    "bug": """# {title}

## Status

```yaml
id: {id}
title: {title}
kind: bug
status: investigating
owner: ""
created: {date}
updated: {date}
```

## Problem

```text
symptom:
expected:
actual:
impact: major
scope:
```

## Reproduction

```yaml
kind: functional
command: ""
input: ""
expected: ""
actual: ""
stable: false
```

## Hypotheses

| ID | Hypothesis | Code location | Prediction | Status |
|---|---|---|---|---|
| H1 |  |  |  | untested |

## Experiments

| ID | Change | Prediction | Result | Evidence |
|---|---|---|---|---|
| E1 |  |  |  |  |

## Verification

```yaml
failing_test_reproduces_old_behavior: false
tests: []
static_checks: []
profiles: []
```

## Decision

```yaml
decision:
root_cause_family:
confidence: low
reviewer:
reason:
follow_ups: []
```
""",
    "performance": """# {title}

## Status

```yaml
id: {id}
title: {title}
kind: performance
status: investigating
owner: ""
created: {date}
updated: {date}
```

## Performance goal

```text
scenario:
input_scale:
concurrency:
current_p95:
target_p95:
current_allocations:
target_allocations:
regression_guard:
```

## Benchmark protocol

```yaml
kind: performance
command: ""
repeat: 5
dataset: ""
concurrency: 1
warmup_runs: 1
environment: ""
metrics:
  - p50_latency
  - p95_latency
  - p99_latency
  - cpu_time
  - allocations
```

## Baseline

| Metric | Before |
|---|---:|
| P50 |  |
| P95 |  |
| P99 |  |
| CPU time |  |
| allocations |  |

## Hypotheses

| ID | Hypothesis | Code location | Predicted metric change | Status |
|---|---|---|---|---|
| H1 |  |  |  | untested |

## Experiments

| ID | Change | Prediction | Result | Artifact |
|---|---|---|---|---|
| E1 |  |  |  |  |

## Verification

```yaml
failing_test_reproduces_old_behavior: false
tests: []
static_checks: []
benchmarks:
  - name: baseline
    phase: before
    artifact: ""
profiles: []
```

## Decision

```yaml
decision:
root_cause_family:
confidence: low
reviewer:
reason:
follow_ups: []
```
""",
    "extension": """# {title}

## Status

```yaml
id: {id}
title: {title}
kind: extension
status: investigating
owner: ""
created: {date}
updated: {date}
```

## Requirement

```text
user-visible behavior:
non-goals:
allowed scope:
forbidden scope:
```

## Candidate designs

| ID | Design | Complexity | Testability | Rollback risk | Decision |
|---|---|---|---|---|---|
| D1 |  |  |  |  |  |
| D2 |  |  |  |  |  |

## Minimal first PR

```text
includes:
excludes:
tests:
```

## Verification

```yaml
failing_test_reproduces_old_behavior: false
tests: []
static_checks: []
profiles: []
```

## Decision

```yaml
decision:
confidence: low
reviewer:
reason:
follow_ups: []
```
""",
}


def next_number(base: Path) -> int:
    base.mkdir(parents=True, exist_ok=True)
    existing = []
    for child in base.iterdir():
        match = re.match(r"(\d{3})-", child.name)
        if child.is_dir() and match:
            existing.append(int(match.group(1)))
    return max(existing) + 1 if existing else 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an evidence-driven investigation record.")
    parser.add_argument("--kind", choices=sorted(KIND_TEMPLATES), required=True)
    parser.add_argument("--slug", required=True, help="Short kebab-case name, e.g. checkout-zero-total")
    parser.add_argument("--base", default="evidence", help="Output base directory. Default: evidence")
    parser.add_argument("--title", help="Human-readable title. Defaults to slug.")
    args = parser.parse_args()

    slug = args.slug.strip().lower()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        parser.error("--slug must be kebab-case, for example checkout-zero-total")

    number = next_number(Path(args.base))
    target = Path(args.base) / f"{number:03d}-{slug}"
    if target.exists():
        parser.error(f"Target already exists: {target}")

    target.mkdir(parents=True)
    today = dt.date.today().isoformat()
    title = args.title or slug.replace("-", " ")
    record_id = target.name
    (target / "README.md").write_text(
        KIND_TEMPLATES[args.kind].format(id=record_id, title=title, date=today),
        encoding="utf-8",
    )
    (target / "evidence.yml").write_text(
        f"""id: {record_id}
title: {title}
kind: {args.kind}
status: investigating
owner: ""
created: {today}
updated: {today}
problem:
  symptom: ""
  expected: ""
  actual: ""
  impact: unknown
  scope: []
reproduction:
  kind: {"performance" if args.kind == "performance" else "functional"}
  command: ""
  stable: false
hypotheses: []
verification:
  failing_test_reproduces_old_behavior: false
  tests: []
  static_checks: []
  benchmarks: []
  profiles: []
decision:
  confidence: low
  follow_ups: []
""",
        encoding="utf-8",
    )
    print(target)


if __name__ == "__main__":
    main()
