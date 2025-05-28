name = input("Podaj imię")
age = input("Podaj wiek")

print("Cześć " + name + " masz " + age + " lat!")

if int(age) <= 18:
    print("nie masz 18 lat")
else:
    print("jesteś pałnoletni")