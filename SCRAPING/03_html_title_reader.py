"""
Wydobycie tytułu strony HTML przy użyciu BeautifulSoup.
Uruchomienie: python examples/03_html_title_reader.py
"""

import requests
from bs4 import BeautifulSoup

PAGE_URL = "https://merito.pl"

if __name__ == "__main__":
    html_doc = requests.get(PAGE_URL, timeout=20).text
    soup = BeautifulSoup(html_doc, "html.parser")

    title = soup.title.text.strip() if soup.title else "(brak tytułu)"
    print("Tytuł strony:", title)
