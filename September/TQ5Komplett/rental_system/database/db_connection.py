import sqlite3
import os

# Pfad zur SQLite-Datenbank
db_path = 'C:\\Users\\mytq\\Desktop\\TQ5\\TQ5Juli\\September\\TQ5Komplett\\rental_system\\rental.db' 
      # or os.path.join('..', 'rental.db')

# Stelle die Verbindung zur Datenbank her
try:
    conn = sqlite3.connect(db_path)
    print("Verbindung zur Datenbank erfolgreich hergestellt.")
except sqlite3.Error as e:
    print(f"Fehler beim Verbinden mit der Datenbank: {e}")

# Erstelle ein Cursor-Objekt
cur = conn.cursor()