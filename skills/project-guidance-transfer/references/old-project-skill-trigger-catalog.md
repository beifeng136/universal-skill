# Old Project Skill Trigger Catalog

Use this catalog when extracting a reusable guidance system from an older
project. It records what each old workflow skill was for, when to trigger it,
and how to reuse it in a target project.

Important nuance: many skills created during the old `new_paper` project are
already globally registered and encode genuinely general mechanisms. Mentions
of `new_paper`, old denominators, old route names, or old claim locks usually
mean "replace this with the target project's authority object", not "do not
reuse this skill".

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

portable-registered-needs-translation:
  Globally registered and generally useful now. The body may still mention old
  project paths, denominators, route IDs, or claim rules. Translate those terms
  into the target project's authority files and evidence objects.

portable-pattern:
  Useful workflow not yet fully generalized as a standalone published skill.
  Reuse the mechanism, but expect to rewrite wording and file references.

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

## Globally Registered Old Project Skills That Are Mostly General

| Skill | Status | Use | Trigger | Translation Rule |
|---|---|---|---|---|
| `project-entry-state-lock` | portable-registered-needs-translation | Start from real project state instead of chat memory. | Continue project, route work, status-aware coding, process hardening. | Replace old preflight/current_state with target preflight/current_state. |
| `research-route-gate` | portable-registered-needs-translation | Open, hold, stop, switch, or report scientific routes. | Route design, pass/hold/stop decision, denominator-sensitive research judgment. | Replace old denominator and route labels with target fixed evidence object and route card. |
| `experiment-launch-denominator-gate` | portable-registered-needs-translation | Prevent experiments from launching without denominator/output/pass-stop rules. | Training, rerun, baseline expansion, metric run, GT-aligned diagnostic, manifest gate. | Require target dataset/split/output root/expected artifacts. |
| `reusable-material-index` | portable-registered-needs-translation | Check existing materials before rerunning or rebuilding. | Before reusing prediction JSON, manifest, runner, feature table, old readout, or dataset slice. | Query target registry/index first; old materials are source-only. |
| `failure-attribution-strategy-bypass` | portable-registered-needs-translation | Diagnose failed/weak/suspicious routes and decide whether to bypass. | Bad result, under-target run, old failed-route resemblance, threshold-only retry temptation. | Convert old failures into target constraints and mechanism-difference checks. |
| `route-readout-card-authoring` | portable-registered-needs-translation | Write route/readout cards with evidence boundaries. | Reporting route status, diagnostic readout, failure summary, next route decision. | Separate observation, diagnosis, route decision, and claim boundary in target terms. |
| `runtime-capability-inventory` | portable-registered-needs-translation | Decide local/server/model/runtime readiness. | Choosing CPU/GPU/server, model cache, model family runtime, dependency probe. | Translate runtime names and paths; do not assume old environment availability. |
| `long-job-nightly-planning` | portable-registered-needs-translation | Plan checked long jobs and overnight runs. | Full training, full inference, full manifest build, server/background/nightly job. | Require target output root, status source, fallback, expected artifacts, finalizer. |
| `engineering-transfer-guardrail` | portable-registered-needs-translation | Harden file transfer, sync dependency, server runner, and path work. | Copying files, server upload/download, queue work, transfer-only-missing, dependency sync. | Verify target absolute paths, hashes, visibility, and non-destructive scope. |
| `server-transfer-runtime-ops` | portable-registered-needs-translation | One-key pre-launch gate for server transfer/runtime. | Server transfer, runtime smoke, queue launch, material bundle, remote bytes/hash verification. | Replace server identities and remote roots; require target smoke command. |
| `server-execution-thread-handoff` | portable-registered-needs-translation | Prepare a separate server execution thread handoff. | Main agent keeps research decisions, server thread only executes checked commands. | Write target-specific prerequisites, output roots, status source, and closure expectation. |
| `engineering-issue-registry-recurrence` | portable-registered-needs-translation | Register repeated engineering issues and promote guardrails. | Same failure class recurs; need self-test/tool/skill update. | Prefer target engineering_errors or equivalent recurrence registry. |
| `subagent-coordination-and-active-registry` | portable-registered-needs-translation | Coordinate bounded support subagents and registry hygiene. | Delegating audits, docs, transfer prep, environment checks, registry sync. | Do not delegate main scientific judgment; close subagent status in target registry. |
| `checked-result-finalizer` | portable-registered-needs-translation | Finalize completed artifacts/results before reuse or claims. | Route card, readout, status sync, long job, support output, reusable artifact completion. | Use target finalizer/finalized_results; drafts cannot advance state. |
| `status-artifact-registry-sync` | portable-registered-needs-translation | Keep registry, decision ledger, state, and checked-result references aligned. | Files changed; status cards/readouts/decisions need durable registration. | Use target artifact_registry and decision_ledger. |
| `paper-claim-writing` | portable-registered-needs-translation | Draft paper/report language from checked evidence only. | Manuscript text, captions, claim map, reviewer response, paper risk note. | No claim without target checked artifact and claim boundary. |
| `multi-role-reviewer` | portable-skill | Stress-test plans from multiple stakeholder/reviewer perspectives. | Route critique, paper risk, experiment design review, reviewer objection simulation. | Use target evidence and target constraints; do not invent checked results. |

## Project Accelerator Skills To Treat As Templates

| Skill | Status | Use | Trigger | Safe Reuse |
|---|---|---|---|---|
| `new-paper-research-accelerator` | portable-pattern | Coordinate large coherent research continuation without route drift. | User says continue/accelerate/report a long-running research project. | Convert into a target accelerator by rewriting project name, stations, route IDs, metric locks, and evidence objects. |
| `densecell-research-accelerator` | project-specific | DenseCell status-aware continuation and route gating. | DenseCell continuation, route planning, progress reporting. | Extract macro-phase execution cadence, fast lane, claim-safe reporting, and visual reporting rules. |

## Target-Specific Entry And Reporting Skills

| Skill | Status | Use | Trigger | Safe Reuse |
|---|---|---|---|---|
| `densecell-project` | project-specific | DenseCell entry router and state authority. | DenseCell/high-density cell segmentation tasks. | Use as an example for creating a target entry skill. |
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

P1 should be generalized next:
  project-entry-state-lock
  research-route-gate
  experiment-launch-denominator-gate
  reusable-material-index
  failure-attribution-strategy-bypass
  route-readout-card-authoring
  checked-result-finalizer
  status-artifact-registry-sync

P2 should be generalized after the core route/result stack:
  runtime-capability-inventory
  long-job-nightly-planning
  subagent-coordination-and-active-registry
  paper-claim-writing
  engineering-transfer-guardrail
  server-transfer-runtime-ops
  server-execution-thread-handoff
  engineering-issue-registry-recurrence

P3 convert only as target accelerator templates:
  new-paper-research-accelerator
  densecell-research-accelerator

P4 keep as target-specific entry/reporting examples:
  densecell-project
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
