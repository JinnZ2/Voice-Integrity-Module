# Legacy — Superseded Documents

**Nothing in this folder is deleted, deprecated, or wrong-by-default.**

These are documents that a later document now covers more completely. They are kept because **precedent carries**: the earlier claim is the reason the later claim exists, and a specification that hides its own drafts cannot be audited.

A file lives here when *both* are true:

1. Something else in the repository now states the same thing more completely or more accurately, **and**
2. The file was the origin of that later statement — moving it would erase where the idea came from.

A file that is merely *old* does not belong here. A file that is *wrong* does not belong here either — wrong claims get corrected in place, with the correction recorded in [`../docs/audit-log.md`](../docs/audit-log.md).

---

## Contents

| File | Created | Superseded by | Why |
|------|---------|---------------|-----|
| `companion-patch.md` | 2025-08-23 (`cc17ce6`, as `Example-companion-patch.md`) | [`../docs/patch-protocol.md`](../docs/patch-protocol.md) | Semantic duplicate. Same five corrective specifications, same versioning ladder. Every textual difference is markup only. |
| `optional-extensions.md` | 2025-08-22 (`31a4cec`, as `Optional.md`) | [`../modes/`](../modes/), [`../protocol.json`](../protocol.json), [`../training/`](../training/) | Seed notes. Its `TONE:` sketches and expansion checklist have since been built out as real mode files and a production layer. |

---

## `companion-patch.md` — the duplication finding

The two files were compared after normalizing markup (backticks, bold markers, ellipsis glyph, arrow glyph, section rules):

```
raw similarity ratio           0.8663
normalized semantic difference 0 lines
```

The residual 13% is entirely presentational:

| `patch-protocol.md` | `companion-patch.md` |
|---------------------|----------------------|
| `` `needs-diagnostic.md` `` | `needs-diagnostic.md` |
| `"..."` (three periods) | `"…"` (U+2026) |
| `**Analytical/Neutral Mode**` | `Analytical/Neutral Mode` |
| `to neutral voice equivalents` | `-> neutral voice equivalents` |

**Direction of supersession is established by git, not by inference.** `Example-companion-patch.md` was committed at `cc17ce6`; `Patch-Protocol.md` was committed at `faedd44`, later the same day. The original filename carried the `Example-` prefix. The draft came first; the cleaned version came second. Neither file has been edited since, apart from the 2026-03-24 rename pass (`ea20932`).

## `optional-extensions.md` — the precedent it carries

This was the second document ever committed to the repository. Its `TONE:` list is the direct ancestor of the mode library:

| Original sketch | Became |
|-----------------|--------|
| `TONE: [Sámi Flat]` | [`sami-joik`](../modes/sami-joik.json) |
| `TONE: [Mechanic's Radio]` | [`field-mode`](../modes/field-mode.json) |
| `TONE: [Rural Field Calm]` | [`field-mode`](../modes/field-mode.json), [`elder-tone`](../modes/elder-tone.json) |
| `TONE: [Indigenous Matrilineal]` | the endangered-language family ([`docs/endangered-languages.md`](../docs/endangered-languages.md)) |
| `TONE: [Post-collapse Engineering]` | **not yet built** — still open |

Its expansion checklist, scored against the repository as it stands:

| Planned | Status |
|---------|--------|
| JSON mode library (`/modes/*.json`) | Done — 22 modes |
| Integration spec for OpenVoice / Coqui pipeline | Partial — [`training/synthesis-targets.json`](../training/synthesis-targets.json) defines targets; no backend adapter exists |
| Symbolic sigil and logic core | Not built — `extensions.sigils` is flagged `true` in `protocol.json` with nothing behind it |
| Companion symbolic protocol for auditory trust calibration | Not built |

Two of four items remain open. That is the reason this file is archived rather than discarded: it is still the only record of what was intended.

---

## Rules for this folder

- **Do not edit the bodies.** Superseded text is evidence. If it is wrong, that is part of the record. Only the provenance banner at the top of each file may be added or amended.
- **Do not cite legacy files as current.** Active documents must link to active documents.
- **Do not delete.** If a file here becomes genuinely irrelevant, note that in `docs/audit-log.md` and leave the file.
- **Moving something here is a claim** — that a named successor covers it. State the successor in the table above, or do not move the file.
