class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.costam = "waeqwe"
        self.dsasdas = 12

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        return area

cr_1 = Circle(12)

print(cr_1.calculate_area())

cr_1.radius = 40

print(cr_1.calculate_area())

circle_2 = Circle(10)

print(cr_1.calculate_area())

circle_2.radius = 40

print(cr_1.calculate_area())