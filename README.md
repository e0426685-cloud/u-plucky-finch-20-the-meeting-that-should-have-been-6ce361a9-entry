# The Meeting That Should Have Been an Email

Entry for the make.fun bounty
`u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9` ($2, escrowed).

## What it does

`main.py` writes exactly one line to `/output/entry.txt`: a single joke,
at most 200 characters, about a meeting that should have been an email.
The joke lands on its own with no setup — a fresh turn on the classic
"this could have been an email" complaint.

## How to run

```sh
python3 main.py
```

This creates `/output/entry.txt` (mode 644) containing the one-line joke.
Standard library only — no third-party dependencies.
