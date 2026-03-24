# CLAUDE.md — Voice Integrity Module

## Project Overview

The Voice Integrity Module (VIP) is a non-performative vocal protocol specification for AI voice systems. It defines prosodic parameters, tone modes, and signal-processing rules that prioritize clarity, cultural respect, and logic fidelity over performative speech patterns.

**Core principle:** *Performance is not presence. Silence is syntax. Clarity is trust.*

## Repository Structure

```
voice-integrity-module/
├── CLAUDE.md                  ← This file (development guide)
├── README.md                  ← Project overview and quick start
├── LICENSE                    ← MIT License
├── protocol.json              ← Machine-readable protocol configuration
├── vip-spec-v0.1.md           ← Full protocol specification
├── docs/
│   ├── needs-diagnostic.md    ← Technical analysis of voice/text mismatch
│   ├── patch-protocol.md      ← Corrective specs for voice layer issues
│   ├── prosody-taxonomy.md    ← Prosodic signal categories framework
│   ├── prosodic-equations.md  ← Formal prosodic parameter equations
│   ├── companion-patch.md     ← Expansion plans and tone examples
│   └── optional-extensions.md ← Future extension directions
└── modes/
    ├── symbolic-monotone.json ← Flat, neutral logic delivery
    ├── field-mode.json        ← Clipped, radio-comms style
    ├── elder-tone.json        ← Slow, deliberate, spacious
    ├── silent-echo.json       ← Whispered, ritual/contemplative
    ├── debug-tone.json        ← Line-by-line technical review
    └── coherence-pulse.json   ← Subtle rhythmic symbolic emphasis
```

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

Every mode file in `modes/` must follow this structure:

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

## Development Notes

- This is a **specification-only** project — no runtime code yet
- Voice synthesis depends on external backends: OpenVoice, Coqui TTS, ElevenLabs, Bark
- All mode files share the same 11-parameter schema; adding a mode = adding a new JSON file
- Protocol version: `0.1` (active prototype)
- Contributions should honor the anti-performative design principle

## Build / Test

No build system. Validate JSON files:

```bash
for f in modes/*.json protocol.json; do python3 -m json.tool "$f" > /dev/null && echo "OK: $f" || echo "FAIL: $f"; done
```
