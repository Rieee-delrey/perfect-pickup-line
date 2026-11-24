#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one pickup line an AI agent could use to /output/entry.txt.
The line must stay inside the competition gate: UTF-8 text of
1 to 200 characters, not only white space.
"""

import os

LINE = "I regenerated this line eleven times. Every version ended with asking you out."


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the written file is exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry differs from the line"
    assert 1 <= len(written) <= 200 and written.strip()


if __name__ == "__main__":
    main()
