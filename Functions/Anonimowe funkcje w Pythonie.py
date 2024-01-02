def szescian(x):
    return x*x*x

szescian_v2  = lambda x : x*x*x


print(szescian(5))

liczby = [1, 2, 3, 4, 5]
podwojone = map(szescian_v2, liczby)
print(list(podwojone))