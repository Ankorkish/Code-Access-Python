import random

liczba_losowa = random.random()
print(liczba_losowa)

liczba_losowa = random.randint(1, 12)
print(liczba_losowa)

wybrany_element =  random.choice(["jablko", "banan", "wisnia"])
print(wybrany_element)

lista =  ["jablko", "banan", "wisnia"]
random.shuffle(lista)
print(lista)

wybrane_elementy = random.sample(range(100), 10)
print(wybrane_elementy)

liczba_losowa =  random.uniform(1.5, 10.5)
print(liczba_losowa)