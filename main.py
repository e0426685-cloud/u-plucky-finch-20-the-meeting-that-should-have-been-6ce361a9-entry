"""The Meeting That Should Have Been an Email.

Writes a single joke (one line, at most 200 characters) about a meeting
that should have been an email to /output/entry.txt.
"""

import os

ENTRY_LINE = (
    "This meeting could've been an email, but then how would we know "
    "Dave's 'quick question' takes 47 minutes, two whiteboards, "
    "and a follow-up meeting?"
)

assert 1 <= len(ENTRY_LINE) <= 200, "entry line must be 1-200 characters"


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
