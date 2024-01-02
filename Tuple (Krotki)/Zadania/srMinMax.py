def oblicz_statystyki(lista):
    if not lista:
        return (0, 0, 0)
    srednia = sum(lista) / len(lista)
    minimum = min(lista)
    maksimum = max(lista)

    return (srednia, minimum, maksimum)

#Przykładowe wywolanie funkcji
wynik =  oblicz_statystyki([1, 2, 3, 4, 5])
print(wynik)