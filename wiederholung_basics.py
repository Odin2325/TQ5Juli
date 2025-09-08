# E - Eingabe
# age = int(input("Gib Dein Alter ein: ")) #Casting zu int, float möglich
# V - Verarbeitung
# if age < 10: #Verarbeitung
#     print("Du bist ein Kind.") #Ausgabe
# elif age < 18:
#     print("Du bist Jugendlich.")
# else:
#     print("Du bist volljährig.") #Ausgabe

# if age >= 18:
#     print("Du bist volljährig.") #Ausgabe
# elif age > 10:
#     print("Du bist Jugendlich.")   
# else:
#     print("Du bist ein Kind.")


# Schleife: feste Anzahl an Wiederholungen
for i in range(5):              # 0, 1, 2, 3, 4
    print("Hallo Welt!")


# Bedingungsgesteuerte Schleife
age = 0
while age < 3:
    print("Du bist noch nicht volljährig.")
    age += 1                    # age = age + 1


# Aufgabe: Es soll ein Bereich von 0 bis 15 durchlaufen werden.
# Währenddessen soll überprüft werden, ob die aktuelle Zahl durch 3 teilbar ist.
# Wenn ja, soll "Fizz" ausgegeben werden.
# Wenn nein, soll die Zahl ausgegeben werden.

for zahl in range(16):          # 0, 1, 2, ..., 15
    if zahl % 3 == 0:           # Überprüfung auf Teilbarkeit durch 3
        print("Fizz")
    else:
        print(zahl)