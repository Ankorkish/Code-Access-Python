import tkinter as tk
import tkinter.ttk as ttk

def pokaz_tekst():
    #entry.delete(0, len(entry.get()))
    entry.insert(0, "Hello world!")
    #print("Wprowadzony tekst:", tekst)

root = tk.Tk()

entry = ttk.Entry(root)
entry.pack()

button = tk.Button(root, text="Wyświetl tekst", command=pokaz_tekst)
button.pack()

root.mainloop()
