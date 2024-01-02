# Definicja klasy Osoba
class Osoba:
    def __init__(self, nazwisko, wzrost, kolor_oczu):
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.kolor_oczu = kolor_oczu

# Definicja klasy Pracownik dziedziczącej po klasie Osoba
class Pracownik(Osoba):
    def __init__(self, nazwisko, wzrost, kolor_oczu, stanowisko):
        # Wywołanie konstruktora klasy Osoba
        super().__init__(nazwisko, wzrost, kolor_oczu)
        # Dodatkowe pole dla klasy Pracownik
        self.stanowisko = stanowisko

# Utworzenie obiektu klasy Osoba
osoba = Osoba("Kowalski", 175, "niebieski")

# Utworzenie obiektu klasy Pracownik
pracownik = Pracownik("Nowak", 180, "zielony", "Programista")

# Wydruk informacji o osobie i pracowniku
print("Osoba:")
print(f"Nazwisko: {osoba.nazwisko}")
print(f"Wzrost: {osoba.wzrost} cm")
print(f"Kolor oczu: {osoba.kolor_oczu}")
print("\nPracownik:")
print(f"Nazwisko: {pracownik.nazwisko}")
print(f"Wzrost: {pracownik.wzrost} cm")
print(f"Kolor oczu: {pracownik.kolor_oczu}")
print(f"Stanowisko: {pracownik.stanowisko}")