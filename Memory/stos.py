lista = [1, 3, 4, 6]
lista2 = lista

print(hex(id(lista)))
print(hex(id(lista2)))

print(lista)
print(lista2)

lista2[2] = "Hello world!"

print()
print(lista)
print(lista2)