"""
Wyszukiwanie tabel na pierwszej stronie PDF i zapis do pliku CSV.
Użycie: python examples/04_table_exporter_pdfplumber.py dokument.pdf
"""

import sys
import csv
import pdfplumber

if __name__ == "__main__":
    pdf_file = sys.argv[1]

    with pdfplumber.open(pdf_file) as pdf:
        first_page = pdf.pages[0]
        detected = first_page.extract_tables() or []

    if not detected:
        print("Brak wykrytych tabel na stronie 1.")
        raise SystemExit(0)

    with open("page1_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(detected[0])

    print("Zapisano: page1_table.csv")
