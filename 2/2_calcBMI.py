weight = input("Podaj wagę")
growth = input("Podaj wzrost") # trzeba zamienić na metry


bmi = float(weight) / ((float(growth) / 100) ** 2)



if bmi < 18.5:
    print("Niedowaga")
elif bmi < 25:
    print("waga prawidłowa")
elif bmi < 30:
    print("nadwaga")
else:
    print("otyłość")

print(bmi)