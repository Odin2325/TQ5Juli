def show_employee_menu():
    """
    Zeigt das Mitarbeiter-Menü an und gibt die Benutzerauswahl zurück.
    """
    print("\n===== Mitarbeiter Menü =====")
    print("1. Alle Fahrzeuge anzeigen")
    print("2. Neues Fahrzeug hinzufügen")
    print("3. Fahrzeugstatus ändern (Available/Rented/Maintenance)")
    print("4. Alle aktiven Vermietungen anzeigen")
    print("5. Logout")
    print("============================\n")

    choice = input("Wählen Sie eine Option: ")
    return choice