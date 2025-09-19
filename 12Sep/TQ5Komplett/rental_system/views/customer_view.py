def show_customer_menu():
    """
    Zeigt das Kunden-Menü an und gibt die Benutzerauswahl zurück.
    """
    print("\n===== Kunden Menü =====")
    print("1. Verfügbare Fahrzeuge anzeigen")
    print("2. Fahrzeug mieten")
    print("3. Fahrzeug zurückgeben")
    print("4. Eigene Miet-Historie anzeigen")
    print("5. Logout")
    print("========================\n")
    
    choice = input("Wählen Sie eine Option: ")
    return choice