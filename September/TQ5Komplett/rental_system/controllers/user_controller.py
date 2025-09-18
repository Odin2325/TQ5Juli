# controllers/user_controller.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importiere Funktionen aus dem Model
from models.user_model import get_login

# Importiere die Menüfunktionen aus der View
from views.main_menu import show_main_menu
from views.customer_view import show_customer_menu
from views.employee_view import show_employee_menu

# Definiere Funktionen zur Steuerung der Benutzeroberfläche
# Dies ist das "geheime" Menü für Administratoren
def manage_users():
    print("\n===== Benutzerverwaltung =====")
    # ... hier kommt die Logik für das Benutzerverwaltungsmenü ...
    pass

def handle_login():
    """Steuert den Anmeldeprozess und leitet zum Menü weiter."""
    print("===== LOGIN =====")
    username = input("Benutzername: ")
    password = input("Passwort: ")

    # Nutze deine get_login-Funktion
    user = get_login(username, password)
    
    if user:
        print(f"\nLogin erfolgreich! Willkommen, {user[1]}!")
        
        # Zeige das entsprechende Menü basierend auf der Rolle
        if user[3] == "Employee":
            show_employee_menu() # Sie können diese Funktion in employee_view.py definieren
        elif user[3] == "Customer":
            show_customer_menu() # Sie können diese Funktion in customer_view.py definieren
        
    else:
        print("\nLogin fehlgeschlagen. Ungültige Anmeldedaten.")

# Dieser Block ist für direkte Tests
if __name__ == "__main__":
    handle_login()