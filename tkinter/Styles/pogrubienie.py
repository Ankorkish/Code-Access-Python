import tkinter as tk
import tkinter.font as font

okno = tk.Tk()
okno.title("Moja Aplikacja Tkinter")
okno.geometry("400x300")

l = tk.Label(text="Hello, world")
l.pack()
# clone the font, set the underline attribute,
# and assign it to our widget
f = font.Font(l, l.cget("font"))
f.configure(underline = True)
l.configure(font=f)

okno.mainloop()