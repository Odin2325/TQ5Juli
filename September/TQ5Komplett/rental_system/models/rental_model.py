# models/rental_model.py
import sqlite3
import datetime

# Importiere die Verbindung und den Cursor aus der db_connection-Datei.
from database.db_connection import conn, cur

def rent_vehicle(user_id, vehicle_id):
    """
    Erstellt eine neue Vermietung in der Datenbank.
    """
    try:
        rent_date = datetime.date.today().isoformat()
        cur.execute("INSERT INTO Rental (UserID, VehicleID, RentDate) VALUES (?, ?, ?)", (user_id, vehicle_id, rent_date))
        conn.commit()
        print(f"Fahrzeug {vehicle_id} erfolgreich an Benutzer {user_id} vermietet.")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")

def return_vehicle(rental_id):
    """
    Markiert eine Vermietung als zurückgegeben.
    """
    try:
        return_date = datetime.date.today().isoformat()
        cur.execute("UPDATE Rental SET ReturnDate = ? WHERE RentalID = ?", (return_date, rental_id))
        conn.commit()
        print(f"Vermietung {rental_id} erfolgreich abgeschlossen.")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")

def get_active_rentals():
    """
    Gibt alle aktiven Vermietungen zurück (ohne Rückgabedatum).
    """
    try:
        cur.execute("SELECT * FROM Rental WHERE ReturnDate IS NULL")
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []

def get_user_rental_history(user_id):
    """
    Gibt die gesamte Vermietungshistorie eines Benutzers zurück.
    """
    try:
        cur.execute("SELECT * FROM Rental WHERE UserID = ?", (user_id,))
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []