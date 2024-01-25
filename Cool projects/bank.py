#Projekt Bank
import time


class Konto:
    liczba_kat = 0

    def __init__(self, account_namae):
        Konto.liczba_kat += 1
        self.account_name = account_namae
        self.numer_konta = Konto.liczba_kat
        self.saldo = 0
        self.historia = []

    def wplac(self, kwota):
        self.kwota = kwota
        self.saldo += self.kwota
        self.historia.append(f"Wpłacono {self.kwota}.")
        return f"Operacja przeprowadzona pomyślnie. Wpłacono {self.kwota}!"

    def wyplac(self, kwota):
        self.kwota = kwota
        self.saldo -= self.kwota
        if self.saldo >= self.kwota:
            self.historia.append(f"Wypłacono {self.kwota}.")
            return f"Operacja przeprowadzona pomyślnie. Wypłacono {self.kwota}!"
        else:
            return f"Operacja niepowiodła się. Sprawdź, czy masz wystarczającą ilość środków do wypłacenia."

    def sprawdz_saldo(self):
        self.historia.append(f"Wyświetlono saldo: {self.saldo}.")
        return f"Twoje aktualne saldo wynosi: {self.saldo}."

    def wyswietl_historie(self):
        return self.historia

class AdminPanel:
    def __init__(self):
        self.Lista_kont = []
        self.wybrane_konto = None

    def menu(self):
        while True:
            print("1. Utwórz konto")
            #time.sleep(0.5)
            print("2. Zaloguj się")
            #time.sleep(0.5)
            print("3. Wpłać")
            #time.sleep(0.5)
            print("4. Wypłać")
            #time.sleep(0.5)
            print("5. Sprawdź saldo")
            #time.sleep(0.5)
            print("6. Historia transakcji")
            #time.sleep(0.5)
            print("7. Wyjdź")
            x = int(input("Wybierz odpowiednią cyfrę, aby podjąć akcję: "))

            if x > 7 and x < 1:
                return

            if x == 1:
                nazwa_konta = input("Podaj nazwę swojego konta: ")
                Nowe_konto = Konto(nazwa_konta)
                print(f"Utworzono konto {nazwa_konta} z numerem {Nowe_konto.liczba_kat}!")
                self.Lista_kont.append(Nowe_konto)
                time.sleep(1.5)
            if x == 2:
                if self.Lista_kont == []:
                    print("Brak aktywnych kont. Wybierz 1 aby stworzyć nowe konto.")
                    time.sleep(1.5)
                else:
                    print("Wybierz swoje konto, podając jego nazwę: ", [konto.account_name for konto in self.Lista_kont])
                    account_name = input()
                    for konto in self.Lista_kont:
                        if not (konto.account_name == account_name):
                            continue
                        print("Wpisz swoj numer konta!")
                        account_number = int(input())
                        print(konto.numer_konta, account_number)
                        if not (konto.numer_konta == account_number):
                            print("Nieprawidłowy numer konta. Spróbuj ponownie!")
                            break
                        print(f"Pomyślnie zalogowano do konta {konto.account_name}!")
                        self.wybrane_konto = konto
            if x == 3:
                if self.wybrane_konto == None:
                    print("Aby kontynuować zaloguj się do konta, wybierając 2.")
                    continue

                kwota = int(input("Wprowadź kwotę do wpłacenia: "))
                print(self.wybrane_konto.wplac(kwota))

            if x == 4:
                if self.wybrane_konto == None:
                    print("Aby kontynuować zaloguj się do konta, wybierając 2.")
                    continue

                kwota = int(input("Wprowadź kwotę do wypłacenia: "))
                print(self.wybrane_konto.wyplac(kwota))
            if x == 5:
                if self.wybrane_konto == None:
                    print("Aby kontynuować zaloguj się do konta, wybierając 2.")
                    continue

                print(self.wybrane_konto.sprawdz_saldo())
            if x == 6:
                if self.wybrane_konto == None:
                    print("Aby kontynuować zaloguj się do konta, wybierając 2.")
                    continue

                print(self.wybrane_konto.wyswietl_historie())
            if x == 7:
                print("Wylogowano pomyślnie!")
                self.wybrane_konto = None
                continue


panel = AdminPanel()

panel.menu()