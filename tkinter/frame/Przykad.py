import tkinter
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("250x200")

ramka = ttk.Frame(borderwidth=1, relief=SOLID,  width=100, height=100, padding=10)
lbl = ttk.Label(ramka, text="Witaj w mojej aplikacji")
lbl.pack()
ramka.pack()

root.mainloop()
