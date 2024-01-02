"""Zbiór zawiera jeden lub więcej elementów,
które niekoniecznie są tego samego typu,
oddzielone przecinkiem i zamknięte w nawiasach
klamrowych {}. Poniżej zdefiniowano zbiór zawierający
liczby parzyste
"""

even_nums = {2, 4, 6, 8, 10}  # zbiór liczb parzystych
emp = {1, 'Steve', 10.5, True}  # zbiór różnych obiektów

"""Zbiór nie przechowuje zduplikowanych obiektów.
Nawet jeśli obiekt zostanie dodany więcej niż
jeden raz wewnątrz nawiasów klamrowych, tylko jedna kopia
jest przechowywana w obiekcie set. W związku z tym operacje
indeksowania i wycinania nie mogą być wykonywane
na obiekcie set.
"""