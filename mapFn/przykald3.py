osoby = [{"imie": "Anna", "wiek": 30}, {"imie": "Bartek", "wiek": 25}, {"imie": "Celina", "wiek": 20}]

def moja_funkcja(i):
    i["wiek"] = i.get("wiek") + 1
    return i

osoby2 = list(map(moja_funkcja, osoby))

print(osoby2)