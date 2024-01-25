class Quiz:
    def __init__(self):
        self.pytania_i_odpowiedzi = [
            {"pytanie": "Stolica Polski to:", "odpowiedz": "Warszawa"},
            {"pytanie": "Ile nóg ma pająk?", "odpowiedz": "8"},
            {"pytanie": "Najdłuższa rzeka na świecie to:", "odpowiedz": "Nil"}
        ]
        self.punkty = 0

    def rozpocznij_quiz(self):
        for pytanie in self.pytania_i_odpowiedzi:
            odpowiedz_uzytkownika = input(pytanie["pytanie"] + " ")
            if odpowiedz_uzytkownika.strip().lower() == pytanie["odpowiedz"].lower():
                print("Dobrze!")
                self.punkty += 1
            else:
                print("Źle! Poprawna odpowiedź to:", pytanie["odpowiedz"])
        print(f"Koniec quizu! Zdobyłeś/aś {self.punkty} punkt(ów) na {len(self.pytania_i_odpowiedzi)}.")

# Użycie klasy
quiz = Quiz()
quiz.rozpocznij_quiz()
