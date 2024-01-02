def podziel(x, y):
    try:
        # Dzielenie całkowite: zwraca tylko część całkowitą wyniku
        wynik = x // y
        print("Tak! Twoja odpowiedź to:", wynik)
    except ZeroDivisionError:
        print("Przepraszamy! Dzielenie przez zero")
    except TypeError as e:
        print("błąd to:", e)
    except:
        print("Something went wrong!")
    else:
        print("Nie ma wyjątku!")

podziel(10, 0)

print("Hello!")