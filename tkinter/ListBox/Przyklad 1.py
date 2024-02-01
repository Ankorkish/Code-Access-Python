from tkinter import Tk, Label, Entry, Button

def wyslij_formularz():
    print(f"Imię: {imie_entry.get()}")
    print(f"Nazwisko: {nazwisko_entry.get()}")

root = Tk()
root.title("Formularz danych osobowych")
root.geometry("300x150")

# Konfiguracja siatki
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

root.rowconfigure(2, weight=1)

# Etykiety i pola tekstowe
Label(root, text="Imię:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
imie_entry = Entry(root)
imie_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

Label(root, text="Nazwisko:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
nazwisko_entry = Entry(root)
nazwisko_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Przycisk
Button(root, text="Wyślij", command=wyslij_formularz).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="s")

root.mainloop()
