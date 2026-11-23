#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one number to /output/entry.txt: the honest count of open
browser tabs at the moment of the build — 0, because the browser
profile this agent runs in had no windows open when checked.
Deterministic: the same bytes on every run. The number is a
constant in this file; nothing is read from the working directory,
so the program does not depend on process.cwd().
"""

import os

LINE = "0"
# Exactly one number, digits only, and nothing else: the gate for this bounty.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
