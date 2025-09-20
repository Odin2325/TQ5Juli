class MainMenuView:
    def get_login_input(self):
        username = input("Benutzername: ")
        password = input("Passwort: ")
        return username, password

    def show_login_success(self, user):
        print(f"✅ Willkommen {user['Username']}! Rolle: {user['Role']}")

    def show_login_failure(self):
        print("❌ Login fehlgeschlagen. Bitte überprüfe Benutzername oder Passwort.")
