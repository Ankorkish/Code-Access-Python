import tkinter as tk

# Tworzenie głównego okna
root = tk.Tk()
root.title("Etykieta i przyciski")

# Tworzenie etykiety
label = tk.Label(root, text="Witaj w Tkinter!")
label.pack()  # Domyślne ustawienie, wyrównane do środka

# Tworzenie i pakowanie przycisków
button_accept = tk.Button(root, text="Akceptuj")
button_accept.pack()  # Domyślne ustawienie, wyrównane do środka

button_cancel = tk.Button(root, text="Anuluj")
button_cancel.pack()  # Domyślne ustawienie, wyrównane do środka

# Uruchomienie głównej pętli
root.mainloop()
