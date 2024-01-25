import random
def graj_kamien_papier_nozyce():
    mozliwe_ruchy = ["kamień", "papier", "nożyce"]
    wybor_komputera = random.choice(mozliwe_ruchy)

    wybor_gracza = input("Wybierz kamień, papier lub nożyce: ").lower()
    while wybor_gracza not in mozliwe_ruchy:
        print("Niepoprawny wybór. Spróbuj ponownie.")
        wybor_gracza = input("Wybierz kamień, papier lub nożyce: ").lower()

    print(f"Twój wybór: {wybor_gracza}")
    print(f"Wybor komputera: {wybor_komputera}")

    if wybor_gracza == wybor_komputera:
        return "Remis!"
    elif (wybor_gracza == "kamień" and wybor_komputera == "nożyce") or \
            (wybor_gracza == "papier" and wybor_komputera == "kamień") or \
            (wybor_gracza == "nożyce" and wybor_komputera == "papier"):
        return "Wygrałeś!"
    else:
        return "Przegrałeś!"


# Uruchomienie gry
wynik = graj_kamien_papier_nozyce()
print(wynik)
