class Uzytkownik:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def pokaz_informacje(self):
        return f"Użytkownik: {self.imie}, Wiek: {self.wiek}"

def dodaj_uzytkownika(lista_uzytkownikow):
    imie = input("Podaj imię użytkownika: ")
    wiek = input("Podaj wiek użytkownika: ")
    nowy_uzytkownik = Uzytkownik(imie, wiek)
    lista_uzytkownikow.append(nowy_uzytkownik)
    print("Dodano nowego użytkownika.")

uzytkownicy = []
while True:
    print("\n1. Dodaj użytkownika")
    print("2. Pokaż użytkowników")
    print("3. Wyjście")

    wybor = input("Wybierz opcję: ")

    if wybor == '1':
        dodaj_uzytkownika(uzytkownicy)
    elif wybor == '2':
        for uzytkownik in uzytkownicy:
            print(uzytkownik.pokaz_informacje())
    elif wybor == '3':
        break
    else:
        print("Niepoprawna opcja, spróbuj ponownie.")

