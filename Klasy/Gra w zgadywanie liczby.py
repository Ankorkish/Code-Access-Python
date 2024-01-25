import random
import math

# Pobieranie danych wejściowych
dolna_granica = int(input("Wprowadź dolną granicę:- "))

# Pobieranie danych wejściowych
gorna_granica = int(input("Wprowadź górną granicę:- "))

# generowanie losowej liczby pomiędzy
# dolną a górną granicą
x = random.randint(dolna_granica, gorna_granica)
print("\n\tMasz tylko",
       round(math.log(gorna_granica - dolna_granica + 1, 2)),
      " szanse, aby zgadnąć liczbę!\n")

# Inicjalizacja liczby prób.
liczba_prob = 0

# do obliczenia minimalnej liczby
# prób w zależności od zakresu
while True:
    liczba_prob += 1

    # przyjmowanie zgadywanej liczby jako wejścia
    zgadnij = int(input("Zgadnij liczbę:- "))

    # Testowanie warunków
    if x == zgadnij:
        print("Gratulacje, udało Ci się za ",
              liczba_prob, " razem")
        # Po zgadnięciu, pętla się zakończy
        break
    elif x > zgadnij:
        print("Zgadłeś za mało!")
    elif x < zgadnij:
        print("Zgadłeś za wysoko!")



