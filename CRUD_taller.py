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

#create_user("Alice", "alice@mail.com","3194769135", "pereira", "cra21#2-81")
#create_user("Wanda", "wanda@mail.com", "3102245252","manisales","calle53#48-28")
#create_user("numar", "numar@mail.com","3022719674","bucaramanga","av42#25-32")
#create_user("gabriela", "gabriela@mail.com","3114880711","floridablanca","cra12#200-105")
#create_user("rafael", "rafael@mail.com","3182853392","giron","cra31#16-28")
#create_user("kevin", "kevin@mail.com","3161735505","piedecuesta","calle8#22-28")


interacion=10


while interacion !=0:
    print("""presione:
            1. para agregar un usuario
            2. para editar el telefono de un usuario
            3. para editar el correo de un usuario
            4. para editar todos los datos del usuario  (sin incluir el nombre)
            5. para imprimir los usuarios
            6. para eliminar un usuario
            0. para terminar
                """)
    interacion=int(input(""))

    if interacion==1:
        nombre = input("ingrese el nombre: ")
        email = input("ingrese el email: ")
        telefono = input("ingrese el telefono: ")
        ciudad = input("ingrese el ciudad: ")
        direccion = input("ingrese la direccion: ")
        create_user(nombre, email, telefono, ciudad, direccion)
    if interacion==2:
        id= int(input("ingrese el id del usuario: "))
        telefono = input("ingrese el telefono: ")
        update_telefono(id, telefono)
    if interacion==3:
        id = int(input("ingrese el id del correo de usuario: "))
        email = input("ingrese el email: ")
        update_email(id, email)
    if interacion==4:
        id = int(input("ingrese el id del usuario: "))
        telefono = input("ingrese el telefono: ")
        email = input("ingrese el email: ")
        direccion = input("ingrese la direccion: ")
        ciudad = input("ingrese el ciudad: ")
        update_user(id, telefono, email, direccion,ciudad,)
    if interacion==5:
        print(read_users())
    if interacion==6:
        id = int(input("ingrese el id del usuario: "))
        delete_user(id)
conn.close()