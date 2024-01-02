# Program Pythona do ilustracji
# **kwargs dla zmiennej liczby argumentów ze słowami kluczowymi
def mojaFunkcja(**kwargs):
    for klucz, wartosc in kwargs.items():
        print(f"{klucz} to {wartosc}")

mojaFunkcja(imie='Anna', zawod='Programista', miasto='Warszawa')
