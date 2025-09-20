import sqlite3

DB_PATH = "rental.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
