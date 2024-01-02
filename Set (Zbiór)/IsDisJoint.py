"""
set.isdisjoint(inny_zbior): Ta metoda sprawdza, czy zbiór
na którym jest wywoływana (set), i zbiór podany jako
argument (inny_zbior) nie mają wspólnych elementów.
Jeśli zbiory są rozłączne (czyli nie mają żadnych wspólnych elementów),
metoda zwraca True. W przeciwnym przypadku,
jeśli zbiory mają choć jeden wspólny element, metoda zwraca False.
"""

# Tworzymy dwa zbiory
pierwszy_zbior = {1, 2, 3}
drugi_zbior = {4, 5, 6}

# Używamy metody isdisjoint() do sprawdzenia, czy zbiory są rozłączne
rozlaczone = pierwszy_zbior.isdisjoint(drugi_zbior)

# Wyświetlamy wyniki
print("Pierwszy Zbiór:", pierwszy_zbior)
print("Drugi Zbiór:", drugi_zbior)
print("Czy Zbiory są Rozłączne:", rozlaczone)
