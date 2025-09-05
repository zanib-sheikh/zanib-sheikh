#!/usr/bin/env python3
import requests, re

README_PATH = "README.md"
START = "<!--STARTS_HERE_QUOTE_README-->"
END = "<!--ENDS_HERE_QUOTE_README-->"

def fetch_quote():
    """
    Fetch a short quote from Quotable. If anything fails, fall back to a nice quote.
    """
    try:
        r = requests.get("https://api.quotable.io/random?maxLength=120", timeout=12)
        r.raise_for_status()
        data = r.json()
        quote = data.get("content", "").strip() or "Dream big. Start small. Act now."
        author = data.get("author", "Unknown").strip() or "Unknown"
        return f'> 💡 "{quote}" — {author}'
    except Exception:
        # Graceful fallback (a good, professional quote)
        return '> 💡 "The future belongs to those who believe in the beauty of their dreams." — Eleanor Roosevelt'

def update_block(md: str, new_block: str) -> str:
    block = f"\n{START}\n{new_block}\n{END}\n"
    if START in md and END in md:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
        return pattern.sub(block.strip(), md)
    # If markers don't exist, append a new section (safety)
    return md + f"\n\n## ✨ Daily Motivation\n" + block

def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    quote_md = fetch_quote()
    updated = update_block(content, quote_md)

    if updated != content:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated)
        print("README updated with a fresh quote ✨")
    else:
        print("No changes detected.")

if __name__ == "__main__":
    main()
