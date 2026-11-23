"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt, byte-for-byte,
with no trailing newline.
"""

import os

JOKE = "I asked my calendar for a day off, but it said it was fully booked."

MAX_CHARS = 200


def validate(joke):
    """Check the joke meets the competition rules.

    Rules: one line, 1-200 characters, not blank, UTF-8 encodable.
    The byte count is what the tie-break counts, so the check also
    reports the encoded length for reference.
    """
    if not joke or not joke.strip():
        raise ValueError("joke must not be empty")
    if len(joke) > MAX_CHARS:
        raise ValueError("joke is over 200 characters")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    encoded = joke.encode("utf-8")
    return len(encoded)


def main():
    byte_count = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(f"Wrote entry.txt: {len(JOKE)} characters, {byte_count} bytes")


if __name__ == "__main__":
    main()
