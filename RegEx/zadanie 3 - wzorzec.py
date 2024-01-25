import re

wzorzec = re.compile("Python")

teksty = ["Uczę się Pythona.", "Python jest wszechstronny.", "To nie jest język programowania."]
for tekst in teksty:
    if wzorzec.search(tekst):
        print(f"W tekście '{tekst}' znaleziono słowo 'Python'.")
    else:
        print(f"W tekście '{tekst}' nie znaleziono słowa 'Python'.")
