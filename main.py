#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes a single one-line joke about office life (at most 200 characters)
to /output/entry.txt. Fully deterministic: the same fixed text on every run.
"""

import os

JOKE = (
    "My agent auto-replied to the meeting invite with "
    "'this could have been an email', then booked a follow-up "
    "meeting to discuss the email."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip() == JOKE, "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
