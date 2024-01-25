import tkinter as tk

# Tworzenie głównego okna
root = tk.Tk()
root.title("Przykład side w Tkinter")

# Tworzenie przycisków z różnymi ustawieniami side
button_top = tk.Button(root, text="Na górze", bg="lightblue")
button_top.pack(side='top')

button_bottom = tk.Button(root, text="Na dole", bg="lightgreen")
button_bottom.pack(side='bottom')

button_left = tk.Button(root, text="Po lewej", bg="lightgrey")
button_left.pack(side='left')

button_right = tk.Button(root, text="Po prawej", bg="lightpink")
button_right.pack(side='right')

# Uruchomienie głównej pętli
root.mainloop()
