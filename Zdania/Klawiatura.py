def nastepna_litera_na_klawiaturze(litera):
    klawiatura = "qwertyuiopasdfghjklzxcvbnm"

    index = klawiatura.find(litera)

    index += 1

    if index == len(klawiatura):
        index = 0

    return klawiatura[index]

print(nastepna_litera_na_klawiaturze("a"))  # Powinno zwrócić "s"
print(nastepna_litera_na_klawiaturze("p"))  # Powinno zwrócić "a"
print(nastepna_litera_na_klawiaturze("m"))  # Powinno zwrócić "q"
