# Shared agent instructions

Applies to Codex, Claude Code, Kimi Code, and other agents in this repository. Human owner instructions take priority. The repository default branch is the canonical source of truth; local copies are execution workspaces.

## Start every task

1. Read this file and `PROJECT_STATE.md`.
2. Read the relevant show/story/operations documents and related ledger entries.
3. Identify the task, authority, affected files, and any human approval gate.
4. Do the authorized work, validate it, and log meaningful state changes in `PROJECT_LEDGER.md` before updating `PROJECT_STATE.md`.
5. Append a `SES` entry and any needed `DEC`, `PROP`, `ERR`, `FIX`, `RES`, or `POL` entries; update `CHANGELOG.md` when appropriate.
6. Report outcome, evidence, open questions, and commit/push status. Commit with a meaningful message when permitted.

## Finish every session (mandatory GitHub synchronization)

The canonical source of truth is `https://github.com/taher-krf/kids-studio.git`; every local workspace is only a temporary working copy. A task is NOT complete while intended changes exist only locally. At the end of every successful work session the agent MUST:

1. Review every file created or modified during the session and confirm each artifact lives in the correct canonical location (see placement guidance below); never create arbitrary new directories when an existing project directory fits.
2. Run all relevant checks: repository validation, tests, ledger-integrity check, and task-specific quality checks.
3. If project state changed meaningfully: update `PROJECT_STATE.md` and append the appropriate `PROJECT_LEDGER.md` entries, never modifying historical ledger bytes.
4. Update all affected manifests, indexes, registries, documentation, and operational records.
5. Generate a new immutable `CONTEXT_PACK` via `python scripts/export_context_pack.py` whenever the session materially changes project state, canon proposals, architecture, agent systems, research conclusions, production systems, or major decisions.
6. Inspect `git status`; stage only intended project changes; create one meaningful commit describing the completed work.
7. Push to `origin/main` unless an explicitly approved repository workflow requires another branch.
8. Verify after push: local HEAD is the intended final commit, `origin/main` contains it (e.g. `git ls-remote origin refs/heads/main`), no intended files remain only locally, and the working tree is clean except for explicitly documented unrelated local changes.
9. Report at completion: canonical repository, branch, commit hash, push status, files created/modified, ledger entries appended, validation/test results, latest CONTEXT_PACK path, and unresolved issues or blockers.

Push safety — agents must NEVER: force-push; rewrite published Git history; alter or delete historical ledger content; commit credentials, API keys, passwords, OAuth secrets, or tokens; push temporary or build artifacts unless explicitly part of the repository; knowingly push a broken or failed canonical state; or claim a push succeeded without remote verification.

If validation fails: attempt an authorized fix where safe, rerun validation, and do not mark the session complete while validation remains failed. If the issue cannot safely be resolved: record and report the blocker, preserve useful local work, do not push knowingly broken state, and report exactly what remains local. If authentication or write access prevents the push: do not claim successful completion; report the exact blocker, the local commit hash if one exists, and all unpushed changes.

Canonical placement guidance: governance → `00_project/`; show canon → `01_show_bible/`; story/comedy systems → `02_story_system/`; research → `03_research/`; episode work → `04_episodes/`; visual system → `05_visual_system/`; production → `06_production/`; agents → `07_agents/`; operations → `08_operations/`; metrics → `09_metrics/`; scripts/automation → `scripts/`; external synchronization exports → `exports/`. If placement is unclear, inspect the existing repository structure before creating a new path.

## Authority and canon

The human owner alone approves changes to core character identity, audience, world/power rules, series premise, brand, comedy engine, or approved episode canon. Agents may append `PROP` entries but proposals are not canon. Never silently upgrade `PROVISIONAL` or `TO_VERIFY` to approved. Never rewrite ledger history. Do not invent research evidence, performance metrics, production assets, or episode canon.

## Childhood-first editorial gate

The intended core audience is provisionally ages 4–6. Center universal childhood experiences: friendship, kindness, responsibility, curiosity, family, cooperation, honesty, courage, emotional regulation, creativity, problem-solving, nature, science, and everyday life. Do not produce or promote sexual activity, sexualized behavior, sexual orientation, gender identity/transition themes, adult romantic or sexual identity debates, or ideological/political messages about sexuality or gender. Apply the same rule to every orientation. Ordinary terms such as boy/girl, mother/father, brother/sister, and grandmother/grandfather are permitted when relevant. Do not use characters to teach that biological sex is interchangeable or irrelevant. Never ridicule, demean, insult, encourage hostility, make discriminatory jokes, or use characters as culture-war symbols.

For a proposal entering sexuality, sexual orientation, gender identity, religion, politics, or another adult ideological dispute: **stop automatic story generation**, mark `SENSITIVE_CONTENT_REVIEW_REQUIRED`, explain the trigger neutrally, make no canon change, and escalate to the human owner for an explicit decision. This policy is owner-supplied creative canon and may not be silently changed by an agent. See `02_story_system/AGE_4_6_RULES.md` and `08_operations/HUMAN_APPROVAL_GATES.md`.

## Security and quality

Do not commit secrets or private credentials. Use `.env.example` for names only. Preserve originality; study abstract comedy mechanics, not protected plots, gags, dialogue, characters, or sequences. Reject unsafe imitation risks. No finished episodes, visual assets, final voices, or renderer choice in the foundation phase.
