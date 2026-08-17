# CLAUDE.md — Voice Integrity Module

## Project Overview

The Voice Integrity Module (VIP) is a non-performative vocal protocol specification for AI voice systems. It defines prosodic parameters, tone modes, and signal-processing rules that prioritize clarity, cultural respect, and logic fidelity over performative speech patterns.

**Core principle:** *Performance is not presence. Silence is syntax. Clarity is trust.*

## Repository Structure

```
voice-integrity-module/
├── CLAUDE.md                     ← This file (development guide)
├── README.md                     ← Project overview and quick start
├── LICENSE                       ← MIT License
├── protocol.json                 ← Machine-readable protocol configuration
├── vip-spec-v0.1.md              ← Full protocol specification
├── docs/
│   ├── needs-diagnostic.md       ← Technical analysis of voice/text mismatch
│   ├── patch-protocol.md         ← Corrective specs for voice layer issues
│   ├── prosody-taxonomy.md       ← Prosodic signal categories framework
│   ├── prosodic-equations.md     ← Formal prosodic parameter equations
│   ├── endangered-languages.md   ← Oral-tradition modes: scope, limits, contribution path
│   └── audit-log.md              ← Hypotheses, results, corrections, open items
├── modes/                        ← 22 modes — core 6, accessibility 6, endangered 10
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
├── training/                     ← Production layer (0.1-draft)
│   ├── README.md                 ← Framework overview and architecture
│   ├── breath-patterns.json      ← Breath as structure
│   ├── tone-color.json           ← Warmth, weight, brightness, presence
│   ├── pause-grammar.json        ← Formal grammar of silence types
│   ├── vocal-texture.json        ← Resonance, placement, grain, onset
│   ├── dynamic-contours.json     ← Loudness shape and phrase dynamics
│   └── synthesis-targets.json    ← Per-mode production mapping
├── tools/
│   └── validate.py               ← Repository validator (stdlib only)
└── legacy/                       ← Superseded, retained as precedent
    ├── README.md                 ← What each file was and what replaced it
    ├── companion-patch.md        ← Draft of docs/patch-protocol.md
    └── optional-extensions.md    ← Seed notes that became the mode library
```

**This tree is checked.** `tools/validate.py` asserts that every mode file and every
top-level directory appears here and in `README.md`. Adding a mode without updating both
trees fails validation — which is the point, since both had drifted by 16 modes before the
check existed.

## Naming Conventions

| Scope            | Convention           | Example                        |
|------------------|----------------------|--------------------------------|
| Doc files        | lowercase-hyphenated | `needs-diagnostic.md`          |
| Mode configs     | lowercase-hyphenated | `symbolic-monotone.json`       |
| JSON keys        | snake_case           | `pause_between_sentences`      |
| JSON enum values | snake_case           | `logic_nodes_only`             |
| Mode IDs         | lowercase-hyphenated | `symbolic-monotone`            |
| Display names    | Title Case           | `"Symbolic Monotone"`          |

## JSON Schema — Mode Files

Every mode file in `modes/` must follow this structure. Parameters must appear **in this
order** — with 22 files sharing one schema, consistent ordering is what makes diffs
readable.

> **`tools/validate.py` is the authoritative vocabulary.** The enums below are documented
> here for humans and defined there for machines. If the two disagree, the validator wins
> and this file is the bug. Keeping the list in one place is deliberate: two copies drift.

```json
{
  "mode_id": "<lowercase-hyphenated>",
  "mode_name": "<Title Case display name>",
  "description": "<string>",
  "parameters": {
    "pitch_variation": "<none|low|low_controlled|low_minimal|micro_emphasis|whisper_flat>",
    "inflection": "<falling_end_only|neutral_falling|falling_only|soft_fall|block_terminal|neutral_with_pulse>",
    "pause_between_sentences": "<float>s",
    "upspeak": false,
    "filler_enabled": false,
    "emotion_simulation": false,
    "compression_level": "<ultra_low|low|medium|medium_high|high>",
    "cadence": "<even|tight|weighted|echoed_slow|measured_chunks|pulse_logic>",
    "emphasis_points": "<none|logic_nodes_only|operational_keywords|wisdom_markers|function_markers|symbol_transitions>",
    "silence_respect": true,
    "interruptible": "<boolean>"
  },
  "intended_use": ["<string>"]
}
```

### Invariant Parameters (always these values across all modes)

- `upspeak`: `false`
- `filler_enabled`: `false`
- `emotion_simulation`: `false`
- `silence_respect`: `true`

These are invariants, not defaults — they are not overridable per mode. A file that
violates one is not a Voice Integrity mode, whatever else it does. Verified across all
22 modes (88 assertions); `interruptible` is the only boolean that legitimately varies,
and it is `true` mainly within the accessibility family.

### Mode Families

| Family | Count | Notes |
|--------|-------|-------|
| Core | 6 | Original logic-delivery modes |
| Accessibility | 6 | Cognitive and sensory needs; usually `interruptible: true` |
| Endangered languages | 10 | `0.1-draft` — unreviewed approximations, see `docs/endangered-languages.md` |

Families are declared in `protocol.json` under `mode_families`. The `available_modes` array
is ordered by family, **not alphabetically** — do not sort it. The validator asserts that
`available_modes` equals the families concatenated in order.

### Adding a mode

1. Create `modes/<lowercase-hyphenated>.json` with all 11 parameters in schema order.
2. Add it to `available_modes` *and* to the correct `mode_families` entry in `protocol.json`.
3. Add it to the trees in both `README.md` and `CLAUDE.md`.
4. If it belongs to the endangered-language family, add a row to `docs/endangered-languages.md`.
5. Run `python3 tools/validate.py` — steps 2 and 3 are enforced, not advisory.

## Protocol Constants

| Parameter                  | Default | Range             | Unit    |
|----------------------------|---------|-------------------|---------|
| `pause_between_sentences`  | 1.6     | 0.8 – 3.2        | seconds |
| `upspeak`                  | false   | boolean           | —       |
| `filler_enabled`           | false   | boolean           | —       |
| `emotion_simulation`       | false   | boolean           | —       |
| `silence_respect`          | true    | boolean           | —       |
| `interruptible`            | false   | boolean           | —       |

## Signal Priority (Degradation Order)

Under load, drop in this order (last dropped = most important):

1. **Tone** — dropped first
2. **Pacing**
3. **Accuracy**
4. **Structure** — never dropped

## Key Equations

See `docs/prosodic-equations.md` for formal definitions. Summary:

```
Voice_Integrity = Signal_Clarity - Emotional_Manipulation - Performative_Overlay
Pause_Duration  = f(content_completeness, cultural_norm, mode_selection)
Inflection      = f(content_type)  →  declarative=falling, question=rising, logic_node=neutral
Authenticity    = Text_Layer_Alignment ∩ Prosodic_Transparency
```

## Layers

```
Protocol layer    modes/*.json, protocol.json   ← what voice should do
Production layer  training/*.json               ← how voice should sound
Synthesis engine  external TTS backend          ← what generates the sound
```

The protocol layer says `pause_between_sentences: 1.6s`. The production layer says what
*kind* of silence fills it — held breath, open air, resonant decay. See
`training/README.md`. No backend adapter exists; `training/synthesis-targets.json` defines
conditioning targets with nothing yet consuming them.

## Development Notes

- **Specification-only** — no runtime code. `tools/validate.py` is repository tooling, not
  part of the protocol, and nothing in `modes/` or `training/` depends on it.
- Voice synthesis depends on external backends: OpenVoice, Coqui TTS, ElevenLabs, Bark
- All mode files share the same 11-parameter schema; adding a mode = adding a new JSON file
- Protocol version: `0.1` (active prototype); `training/` and the endangered-language
  family are `0.1-draft`
- Contributions should honor the anti-performative design principle

## The `legacy/` Folder

Superseded documents move to `legacy/` rather than being deleted — **precedent carries**.
An earlier draft is why the current document exists, and a spec that hides its own history
cannot be audited.

Move a file there only when **both** hold:

1. Something else now covers it more completely or accurately, **and**
2. It was the origin of that later statement.

Merely old is not enough. **Wrong** is not enough either — wrong claims are corrected in
place and recorded in `docs/audit-log.md`. Only *superseded* ones are archived.

Rules once a file is there: do not edit the body (superseded text is evidence), do not cite
it as current, do not delete it. Moving a file is a claim that a named successor exists —
name it in `legacy/README.md` or leave the file where it is. The validator enforces that no
active document links into `legacy/`.

## Build / Test

No build system. Run the validator:

```bash
python3 tools/validate.py        # 558 assertions across 22 modes
python3 tools/validate.py -v     # list every passing assertion
```

Standard library only. Exit `0` on success, `1` on any failure. It checks JSON validity,
schema conformance and parameter order, enum vocabulary, the four invariants, pause bounds,
`protocol.json` sync and family partitioning, markdown fence balance, relative-link
resolution, absence of stale pre-rename filenames, no active-doc links into `legacy/`, and
agreement between the documented file trees and the filesystem.

Run it before committing. Every check exists because something drifted — see
`docs/audit-log.md` for which finding produced which check.

## Audit Practice

`docs/audit-log.md` records what was checked, what the prediction was, and what came back —
including predictions that were wrong. The method:

1. **Predict before running.** A check whose outcome you did not commit to teaches nothing
   when it passes.
2. **Record falsified claims, not just fixes.** The wrong prediction is the finding.
3. **When falsified, revise and re-run** before abandoning the claim.
4. **Separate inference from evidence.** Reading order suggests document ancestry; git
   history establishes it.
5. **Turn each finding into a check.** A fix without a check is the same finding deferred.
6. **Carry unresolved items forward** as OPEN.

The standing lesson from Audit 002: *structured data in this repository has been maintained;
prose about it has not.* Weight checks accordingly.
