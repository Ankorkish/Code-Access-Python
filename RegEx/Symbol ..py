import re

tekst = 'W Pythonie każdy symbol ma znaczenie.'
wzorzec = re.compile(r'.')
print(wzorzec.findall(tekst))
