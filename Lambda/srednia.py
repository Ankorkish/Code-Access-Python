lista = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
nowa_lista = list(map(lambda a: (a[0] + a[1] + a[2]) / 3, lista))
print(nowa_lista)