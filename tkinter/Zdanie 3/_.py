import tkinter as tk
from tkinter import *
from tkinter import ttk

def modyfikuj_liczbe(operacja):
    aktualna_liczba = liczba.get()
    if operacja == Dodawanie:
        aktualna_liczba += 1
    elif operacja == Odejmowanie:
        aktualna_liczba -= 1
    elif operacja == Mnożenie:
        aktualna_liczba *= 2
    elif operacja == Dzielenie:
        aktualna_liczba /= 2

root = tk.Tk()
root.title("Licznik - modyfikatoinator")

liczba = IntVar(value=0)

Dodawanie = tk.Button(root, fg="white", bg="green", variable=liczba, text="Dodaj 1", command=modyfikuj_liczbe)
Dodawanie.pack()
Odejmowanie = tk.Button(root, fg="white", bg="red", variable=liczba, text="Odejmij 1", command=modyfikuj_liczbe)
Odejmowanie.pack()
Mnożenie = tk.Button(root, fg="white", bg="black", variable=liczba, text="Podwój", command=modyfikuj_liczbe)
Mnożenie.pack()
Dzielenie = tk.Button(root, fg="black", bg="white", variable=liczba, text="Podziel na 2", command=modyfikuj_liczbe)
Dzielenie.pack()

etykieta = ttk.Label(root, textvariable=liczba)
etykieta.pack()

root.mainloop()