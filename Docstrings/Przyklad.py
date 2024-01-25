def pomnoz_liczby(a, b):
    """
    Mnoży dwie liczby i zwraca wynik.

    Args:
        a (int): Pierwsza liczba do mnożenia.
        b (int): Druga liczba do mnożenia.

    Returns:
        int: Iloczyn dwóch liczb.
    """
    if a < 0 or b < 0:
        raise ValueError("Jedna z liczb jest ujemna.")
    return a * b

help(pomnoz_liczby)


pomnoz_liczby(2, 3)

