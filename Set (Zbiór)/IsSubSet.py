"""set.issubset(inny_zbior): Ta metoda zwraca True, jeśli zbiór,
na którym jest wywoływana, jest podzbiorem zbioru przekazanego
jako argument (inny_zbior). Innymi słowy, zwraca True,
jeśli każdy element z pierwszego zbioru jest również
elementem drugiego zbioru. Metoda zwraca False, jeśli znajduje
chociaż jeden element w pierwszym zbiorze, który nie występuje w drugim zbiorze."""

# Tworzymy dwa zbiory
pierwszy_zbior = {1, 2, 3}
drugi_zbior = {1, 2, 3, 4, 5}

# Używamy metody issubset() do sprawdzenia, czy pierwszy zbiór jest podzbiorem drugiego
jest_podzbiorem = pierwszy_zbior.issubset(drugi_zbior)

print("Pierwszy Zbiór:", pierwszy_zbior)
print("Drugi Zbiór:", drugi_zbior)
print("Czy Pierwszy Zbiór jest Podzbiorem Drugiego:", jest_podzbiorem)
