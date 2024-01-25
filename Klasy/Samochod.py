class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

moj_samochod = Samochod("Tojota", "Carolla")
print(moj_samochod.__dict__)