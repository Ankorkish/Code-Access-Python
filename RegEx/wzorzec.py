import re

# Kompilujemy wyrażenie regularne do wzorca
wzorzec = re.compile(r'Python')

# Używamy skompilowanego wzorca do wyszukiwania w tekście
tekst_1 = "Python to więcej niż gad, to również świat programistów"
tekst_2 = "to więcej niż gad, to również świat programistów Python"
wynik = wzorzec.search(tekst_1)

# Sprawdzamy, czy znaleziono dopasowanie i wypisujemy wynik
if wynik:
    print(f"Znaleziono: '{wynik.group()}' na pozycji: {wynik.start()}-{wynik.end()}")
else:
    print("Nie znaleziono dopasowania.")
wynik = wzorzec.search(tekst_2)

# Sprawdzamy, czy znaleziono dopasowanie i wypisujemy wynik
if wynik:
    print(f"Znaleziono: '{wynik.group()}' na pozycji: {wynik.start()}-{wynik.end()}")
else:
    print("Nie znaleziono dopasowania.")