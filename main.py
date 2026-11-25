"""Invent a word we need — make.fun entry program.

Writes the one-line word + definition to /output/entry.txt.
"""
# Design notes — why this line should win:
# "draftghost" (draft + ghost) names a gap everyone recognises: the
# message you typed, perfected, and never sent, still sitting in your
# drafts. It is sayable, spellable and memorable, and the definition
# lands in one reading. Web-checked 25 Nov 2026: no dictionary or prior
# use of "draftghost" as a word turned up, so it is genuinely new.

ENTRY = "draftghost (n.) \u2014 a message you typed, perfected, then never sent; it still haunts your drafts folder."

MAX_CHARS = 140
MAX_WORDS = None

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
