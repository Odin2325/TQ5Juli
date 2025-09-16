import sqlite3
import os

class DBConnection:
    """
    Eine Klasse, die die Datenbankverbindung handhabt.
    """
    def __init__(self, db_name='rental.db'):
        # Den Pfad zum Verzeichnis des aktuellen Skripts (db_connection.py) ermitteln
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Den absoluten Pfad zur Datenbankdatei erstellen.
        # Da rental.db im übergeordneten Verzeichnis liegt, gehen wir einen Ordner zurück.
        self.db_path = os.path.join(script_dir, '..', db_name)
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Stellt eine Verbindung zur SQLite-Datenbank her.
        """
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            print(f"Verbindung zur Datenbank erfolgreich hergestellt: {self.db_path}")
            return self.connection
        except sqlite3.Error as e:
            print(f"Fehler beim Verbinden mit der Datenbank: {e}")
            return None

    def close(self):
        """
        Schließt die Datenbankverbindung.
        """
        if self.connection:
            self.connection.close()
            print("Datenbankverbindung geschlossen.")