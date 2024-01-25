class Uzytkownik:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie}: {self.wiek} lat"

def urodziny(uzytkownik):
    uzytkownik.wiek += 1
    return uzytkownik

uzytkownicy = [Uzytkownik("Anna", 30), Uzytkownik("Bartek", 12), Uzytkownik("Celina", 90)]

starsze_uzytkownicy = list(map(urodziny, uzytkownicy))

for i in starsze_uzytkownicy:
    print(i)


