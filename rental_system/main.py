# main.py
from db import init_db, init_logging
from models import UserModel, CustomerModel, VehicleModel, RentalModel, PaymentModel

def seed_demo_data():
    # Demo-Daten nur einmal anlegen (try/except ignoriert Duplikatsfehler)
    try:
        uid_emp = UserModel.create_user("alice", "secret123", "Employee")
    except:
        pass
    try:
        uid_cus = UserModel.create_user("bob", "secret123", "Customer")
        cus = CustomerModel.get_by_user(uid_cus)
        if not cus:
            CustomerModel.create_customer_for_user(uid_cus, "Bob Kunde", "bob@example.com", "089-123456")
    except:
        pass
    # Fahrzeuge
    try:
        VehicleModel.add_vehicle("VW", "Golf", 2022, 49.9)
        VehicleModel.add_vehicle("BMW", "3er", 2021, 79.0)
        VehicleModel.add_vehicle("Tesla", "Model 3", 2023, 129.0)
    except:
        pass

def demo_flow():
    print("Login als bob/secret123 (Customer)...")
    user = UserModel.authenticate("bob", "secret123")
    if not user:
        print("Login fehlgeschlagen.")
        return
    print("Eingeloggt als:", user["Username"], "-", user["Role"])
    cust = CustomerModel.get_by_user(user["UserID"])
    print("Kunde:", cust["Name"])

    print("\nVerfügbare Fahrzeuge:")
    for v in VehicleModel.get_available_vehicles():
        print(f"- {v['VehicleID']} {v['Brand']} {v['Model']} {v['Year']} {v['DailyRate']} EUR/Tag")

    # Miete anlegen
    print("\nMiete anlegen (heute bis übermorgen)...")
    from datetime import date, timedelta
    start = date.today().isoformat()
    end = (date.today() + timedelta(days=2)).isoformat()

    av = VehicleModel.get_available_vehicles()
    if not av:
        print("Keine Fahrzeuge verfügbar.")
        return

    vehicle_id = av[0]["VehicleID"]
    rid, total = RentalModel.create_rental(cust["CustomerID"], vehicle_id, start, end)
    print("RentalID:", rid, "Total:", total)

    # Zahlung
    PaymentModel.add_payment(rid, amount=50.0)
    balance = PaymentModel.get_balance(rid)
    print("Offener Betrag:", balance)

    # Abschluss
    RentalModel.complete_rental(rid)
    print("Miete abgeschlossen.")

def main():
    init_logging()
    init_db()
    seed_demo_data()
    demo_flow()

if __name__ == "__main__":
    main()
