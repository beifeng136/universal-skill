# Common Failure Taxonomy

Portable failure layers:

- `shell_invocation`: wrong shell syntax, quoting, heredoc, pipeline errors.
- `filesystem_permission`: denied writes, locked files, readonly workspace.
- `path_visibility`: path exists locally but not where the job runs.
- `transfer_visibility`: transfer incomplete, missing/mismatched bytes.
- `network_or_proxy`: reset, timeout, proxy mismatch, DNS, TLS issues.
- `runtime_profile`: wrong Python, CUDA, PATH, environment.
- `dependency_import`: package import or version mismatch.
- `model_or_large_artifact`: missing/partial/incorrect model or large file.
- `wrapper_contract`: runner status/log/exit contract mismatch.
- `output_root_identity`: reused or overwritten output root.
- `status_observability`: no reliable status source.
- `queue_control`: stale queue item, owner queue smoke failure.
- `materialization_logic`: output generated with wrong schema or identity.
- `metric_or_evaluator`: evaluator input identity or denominator problem.
- `credential_or_auth`: token, login, permission, auth callback issue.
- `git_or_version_control`: push/pull, branch, remote, large file issue.
- `unknown_engineering`: root cause not known yet.

Portable retry rule:

```text
unknown root cause -> diagnostic only
known root cause + guardrail + self-test -> retry may be allowed
```
