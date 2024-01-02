def suma(*args):
    if len(args) == 0:
        print("len is 0")
    suma1 = 0
    for i in args:
        suma1 += i
    print(suma1)

suma()