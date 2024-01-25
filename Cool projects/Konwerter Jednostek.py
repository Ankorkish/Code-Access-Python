class KonwerterJednostek:
    def cm_na_cale(self, cm):
        return cm * 0.393701

    def cale_na_cm(self, cale):
        return cale * 2.54

    def kg_na_funty(self, kg):
        return kg * 2.20462

    def funty_na_kg(self, funty):
        return funty * 0.453592

# Użycie klasy
konwerter = KonwerterJednostek()

print("10 cm to", konwerter.cm_na_cale(10), "cali")
print("5 cali to", konwerter.cale_na_cm(5), "cm")
print("3 kg to", konwerter.kg_na_funty(3), "funty")
print("2 funty to", konwerter.funty_na_kg(2), "kg")