class LicznikObiektow:
    num_instances = 0

    def __init__(self):
        LicznikObiektow.num_instances += 1



obiekt1 = LicznikObiektow()
obiekt2 = LicznikObiektow()
obiekt3 = LicznikObiektow()

print(obiekt2.num_instances)
print(obiekt1.num_instances)

print(LicznikObiektow.num_instances)

print(type(obiekt1))