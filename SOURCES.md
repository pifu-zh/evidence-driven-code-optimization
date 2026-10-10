# Sources and Attribution

## Methodological source

This project adapts a public methodology pattern described by OpenAI for sharing AI-generated mathematical research:

- OpenAI, “Sharing AI progress in mathematics”: <https://openai.com/index/sharing-ai-progress-in-mathematics/>
- GitHub repository: <https://github.com/openai/math>

The reusable pattern is:

1. explore many candidates;
2. filter for significant or useful results;
3. group related outputs into families;
4. require independently checkable verification artifacts;
5. preserve revisions and provenance.

## Scope of adaptation

This repository transfers that pattern to software engineering:

| Original pattern | Software-engineering adaptation |
|---|---|
| Explore many mathematical attempts | Generate multiple root-cause hypotheses, designs, or patches |
| Select significant results | Prioritize by impact, risk, cost, and expected benefit |
| Group results into families | Group bugs and regressions into reusable root-cause families |
| Formal proof | Minimal reproduction, failing test, type/static check, property/fuzz test, benchmark, profile, and review |
| Versioned manuscripts | Versioned evidence records, patches, benchmarks, and decisions |

## Relationship to OpenAI

This is **not** an official OpenAI project and is **not** endorsed by OpenAI. It does not copy manuscripts, proofs, model outputs, prompts, or other contents from `openai/math`. Only the publicly described methodological pattern is used as inspiration.

## Implementation

The documentation, templates, prompts, schema, and scripts in this repository were independently prepared for software engineering use by [pifu-zh](https://github.com/pifu-zh), with Codex used to assist drafting and organization.
