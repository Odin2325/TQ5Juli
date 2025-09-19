# models/user_model.py
import sqlite3

class UserModel:
    def __init__(self, db_name="rental.db"):
        self.db_name = db_name

    def get_user_by_credentials(self, username, password):
        """
        Prüft, ob ein Benutzer mit Username und Passwort existiert.
        Gibt ein Dictionary mit den User-Daten zurück oder None.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT UserID, Username, Role
            FROM User
            WHERE Username=? AND Password=?
        """, (username, password))
        
        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "UserID": row[0],
                "Username": row[1],
                "Role": row[2]
            }
        return None
