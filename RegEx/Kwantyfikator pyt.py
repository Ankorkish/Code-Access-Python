import re

tekst = "Kot siedział na mat. Kocur siedział na mate."
wzorzec = re.compile(r'mate?')
wynik = wzorzec.findall(tekst)

print(wynik)  # Wyświetla: ['mat', 'mate']
