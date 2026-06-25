---
name: living-engineering-error-loop
description: Record, diagnose, guard, self-test, and prevent repeated engineering failures across projects. Use before retrying failed commands, transfer/server/runtime errors, shell invocation mistakes, permission problems, dependency issues, wrapper/status mismatches, evaluator failures, or any recurring operational error that should update project guardrails or skills.
---

# Living Engineering Error Loop

Use this skill when something fails in a way that could happen again. The goal
is not only to fix the current error, but to make the project harder to break
next time.

## Core Loop

Before retrying the same class of failed action:

```text
1. stop
2. classify failure_layer
3. write expected vs observed
4. identify root_cause or mark bounded diagnostic only
5. add guardrail
6. self-test guardrail
7. decide retry_allowed
8. update relevant skill/tool/template when prevention is procedural
```

If root cause is unknown, the next action may be a diagnostic, not a rerun of
the original heavy command.

## Failure Intake

Every reusable failure record should contain:

```text
error_id:
timestamp:
project:
task:
local_or_server:
command_or_runner:
expected:
observed:
first_bad_artifact_or_log:
failure_layer:
root_cause:
impact:
same_class_history:
guardrail:
self_test:
retry_allowed:
next_output_root_or_retry_scope:
skill_or_tool_update:
```

Use `scripts/error_intake.py` to draft or append JSONL records.

## Failure Layers

Use these portable layers:

```text
shell_invocation
filesystem_permission
path_visibility
transfer_visibility
network_or_proxy
runtime_profile
dependency_import
model_or_large_artifact
wrapper_contract
output_root_identity
status_observability
queue_control
materialization_logic
metric_or_evaluator
credential_or_auth
git_or_version_control
unknown_engineering
```

## Guardrail Promotion

Choose one promotion level:

```text
Level 0 observation: record only
Level 1 local guard: command note, checklist, local script check
Level 2 tool guard: patch script/wrapper/preflight
Level 3 skill guard: update a reusable skill
Level 4 project rule: update AGENTS.md or project OS
```

Promote only as high as needed. Do not make every local typo a project-wide
law.

## Retry Permission

Set `retry_allowed: yes` only when:

```text
root cause is known, or retry is explicitly a bounded diagnostic
registry/intake record exists
guardrail level is chosen
guardrail or manual exception is recorded
self-test passed or manual check is recorded
retry scope/output root is safe
relevant skill/tool update decision is recorded
```

Otherwise set `retry_allowed: no`.

## Common Portable Guardrails

PowerShell:

```text
Do not use Bash heredoc syntax in PowerShell. Use a here-string piped to the
program, or write a small checked script.
Do not combine Get-Content -Raw with -Tail.
Do not build destructive filesystem commands by concatenating paths.
```

Git/GitHub:

```text
If HTTPS git transport resets but browser/API works, test local proxy settings
and retry with explicit http.proxy/https.proxy before blaming credentials.
Do not push large data, caches, model weights, or run outputs to Git.
```

Server:

```text
Local path existence is not server visibility.
Owner queue pending=0 is not enough; require a smoke command before multi-file
transfer.
New long jobs need isolated output roots and status sources.
```

## Forbidden

- Do not retry first and explain later.
- Do not classify engineering failure as research or product evidence.
- Do not overwrite failed roots during retry.
- Do not update a global skill from a one-off failure unless recurrence or risk
  justifies it.
- Do not leave repeated failures only in chat; write an intake record or patch a
  guardrail.
