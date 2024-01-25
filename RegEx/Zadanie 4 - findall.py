import re

tekst = "Wczoraj poszedłem do parku. Spotkałem tam wiele zwierząt, w tym Parkury, małego psa mojego przyjaciela."
wzorzec = re.compile(r'park', re.IGNORECASE)
wynik = wzorzec.findall(tekst)

print(wynik)  # Wyświetli wszystkie wystąpienia "park" w tekście, niezależnie od wielkości liter

