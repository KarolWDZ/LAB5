# Praca z PDF w Pythonie — pypdf & pdfplumber (Windows)

Ten projekt zawiera krótkie przykłady pokazujące, jak w Pythonie obsługiwać pliki PDF przy użyciu bibliotek **pypdf** oraz **pdfplumber**.  
Skrypty demonstrują m.in. odczyt metadanych, łączenie dokumentów, wyodrębnianie tekstu oraz zapisywanie tabel do CSV.

---

## Wymagania
Do uruchomienia przykładów potrzebujesz:

- Windows 10 lub nowszy
- Python 3.10+ (zalecany)
- Zainstalowane biblioteki z pliku `requirements.txt`

---

## Instalacja środowiska (Windows)

1. Utwórz i aktywuj wirtualne środowisko:
   
python -m venv .venv
.venv\Scripts\activate


2. Zainstaluj wymagane pakiety:

pip install -r requirements.txt


---

## Uruchamianie przykładów

Wszystkie skrypty znajdują się w katalogu `examples/`.

Przykłady uruchomisz w PowerShell lub CMD:

python examples/01_pdf_info_reader.py dokument.pdf
python examples/02_pdf_tools_merge_extract.py plik1.pdf  plik2.pdf
python examples/03_text_extract_pdfplumber.py dokument.pdf
python examples/04_table_exporter_pdfplumber.py dokument_z_tabela.pdf


---

## Co zawierają przykłady

| Skrypt | Opis |

| **01_pdf_info_reader.py** | Odczyt liczby stron i metadanych PDF |
| **02_pdf_tools_merge_extract.py** | Łączenie dwóch PDF + zapis pierwszej strony |
| **03_text_extract_pdfplumber.py** | Pobieranie tekstu z pierwszych dwóch stron |
| **04_table_exporter_pdfplumber.py** | Wykrywanie tabel i zapis do CSV |

---

## Cel projektu
Celem jest szybkie zapoznanie się z podstawowymi narzędziami do pracy z PDF w Pythonie na systemie Windows — bez zbędnych zależności i bez skomplikowanej konfiguracji.


