"""
Cel Zadania:

Zaprojektuj klasę bazową Animals oraz dwie klasy dziedziczące po niej.
Twoim zadaniem jest stworzenie hierarchii klas, które odzwierciedlają wspólne
cechy oraz unikalne zachowania różnych gatunków zwierząt.
Klasa Bazowa - Animals:

Zdefiniuj klasę Animals zawierającą podstawowe cechy i zachowania, które są wspólne dla wszystkich zwierząt.
W metodzie __init__(), zainicjuj atrybuty takie jak name (imię) i age (wiek).
Dodaj metody, takie jak eat() i sleep(), które będą reprezentować podstawowe działania zwierząt.
Pierwsza Klasa Dziedzicząca - Wybrany Gatunek Zwierzęcia:

Stwórz pierwszą klasę dziedziczącą po Animals, np. Birds lub Mammals.
Ta klasa powinna zawierać dodatkowe atrybuty i metody specyficzne dla wybranego gatunku.
Na przykład, klasa Birds może zawierać metodę fly() oraz dodatkowy atrybut wing_span (rozpiętość skrzydeł).
Druga Klasa Dziedzicząca - Inny Gatunek Zwierzęcia:

Utwórz drugą klasę dziedziczącą, która reprezentuje inny gatunek zwierząt niż pierwsza klasa.
Na przykład, jeśli pierwszą klasą jest Birds, drugą może być Fish.
Ta klasa powinna mieć unikalne atrybuty i metody, które są charakterystyczne dla jej gatunku.
Dla Fish mogą to być metody takie jak swim() oraz atrybuty typu gill_type (typ skrzeli).
Implementacja i Testowanie:

Utwórz instancje każdej klasy i zademonstruj, jak można używać zarówno wspólnych,
jak i unikalnych metod i atrybutów każdej z klas.
Przetestuj swoje klasy, tworząc różne obiekty, na przykład sparrow
(wróbel) jako obiekt klasy Birds i goldfish (złota rybka) jako obiekt klasy Fish.
Wywołaj na nich metody dziedziczone i specyficzne dla każdej z klas.
Rozważania Dotyczące Dziedziczenia:

Zastanów się nad tym, jak dziedziczenie i polimorfizm są używane w Twoim projekcie, i opisz,
jak te koncepcje pomagają zorganizować kod w bardziej modularny i czytelny sposób.
"""