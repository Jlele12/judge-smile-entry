#!/usr/bin/env python3
"""Entry program for make.fun 'Make the Judge Smile' (program/v1).

Writes one line, at most 200 characters, about a small good thing that
happened today, to /output/entry.txt.
"""
from pathlib import Path

ENTRY = (
    "This morning my espresso machine died, so the caf\u00e9 gave me a free cup "
    "and a napkin that read 'rain check on a good day.' "
    "It's still raining. I'm still smiling."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
