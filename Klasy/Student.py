class Student:
    def __init__(self, name, age, major):
        # Fields
        self.name = name
        self.age = age
        self.major = major
        self.grades = {}  # Słownik do przechowywania ocen przedmiotów

    def enroll_subject(self, subject_name):
        # Metoda zapisania się na nowy przedmiot
        if subject_name not in self.grades:
            self.grades[subject_name] = None
            print(f"{self.name} has enrolled in the {subject_name} course.")
        else:
            print(f"{self.name} is already enrolled in {subject_name}.")

    def submit_grade(self, subject_name, grade):
        # Metoda przesyłania oceny za przedmiot
        if subject_name in self.grades:
            self.grades[subject_name] = grade
            print(f"{self.name} has submitted a grade of {grade} for {subject_name}.")
        else:
            print(f"{self.name} is not enrolled in {subject_name}. Enroll first.")

    def get_average_grade(self):
        # Inicjujemy zmienną, która będzie przechowywać sumę wszystkich ocen
        total = 0
        # Zmienna do przechowywania liczby ważnych ocen
        count = 0

        # Przechodzimy przez każdą ocenę w słowniku ocen
        for grade in self.grades.values():
            # Sprawdzamy, czy ocena nie jest None (czyli czy istnieje)
            if grade is not None:
                # Dodajemy ocenę do sumy
                total += grade
                # Zwiększamy licznik ważnych ocen
                count += 1

        # Sprawdzamy, czy znaleźliśmy jakiekolwiek ważne oceny
        if count > 0:
            # Obliczamy średnią
            average_grade = total / count
            # Zaokrąglamy średnią do dwóch miejsc po przecinku i zwracamy ją
            return round(average_grade, 2)
        else:
            # Jeśli nie znaleźliśmy ważnych ocen, zwracamy odpowiedni komunikat
            return "No grades available."

