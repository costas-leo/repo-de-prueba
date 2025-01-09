import mysql.connector

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            database="inventario"
        )
        print("Conexión exitosa")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
