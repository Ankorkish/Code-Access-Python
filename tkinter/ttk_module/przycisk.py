import tkinter as tk
from tkinter import ttk

def kliknij_mnie():
    root.title("Kliknięto przycisk")

root = tk.Tk()
root.title("Przycis ttk")
root.geometry("300x400")

button = ttk.Button(root, text="kliknij mnie!", command=kliknij_mnie)
button.pack()

root.mainloop()