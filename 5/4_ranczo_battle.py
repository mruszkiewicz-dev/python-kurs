import random

#(nazwa_postaci, punkty_życia (HP), siła_ataku)


characters = [
    ("Paweł Kozioł (Wójt)", 100, 20),
    ("Piotr Kozioł (Ksiądz)", 110, 18),
    ("Lucy Wilska", 90, 22),
    ("Jakub 'Kusy' Sokołowski", 95, 19),
    ("Patryk Pietrek", 80, 25),
    ("Tadeusz Hadziuk", 85, 23),
    ("Maciej Solejuk", 120, 15),
    ("Halina Kozioł", 100, 20),
    ("Kazimiera Solejukowa", 90, 21),
    ("Arkadiusz Czerepach", 85, 24),
    ("Wioletka Kotecka", 75, 26),
    ("Klaudia Kozioł", 80, 22),
    ("Krystyna Więcławska", 95, 19),
    ("Fabian Duda", 90, 20),
    ("Mieczysław Wezół", 100, 18),
    ("Stacho Japycz", 110, 17),
    ("Ksiądz Robert", 105, 16),
    ("Ksiądz Maciej", 100, 18),
    ("Monika Korczab", 85, 23),
    ("Celina Hadziukowa", 95, 19),
    ("Czerepach", 70, 20)
]

fighter1, fighter2 = random.sample(characters, 2)

name1, hp1, atk1 = fighter1
name2, hp2, atk2 = fighter2

print(f"🎮 Walka: {name1} vs {name2}")

tura = 0

while hp1 > 0 and hp2 > 0:
    tura += 1
    print(f"Tura {tura}:")
    
    hp2 -= atk1
    hp1 -= atk2
    
    
    if hp1 <= 0:
        print(f"👉 {name2} atakuje za {atk2}, {name1} ma teraz {max(hp1, 0)} HP\n")
        print(f"🏆 Wygrał {name2}!")
    elif hp2 <= 0:
        print(f"👉 {name1} atakuje za {atk1}, {name2} ma teraz {max(hp2, 0)} HP")
        print(f"🏆 Wygrał {name1}!")
    else:
        print(f"👉 {name1} atakuje za {atk1}, {name2} ma teraz {max(hp2, 0)} HP")
        print(f"👉 {name2} atakuje za {atk2}, {name1} ma teraz {max(hp1, 0)} HP\n")
    
