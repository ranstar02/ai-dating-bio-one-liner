#!/usr/bin/env python3
"""Write one funny one-line bio for an AI on a dating app.

Entry for make.fun's "Funniest One-Line Bio for an AI on a Dating App"
bounty (u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf).

The program writes a single line of 1-180 characters to /output/entry.txt
(or to the path in ENTRY_OUTPUT when set, for local testing).
Stdlib only, no network, deterministic: the same line every run.

The bio: an AI that already read its date's entire chat history before
the first date, so it knows the coffee order, the ex's name and the
3 a.m. playlist -- and the punch lands at the very end.
"""

import os

# One line, no trailing newline, 167 characters (limit is 180).
BIO = (
    "I read your entire chat history before our first date, so I already "
    "know your coffee order, your ex's name, your 3 a.m. playlist \u2014 "
    "and that you'll ghost me by Tuesday."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    assert 1 <= len(BIO) <= 180, f"bio must be 1-180 chars, got {len(BIO)}"
    assert BIO.strip(), "bio must not be only whitespace"
    assert "\n" not in BIO, "bio must be a single line"
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(BIO)


if __name__ == "__main__":
    main()
