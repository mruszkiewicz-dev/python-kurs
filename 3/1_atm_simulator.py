amount  = int(input("Jaką kwotę chcesz wypłacić: "))


if amount > 0 and amount % 10 == 0:
    for bill in [200, 100, 50, 10]:
        count = amount // bill
        amount = amount % bill
        if count > 0:
            print(f"{bill} PLN – {count} banknotów")
else:
    "Nieprawidłowa kwota!"  