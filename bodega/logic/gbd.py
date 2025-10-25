import sqlite3

conn = sqlite3.connect("bodega/data/users.db")
cursor = conn.cursor()


def agregar_usuario(nombre, email, dni, usuario):
    try:
        
        cursor.execute("""
            INSERT INTO users_bodega (nombre, email, dni, user)
            VALUES (?, ?, ?, ?)
        """, (nombre, email, dni, usuario))
        conn.commit()
        conn.close()
        return(f"Usuario {usuario} Creado")
    except Exception:
        return("Error no fue posible crear el ususario")
    
def Validar_users(user, table):

    cursor.execute(f"SELECT nombre, user FROM {table};")
    resultado= cursor.fetchall()
    return(resultado)

