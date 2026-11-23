"""Write one six-word story to /output/entry.txt.

One fixed line, no randomness, no time, no network, stdlib only.
The story: a stargazer counts the stars, and one of them counts back.
"""

import os

STORY = "He counted stars. One counted back."

# The harness reads exactly this path; the gate allows 1-60 characters.
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(STORY + "\n")


if __name__ == "__main__":
    main()
