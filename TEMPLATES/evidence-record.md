# Evidence Record: <id>

## Metadata

```yaml
id: 001-example
title: Example problem
kind: bug
status: investigating
owner: your-name
created: 2026-10-11
updated: 2026-10-11
```

## Problem

```text
symptom:
expected:
actual:
impact:
scope:
```

## Reproduction or measurement

```yaml
kind: functional
command: make test
input: fixtures/example.json
expected: returns 200
actual: returns 500
stable: true
```

或者：

```yaml
kind: performance
command: ./run-benchmark.sh --dataset=100k --concurrency=50
repeat: 5
metrics:
  - p95_latency
  - cpu_time
  - allocations
```

## Hypotheses

| ID | Hypothesis | Code location | Prediction | Status |
|---|---|---|---|---|
| H1 |  |  |  | untested |
| H2 |  |  |  | untested |

## Experiments

| ID | Change | Prediction | Result | Evidence |
|---|---|---|---|---|
| E1 |  |  | confirmed / rejected / inconclusive |  |

## Verification artifacts

```text
failing test:
passing test:
static analysis:
property test:
fuzz test:
benchmark before:
benchmark after:
profile before:
profile after:
```

## Decision

```yaml
decision: accepted
root_cause_family: missing-boundary-check
confidence: high
reviewer: reviewer-name
follow_ups:
  - add static rule
  - extend property test
```
