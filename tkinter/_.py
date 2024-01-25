from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("250x200")

enabled = IntVar()

enabled_checkbutton = ttk.Checkbutton(text="Włącz", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)

enabled_label = ttk.Label(textvariable=enabled)
enabled_label.pack(padx=6, pady=6, anchor=NW)

enabled_label2 = ttk.Label(textvariable=enabled)
enabled_label2.pack(padx=6, pady=6, anchor=NW)

enabled_label1 = ttk.Label(textvariable=enabled)
enabled_label1.pack(padx=6, pady=6, anchor=NW)

root.mainloop()