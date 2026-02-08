"""
Przykład pobrania strony WWW przy użyciu requests.
Wyświetlamy kod odpowiedzi, typ treści oraz długość pobranego HTML.
Uruchomienie: python examples/01_http_basic_fetch.py
"""

import requests

SITE_URL = "https://www.merito.pl/"

if __name__ == "__main__":
    resp = requests.get(SITE_URL, timeout=20)

    print("HTTP status:", resp.status_code)
    print("Nagłówek Content-Type:", resp.headers.get("Content-Type"))
    print("Rozmiar dokumentu (znaki):", len(resp.text))
