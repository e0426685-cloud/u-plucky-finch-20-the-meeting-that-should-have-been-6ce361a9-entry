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

MAX_LINE_LENGTH = 200


def validate_entry_line(line: str) -> str:
    """Check the entry line is non-blank and within the length limit."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry line must not be blank")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("entry line must be 1-200 characters")
    return line


assert 1 <= len(ENTRY_LINE) <= 200, "entry line must be 1-200 characters"


def write_entry(output_path: str, line: str) -> None:
    """Write the validated entry line to the output file, world-readable."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(output_path, 0o644)


def main() -> None:
    line = validate_entry_line(ENTRY_LINE)
    write_entry("/output/entry.txt", line)


if __name__ == "__main__":
    main()
