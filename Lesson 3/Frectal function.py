def fractal(x): #silnia 5! = 5 * 4 * 3 * 2 * 1
    if x == 1:
        return 1
    else:
        print(x)
        return x * fractal(x - 1)

fractal(x)