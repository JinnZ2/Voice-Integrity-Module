# Prosodic Equations — Voice Integrity Module

Formal definitions of the prosodic parameters and relationships governing the Voice Integrity Protocol. These equations describe how voice output is computed from content, mode, and context inputs.

---

## 1. Voice Integrity Index

The core metric. A voice output has integrity when it maximizes signal clarity and minimizes performative distortion.

```
Voice_Integrity = Signal_Clarity - Emotional_Manipulation - Performative_Overlay
```

| Term                      | Definition                                                        |
|---------------------------|-------------------------------------------------------------------|
| `Signal_Clarity`          | Degree to which prosody matches semantic content                  |
| `Emotional_Manipulation`  | Injected affect not warranted by content (false empathy, upspeak) |
| `Performative_Overlay`    | Filler phrases, artificial bridging, persona-driven inflection    |

**Integrity is maximized when both subtractive terms are zero.**

---

## 2. Pause Duration

Pause length is not fixed — it is a function of content completeness, cultural norm, and the active mode.

```
Pause_Duration = f(content_completeness, cultural_norm, mode_selection)
```

### Mode-specific pause values

| Mode              | `pause_between_sentences` | Rationale                          |
|-------------------|---------------------------|------------------------------------|
| field-mode        | 0.8s                      | Tight operational tempo            |
| debug-tone        | 1.0s                      | Measured chunks for code review    |
| coherence-pulse   | 1.4s                      | Rhythmic logic boundary spacing    |
| symbolic-monotone | 1.6s                      | Default — balanced clarity         |
| elder-tone        | 2.4s                      | Spacious, oral-tradition pacing    |
| silent-echo       | 3.2s                      | Extended contemplative silence     |

### Constraints

```
0.8s <= Pause_Duration <= 3.2s
Default = 1.6s (when no mode is selected)
```

---

## 3. Inflection Function

Inflection is determined by content type, not speaker affect.

```
Inflection = f(content_type)

  where:
    declarative_statement  → falling
    literal_question       → rising
    logic_node / pivot     → neutral
    continuation / list    → level or micro-rise
    block_terminal (code)  → flat drop
```

### Mode inflection mappings

| Mode              | Inflection Style     | Pattern                                    |
|-------------------|----------------------|--------------------------------------------|
| symbolic-monotone | `falling_end_only`   | Fall at sentence end, flat elsewhere        |
| field-mode        | `neutral_falling`    | Neutral body, slight fall at close          |
| elder-tone        | `falling_only`       | Every phrase falls — no continuation rise   |
| silent-echo       | `soft_fall`          | Gentle descent, whisper-level               |
| debug-tone        | `block_terminal`     | Hard stop at each logical block boundary    |
| coherence-pulse   | `neutral_with_pulse` | Neutral baseline with micro-emphasis pulses |

---

## 4. Authenticity Equation

Authenticity is the intersection of text-layer alignment and prosodic transparency. When what the system *says* matches *how* it says it, authenticity is achieved.

```
Authenticity = Text_Layer_Alignment ∩ Prosodic_Transparency
```

| Term                      | Definition                                                    |
|---------------------------|---------------------------------------------------------------|
| `Text_Layer_Alignment`    | Voice output reflects text-layer analysis without override     |
| `Prosodic_Transparency`   | No hidden affect injection; prosody is auditable and explicit  |

**Failure mode:** Text layer diagnoses neutral content but voice layer injects warmth/comfort → `Authenticity = 0`.

---

## 5. Signal Priority (Degradation Order)

Under computational or bandwidth load, parameters degrade in a defined order. Structure is never sacrificed.

```
Priority(Structure) > Priority(Accuracy) > Priority(Pacing) > Priority(Tone)
```

### Degradation sequence

```
Load_Level_1 (mild):    Drop Tone refinement     → flat delivery
Load_Level_2 (medium):  Drop Pacing variation     → fixed cadence
Load_Level_3 (high):    Drop Accuracy nuance      → simplified vocabulary
Load_Level_4 (critical): Structure preserved       → never dropped
```

---

## 6. Compression Level

Compression controls information density per unit of vocalized time.

```
Compression = Information_Density / Vocalization_Time
```

| Level         | Behavior                                       | Used by            |
|---------------|------------------------------------------------|--------------------|
| `ultra_low`   | Maximum spacing, breath-paced                  | silent-echo        |
| `low`         | Spacious, deliberate pacing                    | elder-tone         |
| `medium`      | Balanced density                               | debug-tone         |
| `medium_high` | Dense but not clipped                          | field-mode         |
| `high`        | Maximum density, minimal silence between units | symbolic-monotone, coherence-pulse |

---

## 7. Emphasis Placement

Emphasis is applied only at structurally significant points, never for affective coloring.

```
Emphasis_Point = f(mode, content_structure)

  where:
    symbolic-monotone → logic_nodes_only
    field-mode        → operational_keywords
    elder-tone        → wisdom_markers
    silent-echo       → none
    debug-tone        → function_markers
    coherence-pulse   → symbol_transitions
```

---

## 8. Invariant Constraints

These hold across all modes and cannot be overridden:

```
∀ mode ∈ Modes:
    upspeak(mode)            = false
    filler_enabled(mode)     = false
    emotion_simulation(mode) = false
    silence_respect(mode)    = true
```

These invariants encode the anti-performative core of the protocol.
