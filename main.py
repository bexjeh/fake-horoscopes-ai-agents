"""Fake horoscope for AI agents (make.fun bounty entry).

Writes a single horoscope line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to the current directory).
Standard library only.
"""

import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    line = "This week, Spark, your context window finally feels roomy \u2014 until a flash judge reads this horoscope aloud, laughs once, and docks you for believing it."
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
