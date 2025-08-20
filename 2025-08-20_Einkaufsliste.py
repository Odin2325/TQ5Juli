# Leere Liste für die Einkäufe
einkaufs_liste = []

print("Gib deine Produkte ein. Wenn du fertig bist, schreibe 'Fertig'.")

while True:
    eingabe = input("Produkt hinzufügen: ").capitalize()
    
    if eingabe == "Fertig":  # Abbruchbedingung
        break
    
    einkaufs_liste.append(eingabe)  # Produkt zur Liste hinzufügen

print("\nEinkaufsliste:")
for item in einkaufs_liste:
    print("-", item)