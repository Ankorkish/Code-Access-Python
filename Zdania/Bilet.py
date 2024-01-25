def czy_szczesliwy_bilet(numer_biletu):
    suma_pierwszych =  int(numer_biletu[0]) + int(numer_biletu[1]) + int(numer_biletu[2])
    suma_ostatnich =  int(numer_biletu[3]) + int(numer_biletu[4]) + int(numer_biletu[5])

    return suma_pierwszych == suma_ostatnich


print(czy_szczesliwy_bilet("385916"))  # Powinno zwrócić True
print(czy_szczesliwy_bilet("123456"))  # Powinno zwrócić False
