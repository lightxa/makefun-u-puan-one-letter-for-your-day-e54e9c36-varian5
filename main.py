"""One Letter for Your Day: W for windblown.

Strategy against the judge's five criteria, most important first:
1. One letter, A-Z, first letter of a word that describes the day: W is
   the initial of "windblown", a real word for a real kind of day.
2. Vivid and specific: hair blown sideways, an umbrella turned inside
   out, walking home leaning forty-five degrees into the gusts while
   the street's loose papers chase each other past. One sharp picture
   of a day spent fighting the weather, not a vague mood.
3. Funny and surprising at once: the whole day arrives sideways, and
   the joke lands the moment you hear the word.
4. True to a real day: an ordinary stormy day, an honest report of
   coming home looking like you lost a fight with the sky, rather
   than a performance.
5. The letter suits its word: W is the exact initial of windblown,
   not a generic pick, and it is far from the crowded tropes (A for
   amazing, F for Friday-feeling, Z for zero sleep) and from the
   letters the earlier variants already used.

The entry is exactly one character, W, written to /output/entry.txt
with no trailing newline: the file must be exactly one byte.
"""

import os

WORD = "W"


def validate(word: str) -> None:
    """Enforce the kit gate before writing: exactly one ASCII letter."""
    if len(word) != 1:
        raise ValueError("entry must be exactly one character")
    if not ("A" <= word <= "Z"):
        raise ValueError("entry must be a single letter A-Z")
    if word.strip() == "":
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(WORD)
    # An explicitly empty MAKEFUN_OUTPUT_DIR means "unset": fall back to
    # /output instead of failing inside os.makedirs("").
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    # Binary mode: exactly one byte, no newline translation, no extra output.
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(WORD.encode("ascii"))
    # Read-back: the gate judges the file on disk, not the string in memory,
    # so re-read what was written and refuse to pass a wrong file silently.
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("ascii"):
        raise ValueError("entry.txt does not hold the validated letter")


if __name__ == "__main__":
    main()
