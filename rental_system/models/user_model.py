from database.db_connection import get_connection

class UserModel:
    def get_user_by_credentials(self, username, password):
        conn = get_connection()
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
