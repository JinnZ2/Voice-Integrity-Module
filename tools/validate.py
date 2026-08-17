#!/usr/bin/env python3
"""
Voice Integrity Module — repository validator.

Every claim this repository makes about its own structure is checked here, so that
re-verifying it is one command rather than a fresh investigation. Findings are recorded
in docs/audit-log.md; this file is the executable half of that record.

    python3 tools/validate.py           # check
    python3 tools/validate.py -v        # check, listing every passing assertion

Exit code 0 = all checks pass, 1 = at least one failure. Standard library only.

This file is the AUTHORITATIVE vocabulary for mode parameter enums. CLAUDE.md documents
them for humans and points here; if the two disagree, this file wins and CLAUDE.md is
the bug.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Schema -----------------------------------------------------------------------

MODE_TOP_LEVEL = ["mode_id", "mode_name", "description", "parameters", "intended_use"]

# The 11-parameter schema. Order is significant: mode files should list parameters in
# this order for diffability across 22+ files.
MODE_PARAMS = [
    "pitch_variation",
    "inflection",
    "pause_between_sentences",
    "upspeak",
    "filler_enabled",
    "emotion_simulation",
    "compression_level",
    "cadence",
    "emphasis_points",
    "silence_respect",
    "interruptible",
]

ENUMS = {
    "pitch_variation": {
        "none", "low", "low_controlled", "low_minimal", "micro_emphasis", "whisper_flat",
    },
    "inflection": {
        "falling_end_only", "neutral_falling", "falling_only", "soft_fall",
        "block_terminal", "neutral_with_pulse",
    },
    "compression_level": {"ultra_low", "low", "medium", "medium_high", "high"},
    "cadence": {
        "even", "tight", "weighted", "echoed_slow", "measured_chunks", "pulse_logic",
    },
    "emphasis_points": {
        "none", "logic_nodes_only", "operational_keywords", "wisdom_markers",
        "function_markers", "symbol_transitions",
    },
}

BOOLEAN_PARAMS = ["upspeak", "filler_enabled", "emotion_simulation", "silence_respect",
                  "interruptible"]

# Anti-performative core. These are not defaults — they are invariants. A mode that
# violates one is not a Voice Integrity mode.
INVARIANTS = {
    "upspeak": False,
    "filler_enabled": False,
    "emotion_simulation": False,
    "silence_respect": True,
}

PAUSE_MIN, PAUSE_MAX = 0.8, 3.2
PAUSE_FORMAT = re.compile(r"^\d+\.\d+s$")
HYPHEN_CASE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Active docs may not cite superseded legacy *content* as current. Two exemptions:
#   - these files exist to describe the legacy material
#   - legacy/README.md is the folder's index, not superseded content; pointing readers at
#     the archive policy is correct, citing an archived draft as current is not
LEGACY_CITATION_EXEMPT = {"legacy/README.md", "docs/audit-log.md"}
LEGACY_INDEX = "legacy/README.md"


# --- Harness ----------------------------------------------------------------------

class Report:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.failures = []
        self.checks = 0

    def check(self, ok, name, detail=""):
        self.checks += 1
        if ok:
            if self.verbose:
                print(f"  pass  {name}")
        else:
            self.failures.append((name, detail))
            print(f"  FAIL  {name}" + (f"\n          {detail}" if detail else ""))
        return ok

    def section(self, title):
        print(f"\n{title}")


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def md_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            if fn.endswith(".md"):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def json_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            if fn.endswith(".json"):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


# --- Checks -----------------------------------------------------------------------

def check_json_parses(r):
    r.section("JSON parses")
    parsed = {}
    for path in json_files():
        try:
            with open(path, encoding="utf-8") as fh:
                parsed[path] = json.load(fh)
            r.check(True, rel(path))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            r.check(False, rel(path), str(exc))
    return parsed


def load_modes(parsed):
    return {
        os.path.basename(p)[:-5]: v
        for p, v in parsed.items()
        if os.path.dirname(p) == os.path.join(ROOT, "modes")
    }


def check_mode_schema(r, modes):
    r.section("Mode files — 11-parameter schema")
    for name, mode in sorted(modes.items()):
        f = f"modes/{name}.json"

        missing_top = [k for k in MODE_TOP_LEVEL if k not in mode]
        r.check(not missing_top, f"{f}: top-level keys", f"missing {missing_top}")

        params = mode.get("parameters", {})
        got = list(params)
        missing = [p for p in MODE_PARAMS if p not in got]
        extra = [p for p in got if p not in MODE_PARAMS]
        r.check(not missing and not extra, f"{f}: parameter set",
                f"missing={missing} unexpected={extra}")
        r.check(got == MODE_PARAMS, f"{f}: parameter order",
                "parameters should follow schema order for diffability")

        r.check(mode.get("mode_id") == name, f"{f}: mode_id matches filename",
                f"mode_id={mode.get('mode_id')!r}, filename stem={name!r}")
        r.check(bool(HYPHEN_CASE.match(name)), f"{f}: filename is lowercase-hyphenated")

        use = mode.get("intended_use")
        r.check(isinstance(use, list) and len(use) > 0
                and all(isinstance(u, str) and u for u in use),
                f"{f}: intended_use is a non-empty list of strings")
        r.check(isinstance(mode.get("description"), str)
                and len(mode.get("description", "")) > 20,
                f"{f}: description is substantive")


def check_mode_values(r, modes):
    r.section("Mode files — parameter values")
    for name, mode in sorted(modes.items()):
        f = f"modes/{name}.json"
        params = mode.get("parameters", {})

        for field, allowed in ENUMS.items():
            if field in params:
                val = params[field]
                r.check(val in allowed, f"{f}: {field}",
                        f"{val!r} not in documented vocabulary {sorted(allowed)}")

        for field in BOOLEAN_PARAMS:
            if field in params:
                r.check(isinstance(params[field], bool), f"{f}: {field} is boolean",
                        f"got {type(params[field]).__name__}")

        pause = params.get("pause_between_sentences")
        if isinstance(pause, str):
            r.check(bool(PAUSE_FORMAT.match(pause)), f"{f}: pause format",
                    f"{pause!r} should match <float>s, e.g. '1.6s'")
            try:
                val = float(pause.rstrip("s"))
                r.check(PAUSE_MIN <= val <= PAUSE_MAX, f"{f}: pause in range",
                        f"{val}s outside {PAUSE_MIN}s-{PAUSE_MAX}s")
            except ValueError:
                r.check(False, f"{f}: pause parses as float", repr(pause))


def check_invariants(r, modes):
    r.section("Anti-performative invariants (all modes)")
    for field, expected in INVARIANTS.items():
        violators = [
            n for n, m in sorted(modes.items())
            if m.get("parameters", {}).get(field) != expected
        ]
        r.check(not violators, f"{field} == {expected} across all {len(modes)} modes",
                f"violated by {violators}")


def check_protocol_sync(r, parsed, modes):
    r.section("protocol.json is in sync with modes/")
    proto = parsed.get(os.path.join(ROOT, "protocol.json"))
    if proto is None:
        r.check(False, "protocol.json present")
        return

    listed = proto.get("available_modes", [])
    on_disk = set(modes)
    orphan = sorted(set(listed) - on_disk)
    unlisted = sorted(on_disk - set(listed))
    r.check(not orphan, "no listed mode is missing from modes/", f"orphans: {orphan}")
    r.check(not unlisted, "no mode on disk is missing from protocol.json",
            f"unlisted: {unlisted}")
    r.check(len(listed) == len(set(listed)), "available_modes has no duplicates")

    families = proto.get("mode_families")
    if families:
        flat = [m for fam in families.values() for m in fam.get("modes", [])]
        r.check(sorted(flat) == sorted(listed),
                "mode_families partitions available_modes",
                f"families cover {len(flat)}, available_modes has {len(listed)}")
        r.check(len(flat) == len(set(flat)),
                "no mode appears in two families")
        r.check(flat == listed,
                "available_modes is ordered by family",
                "available_modes should be the concatenation of the families in order")


def check_markdown(r):
    r.section("Markdown structure")
    for path in md_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fences = len(re.findall(r"^```", text, flags=re.MULTILINE))
        r.check(fences % 2 == 0, f"{rel(path)}: code fences balanced",
                f"{fences} fence markers — one is unclosed")


def check_links(r):
    r.section("Relative links resolve")
    link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in md_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        base = os.path.dirname(path)
        for target in link.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#")[0].strip()
            if not clean:
                continue
            r.check(os.path.exists(os.path.join(base, clean)),
                    f"{rel(path)} -> {target}", "target does not exist")


def check_legacy_citations(r):
    r.section("Active docs do not cite legacy content as current")
    link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in md_files():
        relpath = rel(path)
        if relpath.startswith("legacy/") or relpath in LEGACY_CITATION_EXEMPT:
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        base = os.path.dirname(path)
        hits = []
        for target in link.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#")[0].strip()
            if not clean:
                continue
            resolved = rel(os.path.normpath(os.path.join(base, clean)))
            # Linking to the archive index is how a reader learns the policy.
            # Linking past it, to a superseded draft, is the thing being prevented.
            if resolved.startswith("legacy/") and resolved != LEGACY_INDEX:
                hits.append(target)
        r.check(not hits, f"{relpath}: no links to superseded legacy content",
                f"found {hits} — link to {LEGACY_INDEX} instead")


def check_stale_filenames(r):
    r.section("No references to pre-rename filenames")
    old = ["Needs-Diagnostic.md", "Patch-Protocol.md", "Prosody-Taxonomy.md",
           "VIP_v0.1.md", "Optional.md", "Example-companion-patch.md"]
    for path in md_files() + json_files():
        relpath = rel(path)
        if relpath.startswith("legacy/") or relpath in LEGACY_CITATION_EXEMPT:
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        hits = [o for o in old if o in text]
        r.check(not hits, f"{relpath}: no stale filenames", f"found {hits}")


def check_doc_trees(r, modes):
    r.section("Documented file trees match the filesystem")
    tracked = {
        "README.md": os.path.join(ROOT, "README.md"),
        "CLAUDE.md": os.path.join(ROOT, "CLAUDE.md"),
    }
    for label, path in tracked.items():
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        missing = [n for n in sorted(modes) if f"{n}.json" not in text]
        r.check(not missing, f"{label}: lists every mode file",
                f"absent from the tree: {missing}")
        for d in ["docs/", "modes/", "training/", "legacy/", "tools/"]:
            r.check(d in text, f"{label}: mentions {d}")


# --- Main -------------------------------------------------------------------------

def main():
    verbose = "-v" in sys.argv or "--verbose" in sys.argv
    r = Report(verbose)

    print("Voice Integrity Module — validator")
    print(f"root: {ROOT}")

    parsed = check_json_parses(r)
    modes = load_modes(parsed)

    if not modes:
        print("\nFAIL  no mode files found under modes/")
        return 1

    check_mode_schema(r, modes)
    check_mode_values(r, modes)
    check_invariants(r, modes)
    check_protocol_sync(r, parsed, modes)
    check_markdown(r)
    check_links(r)
    check_legacy_citations(r)
    check_stale_filenames(r)
    check_doc_trees(r, modes)

    print(f"\n{'-' * 60}")
    if r.failures:
        print(f"FAILED — {len(r.failures)} of {r.checks} checks failed "
              f"across {len(modes)} modes")
        return 1
    print(f"OK — {r.checks} checks passed across {len(modes)} modes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
