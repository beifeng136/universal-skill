# Old Project Skill Trigger Catalog

Use this catalog when extracting a reusable guidance system from an older
project. It records what each old workflow skill was for, when to trigger it,
and whether it is already safe as a general skill or still needs project-local
translation.

Core rule:

```text
Reuse process skills as workflow.
Do not import old project claims, metrics, denominators, paths, credentials, or
route conclusions.
```

## Status Classes

```text
portable-skill:
  Already abstracted enough to be used across projects.

portable-pattern:
  Useful workflow, but the skill body may still mention old project paths or
  old claim rules. Translate into the target project's authority files.

project-specific:
  Keep as an example or warning unless explicitly rewritten for the target.
```

## Already Published As Portable Skills

| Skill | Status | Use | Trigger |
|---|---|---|---|
| `project-os-bootstrap` | portable-skill | Create, repair, or preserve a project operating system. | New project, messy project migration, missing AGENTS/current_state/registry/finalizer, restart discipline. |
| `living-engineering-error-loop` | portable-skill | Turn recurring engineering failures into guardrails and retry rules. | Failed command, transfer/runtime/proxy/path/dependency error, repeated shell mistake, unsafe retry. |
| `cross-project-server-fastlane` | portable-skill | Keep server/transfer/runtime work isolated from the scientific main thread. | GPU/server job, file transfer, hash/path verification, output-root isolation, server status source. |
| `project-guidance-transfer` | portable-skill | Extract old project workflow skills and adapt them into a new project safely. | User asks to inherit old skills, summarize reusable workflow, migrate guidance, or publish generalized skills. |

## Old Project Skills To Reuse As Portable Patterns

| Skill | Status | Use | Trigger | Translation Rule |
|---|---|---|---|---|
| `project-entry-state-lock` | portable-pattern | Start from real project state instead of chat memory. | Continue project, route work, status-aware coding, process hardening. | Replace old preflight/current_state with target preflight/current_state. |
| `new-paper-research-accelerator` | portable-pattern | Coordinate large coherent research continuation without route drift. | User says continue/accelerate/report the old-style research project. | Use as pattern only; rewrite project name, stations, route IDs, AP locks, and evidence objects. |
| `research-route-gate` | portable-pattern | Open, hold, stop, switch, or report scientific routes. | Route design, pass/hold/stop decision, denominator-sensitive research judgment. | Replace old denominator and route labels with target fixed evidence object and route card. |
| `experiment-launch-denominator-gate` | portable-pattern | Prevent experiments from launching without denominator/output/pass-stop rules. | Training, rerun, baseline expansion, metric run, GT-aligned diagnostic, manifest gate. | Require target dataset/split/output root/expected artifacts. |
| `reusable-material-index` | portable-pattern | Check existing materials before rerunning or rebuilding. | Before reusing prediction JSON, manifest, runner, feature table, old readout, or dataset slice. | Query target registry/index first; old materials are source-only. |
| `failure-attribution-strategy-bypass` | portable-pattern | Diagnose failed/weak/suspicious routes and decide whether to bypass. | Bad result, under-target run, old failed-route resemblance, threshold-only retry temptation. | Convert old failures into target constraints and mechanism-difference checks. |
| `route-readout-card-authoring` | portable-pattern | Write route/readout cards with evidence boundaries. | Reporting route status, diagnostic readout, failure summary, next route decision. | Separate observation, diagnosis, route decision, and claim boundary in target terms. |
| `runtime-capability-inventory` | portable-pattern | Decide local/server/model/runtime readiness. | Choosing CPU/GPU/server, model cache, Cellpose/SAM/SAM2-like runtime, dependency probe. | Translate runtime names and paths; do not assume old environment availability. |
| `long-job-nightly-planning` | portable-pattern | Plan checked long jobs and overnight runs. | Full training, full inference, full manifest build, server/background/nightly job. | Require target output root, status source, fallback, expected artifacts, finalizer. |
| `engineering-transfer-guardrail` | portable-pattern | Harden file transfer, sync dependency, server runner, and path work. | Copying files, server upload/download, OSS queue, transfer-only-missing, dependency sync. | Verify target absolute paths, hashes, visibility, and non-destructive scope. |
| `server-transfer-runtime-ops` | portable-pattern | One-key pre-launch gate for server transfer/runtime. | Server transfer, runtime smoke, queue launch, material bundle, remote bytes/hash verification. | Replace server identities and remote roots; require target smoke command. |
| `server-execution-thread-handoff` | portable-pattern | Prepare a separate server execution thread handoff. | Main agent keeps research decisions, server thread only executes checked commands. | Write target-specific prerequisites, output roots, status source, and closure expectation. |
| `engineering-issue-registry-recurrence` | portable-pattern | Register repeated engineering issues and promote guardrails. | Same failure class recurs; need self-test/tool/skill update. | Prefer target engineering_errors or equivalent recurrence registry. |
| `subagent-coordination-and-active-registry` | portable-pattern | Coordinate bounded support subagents and registry hygiene. | Delegating audits, docs, transfer prep, environment checks, registry sync. | Do not delegate main scientific judgment; close subagent status in target registry. |
| `checked-result-finalizer` | portable-pattern | Finalize completed artifacts/results before reuse or claims. | Route card, readout, status sync, long job, support output, reusable artifact completion. | Use target finalizer/finalized_results; drafts cannot advance state. |
| `status-artifact-registry-sync` | portable-pattern | Keep registry, decision ledger, state, and checked-result references aligned. | Files changed; status cards/readouts/decisions need durable registration. | Use target artifact_registry and decision_ledger. |
| `paper-claim-writing` | portable-pattern | Draft paper/report language from checked evidence only. | Manuscript text, captions, claim map, reviewer response, paper risk note. | No claim without target checked artifact and claim boundary. |
| `multi-role-reviewer` | portable-pattern | Stress-test plans from multiple stakeholder/reviewer perspectives. | Route critique, paper risk, experiment design review, reviewer objection simulation. | Use target evidence and target constraints; do not invent checked results. |

## Target-Specific Skills That Should Not Be Generalized Blindly

| Skill | Status | Use | Trigger | Safe Reuse |
|---|---|---|---|---|
| `densecell-project` | project-specific | DenseCell entry router and state authority. | DenseCell/high-density cell segmentation tasks. | Use as an example for creating a target entry skill. |
| `densecell-research-accelerator` | project-specific | DenseCell status-aware continuation and route gating. | DenseCell continuation, route planning, progress reporting. | Extract macro-phase execution cadence and claim-safe reporting patterns. |
| `densecell-progress-map` | project-specific | DenseCell visual progress map/Atlas maintenance. | DenseCell progress tree, roadmap, Atlas, visual status. | Extract visual reporting standard, not DenseCell route facts. |
| `densecell-status-reporting` | project-specific | DenseCell reports and Atlas/mind-map style updates. | DenseCell status report, project report, route summary. | Extract concise report shape and visual-trigger rule. |
| `virtual-staining-project` | project-specific | MSC virtual staining project planning. | Virtual staining/MSC project tasks. | Use as another example of project-specific entry skill design. |

## Trigger Map By Task

```text
Continue / resume project
  -> target entry skill
  -> project-entry-state-lock pattern
  -> checked-result-finalizer if previous work must be closed

Create or repair project OS
  -> project-os-bootstrap
  -> living-engineering-error-loop if repair follows repeated process failure

Migrate old project workflow into new project
  -> project-guidance-transfer
  -> old-project-skill-trigger-catalog.md
  -> adoption-card-template.md

Route design or route switch
  -> research-route-gate
  -> failure-attribution-strategy-bypass when old-route resemblance exists
  -> route-readout-card-authoring

Experiment launch / rerun / scale-up
  -> experiment-launch-denominator-gate
  -> reusable-material-index
  -> research-route-gate
  -> long-job-nightly-planning if heavy

Failure / weak result / suspicious result
  -> failure-attribution-strategy-bypass
  -> living-engineering-error-loop if operational failure is possible
  -> route-readout-card-authoring

Runtime / model / server choice
  -> runtime-capability-inventory
  -> server-transfer-runtime-ops
  -> cross-project-server-fastlane
  -> engineering-transfer-guardrail

Server execution handoff
  -> server-execution-thread-handoff
  -> long-job-nightly-planning
  -> checked-result-finalizer

Subagent delegation
  -> subagent-coordination-and-active-registry
  -> status-artifact-registry-sync after closure

Status / registry / durable record
  -> status-artifact-registry-sync
  -> checked-result-finalizer

Paper/report/claim writing
  -> paper-claim-writing
  -> route-readout-card-authoring
  -> checked-result-finalizer

Repeated engineering failure
  -> living-engineering-error-loop
  -> engineering-issue-registry-recurrence if a project-specific registry exists
```

## Abstraction Priority

If converting more old skills into standalone portable skills, use this order:

```text
P0 already done:
  project-os-bootstrap
  living-engineering-error-loop
  cross-project-server-fastlane
  project-guidance-transfer

P1 good candidates:
  research-route-gate
  experiment-launch-denominator-gate
  failure-attribution-strategy-bypass
  checked-result-finalizer
  status-artifact-registry-sync

P2 useful but more project-coupled:
  route-readout-card-authoring
  reusable-material-index
  runtime-capability-inventory
  long-job-nightly-planning
  subagent-coordination-and-active-registry
  paper-claim-writing

P3 keep as target-specific examples unless rewritten:
  new-paper-research-accelerator
  densecell-project
  densecell-research-accelerator
  densecell-progress-map
  densecell-status-reporting
```

Before promoting a pattern into a standalone portable skill, remove or
parameterize:

```text
old project paths
old metric names as hardcoded claims
old route IDs as target truth
old server identities
old paper claims
old dataset denominators
```
