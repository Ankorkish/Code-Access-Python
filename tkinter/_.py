def formatuj_tekst(tekst, duze_litery=False, odwrotnie=False):
    if duze_litery == True:
        tekst = tekst.upper()
    if odwrotnie == True:
        tekst = tekst[::-1]

    return tekst


print(formatuj_tekst("Witaj Świecie"))
print(formatuj_tekst("Witaj Świecie", duze_litery=True))
print(formatuj_tekst("Witaj Świecie", odwrotnie=True))
print(formatuj_tekst("Witaj Świecie", duze_litery=True, odwrotnie=True))