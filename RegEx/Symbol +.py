import re

tekst = "Oto przykładowe zdanie. Uuu, jakie ciekawe!"
print(f'Tekst: {tekst}')
wzorzec = re.compile(r'[aeiouy]+', re.IGNORECASE)  # Szuka serii jednej lub więcej samogłosek
wynik = wzorzec.findall(tekst)

print(wynik)  # Zwróci ['O', 'o', 'y', 'a', 'o', 'e', 'a', 'ie', 'U', 'u', 'a', 'ie', 'ie', 'a', 'e']
