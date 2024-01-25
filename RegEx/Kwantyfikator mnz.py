import re

tekst = "AAAAACCC"
print(f'Łańcuch: {tekst}')
wzorzec = re.compile(r'B*')
print(wzorzec.findall(tekst))
