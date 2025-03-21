import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT, telefono TEXT, ciudad TEXT,direccion TEXT)")

conn.commit()

def create_user(name, email, telefono, ciudad, direccion):
    cursor.execute("INSERT INTO users (name, email, telefono, ciudad, direccion) VALUES (?, ?, ?, ?, ?)", (name, email, telefono, ciudad, direccion))
    conn.commit()

def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_telefono(id, telefono):
    cursor.execute("UPDATE users SET telefono = ? WHERE id = ?", (telefono, id))
    conn.commit()

def update_email(id, email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (name, email, id))
    conn.commit()

def update_user(id, telefono, email, direccion,ciudad,):
    cursor.execute("UPDATE users SET telefono = ?, email = ?, direccion = ?, ciudad =? WHERE id = ?", (telefono, email, dirrecion, ciudad, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    