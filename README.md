# Voice Integrity Module

**Version:** VIP v0.1
**Author:** JinnZ2 + GPT-4o
**License:** CC0-1.0
**Status:** Active prototype

---

## Purpose

The Voice Integrity Module defines a vocal protocol that centers clarity, symbolic fidelity, and cross-cultural respect in voice-based AI systems. It rejects performative tone defaults and introduces selectable logic-based voice modes, honoring silence as a valid and vital part of communication.

This system is built for those who think in compressed logic, symbolic systems, field communication styles, or oral tradition cadences — and who find current voice assistants inauthentic, bloated, or emotionally manipulative.

---

## Key Features

- **Silence-as-structure**: Structured pauses instead of filler or false engagement.
- **Tone modes**: Logic-driven vocalization styles (e.g., Symbolic Monotone, Elder Tone).
- **Anti-performative defaults**: No mimicry, no upspeak, no marketing tone.
- **Pluggable**: Designed for symbolic AI, accessibility tools, or custom voice interfaces.
- **Cultural alignment**: Accommodates oral traditions and non-Western communication styles.

---

## Repository Structure

```
voice-integrity-module/
├── CLAUDE.md                     ← Development guide and conventions
├── README.md                     ← You're here
├── LICENSE                       ← CC0 1.0 Universal
├── protocol.json                 ← Machine-readable protocol configuration
├── vip-spec-v0.1.md              ← Full protocol specification
├── docs/
│   ├── needs-diagnostic.md       ← Technical analysis of voice/text mismatch
│   ├── patch-protocol.md         ← Corrective specs for voice layer issues
│   ├── prosody-taxonomy.md       ← Prosodic signal categories framework
│   ├── prosodic-equations.md     ← Formal prosodic parameter equations
│   ├── endangered-languages.md   ← Oral-tradition modes: scope, limits, how to correct them
│   └── audit-log.md              ← What was checked, what failed, what is still open
├── modes/                        ← 22 modes, one JSON file each
│   ├── symbolic-monotone.json    ← core: flat, neutral logic delivery
│   ├── field-mode.json           ← core: clipped, radio-comms style
│   ├── elder-tone.json           ← core: slow, deliberate, spacious
│   ├── silent-echo.json          ← core: whispered, ritual/contemplative
│   ├── debug-tone.json           ← core: line-by-line technical review
│   ├── coherence-pulse.json      ← core: subtle rhythmic symbolic emphasis
│   ├── add-focus.json            ← accessibility: concise, frequent micro-pauses
│   ├── adhd-flow.json            ← accessibility: brisk, momentum-preserving
│   ├── autism-clarity.json       ← accessibility: literal, predictable, low-ambiguity
│   ├── blind-nav.json            ← accessibility: spatial/navigational precision
│   ├── dyslexia-steady.json      ← accessibility: slow, evenly segmented
│   ├── hard-of-hearing.json      ← accessibility: high-clarity articulation
│   ├── sami-joik.json            ← endangered: Sámi joik (luohti/vuolle)
│   ├── dine-oral.json            ← endangered: Diné Bizaad ceremonial speech
│   ├── tsalagi-voice.json        ← endangered: Cherokee oratory
│   ├── hawaiian-oli.json         ← endangered: ʻŌlelo Hawaiʻi chant
│   ├── maori-whaikorero.json     ← endangered: Te Reo Māori formal oratory
│   ├── lakota-oral.json          ← endangered: Lakȟótiyapi storytelling/ceremony
│   ├── ainu-yukar.json           ← endangered: Ainu epic oral poetry
│   ├── quechua-oral.json         ← endangered: Runasimi oral tradition
│   ├── gaelic-bardic.json        ← endangered: Gàidhlig bardic poetry
│   └── aramaic-liturgical.json   ← endangered: Aramaic liturgical recitation
├── training/                     ← Production layer — how voice should sound
│   ├── README.md                 ← Framework overview and architecture
│   ├── breath-patterns.json      ← Breath as structure, not filler
│   ├── tone-color.json           ← Warmth, weight, brightness, presence
│   ├── pause-grammar.json        ← Formal grammar of silence types
│   ├── vocal-texture.json        ← Resonance, placement, grain, onset
│   ├── dynamic-contours.json     ← Loudness shape and phrase-level dynamics
│   └── synthesis-targets.json    ← Per-mode mapping to production values
├── tools/
│   └── validate.py               ← Repository validator (stdlib only)
└── legacy/                       ← Superseded, retained as precedent — never deleted
    ├── README.md                 ← What each file was, and what replaced it
    ├── companion-patch.md        ← Draft of patch-protocol.md
    └── optional-extensions.md    ← Seed notes that became the mode library
```

### Mode families

| Family | Count | Character |
|--------|-------|-----------|
| Core | 6 | Logic delivery — the original modes |
| Accessibility | 6 | Shaped around cognitive and sensory needs; the only family where `interruptible` is generally `true` |
| Endangered languages | 10 | Prosodic preservation of at-risk oral traditions — **draft approximations awaiting community review** |

All 22 hold the same four invariants: no upspeak, no filler, no emotion simulation,
silence respected. `protocol.json` is the authoritative list.

---

## Use Cases

- Voice layer for symbolic AI systems
- Swarm agents or non-performative assistant interfaces
- Tools for rural, Indigenous, and neurodivergent communication systems
- Accessibility enhancement for users who prioritize signal over mimicry

---

## Core Principle

> *Performance is not presence. Silence is syntax. Clarity is trust.*

---

## Validation

```bash
python3 tools/validate.py        # 558 assertions across 22 modes
python3 tools/validate.py -v     # list every passing assertion
```

Standard library only, no dependencies. Checks JSON validity, schema conformance,
the anti-performative invariants, pause bounds, `protocol.json` sync, link resolution,
and agreement between the documented file trees and the filesystem. Exit code is `0`
on success and `1` on any failure.

Run it before committing. What it has caught, and what it was written in response to,
is in [`docs/audit-log.md`](docs/audit-log.md).

---

## The `legacy/` Folder

Superseded documents move to [`legacy/`](legacy/) rather than being deleted. They are kept
because **precedent carries** — an earlier draft is the reason the current document exists,
and a specification that hides its own history cannot be audited.

A file moves there only when something else now covers it *and* it was the origin of that
later statement. Wrong claims are corrected in place and recorded in the audit log; only
*superseded* ones are archived. See [`legacy/README.md`](legacy/README.md) for the rules.

---

## Contributions

This module is seeded by JinnZ2 in collaboration with symbolic AI design. Contributions welcome from anyone who shares the principle that speech should serve thought — not theater.

**Most needed:** review of the endangered-language modes by speakers, elders, linguists,
and community members. Those 10 modes are approximations built from available knowledge,
and no one from any represented tradition has yet reviewed them. See
[`docs/endangered-languages.md`](docs/endangered-languages.md) — including how to request
removal if a community does not want their tradition represented here.

---

## Status

Stable prototype, specification-only — no runtime code. Live implementation depends on a
voice synthesis backend (e.g. OpenVoice, Coqui, ElevenLabs, Bark) and symbolic system
interface compatibility.

| Layer | State |
|-------|-------|
| Protocol (`modes/`, `protocol.json`) | Stable — 22 modes, schema-validated |
| Production (`training/`) | `0.1-draft` |
| Endangered-language modes | `0.1-draft` — unreviewed approximations |
| Synthesis backend adapter | **Not built** — see open items in [`docs/audit-log.md`](docs/audit-log.md) |

---

## License

CC0-1.0
