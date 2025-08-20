import random

held = 10
monster = 10
schaden_monster = 0
schaden_held = 0

while True:
    if held > 0 and monster > 0:
        # Angriff des Helden
        schaden_monster = random.randint(1,10)
        monster -= schaden_monster  # Zufälliger Schaden für das Monster
        print(f"Du hast dem Monster {schaden_monster} Schadenspunkte zugefügt! Es hat jetzt {monster} Lebenspunkte.")
        if monster > 0:
            # Angriff des Monsters
            schaden_held = random.randint(1, 10)
            held -= schaden_held  # Zufälliger Schaden für den Helden
            print(f"Das Monster hat Dir {schaden_held} Schadenspunkte zugefügt! Du hast jetzt {held} Lebenspunkte.")
        else:
            print("Das Monster ist besiegt! Du hast gewonnen!")
            break
    elif held <= 0:
        print("Du wurdest besiegt! Das Monster hat gewonnen.")
        break