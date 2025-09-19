def show_main_menu():
    """Zeigt das Hauptmenü an und gibt die Benutzereingabe zurück."""
    print("\n===== Hauptmenü =====")
    print("1. Benutzerverwaltung")
    print("2. Fahrzeugverwaltung")
    print("3. Vermietungen")
    print("4. Abmelden")
    print("=======================\n")
    
    choice = input("Wählen Sie eine Option: ")
    return choice