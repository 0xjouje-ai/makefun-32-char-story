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


def main() -> None:
    assert 1 <= len(WIFI_NAME) <= 32, "name must be 1-32 characters"
    assert WIFI_NAME.strip() == WIFI_NAME, "name must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WIFI_NAME)
    print(WIFI_NAME)
    print(f"wrote {len(WIFI_NAME)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
