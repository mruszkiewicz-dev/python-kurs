'''Zadanie: Gra w zgadywanie liczby
Program losuje tajną liczbę z zakresu 1–100 (użyj import random i random.randint(1, 100)).

Użytkownik ma zgadywać liczbę, dopóki nie trafi.

Po każdej próbie program podpowiada:

Too low! – jeśli liczba jest za mała

Too high! – jeśli za duża

Correct! – jeśli trafiona

Program liczy liczbę prób i wypisuje ją na końcu.'''

import random 

num = random.randint(1, 100)

print(num)

total = 0
while True:
    n = int(input("Podaj liczbę: "))
    total += 1
    if n < num:
        print("Za mała!")
        continue
    elif n > num:
        print("Za duzą")
        continue
    elif n == num:
        print(f"Trafiłeś po {total} probach")
        break 

