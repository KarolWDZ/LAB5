"""
Wyszukiwanie wszystkich linków <a href="..."> na stronie.
Uruchomienie: python examples/04_html_link_collector.py
"""

import requests
from bs4 import BeautifulSoup

PAGE_URL = "https://merito.pl"

if __name__ == "__main__":
    html_doc = requests.get(PAGE_URL, timeout=20).text
    soup = BeautifulSoup(html_doc, "html.parser")

    found_links = [tag["href"] for tag in soup.select("a[href]")]

    print("Znalezione odnośniki:")
    for link in found_links:
        print("•", link)
