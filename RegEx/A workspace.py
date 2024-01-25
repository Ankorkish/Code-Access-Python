globalna_zminna = [1, 2, 3, 4]

def sprawdz_tozsamosc(obiket):
    return obiket is globalna_zminna

testowy_obiekt = [1, 2, 3, 4]

print(sprawdz_tozsamosc(globalna_zminna))