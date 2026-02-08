"""
Wydobywanie tekstu z dwóch pierwszych stron PDF przy użyciu pdfplumber.
Użycie: python examples/03_text_extract_pdfplumber.py dokument.pdf
"""

import sys
import pdfplumber

if __name__ == "__main__":
    path = sys.argv[1]

    with pdfplumber.open(path) as pdf:
        for idx, page in enumerate(pdf.pages[:2], start=1):
            content = (page.extract_text() or "").strip()
            print(f"\n=== Strona {idx} ===")
            print(content[:1200])  # ograniczenie długości
