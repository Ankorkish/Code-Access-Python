"""
Zadanie: Napisz program w języku Python, który używa pętli while do wykonywania następujących czynności:
1.	Inicjalizuje zmienną n wartością 1.
2.	Uruchamia pętlę while, która ma się wykonywać dopóki wartość zmiennej n jest mniejsza niż 5.
3.	W każdej iteracji pętli wypisuje na ekranie tekst "Hello Pythonista".
4.	Po wypisaniu tekstu, zwiększa wartość zmiennej n o 1.
5.	Sprawdza, czy wartość zmiennej n osiągnęła 3. Jeśli tak, używa instrukcji break do natychmiastowego zakończenia pętli.
"""
n = 1

while n < 5:
    print("Hello Pythonista")
    n = n + 1
    
