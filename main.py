"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene to /output/entry.txt: a Sunday-morning
pancake disaster that turns into the family's favourite memory.

The angle I chose: instead of a perfect, glossy family moment, the scene
is a small kitchen failure that everyone decides to love anyway. Dad
flips a pancake too hard and it sticks to the ceiling. Nobody scolds
him. For one whole minute the whole family just stares up at it, and
then the youngest child rescues the moment with a single wry line --
"It's art now" -- and suddenly the ruined breakfast is a masterpiece.
Mum plays along completely, serving the rest of breakfast underneath
the pancake as if the kitchen had a chandelier. That is the warmth:
nobody fixes the mistake, they crown it. That is the humour: a burnt
pancake treated like gallery art and a ceiling treated like a dining
room. And the heart is in the last beat, the family eating happily
under their accidental chandelier, because the point of the morning
was never the pancake at all, it was being together while it went
wrong. The scene is specific -- a pancake, a ceiling, a little sister,
a chandelier -- so it reads like a real household, not a greeting
card, and it fits in two lines with no word wasted.
"""

import os

# The scene itself: two lines, one small domestic disaster, one family
# that chooses laughter over a lecture. Kept well under the 280
# character cap so the gate passes with room to spare.
SCENE = (
    "Dad flipped the pancake so high it stuck to the ceiling, and the "
    "whole kitchen went quiet \u2014 then my little sister declared, "
    "\"It's art now,\" and Mum served breakfast beneath it, like the "
    "ceiling had grown a chandelier."
)

# The bounty gate: the text must be 1 to 280 characters and not only
# whitespace. This helper checks that here, before writing, so a
# too-long draft fails loudly on my machine instead of silently
# failing the sealed scorer on the server.
MAX_CHARS = 280


def validate_scene(text):
    """Check the scene against the gate: non-blank, at most 280 chars."""
    if not text or not text.strip():
        raise ValueError("scene must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "scene is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    scene = validate_scene(SCENE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(scene)
    # Make the output readable by every user: the grader collects the
    # file as a different user than the one running this program.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
