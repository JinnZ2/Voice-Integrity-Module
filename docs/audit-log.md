# Audit Log

**How this repository checks itself.**

A specification that describes its own structure will drift from that structure. The
defense is not care — it is falsification: state each claim so it can be run, run it, and
record what came back, including the claims that failed.

This file is the record. [`tools/validate.py`](../tools/validate.py) is the executable half:
every finding below that could be made machine-checkable was turned into a check, so the
same drift is caught by running one command rather than by noticing it again.

```bash
python3 tools/validate.py        # 558 assertions across 22 modes
python3 tools/validate.py -v     # list every passing assertion
```

**Conventions used here**

| | |
|---|---|
| **HELD** | Prediction survived the run. |
| **FALSIFIED** | Prediction failed. The claim was revised, not the evidence. |
| **REVISED** | A falsified claim, re-stated and re-run. |
| **OPEN** | Identified, not yet resolved. Carried forward. |

Findings are kept after they are fixed. A fixed finding is the reason a check exists.

---

## Audit 002 — 2026-08-14 · Legacy reorganization

**Scope.** Reconcile the repository against its own documentation after two feature
commits (`dbbe09d` endangered-language modes, `93424a1` training framework) had landed
without the docs being updated. Establish a legacy policy.

**Prior state.** 22 modes, 7 docs, 6 training files. Documentation described 6 modes and
6 docs.

### H1 — All mode JSON files parse

**Predicted** pass. **Ran** `json.load` over all 23 JSON files. **HELD** — 22 modes plus
`protocol.json`, all valid.

### H2 — All modes conform to the 11-parameter schema

**Predicted** failure. The schema was written when 6 modes existed; 16 have been added
since by two separate commits, and schema drift across independent additions is the normal
outcome.

**Ran** structural comparison of every mode's top-level keys and parameter set against the
schema in `CLAUDE.md`.

**HELD** — 22/22 conform exactly. No missing parameters, no extra parameters, no
missing top-level keys.

*This was the most surprising result of the audit.* The prediction was wrong in the
useful direction: the schema had held across sixteen additions by two commits without
enforcement. That it held by discipline rather than by mechanism is precisely why the
mechanism now exists — `tools/validate.py` makes the next sixteen cheap to trust.

### H3 — The four anti-performative invariants hold across all modes

**Predicted** pass, with low confidence for the endangered-language family, where honoring
an oral tradition could plausibly have required an exception.

**Ran** invariant check over all 22 modes × 4 invariants.

**HELD** — 88/88. No mode sets `upspeak`, `filler_enabled`, or `emotion_simulation` to
true, and none sets `silence_respect` to false. The traditions modeled turn out to align
with the anti-performative core rather than strain against it.

### H4 — Some mode uses a parameter value the documentation does not list

**Predicted** failure, for the same reason as H2.

**Ran** set difference between values in use and the documented vocabulary, per enum field.

**HELD** — zero undocumented values across all five enum fields, and zero documented
values that no mode uses. The vocabulary and the corpus match exactly in both directions.

**Action taken anyway.** The vocabulary lived only in `CLAUDE.md` prose. It has been moved
into `tools/validate.py` as the authoritative definition, with `CLAUDE.md` pointing at it.
Two copies of a list drift; one copy plus a pointer does not.

### H5 — `pause_between_sentences` stays inside the documented 0.8s–3.2s range

**Predicted** failure at the ceiling — ceremonial modes (`lakota-oral`,
`aramaic-liturgical`, `hawaiian-oli`) were expected to want pauses beyond 3.2s.

**Ran** parse and range check on all 22 values.

**HELD** — every value in range. `field-mode` sits exactly at the floor (0.8s) and
`silent-echo` exactly at the ceiling (3.2s). The ceremonial modes cluster at 2.6s–2.8s,
below the limit. The bounds were set with 6 modes and have survived 22.

### H6 — `protocol.json` has fallen out of sync with `modes/`

**Predicted** failure — the most common drift in a repo where modes are added by file.

**Ran** set comparison between `available_modes` and the directory contents.

**HELD** — exact match, no orphans, no unlisted modes, no duplicates.

**Latent issue found while checking.** `available_modes` is *not* alphabetical; it is
grouped core → accessibility → endangered, and that grouping was load-bearing but
undocumented. Anyone "fixing" the order by sorting it would have destroyed information
without any check objecting.

**Action.** Grouping made explicit as `mode_families` in `protocol.json`, and the
validator now asserts that the families partition `available_modes` *and* that
`available_modes` is their concatenation in order. The ordering is now defended.

### H7 — `companion-patch.md` is an exact duplicate of `patch-protocol.md`

**Predicted** exact duplication, from a first reading of both files.

**Ran** normalized text comparison.

**FALSIFIED.**

```
similarity ratio  0.8663   →  13.4% of the text differs
```

The claim as stated was wrong. Rather than abandon it, the discrepancy was inspected
directly instead of assumed to be meaningful.

**REVISED — "the difference is entirely markup, and the files are semantically
identical."**

**Re-ran** with markup normalized (backticks, bold markers, ellipsis glyph, arrow glyph,
section rules) and compared line by line.

**HELD** — zero semantic differences. All 13.4% is presentational:

| `patch-protocol.md` | `companion-patch.md` |
|---------------------|----------------------|
| `` `needs-diagnostic.md` `` | `needs-diagnostic.md` |
| `"..."` (three periods) | `"…"` (U+2026) |
| `**Analytical/Neutral Mode**` | `Analytical/Neutral Mode` |
| `to neutral voice equivalents` | `-> neutral voice equivalents` |

**Unknown surfaced by the revision.** Semantic identity establishes duplication but not
*direction* — which file supersedes which. Reading order suggested `patch-protocol.md` was
the successor, but that was inference, not evidence.

**Resolved from git rather than from reading.** `Example-companion-patch.md` was committed
at `cc17ce6`; `Patch-Protocol.md` at `faedd44`, later the same day. The original filename
carried the `Example-` prefix. The draft came first. Direction established from the record,
not from the prose.

**Action.** `docs/companion-patch.md` → [`legacy/companion-patch.md`](../legacy/companion-patch.md).

### H8 — Markdown code fences are balanced

**Predicted** pass — trivially true in most repos.

**Ran** fence-marker parity count over every `.md` file.

**FALSIFIED** — `vip-spec-v0.1.md` had 1 fence marker. Its closing ` ``` ` was missing, so
the sample-JSON block ran unterminated to end of file. Present since `c534caa`
(2025-08-22), the first content commit — unnoticed for nearly a year, because most
renderers close a trailing fence silently.

**Action.** Fence closed; parity check added to the validator.

### H9 — All internal cross-references point at files that exist

**Predicted** failure — the 2026-03-24 rename pass (`ea20932`) standardized filenames to
lowercase-hyphenated, and rename passes routinely miss references in prose.

**Ran** grep for pre-rename filenames, plus resolution of every relative markdown link.

**FALSIFIED**, as predicted. `docs/prosody-taxonomy.md` still referenced
`Needs-Diagnostic.md` and `Patch-Protocol.md` — filenames that had not existed for five
months. Both were bare code spans, not links, which is why nothing broke visibly and why
no reader reported it.

**Action.** References corrected to lowercase and converted to real links, so that a
future rename breaks them detectably. Two checks added: stale-filename grep, and
relative-link resolution.

### H10 — The documented file trees match the filesystem

**Predicted** failure with high confidence — this was the audit's motivating suspicion.

**Ran** membership check of every mode filename and every top-level directory against the
trees in `README.md` and `CLAUDE.md`.

**FALSIFIED**, severely. Both trees described the repository as it stood on 2026-03-24:

| | Documented | Actual |
|---|---|---|
| Modes | 6 | 22 |
| Docs | 6 | 7 |
| Top-level dirs | `docs/`, `modes/` | `docs/`, `modes/`, `training/` |

16 modes, `docs/endangered-languages.md`, and the entire `training/` layer were absent
from both trees. The trees had been correct when written and were never revisited.

**Action.** Both trees rewritten against the filesystem. A tree-membership check added to
the validator, which is the real fix — a hand-maintained tree will drift again, and now
drift fails a run.

### H11 — `protocol.json` accurately reports which extensions exist

**Not predicted.** Surfaced while cataloguing the expansion checklist in
`legacy/optional-extensions.md` against what was actually built.

`protocol.json` declared `"extensions": {"sigils": true}`. Nothing in the repository
implements sigils — no schema, no mode field, no doc. The flag had been aspirational from
the start and read as a capability claim in the one file a consuming system would parse.

This is the audit's only finding that could mislead a machine rather than a person.

**Action.** Corrected to `false`, with a `planned_extensions` block recording what was
intended, where it was proposed, and that it is unbuilt. Two adjacent unbuilt items
(auditory trust calibration, backend adapter) recorded in the same block.

### H12 — The new checks are correctly specified

**Predicted** pass. Written last, after the findings they encode.

**Ran** the validator against the corrected repository.

**FALSIFIED** — one check failed, and the check was wrong rather than the repository.

`check_legacy_citations` was written as *"no active document may link into `legacy/`"* and
it fired on `README.md` linking to `legacy/README.md`. But that link is correct: it is how
a reader finds the archive policy. The rule as coded forbade the behavior it should have
encouraged.

**REVISED — "no active document may link to superseded legacy *content*."** The folder's
index is not superseded content; the drafts inside it are.

**Re-ran** with the check resolving each link and exempting `legacy/README.md` only.
**HELD** — 558/558.

**Note.** The check was over-broad in a way that produced a *false positive*, so it
surfaced immediately. Had it been over-narrow it would have passed silently and protected
nothing. Checks that fail loudly when wrong are worth more than checks that are right by
construction.

### H13 — The checks detect the failures they claim to detect

**Not predicted.** A validator that has only ever passed proves nothing: a check that is
silently inert is indistinguishable from a check that is satisfied.

**Ran** ten single-fault mutations against a scratch copy, each reverted before the next,
plus an unmutated control.

| Mutation | Result |
|----------|--------|
| `emotion_simulation: true` on `elder-tone` | caught |
| `pause_between_sentences: "4.5s"` on `silent-echo` | caught |
| `cadence: "swooping"` — value outside vocabulary | caught |
| New mode file added, docs not updated | caught (3 failures) |
| `available_modes` sorted alphabetically | caught |
| Unclosed code fence appended | caught |
| Broken relative link appended | caught |
| Active doc linking to a superseded legacy draft | caught |
| Mode parameters reordered | caught |
| `mode_id` no longer matching its filename | caught |
| **Control — no mutation** | **passed, no false positives** |

**HELD** — 10/10 caught, control clean.

The alphabetical-sort mutation is the one worth noting: it is the plausible "tidying" edit
that H6 identified as silently destructive, and it is now the mutation the family-partition
check exists to catch. Finding, check, and proof that the check works are three separate
steps, and only the third makes the first two durable.

### Falsification summary

| | Predicted | Result |
|---|---|---|
| H1 parse | pass | **HELD** |
| H2 schema | fail | **HELD** — prediction wrong |
| H3 invariants | pass | **HELD** |
| H4 vocabulary | fail | **HELD** — prediction wrong |
| H5 pause range | fail | **HELD** — prediction wrong |
| H6 protocol sync | fail | **HELD** — prediction wrong; latent ordering issue found |
| H7 duplication | exact dup | **FALSIFIED** → revised → **HELD** |
| H8 fences | pass | **FALSIFIED** |
| H9 cross-refs | fail | **FALSIFIED** as predicted |
| H10 file trees | fail | **FALSIFIED** as predicted |
| H11 extensions | — | unpredicted finding |
| H12 checks correct | pass | **FALSIFIED** → check revised → **HELD** |
| H13 checks effective | — | **HELD** — 10/10 mutations caught, control clean |

**What the pattern says.** Every prediction about the *data* (H2, H4, H5, H6) was wrong in
the same direction: the machine-readable layer was in better shape than expected. Every
prediction about the *prose* (H8, H9, H10) was right or worse than expected. The mode files
were disciplined; the documentation describing them was nearly a year stale.

The inference for future work: **structured data in this repository has been maintained,
prose about it has not.** Checks were therefore weighted toward prose-vs-filesystem
agreement rather than toward the JSON, which was already sound.

### Open items carried forward

| # | Item | Source |
|---|------|--------|
| O-1 | `sigils` extension proposed, never built | H11, `legacy/optional-extensions.md` |
| O-2 | Auditory trust calibration protocol proposed, never built | `legacy/optional-extensions.md` |
| O-3 | No backend adapter — `training/synthesis-targets.json` defines targets with nothing consuming them | `legacy/optional-extensions.md` |
| O-4 | `TONE: [Post-collapse Engineering]` sketched, no mode built | `legacy/optional-extensions.md` |
| O-5 | Endangered-language modes are unreviewed approximations; no speaker or elder has validated any of them | `docs/endangered-languages.md` |
| O-6 | `docs/prosodic-equations.md` tables cover the 6 core modes only; 16 modes are absent from the worked examples | H10 follow-on |
| O-7 | Validator does not run automatically — no CI, no hook. Drift is caught only when someone runs it | this audit |

O-5 is the one that matters most and the one this repository cannot resolve on its own.

---

## Audit 001 — 2026-03-24 · Reconstructed

Reconstructed from commit `ea20932` ("Audit and organize"); no log was kept at the time.
Recorded here because its decisions are load-bearing for Audit 002 and were otherwise
recoverable only from the diff.

| Finding | Action |
|---------|--------|
| Filenames inconsistently cased (`VIP_v0.1.md`, `Needs-Diagnostic.md`, `Optional.md`) | Standardized to lowercase-hyphenated |
| Invalid JSON in mode files | Fixed |
| No conventions documented | `CLAUDE.md` added |
| Prosodic relationships informal | `docs/prosodic-equations.md` added |

**Missed by Audit 001, found by Audit 002:** the rename pass left stale references in
`docs/prosody-taxonomy.md` (H9), and did not detect that `companion-patch.md` duplicated
`patch-protocol.md` (H7) — both files were renamed and carried forward as if distinct.

This is the argument for keeping the log. Audit 001's blind spot was invisible until a
second pass looked for it, and would have been cheaper to find had its reasoning been
written down.

---

## Running an audit

1. **Predict before running.** A check whose outcome you did not commit to in advance
   teaches you nothing when it passes.
2. **Run** `python3 tools/validate.py`.
3. **Record falsified claims, not just fixes.** The wrong prediction is the finding.
   H2 passing when failure was expected changed how the rest of the audit was weighted.
4. **When a claim is falsified, revise and re-run it** before abandoning it. H7 was wrong
   as stated and correct once narrowed.
5. **Separate inference from evidence.** H7's supersession direction *looked* obvious from
   reading the files and was only settled by git history.
6. **Turn each finding into a check.** A fix without a check is the same finding deferred.
7. **Test the checks by breaking things on purpose.** A check that has only ever passed has
   not been shown to work — mutate the repository, confirm it fails, revert. H13 is that
   step, and it is the difference between a validator and the appearance of one.
8. **Carry unresolved items forward** as OPEN rather than dropping them.
