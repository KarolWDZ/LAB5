"""
Podstawowy odczyt informacji o pliku PDF przy użyciu pypdf.
Użycie: python examples/01_pdf_info_reader.py dokument.pdf
"""

import sys
from pypdf import PdfReader

if __name__ == "__main__":
    source = sys.argv[1]  # ścieżka wejściowa
    pdf = PdfReader(source)

    # Wyświetlamy liczbę stron oraz dostępne metadane
    print("Stron w dokumencie:", len(pdf.pages))
    print("Dane opisowe:", pdf.metadata)
