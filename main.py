"""One-line roast for make.fun: the phone's battery saver "saving" the phone
by killing the very thing it was needed for. Writes the line to entry.txt.

The line is a single sentence (181 chars, within the 200-char cap), names a
specific daily gadget (the phone) and a specific behaviour (battery saver
dimming the screen and killing maps, then boasting about 4% saved), and lands
on a reversal: a lifeguard drowning you to keep you dry.
"""

import os

TEXT = "My phone's battery saver kicked in at 2pm, dimmed the screen, killed my maps mid-journey, and then proudly notified me it had saved 4% — like a lifeguard drowning me to keep me dry."

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
assert 1 <= len(TEXT) <= 200, len(TEXT)
assert TEXT.strip() == TEXT
assert "\n" not in TEXT


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
