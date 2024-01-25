def podziel(x, y):
    try:
        # Dzielenie całkowite: zwraca tylko część całkowitą wyniku
        print("Try block")
        print("Try block")
        wynik = x // y
        print("Try block")
        print("Try block")
        print("Tak! Twoja odpowiedź to:", wynik)
    except ZeroDivisionError:
        print("Przepraszamy! Dzielenie przez zero")
    else:
        print("No error!")

podziel(10, 0)

print("Hello!")