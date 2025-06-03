fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
   print(i, fruits[i])    

for i, fruit in enumerate(fruits):
    print(f"index {i} = {fruit}")