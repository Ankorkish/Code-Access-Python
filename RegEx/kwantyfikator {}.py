import re

tekst = "ha ha ha haaa ha"
wzorzec = re.compile(r'ha{3}')
wynik = wzorzec.findall(tekst)

print(wynik)  # Wyświetla: ['haaa']
