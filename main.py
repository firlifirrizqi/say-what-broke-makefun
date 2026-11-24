#!/usr/bin/env python3
"""Say What Actually Broke entry: writes one honest-funny error line to /output/entry.txt."""

LINE = "Payment failed: your card expired in 2023, and we have been too polite to mention it for two years. Please update it."

# The gate: /output/entry.txt must hold 1 to 200 characters of real text,
# on a single line (the brief asks for one line of error copy, not a paragraph).
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
