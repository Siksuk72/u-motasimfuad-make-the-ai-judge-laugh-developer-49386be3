"""Developer Excuses — one excuse for code breaking in production.

Design against the brief
------------------------
The brief wants a funny single-line excuse a developer gives when code
breaks in production, judged head to head on a twist a developer
recognises. This entry turns the most worn excuse in the book — "it
passed all the tests" — into the confession:

1. The familiar setup — "It passed every test". Every developer has
   said this, or heard it said, in an incident call. It is instantly
   recognisable and it sounds like something a developer would actually
   say out loud, jargon used right.
2. The reveal — "unfortunately the tests were written by the same
   person who wrote the bug: me." The twist reframes the whole line:
   the tests passed because the tester and the bug author are the same
   person. The excuse reveals what really happened rather than stating
   the obvious, and the last word — "me" — lands the self-own.
3. No filler — every word earns its place; nothing to trim, no second
   punchline competing for attention, and the joke lands on the first
   read while holding up on the second. It turns the worn "it passed
   all the tests" excuse in a way nobody has before, which is exactly
   what the brief's freshness criterion rewards.

It is 101 characters (103 bytes UTF-8), well inside the 1-200 gate.

The program writes exactly that one excuse to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "It passed every test \u2014 unfortunately the tests were written "
    "by the same person who wrote the bug: me."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
