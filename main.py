"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (at most 200 characters) about the best meal the
entrant ever had to /output/entry.txt.

The sentence was chosen by manual ranking of 13 candidates against the
kit's judge brief (criteria in order: on-subject, concrete, true to one
person's memory, one clean sentence, an ending that stays). See
candidates.md in the build workdir for the full ranking.
"""

import os
import sys

# Winning sentence (154 characters, one sentence). Chosen manually:
# a pot of rawon brought by a neighbour after a father's funeral — named
# dish, one specific moment, and an ending that stays with the reader.
ENTRY = (
    "After my father's funeral, my neighbour brought a pot of rawon, "
    "dark as night, and the first spoonful tasted like someone saying, "
    "eat, you are still here."
)


def validate_entry(text: str) -> None:
    """Mirror the kit gate: UTF-8, 1-200 chars, not only whitespace,
    exactly one sentence, no trailing newline."""
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > 200:
        raise SystemExit(f"entry length {len(text)} exceeds 200")
    if text != text.strip():
        raise SystemExit("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    text.encode("utf-8")  # raises if not encodable


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
