# Web scraping w Pythonie — requests + BeautifulSoup4

## Opis
Ten zestaw przykładów pokazuje podstawowe techniki pobierania i analizowania stron WWW:
- **requests** — wykonywanie zapytań HTTP i pobieranie danych,
- **BeautifulSoup4** — parsowanie HTML i wyszukiwanie elementów.

Skrypty znajdują się w katalogu `examples/`.

## Instalacja środowiska (Windows)
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

## Uruchamianie przykładów

python examples/01_http_basic_fetch.py
python examples/02_http_stream_download.py
python examples/03_html_title_reader.py
python examples/04_html_link_collector.py


## Zawartość
- **01_http_basic_fetch.py** — pobranie strony i analiza nagłówków  
- **02_http_stream_download.py** — pobieranie pliku strumieniowo  
- **03_html_title_reader.py** — odczyt tytułu strony  
- **04_html_link_collector.py** — wyciąganie wszystkich linków z HTML  
