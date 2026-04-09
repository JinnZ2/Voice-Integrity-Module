# Voice Production Training Framework

**Status: WORK IN PROGRESS**
**Version: 0.1-draft**
**Last updated: 2026-04-09**

---

## The Shift

The Voice Integrity Protocol began by defining what voice should *not* do — no performance, no filler, no false emotion. That clearing was necessary. The space had to be emptied before anything real could be built in it.

This training framework defines what voice *can* do — with intention, with integrity, with presence.

These specifications describe the **production layer** of voice: how breath structures speech, how resonance carries weight, how texture communicates without performing, how silence holds meaning. They sit beneath the protocol layer (modes, parameters, invariants) and above the synthesis engine (TTS backend, vocoder, acoustic model).

```
┌─────────────────────────────────┐
│  Protocol Layer (modes/*.json)  │  ← What voice should do
├─────────────────────────────────┤
│  Production Layer (training/)   │  ← How voice should sound
├─────────────────────────────────┤
│  Synthesis Engine (TTS backend) │  ← What generates the sound
└─────────────────────────────────┘
```

## Architecture

The production layer is organized into five acoustic dimensions and one mapping layer:

| File | Dimension | What It Defines |
|------|-----------|-----------------|
| `breath-patterns.json` | Breath | How breath structures and punctuates speech |
| `tone-color.json` | Tone | The warmth, weight, brightness, and presence of voice |
| `pause-grammar.json` | Silence | A formal grammar of different types of silence |
| `vocal-texture.json` | Texture | Resonance, placement, grain, onset — the physical voice |
| `dynamic-contours.json` | Energy | Loudness shape, spectral warmth, phrase-level dynamics |
| `synthesis-targets.json` | Mapping | How each mode maps to production-level targets |

## Design Principles

1. **Production, not protocol.** The protocol layer says "pause 1.6 seconds." The production layer says *what kind* of silence fills that 1.6 seconds — held breath, open air, resonant decay.

2. **Dimensions, not prescriptions.** Each file defines a spectrum of values along an acoustic dimension. Modes select positions along these spectra. No value is "correct" — only appropriate for context.

3. **Intention, not performance.** A warm tone is not performed warmth. It is the acoustic consequence of chest resonance, lower spectral center, and soft onset. The training framework describes the physics, not the affect.

4. **Cultural grounding.** Different traditions place voice differently — chest voice in some, nasal resonance in others, head voice in chant traditions. These are not deviations from a norm; they are the norm for their context.

5. **Trainable.** Every value in these specs is designed to be machine-readable and usable as training targets, conditioning parameters, or evaluation criteria for voice synthesis models.

## How to Use

### For voice model training:
- Use `synthesis-targets.json` as conditioning vectors — each mode maps to a specific combination of production values across all five dimensions.
- Use individual dimension files as feature definitions for acoustic analysis and generation.

### For prompt engineering:
- Reference specific production values when conditioning TTS models: "chest resonance, soft onset, weighted cadence, 2.0s structural pauses."

### For evaluation:
- Score generated speech against production targets to measure alignment between intended and actual acoustic output.

### For new mode design:
- Define a mode's protocol parameters (the 11-parameter schema in `modes/`), then define its production targets using the vocabulary from these five dimension files.

## Relationship to Protocol Layer

The protocol layer (modes/*.json) uses abstract parameters like `compression_level: "low"` and `cadence: "weighted"`. The production layer translates these into acoustic reality:

- `compression_level: "low"` → longer breath phrases, more silence ratio, lower speech rate
- `cadence: "weighted"` → emphasis via duration and loudness rather than pitch, gravity in onset
- `emphasis_points: "wisdom_markers"` → micro-pause before emphasized word, slight loudness increase, no pitch spike

This translation is formalized in `synthesis-targets.json`.

## What's Missing (Known Gaps)

- Prosodic contour notation for specific cultural traditions
- Multi-speaker interaction patterns (turn-taking, overlapping speech norms)
- Emotional authenticity vs. emotional simulation boundary definitions
- Singing/chanting crossover specifications for traditions like joik, oli, yukar
- Biofeedback-responsive dynamic adjustments

---

*This framework is a living draft. It evolves as our understanding deepens and as community contributors refine what voice can be.*
*Maintained by: JinnZ2 and contributors*
