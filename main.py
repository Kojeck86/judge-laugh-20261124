"""Entry for make.fun bounty u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes one single-line joke about office life to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The joke: the shared office fridge, where a "DO NOT TOUCH" label fails
but a "meeting notes" label protects a lunch forever — because nobody
in the office ever touches meeting notes.
"""

import os

JOKE = (
    "Someone labelled their lunch 'DO NOT TOUCH' in the shared fridge, "
    "so I labelled mine 'meeting notes' — it's been untouched for "
    "six months."
)


def main():
    # Gate: 1-199 characters, one line, no trailing newline.
    if not 1 <= len(JOKE) <= 199:
        raise ValueError("entry line must be 1-199 characters, got %d" % len(JOKE))
    if "\n" in JOKE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
