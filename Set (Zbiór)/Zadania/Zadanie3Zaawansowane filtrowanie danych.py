# Definiowanie zbiorów
zbior1 = {"jabłko", "banan", "wiśnia"}
zbior2 = {"banan", "pomarańcza", "wiśnia"}

# Tworzenie nowego zbioru z unikalnymi słowami
unikalny_zbior = set()
for slowo in zbior1:
    unikalny_zbior.add(slowo)
for slowo in zbior2:
    unikalny_zbior.add(slowo)

# Wyświetlenie zbioru
print(unikalny_zbior)
