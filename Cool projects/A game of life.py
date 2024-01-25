import time

def wypisz_sitke(siatka):
    for wiersz in siatka:
        for komurka in wiersz:
            print("#" if komurka == 1 else "_", end=" ")
        print()

def zdicz_sasiadow(siatka, x, y):
    sasiedzi = 0
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < len(siatka) and 0 <= y + dy < len(siatka[0]):
                sasiedzi += siatka[x + dx][y + dy]
    return sasiedzi

def nastepna_runda(siatka):
    nowa_siatka = [[0 for _ in range(20)] for _ in range(20)]
    for x in range(len(siatka)):
        for y in range(len(siatka)):
            sasiedzi = zdicz_sasiadow(siatka, x, y)
            if siatka[x][y]:
                if sasiedzi == 2 or sasiedzi == 3:
                    nowa_siatka[x][y] = 1
                else:
                    nowa_siatka[x][y] = 0
            else:
                if sasiedzi == 3:
                    nowa_siatka[x][y] = 1
    return nowa_siatka

def uruchom_gre():
    siatka = [[0 for _ in range(20)] for _ in range(20)]

    siatka[4][5] = 1
    siatka[4][6] = 1
    siatka[5][5] = 1
    siatka[5][4] = 1
    siatka[6][5] = 1

    for _ in range(100):
        wypisz_sitke(siatka)
        siatka = nastepna_runda(siatka)
        print()
        time.sleep(1)

uruchom_gre()