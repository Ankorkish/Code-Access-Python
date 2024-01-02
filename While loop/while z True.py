# Inicjalizacja licznika
licznik = 0

# Pętla nieskończona
while True:
    # Zwiększanie licznika
    licznik += 1
    print(f"Licznik wynosi {licznik}")

    # Sprawdzenie, czy licznik osiągnął określoną wartość
    if licznik == 10:
        # Jeśli tak, zakończ pętlę
        break

# To zostanie wykonane po wyjściu z pętli
print("Pętla się zakończyła.")
