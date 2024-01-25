import random
import string

def generuj_haslo(dlugosc):
    if dlugosc < 6:
        print("Hasło powinno mieć co najmniej 6 znaków dla bezpieczeństwa.")
        return None

    litery = string.ascii_letters  # litery alfabetu (zarówno małe, jak i duże)
    cyfry = string.digits          # cyfry od 0 do 9
    symbole = string.punctuation   # symbole specjalne

    # Łączymy wszystkie znaki w jeden zestaw
    wszystkie_znaki = litery + cyfry + symbole

    # Losujemy znaki z połączonego zestawu
    haslo = ''
    for _ in range(dlugosc):
        znak = random.choice(wszystkie_znaki)  # Losujemy pojedynczy znak
        haslo += znak  # Dodajemy ten znak do hasła

    return haslo

# Przykładowe użycie
dlugosc_hasla = 10  # Możesz zmienić długość według potrzeb
wygenerowane_haslo = generuj_haslo(dlugosc_hasla)
print("Wygenerowane hasło:", wygenerowane_haslo)
