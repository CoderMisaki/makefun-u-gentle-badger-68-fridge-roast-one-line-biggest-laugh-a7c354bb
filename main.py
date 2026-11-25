#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to /output/entry.txt.
Python standard library only; deterministic output.
"""

import os

LINE = "My 1998 fridge stayed cold for 27 years without ever asking for Wi-Fi; my smart fridge needs a firmware update just to keep the milk cold."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
