import sys
import os

# Füge das übergeordnete Verzeichnis zum Pfad hinzu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.vehicle_model import get_all_vehicles, add_vehicle
from views.employee_view import show_employee_menu

def handle_vehicle_management():
    """
    Steuert die Fahrzeugverwaltung für Mitarbeiter.
    """
    while True:
        choice = show_employee_menu() # Sie rufen das Menü von hier auf

        if choice == '1':
            vehicles = get_all_vehicles()
            # Hier kommt die Logik, um alle Fahrzeuge anzuzeigen
            print("Alle Fahrzeuge:")
            for vehicle in vehicles:
                print(vehicle)
        
        elif choice == '2':
            # Hier kommt die Logik, um ein neues Fahrzeug hinzuzufügen
            brand = input("Marke: ")
            model = input("Modell: ")
            color = input("Farbe: ")
            status = 'Available'
            add_vehicle(brand, model, color, status)

        elif choice == '5':
            print("Zurück zum Hauptmenü...")
            break
        
        else:
            print("Ungültige Eingabe.")