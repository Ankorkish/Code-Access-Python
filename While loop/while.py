# Program w Pythonie demonstrujący
# pętlę while-else

i = 0
while i < 4:
    i += 1
    print(i)
else:  # Wykonane, ponieważ nie ma break w pętli
    print("Brak Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Nie wykonane, ponieważ jest break
    print("Brak Break")
