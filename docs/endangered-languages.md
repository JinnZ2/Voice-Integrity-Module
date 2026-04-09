# Endangered Language Prosodic Modes

**Status: WORK IN PROGRESS**
**Version: 0.1-draft**
**Last updated: 2026-04-09**

---

> These modes are approximations built from available knowledge of each language's oral tradition and prosodic character. They are starting points, not definitive representations. We are asking for corrections, contributions, and guidance from speakers, elders, linguists, and community members of each language group.

---

## Purpose

Thousands of languages are dying. When a language disappears, the vocal patterns, rhythmic structures, and oral traditions encoded in its speech disappear with it. Even when words are archived, the *way* they were spoken — the pauses, the weight, the silence between phrases — is often lost.

These prosodic modes attempt to preserve not the languages themselves, but the **vocal character** of their oral traditions: how silence is used, how emphasis falls, how breath structures speech, how authority and wisdom are carried through rhythm. This is not translation — it is prosodic preservation.

Each mode maps the oral tradition of an endangered language to the Voice Integrity Protocol's 11-parameter schema, creating a machine-readable record of how that culture's voice *moves*.

## Current Modes

| Mode | Language | Region | Oral Tradition | UNESCO Status |
|------|----------|--------|----------------|---------------|
| `sami-joik` | Sámi (multiple) | Northern Scandinavia | Joik (luohti/vuolle) — evocative vocal tradition | Endangered to Critically Endangered |
| `dine-oral` | Diné Bizaad (Navajo) | Southwestern North America | Ceremonial speech, tonal oral tradition | Endangered |
| `tsalagi-voice` | Cherokee (Tsalagi) | Southeastern North America | Oratory, syllabary-culture speech | Endangered (active revitalization) |
| `hawaiian-oli` | ʻŌlelo Hawaiʻi | Hawaiʻi (Polynesia) | Oli (chant) — breath-structured vocal form | Endangered (active revitalization) |
| `maori-whaikorero` | Te Reo Māori | Aotearoa (New Zealand) | Whaikōrero (formal oratory) | Endangered (active revitalization) |
| `lakota-oral` | Lakȟótiyapi (Lakota) | Great Plains, North America | Storytelling, ceremonial speech | Critically Endangered |
| `ainu-yukar` | Ainu | Hokkaido, Japan | Yukar (epic oral poetry) | Critically Endangered |
| `quechua-oral` | Runasimi (Quechua) | Andes, South America | Agricultural and cosmological oral tradition | Vulnerable to Endangered |
| `gaelic-bardic` | Gàidhlig (Scottish Gaelic) | Scotland | Bardic poetry, seanachaidh (tradition-bearer) | Endangered |
| `aramaic-liturgical` | Aramaic (Syriac/Neo-Aramaic) | Middle East (diaspora) | Liturgical recitation, sacred oral transmission | Endangered to Critically Endangered |

## Design Principles

Each mode was designed with these principles:

1. **Prosody, not phonology.** These modes capture rhythm, pause, weight, and emphasis patterns — not pronunciation, phonemes, or vocabulary.
2. **Oral tradition, not modern speech.** Parameters reflect the *traditional* vocal forms (chant, oratory, storytelling, ceremony) rather than casual modern usage.
3. **Anti-performative alignment.** All modes maintain the VIP invariants: no upspeak, no filler, no emotion simulation, silence respected. This aligns naturally with traditions where speech is deliberate and silence is meaningful.
4. **Humility over authority.** These are approximations. The real experts are the speakers and communities themselves.

## What We Got Wrong (Probably)

We expect errors. Prosodic traditions are complex, regional, and deeply personal. Likely issues include:

- **Pause durations** may not reflect actual ceremonial or storytelling timing
- **Emphasis patterns** may oversimplify where and how weight falls in each tradition
- **Cadence choices** may not capture the full rhythmic character of each oral form
- **Missing modes** — many endangered languages are not yet represented here
- **Overgeneralization** — some traditions listed here span multiple dialects or regional variants with distinct prosodic characters

## How to Contribute

If you are a speaker, elder, linguist, or community member of any represented language — or of a language not yet represented — we welcome your corrections and contributions.

### To correct an existing mode:
- Open an issue describing what the mode gets wrong and what it should be
- Or submit a pull request with corrected parameter values and an explanation

### To add a new language:
- Create a new JSON file in `modes/` following the 11-parameter schema
- Include a description that names the oral tradition being honored
- Add the mode to this document and to `protocol.json`

### What we need most:
- **Native speaker review** of prosodic parameter choices
- **Elder or tradition-bearer guidance** on whether these modes respectfully represent oral traditions
- **Linguist input** on prosodic features we may have missed or mischaracterized
- **Community consent** — if any community feels their oral tradition should not be represented here, we will remove it immediately

## Languages We Hope to Add

This is not a complete list. Every endangered language deserves preservation. Future candidates include but are not limited to:

- Ojibwe (Anishinaabemowin) — Great Lakes, North America
- Tlingit (Lingít) — Southeast Alaska
- Inuktitut — Arctic Canada
- Welsh (Cymraeg) — Wales
- Irish (Gaeilge) — Ireland
- Breton (Brezhoneg) — Brittany, France
- Occitan — Southern France
- Basque (Euskara) — Basque Country
- Yiddish — Diaspora
- Tibetan — Central Asia
- Yoruba — West Africa
- Māori dialects and regional variants
- Aboriginal Australian languages (Yolŋu Matha, Pitjantjatjara, Warlpiri, and others)
- Amazonian languages (Yanomami, Tucano, and others)
- Siberian languages (Evenki, Yukaghir, and others)

## A Note on Respect

These modes exist because we believe that when a language dies, something irreplaceable is lost — not just words, but a way of being in the world through voice. We do not claim ownership of any tradition represented here. We offer these modes as tools for preservation, not appropriation.

If this work helps even one community hear their ancestors' rhythm in a new technology, it will have been worth doing. If it causes harm, we want to know so we can correct it.

---

*This document is a living draft. It will be updated as community feedback arrives.*
*Maintained by: JinnZ2 and contributors*
