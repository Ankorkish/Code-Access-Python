class Kalkulator:
    def dodaj(self, a, b):
        return a + b

    def odejmij(self, a, b):
        return a - b

    def pomnoz(self, a, b):
        return a * b

    def podziel(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Błąd: Dzielenie przez zero!"

# Użycie klasy
kalkulator = Kalkulator()

print("Dodawanie: 7 + 5 =", kalkulator.dodaj(7, 5))
print("Odejmowanie: 10 - 4 =", kalkulator.odejmij(10, 4))
print("Mnożenie: 6 * 3 =", kalkulator.pomnoz(6, 3))
print("Dzielenie: 8 / 2 =", kalkulator.podziel(8, 2))
print("Dzielenie: 5 / 0 =", kalkulator.podziel(5, 0))  # Przykład próby dzielenia przez zero
