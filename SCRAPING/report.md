# Web scraping — requests + BeautifulSoup4

## 1. Zakres
Przykłady demonstrują podstawowe techniki pobierania stron internetowych oraz analizowania ich zawartości w Pythonie.  
Podejście to jest często wykorzystywane do automatyzacji, monitoringu stron i ekstrakcji danych.

---

## 2. Biblioteka: requests

### Zastosowanie
- wykonywanie zapytań HTTP (GET, POST itd.),
- pobieranie treści stron,
- obsługa nagłówków i statusów,
- pobieranie plików (również strumieniowo).

### Zalety
- bardzo prosty interfejs,
- szerokie wsparcie społeczności,
- czytelny i intuicyjny kod.

### Ograniczenia
- brak natywnej obsługi async,
- niektóre strony mogą blokować scraping.

---

## 3. Biblioteka: BeautifulSoup4

### Zastosowanie
- parsowanie HTML i XML,
- wyszukiwanie elementów po tagach, klasach i selektorach CSS,
- pobieranie tekstu i atrybutów (np. `href`).

### Zalety
- szybkie prototypowanie,
- łatwa nawigacja po strukturze dokumentu.

### Ograniczenia
- nie wykonuje JavaScript,
- jakość wyników zależy od poprawności HTML.

---

## 4. Podsumowanie
`requests` odpowiada za pobranie danych, a `BeautifulSoup4` za ich analizę.  
Razem tworzą prosty, lekki i skuteczny zestaw narzędzi do web scrapingu w Pythonie.
