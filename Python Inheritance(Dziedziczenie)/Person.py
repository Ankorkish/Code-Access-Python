class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        print(f"{self.first_name} {self.last_name} is talking.")

    def walk(self):
        print(f"{self.first_name} {self.last_name} is walking.")

# Klasa Student dziedziczy po klasie Person
class Student(Person):
    def study(self):
        print(f"{self.first_name} {self.last_name} is studying.")

# Klasa GraduateStudent dziedziczy po klasie Person
class GraduateStudent(Student):
    def research(self, topic):
        print(f"The graduate student is researching {topic}.")

class Professor(Person):
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subject = subject

    def talk(self):
        print(f"{self.first_name} {self.last_name} is lecturing on {self.subject}.")

# Przykładowe użycie
alice = Student("Alice", "Nowak")
print(alice.first_name + " " + alice.last_name)
alice.walk()
alice.talk()

bob = GraduateStudent("Bob", "Kowalski")
print(bob.first_name + " " + bob.last_name)
bob.walk()
bob.talk()
bob.research("artificial intelligence")

dr_williams = Professor("John", "Williams", "Physics")
print(dr_williams.first_name + " " + dr_williams.last_name)
dr_williams.walk()  # Metoda odziedziczona z klasy Person
dr_williams.talk()  # Nadpisana metoda z klasy Professor