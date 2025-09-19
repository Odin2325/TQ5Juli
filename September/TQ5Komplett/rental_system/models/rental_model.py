# models/rental_model.py
import sqlite3
import datetime

# Importiere die Verbindung und den Cursor aus der db_connection-Datei.
from database.db_connection import conn, cur

def rent_vehicle(user_id, vehicle_id):
    """
    Erstellt eine neue Vermietung in der Datenbank mit dem Status 'Active'.
    """
    try:
        rent_date = datetime.date.today().isoformat()
        # Hinweis: 'CustomerID' ist in der DB vorhanden, nicht 'UserID'
        cur.execute("INSERT INTO Rental (CustomerID, VehicleID, StartDate, Status) VALUES (?, ?, ?, ?)", (user_id, vehicle_id, rent_date, 'Active'))
        conn.commit()
        print(f"Fahrzeug {vehicle_id} erfolgreich an Benutzer {user_id} vermietet.")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")

def return_vehicle(rental_id):
    """
    Aktualisiert den Status einer Vermietung auf 'Completed'.
    """
    try:
        return_date = datetime.date.today().isoformat()
        cur.execute("UPDATE Rental SET EndDate = ?, Status = 'Completed' WHERE RentalID = ?", (return_date, rental_id))
        conn.commit()
        print(f"Vermietung {rental_id} erfolgreich abgeschlossen.")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")

def get_active_rentals():
    """
    Gibt alle aktiven Vermietungen zurück (basierend auf dem Status).
    """
    try:
        cur.execute("SELECT * FROM Rental WHERE Status = 'Active'")
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []

def get_user_rental_history(user_id):
    """
    Gibt die gesamte Vermietungshistorie eines Benutzers zurück.
    """
    try:
        cur.execute("SELECT * FROM Rental WHERE CustomerID = ?", (user_id,))
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []