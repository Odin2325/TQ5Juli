namen = []
noten = []

# Anzahl der Schüler abfragen
schuelerzahl = int(input("Gib die Anzahl der Schüler der Klasse ein: "))
print(f"Die Klasse besteht aus {schuelerzahl} Schülern.")  # Ausgabe der Klassegröße

# Eingabe von Namen und Noten
for schueler in range(schuelerzahl):  # Schleife für Eingaben in Anzahl schuelerzahl
    name = input(f"Gib den Namen des Schülers {schueler+1} ein: ").capitalize()  # Namen in Großbuchstaben umwandeln
    namen.append(name)
    while True:  # Eingabevalidierung für Note
        note = int(input(f"Gib die Note für {namen[schueler]} ein (1-6): "))
        if 1 <= note <= 6:
            noten.append(note)
            break  # Schleife verlassen, wenn die Note gültig ist
        else:
            print("Ungültige Note. Bitte gib eine Note zwischen 1 und 6 ein.")

# Ausgabe der Schüler und ihrer Noten
print("\nDie Notenverteilung der Klasse:")
for schueler in range(schuelerzahl):
    print(f"{namen[schueler]} hat die Note {noten[schueler]}")  # Ausgabe der Schüler und ihrer Noten

# Durchschnittsnote berechnen
notendurchschnitt = sum(noten) / schuelerzahl if schuelerzahl > 0 else 0  # Durchschnittsnote
print(f"\nDie Durchschnittsnote der Klasse ist: {notendurchschnitt:.2f}")  # Ausgabe der Durchschnittsnote

# Beste Note der Klasse
beste_note = min(noten)  
beste_schueler = [namen[schueler] for schueler in range(schuelerzahl) if noten[schueler] == beste_note] 
print(f"Beste Note: {beste_note}, erzielt von: {', '.join(beste_schueler)}")

# Schlechteste Note der Klasse
schlechteste_note = max(noten)  
schlechteste_schueler = [namen[schueler] for schueler in range(schuelerzahl) if noten[schueler] == schlechteste_note] 
print(f"Schlechteste Note: {schlechteste_note}, erzielt von: {', '.join(schlechteste_schueler)}")