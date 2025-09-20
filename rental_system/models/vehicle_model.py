from database.db_connection import get_connection

class VehicleModel:
    def get_all_vehicles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VehicleID, Brand, Model, Year, DailyRate, Status FROM Vehicle")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_available_vehicles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VehicleID, Brand, Model, Year, DailyRate FROM Vehicle WHERE Status='Available'")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def add_vehicle(self, brand, model, year, daily_rate):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Vehicle (Brand, Model, Year, DailyRate, Status) VALUES (?, ?, ?, ?, 'Available')",
            (brand, model, year, daily_rate)
        )
        conn.commit()
        conn.close()
        return True

    def update_status(self, vehicle_id, status):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Vehicle SET Status=? WHERE VehicleID=?", (status, vehicle_id))
        conn.commit()
        conn.close()
        return True

def update_price(self, vehicle_id, new_rate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Vehicle SET DailyRate=? WHERE VehicleID=?", (new_rate, vehicle_id))
    conn.commit()
    conn.close()
    return True
