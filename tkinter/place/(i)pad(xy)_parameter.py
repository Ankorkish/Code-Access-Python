import tkinter as tk

# Tworzenie głównego okna
root = tk.Tk()
root.title("Przykład padding w Tkinter")

# Tworzenie przycisku z wewnętrznym i zewnętrznym odstępem
button1 = tk.Button(root, text="Wewnętrzny odstęp", bg="lightblue")
button1.pack(ipadx=20, ipady=20)  # Wewnętrzny odstęp: 20x20

button2 = tk.Button(root, text="Zewnętrzny odstęp", bg="lightgreen")
button2.pack(padx=20, pady=20)  # Zewnętrzny odstęp: 20x20

# Uruchomienie głównej pętli
root.mainloop()
