"""Treść zadania: Masz dwa zbiory: pierwszy_zbior = {"jabłko", "banan", "pomarańcza"}
i drugi_zbior = {"kiwi", "banan", "winogrono"}. Napisz program,
który utworzy nowy zbiór zawierający tylko te owoce,
które nie powtarzają się w obu zbiorach. Użyj metodę union()."""

# Definiowanie zbiorów
pierwszy_zbior = {"jabłko", "banan", "pomarańcza"}
drugi_zbior = {"kiwi", "banan", "winogrono"}

# Tworzenie nowego zbioru z unikalnymi owocami
unikalne_owoce = pierwszy_zbior.union(drugi_zbior)


# Wyświetlenie zbioru
print("Unikalne owoce:", unikalne_owoce)
