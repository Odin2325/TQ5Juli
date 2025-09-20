class MainMenuView:
    def get_login_input(self):
        username = input("Benutzername: ")
        password = input("Passwort: ")
        return username, password

    def show_login_success(self, user):
        print(f"✅ Willkommen {user['Username']}! Rolle: {user['Role']}")

    def show_login_failure(self):
        print("❌ Login fehlgeschlagen. Bitte überprüfe Benutzername oder Passwort.")

    def customer_menu(self):
        print("\n=== Kundenmenü ===")
        print("1. Mieten")
        print("2. Bestand ansehen")
        print("3. Exit")
        return input("Wähle eine Option: ")

    def employee_menu(self):
        print("\n=== Mitarbeitermenü ===")
        print("1. Mieten")
        print("2. Bestand ansehen")
        print("3. Fahrzeug hinzufügen")
        print("4. Preis bearbeiten")
        print("5. Exit")
        return input("Wähle eine Option: ")