# Raport — Przetwarzanie PDF w Pythonie (pypdf + pdfplumber)

## 1. Zakres projektu
Przykłady pokazują dwa różne podejścia do pracy z PDF:
- manipulowanie strukturą dokumentu (strony, scalanie, metadane),
- wydobywanie treści i danych tabelarycznych.

Obie biblioteki dobrze się uzupełniają — jedna operuje na „szkieletach” PDF, druga na zawartości.

---

## 2. pypdf — operacje na strukturze PDF

### Charakterystyka
`pypdf` to lekka biblioteka pozwalająca czytać i tworzyć dokumenty PDF.  
Nadaje się do:
- pobierania liczby stron,
- odczytu metadanych,
- łączenia kilku PDF w jeden,
- wyodrębniania stron i zapisywania ich jako osobne pliki.

### Zalety
- proste API,
- brak zewnętrznych zależności,
- szybkie działanie.

### Ograniczenia
- ekstrakcja tekstu jest podstawowa — w przypadku skanów lub nietypowych PDF może nie działać idealnie.

---

## 3. pdfplumber — wydobywanie treści i tabel

### Charakterystyka
`pdfplumber` specjalizuje się w analizie zawartości stron PDF.  
Pozwala pobierać:
- tekst,
- układ elementów,
- tabele (jeśli są rozpoznawalne).

### Zalety
- bardzo dobre narzędzia do ekstrakcji tekstu,
- obsługa tabel, co jest trudne w wielu innych bibliotekach.

### Ograniczenia
- wykrywanie tabel zależy od jakości dokumentu,
- czasem wymaga dostrajania parametrów.

---

## 4. Wnioski
- **pypdf** najlepiej sprawdza się przy operacjach technicznych: scalanie, dzielenie, metadane.  
- **pdfplumber** jest znacznie lepszy, gdy potrzebujemy wyciągnąć treść lub dane z wnętrza dokumentu.  
- Połączenie obu bibliotek daje szerokie możliwości pracy z PDF w Pythonie — od prostych operacji po analizę dokumentów.

