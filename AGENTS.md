# Shared agent instructions

Applies to Codex, Claude Code, Kimi Code, and other agents in this repository. Human owner instructions take priority. The repository default branch is the canonical source of truth; local copies are execution workspaces.

## Start every task

1. Read this file and `PROJECT_STATE.md`.
2. Read the relevant show/story/operations documents and related ledger entries.
3. Identify the task, authority, affected files, and any human approval gate.
4. Do the authorized work, validate it, and log meaningful state changes in `PROJECT_LEDGER.md` before updating `PROJECT_STATE.md`.
5. Append a `SES` entry and any needed `DEC`, `PROP`, `ERR`, `FIX`, `RES`, or `POL` entries; update `CHANGELOG.md` when appropriate.
6. Report outcome, evidence, open questions, and commit/push status. Commit with a meaningful message when permitted.

## Authority and canon

The human owner alone approves changes to core character identity, audience, world/power rules, series premise, brand, comedy engine, or approved episode canon. Agents may append `PROP` entries but proposals are not canon. Never silently upgrade `PROVISIONAL` or `TO_VERIFY` to approved. Never rewrite ledger history. Do not invent research evidence, performance metrics, production assets, or episode canon.

## Childhood-first editorial gate

The intended core audience is provisionally ages 4–6. Center universal childhood experiences: friendship, kindness, responsibility, curiosity, family, cooperation, honesty, courage, emotional regulation, creativity, problem-solving, nature, science, and everyday life. Do not produce or promote sexual activity, sexualized behavior, sexual orientation, gender identity/transition themes, adult romantic or sexual identity debates, or ideological/political messages about sexuality or gender. Apply the same rule to every orientation. Ordinary terms such as boy/girl, mother/father, brother/sister, and grandmother/grandfather are permitted when relevant. Do not use characters to teach that biological sex is interchangeable or irrelevant. Never ridicule, demean, insult, encourage hostility, make discriminatory jokes, or use characters as culture-war symbols.

For a proposal entering sexuality, sexual orientation, gender identity, religion, politics, or another adult ideological dispute: **stop automatic story generation**, mark `SENSITIVE_CONTENT_REVIEW_REQUIRED`, explain the trigger neutrally, make no canon change, and escalate to the human owner for an explicit decision. This policy is owner-supplied creative canon and may not be silently changed by an agent. See `02_story_system/AGE_4_6_RULES.md` and `08_operations/HUMAN_APPROVAL_GATES.md`.

## Security and quality

Do not commit secrets or private credentials. Use `.env.example` for names only. Preserve originality; study abstract comedy mechanics, not protected plots, gags, dialogue, characters, or sequences. Reject unsafe imitation risks. No finished episodes, visual assets, final voices, or renderer choice in the foundation phase.
