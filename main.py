"""Write one six-word story to /output/entry.txt.

One fixed line, no randomness, no time, no network, stdlib only.
The story: a stargazer counts the stars, and one of them counts back.
"""

import os

STORY = "He counted stars. One counted back."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(STORY + "\n")


if __name__ == "__main__":
    main()
