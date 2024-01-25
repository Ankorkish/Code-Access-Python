import tkinter as tk

# Tworzenie głównego okna
root = tk.Tk()
root.title("Przykład fill w Tkinter")

# Tworzenie widgetów
button1 = tk.Button(root, text="Nie rozciąga się", bg="lightgrey")
button1.pack(fill='none')

button2 = tk.Button(root, text="Rozciąga się w poziomie", bg="lightblue")
button2.pack(fill='x')

button3 = tk.Button(root, text="Rozciąga się w pionie", bg="lightgreen")
button3.pack(fill='y')

button4 = tk.Button(root, text="Rozciąga się w obu kierunkach", bg="lightpink")
button4.pack(fill='both', expand=True)

# Uruchomienie głównej pętli
root.mainloop()
