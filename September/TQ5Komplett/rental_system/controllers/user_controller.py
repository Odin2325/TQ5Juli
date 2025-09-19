# controllers/user_controller.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importiere alle notwendigen Funktionen
from models.user_model import get_login
from models.vehicle_model import get_all_vehicles, add_vehicle, update_vehicle_status, get_available_vehicles
from models.rental_model import get_active_rentals, rent_vehicle, return_vehicle, get_user_rental_history
from views.customer_view import show_customer_menu
from views.employee_view import show_employee_menu

def handle_user_management(user_role, user_id):
    """
    Steuert die Menü-Logik basierend auf der Benutzerrolle.
    """
    if user_role == "Employee":
        while True:
            choice = show_employee_menu()

            if choice == '1':
                print("\nAlle Fahrzeuge:")
                vehicles = get_all_vehicles()
                for vehicle in vehicles:
                    print(f"ID: {vehicle[0]}, Marke: {vehicle[1]}, Modell: {vehicle[2]}, Status: {vehicle[4]}")
            
            elif choice == '2':
                brand = input("Marke: ")
                model = input("Modell: ")
                color = input("Farbe: ")
                add_vehicle(brand, model, color)

            elif choice == '3':
                vehicle_id = int(input("Fahrzeug-ID: "))
                new_status = input("Neuer Status (Available, Rented, Maintenance): ")
                update_vehicle_status(vehicle_id, new_status)

            elif choice == '4':
                print("\nAlle aktiven Vermietungen:")
                rentals = get_active_rentals()
                for rental in rentals:
                    print(f"Vermietungs-ID: {rental[0]}, Benutzer-ID: {rental[1]}, Fahrzeug-ID: {rental[2]}")
            
            elif choice == '5':
                print("Abmeldung...")
                break
            
            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine Zahl von 1 bis 5.")
                
    elif user_role == "Customer":
        while True:
            choice = show_customer_menu()
            
            if choice == '1':
                print("\nVerfügbare Fahrzeuge:")
                vehicles = get_available_vehicles()
                for vehicle in vehicles:
                    print(f"ID: {vehicle[0]}, Marke: {vehicle[1]}, Modell: {vehicle[2]}")

            elif choice == '2':
                vehicle_id = int(input("Fahrzeug-ID: "))
                rent_vehicle(user_id, vehicle_id)
                update_vehicle_status(vehicle_id, 'Rented')

            elif choice == '3':
                rental_id = int(input("Vermietungs-ID: "))
                return_vehicle(rental_id)
                vehicle_id = int(input("Fahrzeug-ID: "))
                update_vehicle_status(vehicle_id, 'Available')
            
            elif choice == '4':
                print("\nIhre Miet-Historie:")
                history = get_user_rental_history(user_id)
                for rental in history:
                    print(rental)

            elif choice == '5':
                print("Abmeldung...")
                break
                
            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine Zahl von 1 bis 5.")


def handle_login():
    """Steuert den Anmeldeprozess und leitet zum Menü weiter."""
    print("===== LOGIN =====")
    username = input("Benutzername: ")
    password = input("Passwort: ")

    user = get_login(username, password)
    
    if user:
        print(f"\nLogin erfolgreich! Willkommen, {user[1]}!")
        handle_user_management(user[3], user[0])
    else:
        print("\nLogin fehlgeschlagen. Ungültige Anmeldedaten.")

if __name__ == "__main__":
    handle_login()