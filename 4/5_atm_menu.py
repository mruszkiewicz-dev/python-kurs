import random

balance = 100  # lub: round(random.uniform(1, 100000), 2)

while True:
    user_choice = input("""
Wybierz opcję:
1. Sprawdź saldo
2. Wpłać
3. Wypłać
4. Wyjście
Twój wybór: """)

    match user_choice:
        case "1":
            print(f"Twoje saldo: {balance:.2f} zł")
        case "2":
            add_balance = float(input("Podaj kwotę do wpłaty: "))
            balance += add_balance
            print(f"Wpłacono {add_balance:.2f} zł. Saldo: {balance:.2f} zł")
        case "3":
            subtract_balance = float(input("Podaj kwotę do wypłaty: "))
            if subtract_balance <= balance:
                balance -= subtract_balance
                print(f"Wypłacono {subtract_balance:.2f} zł. Saldo: {balance:.2f} zł")
            else:
                print("Nie masz tylu środków.")
        case "4":
            print("Do widzenia!")
            break
        case _:
            print("Nieznana opcja, spróbuj ponownie.")
