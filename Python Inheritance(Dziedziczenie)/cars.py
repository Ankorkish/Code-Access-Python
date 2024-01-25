class Smochod:
    def __init__(self, liczba_kol):
        self.liczba_kol = liczba_kol

    def jedz(self):
        print("Samochód jedzie")

class Osobowy(Smochod):
    pass

class Ciezarowy(Smochod):
    def __init__(self, liczba_kol, wysokosc):
        super().__init__(liczba_kol)
        self. wysokosc = wysokosc
    def zaladunek(self):
        print("Załadunek towaru")

    def jedz(self):
        print("Samochód jedzie2")
    def show_info(self):
        print(self.liczba_kol)
        print(self.wysokosc)



osobowy = Osobowy(4)
osobowy.jedz()

print()

ciezarowy = Ciezarowy(6, 7)
ciezarowy.jedz()
ciezarowy.zaladunek()
ciezarowy.show_info()