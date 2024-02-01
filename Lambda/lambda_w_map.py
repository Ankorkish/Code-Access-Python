liczby = [1, 2, 3, 4, 5, 6]
kwadraty_liczb = map(lambda x: x * x, liczby)
print(list(kwadraty_liczb))

liczby_odwrotne = map(lambda x: 1 /x, liczby)
print(list(liczby_odwrotne))

liczby_ozwekszone_o_10 = map(lambda x: x + 10, liczby)
print(list(liczby_ozwekszone_o_10))

liczby_parzyste = filter(lambda x: x % 2 == 0, liczby)
print(list(liczby_parzyste))