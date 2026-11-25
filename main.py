#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes a single Wi-Fi network name to /output/entry.txt.

The name: Password: 'WeNeedToTalk'

The joke: the network's own name tells you its password — and the
password is the classic breakup opener. A whole story in 24 characters:
someone changed the Wi-Fi password to deliver the breakup, and now
everyone in the house reads it every time they open the network list.
"""

import os

WIFI_NAME = "Password: 'WeNeedToTalk'"
OUTPUT_PATH = "/output/entry.txt"
MAX_NAME_LENGTH = 32


def validate_name(name: str) -> None:
    """Check the name against the competition gate plus Wi-Fi sanity rules.

    The gate needs 1-32 UTF-8 characters, not only whitespace. A network
    name also cannot carry control characters (an SSID with one would
    never show up cleanly in a phone's network list), so reject those too.
    """
    assert 1 <= len(name) <= MAX_NAME_LENGTH, "name must be 1-32 characters"
    assert name.strip() == name, "name must not be only whitespace"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in name), (
        "name must not contain control characters"
    )


def main() -> None:
    validate_name(WIFI_NAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WIFI_NAME)
    # Read back what was written: the file on disk must be byte-identical
    # to the name, so a truncated or re-encoded write fails loudly here
    # instead of reaching the grader.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == WIFI_NAME, "written entry does not match the name"
    print(WIFI_NAME)
    print(f"wrote {len(WIFI_NAME)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
