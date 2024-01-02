try:
    kwota = 3999
    if kwota < 2999:
        raise ValueError("proszę dodać pieniądze do swojego konta")
    else:
        print("Jesteś uprawniony do zakupu kursu")
except ValueError as e:
    print(e)
