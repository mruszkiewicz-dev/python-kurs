questions = [
    ("Stolica Polski to?", "Warszawa", 2),
    ("Ile to 5 + 7?", "12", 1),
    ("Jaki język programowania używa się w Django?", "Python", 2),
    ("Czy 15 to liczba pierwsza? (tak/nie)", "nie", 1),
    ("Który kontynent ma najwięcej państw?", "Afryka", 2),
    ("Jakie jest rozszerzenie pliku Pythona?", ".py", 1),
    ("Ile dni ma rok przestępny?", "366", 1),
    ("W którym roku był pierwszy człowiek na Księżycu?", "1969", 3)
]

pkt = 0

for q in questions:
   odp = input(q[0])
   if odp == q[1]:
       print(f"Dobrze zdobyłeś {q[2]} pkt.!")
       pkt += q[2]
   else:
       print("Zła odpowiedz")
       
print(f"Zdobyłeś {pkt} pkt")