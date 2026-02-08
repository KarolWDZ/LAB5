"""
Łączenie dwóch plików PDF oraz zapis wyłącznie pierwszej strony.
Użycie: python examples/02_pdf_tools_merge_extract.py plik1.pdf plik2.pdf
"""

import sys
from pypdf import PdfReader, PdfWriter


def combine_pdfs(first: str, second: str, output: str) -> None:
    """Łączy dwa dokumenty PDF w jeden."""
    writer = PdfWriter()

    for file_path in (first, second):
        reader = PdfReader(file_path)
        for pg in reader.pages:
            writer.add_page(pg)

    with open(output, "wb") as f:
        writer.write(f)


def extract_page_one(pdf_file: str, output: str) -> None:
    """Zapisuje stronę nr 1 jako osobny dokument."""
    reader = PdfReader(pdf_file)
    writer = PdfWriter()
    writer.add_page(reader.pages[0])

    with open(output, "wb") as f:
        writer.write(f)


if __name__ == "__main__":
    file_a, file_b = sys.argv[1], sys.argv[2]

    combine_pdfs(file_a, file_b, "combined.pdf")
    extract_page_one("combined.pdf", "combined_page1.pdf")

    print("Gotowe: combined.pdf oraz combined_page1.pdf")
