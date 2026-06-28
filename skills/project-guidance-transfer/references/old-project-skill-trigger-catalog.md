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
| `project-entry-state-lock` | portable-skill | Start from real project state instead of chat memory. | Continue project, route work, status-aware coding, process hardening. |
| `research-route-gate` | portable-skill | Open, hold, stop, switch, or report scientific routes. | Route design, pass/hold/stop decision, denominator-sensitive research judgment. |
| `experiment-launch-denominator-gate` | portable-skill | Prevent experiments from launching without denominator/output/pass-stop rules. | Training, rerun, baseline expansion, metric run, fixed evidence gate. |
| `checked-result-finalizer` | portable-skill | Finalize completed artifacts/results before reuse or claims. | Route card, readout, status sync, long job, support output, reusable artifact completion. |
| `status-artifact-registry-sync` | portable-skill | Keep registry, decision ledger, state, and checked-result references aligned. | Files changed; status cards/readouts/decisions need durable registration. |
| `reusable-material-index` | portable-skill | Check existing materials before rerunning, rebuilding, or reusing artifacts. | Before reusing prediction/output files, manifests, feature tables, runners, readouts, dataset slices, or source materials. |
| `failure-attribution-strategy-bypass` | portable-skill | Diagnose failed/weak/suspicious routes and decide whether to diagnose, stop, switch, or bypass. | Bad result, under-target run, old failed-route resemblance, threshold-only retry temptation. |
| `route-readout-card-authoring` | portable-skill | Write route/readout cards with evidence boundaries, artifact state, diagnosis, and next action. | Reporting route status, diagnostic readout, failure summary, or next route decision. |
| `runtime-capability-inventory` | portable-skill | Decide local/server/model/runtime readiness from evidence. | Choosing CPU/GPU/server/CI, model cache, dependency probe, or execution location. |
| `long-job-nightly-planning` | portable-skill | Plan checked long jobs and background runs. | Full training, full inference, materialization, audit, server/background/nightly job. |
| `engineering-transfer-guardrail` | portable-skill | Harden file transfer, dependency sync, server runner, queue, and path work. | Copying files, remote upload/download, queue work, missing/mismatch transfer, dependency sync. |
| `server-transfer-runtime-ops` | portable-skill | Gate remote/server transfer and runtime launch end to end. | Server transfer, runtime smoke, queue launch, material bundle, remote bytes/hash verification. |
| `server-execution-thread-handoff` | portable-skill | Prepare bounded server/worker execution thread handoffs. | Main agent keeps decisions; worker thread executes checked probes/runners/audits. |
| `engineering-issue-registry-recurrence` | portable-skill | Register repeated engineering issues and promote guardrails. | Same failure class recurs; retry requires root cause, guardrail, and self-test. |
| `subagent-coordination-and-active-registry` | portable-skill | Coordinate bounded support subagents and registry hygiene. | Delegating audits, docs, transfer prep, environment checks, registry sync. |
| `paper-claim-writing` | portable-skill | Draft paper/report/release language from checked evidence only. | Manuscript text, captions, claim map, reviewer response, limitation or risk note. |
| `research-accelerator` | portable-skill | Coordinate large coherent research continuation without route drift. | User says continue, accelerate, plan, execute, or report a governed research project. |
| `multi-role-reviewer` | portable-skill | Stress-test plans from multiple stakeholder/reviewer perspectives. | Route critique, paper risk, experiment design review, reviewer objection simulation. |

## Project Accelerator Skills Kept As Source Examples

| Skill | Status | Use | Trigger | Safe Reuse |
|---|---|---|---|---|
| `new-paper-research-accelerator` | source-example | Old project-specific accelerator that inspired `research-accelerator`. | Historical source review only. | Use `research-accelerator` for new projects; do not import old station, route, metric, or evidence details. |
| `densecell-research-accelerator` | project-specific | DenseCell status-aware continuation and route gating. | DenseCell continuation, route planning, progress reporting. | Extract macro-phase execution cadence, fast lane, claim-safe reporting, and visual reporting rules only when building another target accelerator. |

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

## Abstraction Status

The old workflow stack has now been converted into standalone portable skills
for ordinary reuse:

```text
generalized:
  project-os-bootstrap
  living-engineering-error-loop
  cross-project-server-fastlane
  project-guidance-transfer
  project-entry-state-lock
  research-route-gate
  experiment-launch-denominator-gate
  checked-result-finalizer
  status-artifact-registry-sync
  reusable-material-index
  failure-attribution-strategy-bypass
  route-readout-card-authoring
  runtime-capability-inventory
  long-job-nightly-planning
  subagent-coordination-and-active-registry
  paper-claim-writing
  engineering-transfer-guardrail
  server-transfer-runtime-ops
  server-execution-thread-handoff
  engineering-issue-registry-recurrence
  research-accelerator

keep as target-specific examples:
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
