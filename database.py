import sqlite3
def get_connection():
    return sqlite3.connect('users.db')

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT not NULL,
    email TEXT NOT NULL)""")

    conn.commit()
    conn.close()