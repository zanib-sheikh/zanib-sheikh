import requests
import random
import re

README_FILE = "README.md"

# Fallback quotes in case API fails
FALLBACK_QUOTES = [
    '"The future belongs to those who believe in the beauty of their dreams." – Eleanor Roosevelt',
    '"Do what you can, with what you have, where you are." – Theodore Roosevelt',
    '"Believe you can and you’re halfway there." – Theodore Roosevelt',
    '"Happiness depends upon ourselves." – Aristotle',
    '"Stay positive, work hard, make it happen." – Unknown',
]

def fetch_quote():
    """Fetch quote from API, otherwise return fallback"""
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return f"\"{data[0]['q']}\" – {data[0]['a']}"
    except Exception:
        pass
    # If API fails → return random fallback quote
    return random.choice(FALLBACK_QUOTES)

def update_readme(quote):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"<!--START_QUOTE-->.*?<!--END_QUOTE-->",
        f"<!--START_QUOTE--> {quote} <!--END_QUOTE-->",
        content,
        flags=re.DOTALL
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    quote = fetch_quote()
    update_readme(quote)
