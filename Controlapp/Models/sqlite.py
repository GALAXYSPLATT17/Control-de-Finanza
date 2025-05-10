import sqlite3

def get_connection():
    conn = sqlite3.connect("control.db")
    conn.row_factory = sqlite3.Row  # Permite acceder por nombre de columna
    return conn

