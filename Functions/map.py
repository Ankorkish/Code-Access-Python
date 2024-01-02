lista = ["1", "2", "3", "4", "5"]
for i in lista:
    print(type(i))

lista = list(map(int, lista))

for i in lista:
    print(type(i))

szescian_v2  = lambda x : x*x*x
lista = list(map(szescian_v2, lista))

print(lista)
