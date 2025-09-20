import sqlite3

DB_PATH = "C:\\Users\\mytq\\Documents\\GitHub\\TQ5Juli\\TQ5Juli\\rental_system\\rental.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
