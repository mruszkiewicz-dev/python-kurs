n = int(input("Podaj liczbę: "))

if n > 0:
    total = 0
    for i in range(n, 0, -2):
        total += i
    print(total)
else:
    print("liczba nie jest większa od zera!")