import re
wynik = re.search(r'Python', 'to więcej niż gad, to również świat programistów Python')
print(f"Dopasowano: '{wynik.group()}', początek: {wynik.span()[0]}, koniec: {wynik.span()[1]}")

#przyklad 2
"""
wynik = re.match(r'ni', 'Python to więcej niż gad, to również świat programistów')
print(wynik)
"""
