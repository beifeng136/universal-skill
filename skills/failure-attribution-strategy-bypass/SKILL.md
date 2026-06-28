---
name: failure-attribution-strategy-bypass
description: Attribute failed, weak, suspicious, blocked, or old-route-resembling work before retrying it. Use when a result underperforms, a route stalls, a run looks suspicious, an engineering failure may be confused with science, or a proposed approach resembles a known failed route and needs a mechanism-difference or strategy-bypass decision.
---

# Failure Attribution Strategy Bypass

Use this skill to turn failure into constraints. Do not rename the same failed
route and try again without proving what changed.

## Failure Map

Before the next retry or scale-up, write:

```text
route or task:
fixed evidence object / benchmark / target:
expected outcome:
observed outcome:
failure_layer:
root_cause:
evidence:
engineering_or_domain_failure:
old-route resemblance:
mechanism difference now:
allowed next diagnostic:
strategy bypass:
stop condition:
```

Common failure layers:

```text
source_material_failure
candidate_generation_failure
model_or_algorithm_failure
selection_or_ranking_failure
actionability_failure
integration_or_conversion_failure
postprocessing_failure
evaluation_or_metric_failure
denominator_or_evidence_failure
runtime_failure
transfer_failure
permission_or_filesystem_failure
claim_design_failure
unknown
```

## Mechanism Difference Standard

A route that resembles a known failed shape must show a concrete mechanism
difference, such as:

```text
new evidence signal
new binding between error and target action
new protected intervention or rollback mechanism
new conversion/integration mechanism
new source family with non-duplicate material
new evaluation object that directly tests the suspected failure layer
```

These are not mechanism differences by themselves:

```text
larger run
new threshold
renamed scorer
same generator with a new wrapper
more candidates without better binding
retry after an unexplained failure
```

## Strategy Bypass

Ask:

```text
What outcome is actually needed?
Can another mechanism reach the same project objective?
Can generation become evidence acquisition?
Can direct repair become selection, arbitration, or evaluation?
Can the failure become a limitation, ablation, risk note, or stop rule?
What is the smallest diagnostic that distinguishes the next mechanism?
```

## Retry Rule

If root cause is unknown, the next action is a bounded diagnostic, not a larger
rerun. If the failure is operational, classify it as engineering until logs
prove a domain limitation.

## Forbidden

- Do not launch a larger run when the failed layer is unknown.
- Do not tune thresholds after the generator or evidence source has failed.
- Do not treat runtime, transfer, or permissions failure as scientific evidence.
- Do not revive stopped routes under new names without a failure map.
