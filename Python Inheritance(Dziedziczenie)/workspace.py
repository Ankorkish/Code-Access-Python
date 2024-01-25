class Pojazd:
    def __init__(self, marka, rodzaj_paliwa):
        self.marka = marka
        self.rodzajpaliwa = rodzaj_paliwa

    def wyswietl_info(self):
        return self.marka, self.rodzajpaliwa

class SamochodOsobowy(Pojazd):
    def __init__(self, marka, rodzaj_paliwa, liczba_miejsc):
        super().__init__(marka, rodzaj_paliwa)
        self.liczbamiejsc = liczba_miejsc

    def wyswietl_info(self):
        marka, rodzajpaliwa = super().wyswietl_info()
        return self.liczbamiejsc, marka, rodzajpaliwa


Auto = Pojazd("Lexus", "Diesel")
Auto2 = SamochodOsobowy("Skoda", "Benzyna", 5)
Auto.wyswietl_info()
Auto2.wyswietl_info()

print(Auto2.wyswietl_info())