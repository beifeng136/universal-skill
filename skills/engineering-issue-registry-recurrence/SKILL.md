---
name: engineering-issue-registry-recurrence
description: Register, diagnose, guard, self-test, and retry repeated engineering, runtime, transfer, evaluator, permission, dependency, shell, queue, or runner failures. Use before retrying a failed engineering action, when the same class of failure may recur, or when support work must update an engineering issue registry without making route, metric, evidence, release, or claim decisions.
---

# Engineering Issue Registry Recurrence

Use this skill to close repeated engineering failures before retry. It is a
guardrail wrapper, not a route decision tool.

## Failure Intake

Before repeating the same class of action, write or update:

```text
error_id:
timestamp:
task:
local_or_remote:
command_or_runner:
expected:
observed:
first_bad_artifact_or_log:
failure_layer:
root_cause:
engineering_or_domain: engineering
same_class_history:
guardrail:
patch_target:
self_test:
retry_allowed:
next_output_root:
related_skill_or_tool_update_needed:
```

If root cause is unknown, the next action may only be a bounded diagnostic.

## Retry Permission

Retry is allowed only when:

```text
root cause is known or diagnostic-only
registry/update is done
guardrail level is chosen
patch or manual exception is recorded
self-test passed or manual check is recorded
new output root exists or checkpoint resume is proven
related skill/tool update check is done
```

## Failure Layers

Use precise labels:

```text
path_visibility
runtime_profile
model_or_asset_weight
wrapper_contract
output_root_identity
status_observability
shell_invocation
queue_control
materialization_logic
metric_or_evaluator
permission_or_filesystem
dependency_gap
unknown_engineering
```

## Guardrail Levels

```text
Level 0 observation
Level 1 local guard
Level 2 launch/fastlane rule
Level 3 tool or skill rule
Level 4 project operating rule
```

Promote only as far as recurrence and impact justify.

## Forbidden

- Do not retry first and explain later.
- Do not classify engineering failure as scientific/domain evidence.
- Do not overwrite failed roots or reuse stale commands without resume proof.
- Do not advance project state from an unfinalized registry note.
- Do not parse huge artifacts interactively when a streaming/hash summary would
  answer the engineering question.
