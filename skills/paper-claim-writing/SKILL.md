---
name: paper-claim-writing
description: Draft, revise, adapt, or audit manuscript, report, claim-map, table, caption, qualitative-example, submission, reviewer-response, or release-note language from checked evidence without expanding claims beyond finalized artifacts. Use when writing must distinguish draft language, checked evidence, diagnostic support, limitations, and unsupported claims.
---

# Paper Claim Writing

Use this skill for writing-layer work only. It converts checked evidence into
scoped language; it does not create new results.

## Claim Trace

For every number, example, qualitative case, or comparative statement, trace:

```text
artifact id:
result id:
evidence object / benchmark / test suite:
metric or evaluation definition:
source file:
checked/finalized status:
claim scope:
allowed as paper/report/release claim? yes/no:
```

## Claim Types

Classify language as:

```text
draft only
checked evidence summary
bounded diagnostic result
mechanism support
ablation / limitation
future work
table or caption skeleton
claim map update proposal
reviewer-risk note
```

If an artifact is fixed but not broad, write it as bounded evidence rather than
a general headline result.

## Writing Rule

Use precise verbs:

```text
observed
supports
suggests
is consistent with
fails to show
is not yet evaluated for
```

Avoid stronger language unless the checked evidence supports it.

## Forbidden

- Do not introduce new metrics or results in prose.
- Do not promote support-only or diagnostic evidence into headline claims.
- Do not cite unfinalized long-job outputs as checked evidence.
- Do not revise denominators, predictions, ground truth, release state, or route
  status from a writing task.
