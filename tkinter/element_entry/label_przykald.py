import tkinter as tk


def funkcja_klikniencia():
    okno.destroy()



okno = tk.Tk()
okno.title("Moja Aplikacja Tkinter")
okno.geometry("400x300")


etykieta = tk.Label(okno, text="Witaj w Tkinter")
etykieta.pack()

przycisk = tk.Button(okno, text="Kliknij mnie!", command=funkcja_klikniencia)
przycisk.pack()

okno.mainloop()