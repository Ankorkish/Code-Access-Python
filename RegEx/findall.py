import re

tekst = "Nina i Nino wybrali się do kina, a potem na obiad do Niny."
wzorzec = re.compile(r'ni', re.IGNORECASE)  # re.IGNORECASE ignoruje wielkość liter
wynik = wzorzec.findall(tekst)

print(wynik)  # Wyświetli wszystkie wystąpienia "ni" w tekście, niezależnie od wielkości liter
