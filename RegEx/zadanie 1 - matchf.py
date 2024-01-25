"""
Zadanie: Sprawdzanie, Czy Tekst Zaczyna Się Od Określonego Wyrazu
Cel: Napisz krótki skrypt w Pythonie, który używa re.match, aby sprawdzić, czy dany tekst zaczyna się od słowa "Witaj".

Wskazówki:

Zaimportuj moduł re.
Użyj funkcji re.match, aby sprawdzić, czy tekst zaczyna się od "Witaj". Wzorzec wyrażenia regularnego to "Witaj".
Skrypt powinien zwracać informację, czy tekst pasuje do wzorca.
"""

import re

tekst = "Uczymy się programowania w języku Python."
szukaj = re.search("Python", tekst)

if szukaj:
    print(f"Słowo 'Python' znaleziono na pozycji: {szukaj.start()}")
else:
    print("Słowo 'Python' nie zostało znalezione w tekście.")

