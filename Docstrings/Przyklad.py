def pomnoz_liczby(a, b):
    """
    Mnoży dwie liczby i zwraca wynik.

    Args:
        a (int): Pierwsza liczba do mnożenia.
        b (int): Druga liczba do mnożenia.

    Returns:
        int: Iloczyn dwóch liczb.

    Raises:
        ValueError: Jeśli jedna z liczb jest ujemna.

    Examples:
        >>> pomnoz_liczby(3, 4)
        12
    """
    if a < 0 or b < 0:
        raise ValueError("Jedna z liczb jest ujemna.")
    return a * b

pomnoz_liczby(12, 12)
print()