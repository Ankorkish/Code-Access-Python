def kwadrat(liczba):
    return liczba * liczba

liczby = [1, 2, 3, 4, 5]

wynik = list(map(kwadrat, liczby))

print(wynik)
