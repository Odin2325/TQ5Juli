from random import *
wuerfel1 = randint(1,6)
wuerfel2 = randint(1,6)
wuerfel3 = randint(1,6)



print(f"Wurf: {wuerfel1} + {wuerfel2} + {wuerfel3} = {wuerfel1 + wuerfel2 + wuerfel3}")
bonuspunkte = 0
if wuerfel1 == wuerfel2 == wuerfel3:
    bonuspunkte = 6
    print(f"Dreierpasch! +{bonuspunkte} Bonuspunkte!")
elif wuerfel1 == wuerfel2 or wuerfel1 == wuerfel3 or wuerfel2 == wuerfel3:
    bonuspunkte = 2
    print(f"Zweierpasch! +{bonuspunkte} Bonuspunkte!")

if wuerfel1 + wuerfel2 + wuerfel3 + bonuspunkte >= 16:
    print("Herzlichen Glückwunsch, Du hast ein Auto gewonnen!")
elif wuerfel1 + wuerfel2 + wuerfel3 + bonuspunkte >= 10:
    print("Herzlichen Glückwunsch, Du hast einen Laptop gewonnen!")
elif wuerfel1 + wuerfel2 + wuerfel3 + bonuspunkte == 7:
    print("Herzlichen Glückwunsch, Du hast eine Reise gewonnen!")
else:
    print("Du hast leider verloren, Als Trostpreis erhältst Du ein Katzenbild! Aber runterladen musst Du es selbst.")