"""
Pobieranie pliku metodą strumieniową (chunkami) i zapis na dysk.
Uruchomienie: python examples/02_http_stream_download.py
"""

from pathlib import Path
import requests

FILE_URL = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
OUTPUT_PATH = Path("sample_download.pdf")

if __name__ == "__main__":
    # stream=True pozwala pobierać dane partiami
    with requests.get(FILE_URL, stream=True, timeout=20) as resp:
        resp.raise_for_status()

        with open(OUTPUT_PATH, "wb") as f:
            for block in resp.iter_content(64 * 1024):
                if block:
                    f.write(block)

    print("Plik zapisany pod:", OUTPUT_PATH.resolve())
