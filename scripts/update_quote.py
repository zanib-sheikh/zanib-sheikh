import requests
import random

README_FILE = "README.md"

# Fallback quotes in case API fails
FALLBACK_QUOTES = [
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. – William James",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman"
]

def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} – {data[0]['a']}"
    except Exception as e:
        print("API failed, using fallback:", e)
    return random.choice(FALLBACK_QUOTES)

def update_readme(quote):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace placeholder inside README
    new_content = []
    inside_motivation = False
    for line in content.splitlines():
        if line.strip().startswith("## ✨ Daily Motivation"):
            inside_motivation = True
            new_content.append(line)
            continue
        if inside_motivation and line.strip().startswith("💡"):
            new_content.append(f'💡 "{quote}"')
            inside_motivation = False
            continue
        new_content.append(line)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(new_content))

if __name__ == "__main__":
    quote = fetch_quote()
    update_readme(quote)
    print("✅ Updated README with new quote:", quote)

