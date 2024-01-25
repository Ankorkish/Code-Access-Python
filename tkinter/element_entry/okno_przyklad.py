import tkinter as tk

okno = tk.Tk()
okno.title("Moja Aplikacja Tkinter")

etykieta = tk.Label(okno, text="Witaj w Tkinter")
etykieta.pack()

okno.mainloop()