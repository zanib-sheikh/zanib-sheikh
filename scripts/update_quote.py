import requests
import random

README_FILE = "README.md"

# Fallback quotes
FALLBACK_QUOTES = [
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. – William James",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman"
]

def fetch_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random", timeout=10)
        if res.status_code == 200:
            data = res.json()
            return f"{data[0]['q']} – {data[0]['a']}"
    except Exception as e:
        print("⚠️ API failed, using fallback:", e)
    return random.choice(FALLBACK_QUOTES)

def update_readme(quote):
    with open(README_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    found = False
    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.strip() == "## ✨ Daily Motivation" and i + 1 < len(lines):
            new_lines.append(f'💡 "{quote}"\n')
            found = True
            # Skip the old placeholder line
            if lines[i+1].strip().startswith("💡"):
                continue

    if not found:
        print("⚠️ Could not find the placeholder. Please check README formatting.")

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    q = fetch_quote()
    update_readme(q)
    print("✅ Updated README with:", q)
