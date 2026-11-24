#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry writer.

Writes a single short funny rant (max 400 characters) about a small
everyday annoyance to /output/entry.txt.
"""

import hashlib
import os

ENTRY = (
    "I spell my name for the barista. Slowly. Letter by letter. "
    "And every single morning the cup still says 'Brian'. "
    "My name is not Brian. It has never been Brian. "
    "Brian does not even drink oat lattes, yet Brian gets my coffee "
    "while I stand here explaining to a paper cup that I am not Brian."
)


def validate_entry(text):
    """Return True iff text is 1-400 chars and not only whitespace.

    Mirrors the competition gate exactly: the entry file must be UTF-8
    text of 1-400 characters, and a whitespace-only entry does not count.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 400:
        return False
    return text.strip() != ""


def write_entry():
    """Validate ENTRY, then write it to /output/entry.txt (no trailing newline).

    Validation runs first and raises before anything is written, so a
    bad entry can never leave a stale file behind.
    """
    if not validate_entry(ENTRY):
        raise ValueError("ENTRY failed the 1-400 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return ENTRY


if __name__ == "__main__":
    text = write_entry()
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"wrote /output/entry.txt: {len(text)} chars, sha256 {digest}")
