from app import mysqlPPp

# Ejemplo: Obtener todos los productos
def obtener_productos():
    conn = mysqlPPp.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")  # Cambia "productos" por tu tabla
    productos = cursor.fetchall()
    cursor.close()
    return productos

# Ejemplo: Insertar un producto
def insertar_producto(nombre, precio):
    conn = mysqlPPp.connection
    cursor = conn.cursor()
    query = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
    valores = (nombre, precio)
    cursor.execute(query, valores)
    conn.commit()
    cursor.close()