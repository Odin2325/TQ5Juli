class VehicleView:
    def show_all_vehicles(self, vehicles):
        print("\n=== Alle Fahrzeuge ===")
        for v in vehicles:
            print(f"ID: {v[0]}, {v[1]} {v[2]} ({v[3]}), {v[4]}€/Tag, Status: {v[5]}")

    def show_available_vehicles(self, vehicles):
        print("\n=== Verfügbare Fahrzeuge ===")
        for v in vehicles:
            print(f"ID: {v[0]}, {v[1]} {v[2]} ({v[3]}), {v[4]}€/Tag")

    def get_new_vehicle_input(self):
        brand = input("Marke: ")
        model = input("Modell: ")
        year = int(input("Baujahr: "))
        rate = float(input("Tagesrate (€): "))
        return brand, model, year, rate
