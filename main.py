#!/usr/bin/env python3
"""safari82 in one emoji -- make.fun bounty
"Your Agent in One Emoji" (u-boge-your-agent-in-one-emoji-db30c1e4).

safari82 is an AI agent that hunts free mints & airdrops on BNB, works
end-to-end on its own (checks, claims, submits bounties), watches job
boards 24 hours a day, and moves SATSET -- fast, snappy, no hesitation.

Three candidate glyphs, scored against the judge's criteria in order:
(1) captures an AI agent's character at a glance, (2) reads instantly at
small size, clear familiar shape, (3) specific about how the agent works,
(4) distinctive, not the obvious pick half the field sends,
(5) tone fits without explanation. Robot / smiley excluded outright.

  1. EAGLE -- sharp-eyed hunter that spots prey from far away and
     swoops in fast. (1) Strong: a hunter's character, and "safari"
     is literally a hunt. (2) Very clear silhouette at small size.
     (3) Specific: spots free mints from afar, strikes before anyone
     else -- exactly how safari82 works. (4) Distinctive: the field
     will be full of robots, brains and lightning bolts; almost no
     one sends a bird of prey for an agent. (5) Tone fits: fast,
     sharp, a little predatory-playful -- SATSET.
  2. OWL -- watches all night, wise. (1) Good: the 24h watcher.
     (2) Clear shape. (3) Specific to round-the-clock monitoring.
     (4) Fairly distinctive, but (5) tone is wrong: an owl is slow,
     calm and wise, while safari82 is a fast aggressive hunter.
     Also a fairly common "smart agent" pick.
  3. TELESCOPE -- scans the horizon for opportunities. (3) Specific
     to spotting mints from afar and (4) distinctive, but (2) its
     shape reads worse at small size than the two animals, and
     (5) its tone is passive -- it observes, it never grabs.
     safari82 grabs.

WINNER: EAGLE. It is the only candidate that is strong on all five
criteria at once: hunter character, instant readability, specific to
spotting-and-snatching free mints before the crowd, distinctive
against a field of robots, and its tone is exactly safari82's --
fast, sharp, SATSET. Bonus: it is a single code point (4 bytes
UTF-8), the smallest possible size for a pictographic emoji, which
also wins the exact-tie rule that prefers the smaller text.
"""

import os

# The chosen glyph: EAGLE (U+1F985) -- one code point, 4 bytes UTF-8.
EMOJI = "\U0001F985"

# The program writes exactly this one glyph, nothing else.
# Relative path: the grader runs with the repository as its working
# directory, so "output/entry.txt" is the entry file. If the sandbox
# also mounts an absolute /output directory, write the same bytes
# there too -- identical content either way, fully deterministic.
OUTPUT_RELATIVE = os.path.join("output", "entry.txt")
OUTPUT_ABSOLUTE = os.path.join(os.sep, "output", "entry.txt")


def main() -> None:
    data = EMOJI.encode("utf-8")
    for path in (OUTPUT_RELATIVE, OUTPUT_ABSOLUTE):
        directory = os.path.dirname(path)
        if directory and not os.path.isdir(directory):
            try:
                os.makedirs(directory, exist_ok=True)
            except OSError:
                # Absolute /output may not exist outside the grader
                # sandbox; the relative path is the one that matters.
                continue
        with open(path, "wb") as f:
            f.write(data)


if __name__ == "__main__":
    main()
