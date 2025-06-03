n = int(input("Podaj liczbę: "))

if n > 0:
    total = 0
    for i in range(1,n+1):
        if n % i == 0:
            print(i)  
            total += 1
    print(f"liczba {n} ma {total} podzielników")        
else:
    print("liczba nie jest wieksza od 0!")
