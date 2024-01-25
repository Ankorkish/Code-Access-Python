import tkinter as tk
from PIL import Image,ImageTk


okno = tk.Tk()
okno.title("Moja Aplikacja Tkinter")
okno.geometry("500x500")


obraz = Image.open(r"C:/AndriiKorkishko/CA_Python_1/tkinter/Images/img.jpg")
obraz_tk = ImageTk.PhotoImage(obraz)

etykieta = tk.Label(okno, image=obraz_tk)
etykieta.pack()

okno.mainloop()