class LibraryBook:
    def __init__(self, tytul, autor):
        # Członkowie publiczni
        self.tytul = tytul
        self.autor = autor
        self._czy_dostepna = True  # Członek niepubliczny zaczynający się od _

    def wyswietl_informacje(self):
        # Metoda publiczna
        dostepnosc = "dostępna" if self._czy_dostepna else "niedostępna"
        print(f"Książka: {self.tytul}, Autor: {self.autor}, Dostępność: {dostepnosc}")

    def zmien_dostepnosc(self, dostepnosc):
        # Metoda niepubliczna
        self._czy_dostepna = dostepnosc


# Użytkowanie klasy
ksiazka1 = LibraryBook("Władca Pierścieni", "J.R.R. Tolkien")

# Wywołanie metody publicznej
ksiazka1.wyswietl_informacje()

# Zmiana dostępności przy użyciu metody niepublicznej
ksiazka1.zmien_dostepnosc(False)

# Sprawdzenie dostępności
# Proszę zauważyć, że to jest niezalecane w rzeczywistych scenariuszach i jest używane tylko dla celów zadania.
ksiazka1.wyswietl_informacje()
