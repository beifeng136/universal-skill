# Skills Included

This repository contains generalized workflow skills extracted from real
research and engineering project failures. They are project-agnostic: use the
target project's own `AGENTS.md`, current state, registry, finalizer, routes,
datasets, metrics, releases, and claim rules as authority.

## Project OS And Transfer

### project-os-bootstrap

Purpose: install or audit a minimal project OS with entry rules, current state,
artifact registry, decision ledger, finalizer, and preservation templates.

Use for:

- new research or engineering projects
- migration of messy projects into a restartable structure
- project preservation before pausing

### project-guidance-transfer

Purpose: extract workflow systems, route gates, failure lessons, reporting
standards, and evidence/claim boundaries from an old project without importing
old project-specific claims.

Use for:

- learning from an older project without copying its results
- adapting old workflow skills into a new project
- building a target-local skill routing matrix
- turning failed old routes into constraints and stop conditions
- publishing generalized project-guidance skills

Reference:

- `skills/project-guidance-transfer/references/old-project-skill-trigger-catalog.md`
  records the old project skill stack, usage, trigger scenarios, and
  abstraction priority.

## State, Route, Evidence, And Closure

### project-entry-state-lock

Purpose: start any governed project work block from entry rules, preflight or
status gate, current state, fixed evidence object, and subagent decision.

Use for:

- continue-project turns
- status-aware coding or route work
- reports and process hardening
- any task that depends on current project state

### research-accelerator

Purpose: coordinate long-running research or evidence-driven work without route
drift.

Use for:

- continuing or accelerating a governed research project
- selecting the minimal companion skill stack
- splitting work into main research, support, evidence ladder, and long-job
  lanes
- combining planning, implementation, readout, and finalization into coherent
  work blocks

### research-route-gate

Purpose: open, hold, stop, switch, scale, or report evidence-driven research
routes with fixed evidence and claim boundaries.

Use for:

- route design and route switch decisions
- pass/hold/stop criteria
- scale-up decisions
- metric-safe scientific judgments

### experiment-launch-denominator-gate

Purpose: gate experiment launches and reruns before they consume time, compute,
data, or server resources.

Use for:

- training, reruns, baseline expansion, or metric gates
- fixed evidence object and output-root checks
- reusable-material lookup before recreation
- long/server experiment handoff readiness

### reusable-material-index

Purpose: query and verify existing artifacts before rebuilding, rerunning, or
reusing material.

Use for:

- manifests, prediction files, feature tables, source materials, benchmark
  outputs, scripts, model artifacts, and known risk notes
- avoiding stale denominators/evidence objects
- refreshing a reusable-material index after checked artifacts are produced

### checked-result-finalizer

Purpose: mark completed work as checked, draft, hold, or unfinalized before it
can affect state, claims, route progression, or reuse.

Use for:

- route cards and readouts
- long jobs and experiment outputs
- subagent handoffs
- docs/process artifacts that future work may rely on

### status-artifact-registry-sync

Purpose: keep current state, artifact registry, decision ledger, finalized
results, active subagents, and reusable-material indexes aligned.

Use for:

- artifact registration
- decision ledger updates
- status card sync
- finalized-result reference updates
- registry hygiene after docs/process/engineering work

## Failure, Readout, And Claims

### failure-attribution-strategy-bypass

Purpose: diagnose failed, weak, suspicious, blocked, or old-route-resembling
work before retry.

Use for:

- underperforming results
- repeated threshold/scorer/generator retry temptation
- separating engineering failure from domain failure
- deciding whether to diagnose, stop, switch, or bypass

### route-readout-card-authoring

Purpose: write route cards, diagnostic readouts, experiment summaries, decision
notes, and status cards with explicit evidence scope and claim boundaries.

Use for:

- readouts that must separate observation, diagnosis, decision, and next action
- marking missing finalizers as hold/unfinalized
- preventing draft notes from becoming unsupported route claims

### paper-claim-writing

Purpose: draft or audit manuscript, report, table, caption, claim-map,
reviewer-response, or release-note language from checked evidence only.

Use for:

- converting finalized results into scoped writing
- distinguishing diagnostic support from headline claims
- reviewer-risk and limitation notes

## Runtime, Server, Transfer, And Long Jobs

### runtime-capability-inventory

Purpose: choose local, server, CI, GPU, model, dependency, cache, and execution
environments from evidence rather than names.

Use for:

- model inference/training readiness
- dependency/runtime probes
- file visibility and model-weight byte/hash checks
- local vs server execution decisions

### long-job-nightly-planning

Purpose: package heavy, background, nightly, server, training, inference,
materialization, audit, transfer, or evaluation jobs safely.

Use for:

- isolated output roots
- fixed inputs and expected artifacts
- status sources and fallback conditions
- finalizer or closure commands

### cross-project-server-fastlane

Purpose: prevent server/transfer/runtime work from consuming the main project
thread.

Use for:

- server or GPU jobs
- large file movement
- runtime checks
- output-root and status-source gating

### engineering-transfer-guardrail

Purpose: harden file transfer, remote execution, queue work, dependency sync,
remote/local path mapping, runner wrappers, materialization, and engineering
retries.

Use for:

- transfer manifests and bytes/hash proof
- remote-visible path checks
- BLOCK/HOLD/ALLOW launch decisions
- keeping infrastructure problems out of scientific/product claims

### server-transfer-runtime-ops

Purpose: run an end-to-end pre-launch gate for server or remote transfer and
runtime execution.

Use for:

- material manifests
- queue health
- runtime profiles
- runner wrapper checks
- large artifact bundles
- checked server launches

### server-execution-thread-handoff

Purpose: prepare bounded server, remote, CI, or worker execution packets while
keeping judgment on the main thread.

Use for:

- server-side probes, runners, audits, or long jobs
- prerequisite cards
- forbidden-decision boundaries for worker threads
- status and finalization expectations

## Engineering Recurrence And Delegation

### living-engineering-error-loop

Purpose: make repeated engineering errors evolve into explicit guardrails.

Use for:

- failed commands
- transfer/runtime errors
- permission/path/proxy issues
- shell invocation mistakes
- retry permission decisions

### engineering-issue-registry-recurrence

Purpose: register, diagnose, guard, self-test, and retry repeated engineering,
runtime, transfer, evaluator, permission, dependency, shell, queue, or runner
failures.

Use for:

- same-class engineering failures
- deciding whether retry is allowed
- promoting recurring errors into local, tool, skill, or project rules

### subagent-coordination-and-active-registry

Purpose: coordinate bounded support subagents and active-subagent registry
hygiene.

Use for:

- environment audits
- transfer prep
- docs/readout drafts
- registry synchronization
- keeping route, metric, evidence, release, and claim decisions on the main
  agent
