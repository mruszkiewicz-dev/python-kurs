l =[]
for i in range(5):
   l.append(int(input(f"Podaj {i +1} liczbę ")))
   
l.sort()

suma = sum(l)
    
ave = suma / len(l)

print(f"Suma: {suma}, Średnia {ave}, Najwieksza {l[-1]} ,Najmiejsza {l[0]}" )