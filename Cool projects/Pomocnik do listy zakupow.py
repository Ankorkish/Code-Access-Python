class ListaZakupow:
    def __init__(self):
        self.lista = []

    def dodaj(self, przedmiot):
        self.lista.append(przedmiot)
        print(f"Dodano: {przedmiot}")

    def usun(self, przedmiot):
        if przedmiot in self.lista:
            self.lista.remove(przedmiot)
            print(f"Usunięto: {przedmiot}")
        else:
            print("Przedmiot nie znaleziony na liście.")

    def wyswietl(self):
        if self.lista:
            print("Lista zakupów:")
            for przedmiot in self.lista:
                print(f"- {przedmiot}")
        else:
            print("Lista zakupów jest pusta.")

# Użycie klasy
lista_zakupow = ListaZakupow()

# Dodawanie przedmiotów
lista_zakupow.dodaj("Mleko")
lista_zakupow.dodaj("Chleb")

# Wyświetlanie listy
lista_zakupow.wyswietl()

# Usuwanie przedmiotu
lista_zakupow.usun("Mleko")

# Wyświetlanie listy po usunięciu
lista_zakupow.wyswietl()