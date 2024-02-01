def stworz_profil_uzytkownika(**informacje_uzytkownika):
    print("Profil użytkownika:")
    for klucz, wartosc in informacje_uzytkownika.items():
        print(f"{klucz}: {wartosc}")

stworz_profil_uzytkownika(imie="Anna", wiek=30, zawod="Inżynier")
