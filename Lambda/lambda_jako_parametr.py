def do_operation(a, b, operacja):
    wynik = operacja(a, b)
    print(f"Wynik {wynik}")

def select_opertaion(choice):
    if choice == 1:
        return lambda a,b: a + b

moja_operacja = select_opertaion(1)

do_operation(4, 5, moja_operacja)
do_operation(4, 5, lambda a, b: a * b)
