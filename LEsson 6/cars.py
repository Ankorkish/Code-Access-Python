ev_data = [['Pojazd', 'Zasięg', 'Cena'],
           ['Tesla Model 3 LR', '310', '49900'],
           ['Hyundai Ioniq EV', '124', '30315'],
           ['Chevy Bolt', '238', '36620']]
for row in ev_data[1:]:
    ev_range = row[1]
    ev_range = int(ev_range)
    row[1] = ev_range

    ev_price = row[2]
    ev_price = int(ev_price)
    row[2] = ev_price

total_range = 0
count = len(ev_data[1:])

for row in ev_data[1:]:
    total_range += row[1]

lista_samochodow_dlogiego_zasiegu = []

for row in ev_data[1:]:

    zasieg_samochodu = row[1]
    if zasieg_samochodu > 200:
        lista_samochodow_dlogiego_zasiegu.append(row)
    if row[0] == "Hyundai Ioniq EV":
        break

lista_samochodow_krotkiego_zasiegu = []

for row in ev_data[1:]:
    zasieg_samochodu = row[1]
    if zasieg_samochodu > 200:
        continue
    lista_samochodow_krotkiego_zasiegu.append(row)


print(lista_samochodow_krotkiego_zasiegu)