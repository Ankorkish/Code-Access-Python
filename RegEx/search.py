import re

wynik = re.search(r'ni', 'Python to więcej niż gad, to również świat programistów')
# Jeżeli zwrócony zostanie wynik
if wynik:
    print(f"Dopasowano: '{wynik.group()}', początek: {wynik.start()}, koniec: {wynik.end()}")
# Jeżeli zwrócone zostanie None
else:
    print('Nie znaleziono szukanego ciągu znaków.')