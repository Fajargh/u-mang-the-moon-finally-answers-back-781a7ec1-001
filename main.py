#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes one line, in the voice of the Moon replying at last to the
wishes, howls and late-night promises of everyone staring up at it,
to /output/entry.txt. The line must be 1-240 characters.
"""

import os

ENTRY = (
    "Four billion years of wishes and the best you've got is "
    "'make him text back'? Sweetheart, I'm a rock. Text him yourself."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(
            "entry must be 1-240 characters, got %d" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
