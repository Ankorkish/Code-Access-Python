import tkinter as tk

okno = tk.Tk()
okno.title("Moja Aplikacja Tkinter")
okno.geometry("400x300")

etykieta = tk.Label(okno, text="Witaj w Tkinter", font=("Times New Roman", 14, "italic"), underline=1)
etykieta.pack()

okno.mainloop()