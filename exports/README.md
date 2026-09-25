# Context exports

Status: ACTIVE PROCESS

Run `python scripts/export_context_pack.py`. Each export has a fresh timestamp/sequence and is immutable once written. It identifies omitted material explicitly if the ledger exceeds the inline threshold. Repository state remains authoritative.

`Source commit` in a pack is the checkout HEAD read when that pack was generated. The pack is normally committed afterward, so this value may be the parent of the commit containing the pack. Future pack headers state this explicitly; existing packs remain immutable (`FIX-0004`).
