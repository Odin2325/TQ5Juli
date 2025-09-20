from models.vehicle_model import VehicleModel
from views.vehicle_view import VehicleView

class VehicleController:
    def __init__(self):
        self.model = VehicleModel()
        self.view = VehicleView()

    def list_all(self):
        vehicles = self.model.get_all_vehicles()
        self.view.show_all_vehicles(vehicles)

    def list_available(self):
        vehicles = self.model.get_available_vehicles()
        self.view.show_available_vehicles(vehicles)

    def add_vehicle(self):
        brand, model, year, rate = self.view.get_new_vehicle_input()
        success = self.model.add_vehicle(brand, model, year, rate)
        if success:
            print("✅ Fahrzeug erfolgreich hinzugefügt!")
