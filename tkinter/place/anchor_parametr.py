import tkinter as tk

# Tworzenie głównego okna
root = tk.Tk()
root.geometry("300x200")
root.title("Przykład anchor w Tkinter")

# Tworzenie i umieszczanie przycisków z różnymi ustawieniami anchor
button_n = tk.Button(root, text="Góra (N)", bg="lightblue")
button_n.pack(anchor='n')

button_e = tk.Button(root, text="Prawo (E)", bg="lightgrey")
button_e.pack(anchor='e')

button_w = tk.Button(root, text="Lewo (W)", bg="lightpink")
button_w.pack(anchor='w')

button_center = tk.Button(root, text="Centrum (C)", bg="lightyellow")
button_center.pack(anchor='center')

button_s = tk.Button(root, text="Dół (S)", bg="lightgreen")
button_s.pack(anchor='s')


# Uruchomienie głównej pętli
root.mainloop()