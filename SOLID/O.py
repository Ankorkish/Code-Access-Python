from abc import ABC, abstractmethod

class Podatek(ABC):
    @abstractmethod
    def oblicz(self, kwota):
        pass

class VAT(Podatek):
    def oblicz(self, kwota):
        return kwota * 0.23

class KalkulatorPodatkowy:
    def oblicz_podatek(self, kwota, podatek: Podatek):
        return podatek.oblicz(kwota)

# Użycie
vat = VAT()
kalkulator = KalkulatorPodatkowy()
print(kalkulator.oblicz_podatek(100, vat))  # Wyświetla 23