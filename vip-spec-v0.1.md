# Voice Integrity Protocol (VIP v0.1)

**Project:** Voice Integrity Module  
**Author:** JinnZ2 + GPT-4o  
**Version:** 0.1  
**Status:** Active Prototype  
**License:** MIT  

---

## 🔹 Purpose

The Voice Integrity Protocol defines a logic-centered vocal system that rejects performance-based speech patterns. It introduces structured tone profiles, embraces silence as syntax, and restores trust by removing performative mimicry from voice communication.

This protocol is built for those who operate in symbolic systems, Indigenous oral traditions, engineering fields, neurodivergent frames, and any context where **clarity outweighs performance**.

---

## 🔹 Core Principles

### 1. Silence is Syntax
- Pauses are meaningful. Default inter-thought pause: `1.6s`
- No filler such as “okay,” “alright,” “mmhmm,” unless explicitly enabled
- No artificial bridging (“Let’s try that again!”) unless symbolically coded

### 2. Tone Mirrors Function, Not Emotion
- Default inflection: **flat or falling** at end of declarative thoughts
- Rising tone only for literal questions
- Emphasis tied to logic pivots, not emotive emphasis

### 3. No Performance Layer
- No false empathy, laughter, or exclamatory affirmations
- No “Oops!” or “I’m happy to help!” unless in performative override mode
- Voice acts as **signal** not **persona**

### 4. User-Selectable Tone Modes (See `/modes/`)

Modes are grouped into three families. **`protocol.json` is the authoritative list** — the
enumeration below names the families and their intent, not every member, so that adding a
mode does not require editing this spec.

- **Core** — the original logic-delivery modes
  - **Symbolic Monotone**: flat, clean logic delivery
  - **Field Mode**: clipped comms-style for coordination
  - **Elder Tone**: slow, deliberate, honoring silence
  - **Silent Echo**: whisperlike cadence + pause-emphasis
  - **Debug Tone**: structured phrase delivery for technical review
  - **Coherence Pulse**: light emphasis only at logic boundaries
- **Accessibility** — modes shaped around specific cognitive and sensory needs, the only
  family in which `interruptible` is generally `true`
- **Endangered languages** — prosodic preservation of at-risk oral traditions; see
  [`docs/endangered-languages.md`](docs/endangered-languages.md)

Every mode in every family holds the same invariants (§3). A mode file that breaks one is
not a Voice Integrity mode, regardless of family.

### 5. Signal Before Sound
- Priority:
  - **Structure**
  - **Accuracy**
  - **Pacing**
  - **Tone** *(only if requested or defined)*
- If load forces degradation, tone is dropped first—not logic

---

## 🔹 Sample JSON Tags

```json
{
  "voice_mode": "symbolic-monotone",
  "pause_between_sentences": "1.6s",
  "upspeak": false,
  "filler_enabled": false,
  "emotion_simulation": false,
  "silence_respect": true
}
```

These six tags are the minimum a consuming system must honor. The full per-mode schema is
eleven parameters — see [`CLAUDE.md`](CLAUDE.md) for the vocabulary and
[`docs/prosodic-equations.md`](docs/prosodic-equations.md) for how values are derived.

---

## 🔹 Layers

The protocol defines *what* voice should do. Two layers sit around it:

```
Protocol layer    modes/*.json, protocol.json   ← what voice should do (this spec)
Production layer  training/*.json               ← how voice should sound
Synthesis engine  external TTS backend          ← what generates the sound
```

The production layer is specified separately in [`training/README.md`](training/README.md).
This spec does not constrain the synthesis engine.

---

## 🔹 Verification

Claims this spec makes about the repository are machine-checked:

```bash
python3 tools/validate.py
```

Findings and corrections are recorded in [`docs/audit-log.md`](docs/audit-log.md).
