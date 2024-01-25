class KontoBankowe:
    def __init__(self, saldo_początkowe, typ_konta):
        self.saldopoczatkowe = saldo_początkowe
        self.typkonta = typ_konta
        self._costam = "sadasd"

    def _wykonaj_przelew(self):
        kwota_przelewu = int(input("Jaką kwotę chcesz przelać? "))
        self.saldopoczatkowe -= kwota_przelewu

        return "Kwota ", kwota_przelewu, "została przelana na inne konto!"


    def sprawdz_saldo(self):
        return self.saldopoczatkowe


Konto = KontoBankowe(1000, "oszczędnościowe")

print(Konto.sprawdz_saldo())
print(Konto._wykonaj_przelew())

print(Konto.sprawdz_saldo())


Konto2 = KontoBankowe(1900, "oszczędnościowe")

print(Konto2.sprawdz_saldo())
print(Konto2.wykonaj_przelew())


print(Konto2.saldopoczatkowe)
print(Konto2.sprawdz_saldo())