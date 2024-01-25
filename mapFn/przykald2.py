liczby = ['1', '2', '3', '4', '5']

#wynik = list(map(int, liczby))

wynik = []
for i in liczby:
    i += 1

    wynik.append(int(i))

print(wynik)
