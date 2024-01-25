def zarobki(pracownik1 ,pracownik2, pracownik3):
    listaPracownikow = [pracownik1, pracownik2, pracownik3]
    return max(listaPracownikow) - min(listaPracownikow)

x, y, z = map(int, input().split())

print(zarobki(x, y, z))