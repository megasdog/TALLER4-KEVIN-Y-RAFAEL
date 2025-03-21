import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT, telefono TEXT, ciudad TEXT,direccion TEXT)")

conn.commit()
