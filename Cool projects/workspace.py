import random


class Quiz:
    def __init__(self):
        self.pytania_i_odpowiedzi = [
            {"pytanie": "Stolica Polski to:", "odpowiedz": "Warszawa"},
            {"pytanie": "Ile nóg ma pająk?", "odpowiedz": "8"},
            {"pytanie": "Najdłuższa rzeka na świecie to:", "odpowiedz": "Nil"}
        ]
        self.punkty = 0

        random.shuffle(self.pytania_i_odpowiedzi)

        print(self.pytania_i_odpowiedzi[0]["pytanie"])

    def rozpocznij_quiz(self):
        print("Rozpoczynamy dzisiejszą grę w Milionerów!")
        print("TUTUTUTUTUTU (Muzyka)")
        for runda in self.pytania_i_odpowiedzi:
            print(runda["pytanie"] + " ")
            if input().lower() == runda["odpowiedz"].lower():
                print("Gratuluję, odpowiedź poprawna")
                self.punkty += 1
            else:
                print("Niestety przegrana.")
        print(f"Twoje punkty: {self.punkty}")

lista = [112, 12, 23, 3]

for i in lista:
    print(i)


# Użycie klasy
quiz = Quiz()
quiz.rozpocznij_quiz()