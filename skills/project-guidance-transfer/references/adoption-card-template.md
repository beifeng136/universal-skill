# Adoption Card Template

Use this template to make the transfer durable.

```markdown
# <Target Project> Workflow Skill Adoption - <date>

artifact_kind: process_skill_adoption_card
status: checked_process_guidance
source_project:
target_project:
target_state:

## Purpose

Explain what old project guidance is being adopted and why.

## Adoption Rule

```text
Reuse workflow.
Do not reuse old scientific or product claims.
Translate old paths into target-local state and tools.
```

## Target Authority

```text
<target AGENTS.md>
<target current_state>
<target artifact registry>
<target decision ledger>
<target finalized results>
<target preflight>
<target skill routing>
```

## Reused Skill Families

```text
1. Entry/state lock
2. Route and experiment gates
3. Failure attribution and strategy bypass
4. Runtime / server / transfer / long jobs
5. Engineering error prevention
6. Subagents, registry, and finalization
7. Claim and paper writing
8. Project OS repair
```

## Translation Table

```text
old preflight -> target preflight
old current_state -> target current_state
old artifact registry -> target artifact registry
old decision ledger -> target decision ledger
old finalized results -> target finalized results
old denominator -> target fixed evidence object / split / benchmark
old metric lock -> target claim lock
```

## Forbidden Imports

```text
old AP / accuracy / metric numbers
old denominators
old route conclusions
old paper claims
old product or commercial conclusions
old result identities as target evidence
credentials, weights, large data, caches, raw outputs
```

## Failure Lessons As Constraints

```text
old route:
failure layer:
root cause:
safe reuse:
required mechanism difference:
stop condition:
```

## Updated Files

```text
...
```

## Claim Boundary

Allowed:

```text
The target project adopted process guidance from the source project.
```

Forbidden:

```text
Any unsupported metric, model superiority, paper, product, or commercial claim.
```
```
