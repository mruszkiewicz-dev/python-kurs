import random

cards = ["🍎", "🍌", "🍇", "🍓", "🍍", "🍉", "🍇", "🍓", "🍍", "🍉", "🍎", "🍌"]
random.shuffle(cards)

hidden_cards = cards.copy()

#zmiana na ?

for i in range(len(hidden_cards)):
    hidden_cards[i] = "?"

shot = []


while hidden_cards != cards:
    print(hidden_cards)

    for i in range(2):
        shot.append(int(input(f"Podaj {i + 1} strzał: ")))
    
    if cards[shot[0]] == cards[shot[1]]:
        print("Dobrze!!")
        hidden_cards[shot[0]] = cards[shot[0]]
        hidden_cards[shot[1]] = cards[shot[1]]
        shot.clear()
    else:
        print("Nie trafiłeś, graj dalej")  
          