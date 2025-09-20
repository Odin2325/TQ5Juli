from controllers.user_controller import UserController
from controllers.vehicle_controller import VehicleController

def main():
    print("=== Vehicle Rental System ===")
    user_controller = UserController()
    user = user_controller.login()

    if not user:
        return  # Login fehlgeschlagen, Programm endet

    vc = VehicleController()
    role = user["Role"]

    while True:
        if role == "Customer":
            choice = user_controller.view.customer_menu()

            if choice == "1":
                print("👉 Mietfunktion (kommt in Woche 3 mit RentalModel)")
            elif choice == "2":
                vc.list_available()
            elif choice == "3":
                print("👋 Auf Wiedersehen!")
                break
            else:
                print("❌ Ungültige Eingabe!")

        elif role == "Employee":
            choice = user_controller.view.employee_menu()

            if choice == "1":
                print("👉 Mietfunktion (kommt in Woche 3 mit RentalModel)")
            elif choice == "2":
                vc.list_all()
            elif choice == "3":
                vc.add_vehicle()
            elif choice == "4":
                vehicle_id = int(input("Fahrzeug-ID: "))
                new_rate = float(input("Neuer Tagespreis (€): "))
                vc.model.update_price(vehicle_id, new_rate)
                print("✅ Preis aktualisiert!")
            elif choice == "5":
                print("👋 Auf Wiedersehen!")
                break
            else:
                print("❌ Ungültige Eingabe!")

