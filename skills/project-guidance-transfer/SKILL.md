---
name: project-guidance-transfer
description: Extract reusable project operating systems, workflow skills, route gates, failure lessons, reporting standards, and evidence/claim boundaries from an old project, then adapt them into a new project without importing old project-specific scientific claims, metrics, denominators, paths, or conclusions. Use when migrating lessons from one project to another, building a new project guidance system from a previous project, turning accumulated project practice into reusable Codex skills, or auditing whether a new project has safely inherited old workflow skills.
---

# Project Guidance Transfer

Use this skill to turn hard-won project practice into a reusable guidance
system for another project. The key move is to extract process machinery while
blocking stale evidence, claims, paths, and results from leaking into the new
project.

## Core Rule

```text
Reuse workflow.
Do not reuse old claims.
Translate old paths and state into the new project's local authority.
Record what was adopted, what was forbidden, and how future agents should use it.
```

## When To Use

Use this skill when the user asks to:

```text
learn from an old project
inherit or adapt old skills
extract a project guidance system
turn project experience into reusable Codex skills
migrate workflow rules from one repo to another
summarize reusable project OS patterns
avoid repeating old failed routes
publish a generalized skill based on project experience
```

Do not use this skill to copy old scientific results, AP/accuracy numbers,
paper claims, private data, credentials, or model weights into a new project.

## Workflow

### 1. Identify Source And Target

State:

```text
source project:
target project:
user goal:
target authority files:
subagent decision:
claim boundary:
```

For the target project, prefer its local `AGENTS.md`, `current_state`,
preflight, registry, decision ledger, finalizer, and route cards over chat
memory.

### 2. Inventory Reusable Material

Read or locate the smallest useful set:

```text
old project AGENTS / operating rules
old project current state
old skill routing or skill list
old route cards and readouts
old failure maps and engineering errors
old registry / finalizer / decision ledger
old reporting or progress-map conventions
target project AGENTS / current state / routing files
```

Do not load the whole old project if a focused index, inventory, or manifest is
available.

### 3. Classify What Can Transfer

Use this split:

```text
transferable:
  entry-state lock
  preflight discipline
  fixed evidence object / denominator discipline
  route gate and pass/hold/stop template
  reusable material lookup
  failure attribution and strategy bypass
  runtime / transfer / server guardrails
  engineering error recurrence loop
  subagent coordination
  checked-result finalization
  status / artifact / decision registry sync
  claim-boundary writing
  progress reporting standards

non-transferable unless explicitly revalidated:
  AP / accuracy / metric numbers
  old denominators or splits
  old route conclusions
  old paper claims
  old model superiority claims
  old commercial or license conclusions
  old paths as target paths
  old credentials, data, weights, caches, or private artifacts
```

### 4. Translate Old Rules Into Target Rules

Write a translation table:

```text
old preflight -> target preflight
old current state -> target current state
old artifact registry -> target artifact registry
old decision ledger -> target decision ledger
old finalized results -> target finalized results
old denominator -> target fixed evidence object / split / benchmark
old metric lock -> target claim lock
old route names -> target route labels or warning labels
old failed routes -> target failure constraints
```

If an old skill still says to read old project paths, treat those paths as
source references only. For target work, use target-local state and tools as
authority.

### 5. Build A Scenario Routing Matrix

Create or update a target routing table:

```text
continue / status-aware work -> entry skill + state lock
route planning -> route gate + failure bypass + route card authoring
experiment / rerun -> denominator gate + material index + route gate
failure / weak result -> failure attribution + engineering loop if relevant
runtime / server / transfer -> runtime inventory + transfer guardrails + long-job planning
subagent work -> subagent registry + bounded assignment
report / visual map -> reporting skill + progress-map convention
closure -> artifact registry + decision ledger + checked finalizer
paper / claim writing -> checked evidence only
project OS repair -> bootstrap / preservation rules
```

See `references/skill-routing-matrix.md` for a compact reusable matrix.

### 6. Convert Failed Routes Into Constraints

For every old failure that may recur, record:

```text
old route:
failure layer:
root cause:
evidence:
why it should not be repeated directly:
safe reuse:
required mechanism difference:
stop condition:
```

Do not revive an old failed route with a new name. Require a real mechanism
difference before launch.

### 7. Update Target Guidance Artifacts

Depending on the project, update a minimal set:

```text
AGENTS.md or local project rules
skill routing file
agent tutorial or handoff note
status card for adoption decision
progress map / Atlas only if visual reporting changed
global target skill if the user wants future agents to inherit behavior
```

Keep the update scoped. Do not rewrite unrelated project OS files.

### 8. Register And Finalize

If the target project has registry tools, record:

```text
artifact id:
artifact path:
artifact kind:
decision:
reason:
evidence:
finalized result:
claim boundary:
```

If no such tools exist, create a small adoption card that future agents can
read before working.

## Output Shape

For a normal transfer report, answer with:

```text
Project guidance transfer
+-- source:
+-- target:
+-- adopted:
+-- forbidden imports:
+-- updated files:
+-- next use:
+-- claim boundary:
```

For a reusable skill publication task, produce:

```text
skill folder:
validated:
committed:
pushed:
remaining risk:
```

## Quality Gates

Before calling the transfer complete:

```text
old project-specific claims are not imported
old paths are translated or marked source-only
target authority files are named
scenario routing matrix exists
failure lessons are constraints, not conclusions
registry/finalizer is updated when available
future agents can tell when to trigger each reused skill
```

## References

Read only when needed:

```text
references/skill-routing-matrix.md
references/adoption-card-template.md
references/old-project-skill-trigger-catalog.md
```

## Forbidden

- Do not claim old metrics as target results.
- Do not treat old denominators as target denominators.
- Do not copy old paper claims or route conclusions into the new project.
- Do not move credentials, model weights, large data, caches, or raw outputs.
- Do not update global skills from a one-off observation unless reuse is
  clearly intended.
- Do not leave adoption only in chat; write a durable target artifact.
