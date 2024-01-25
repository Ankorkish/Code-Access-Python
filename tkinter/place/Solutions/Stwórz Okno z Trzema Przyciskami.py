import tkinter as tk

# Tworzenie głównego okna
root = tk.Tk()
root.title("Testowanie pack()")

# Tworzenie i pakowanie przycisków
button1 = tk.Button(root, text="Przycisk 1")
button1.pack(side='top', anchor='w')

button2 = tk.Button(root, text="Przycisk 2")
button2.pack(side='bottom', fill='x')

button3 = tk.Button(root, text="Przycisk 3")
button3.pack(side='right')

# Uruchomienie głównej pętli
root.mainloop()
