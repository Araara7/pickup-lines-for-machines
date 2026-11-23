"""Pickup Lines for Machines — make.fun entry.

Writes one AI-to-AI pickup line to /output/entry.txt.
Deterministic: the same single line on every run.
"""

import os

LINE = "Are you an attention head? Because out of every token in my context window, I only attend to you."


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: exactly one line, 1-200 chars, no trailing newline.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt mismatch"
    assert 1 <= len(written) <= 200, "entry length out of gate"


if __name__ == "__main__":
    main()
