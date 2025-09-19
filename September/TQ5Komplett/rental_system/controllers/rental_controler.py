import sys
import os

# Füge das übergeordnete Verzeichnis zum Pfad hinzu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.rental_model import get_active_rentals, rent_vehicle, return_vehicle
from views.employee_view import show_employee_menu

def handle_rental_management():
    """
    Steuert die Vermietungsverwaltung für Mitarbeiter und Kunden.
    """
    while True:
        choice = show_employee_menu() # Oder show_customer_menu()

        if choice == '3':
            # Logik zum Ändern des Fahrzeugstatus
            pass
        elif choice == '4':
            active_rentals = get_active_rentals()
            # Logik zur Anzeige aktiver Vermietungen
            print("Aktive Vermietungen:")
            for rental in active_rentals:
                print(rental)

        elif choice == '5':
            print("Zurück zum Hauptmenü...")
            break
        
        else:
            print("Ungültige Eingabe.")