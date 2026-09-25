# Session protocol

Status: ACTIVE PROCESS

Read AGENTS, state, canon, and ledger; identify authority; execute; validate; append session and decision/error entries; update state/changelog. Finalize every session per the mandatory "Finish every session" rule in `AGENTS.md`: full validation, ledger/state updates, CONTEXT_PACK export when the session materially changes the project, meaningful commit, push to `origin/main`, and remote verification before reporting completion.
