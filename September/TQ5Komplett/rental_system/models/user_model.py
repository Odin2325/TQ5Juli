from database.db_connection import cur

def get_user_by_credentials(username, password):
    # Hier ist der SELECT-Befehl!
    cur.execute("SELECT * FROM User WHERE Username = ? AND Password = ?", (username, password))
    user = cur.fetchone()
    return user