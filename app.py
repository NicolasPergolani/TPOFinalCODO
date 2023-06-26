import sqlite3
# Configurar la conexión a la base de datos SQLite
DATABASE = 'inventario.db'
def get_db_connection():
    print("Obteniendo conexión...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
# Crear la tabla 'productos' si no existe
def create_table():
    print("Creando tabla productos...") # Para probar que se ejecuta la 
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
    codigo INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
    ) ''')
    conn.commit()
    cursor.close()
    conn.close()
# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
    print("Creando la BD...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()
# Programa principal
# Crear la base de datos y la tabla si no existen
    create_database()
class Producto:
    # Definimos el constructor e inicializamos los atributos de instancia
        def __init__(self, codigo, descripcion, stock, precio):
            self.codigo = codigo # Código 
            self.descripcion = descripcion # Descripción
            self.stock = stock # Cantidad disponible (stock)
            self.precio = precio # Precio 
# Este método permite modificar un producto.
def modificar(self, nueva_descripcion, nuevo_stock, nuevo_precio):
    self.descripcion = nueva_descripcion # Modifica la descripción
    self.cantidad = nuevo_stock # Modifica la cantidad
    self.precio = nuevo_precio # Modifica el precio
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
def agregar_producto(self, codigo, descripcion, stock, precio):
    producto_existente = self.consultar_producto(codigo)
    if producto_existente:
        print("Ya existe un producto con ese código.")
        return False
    nuevo_producto = Producto(codigo, descripcion, stock, precio)
    sql = f'INSERT INTO productos VALUES ({codigo}, "{descripcion}",{stock}, {precio});'
    self.cursor.execute(sql)
    self.conexion.commit()
    return True
def consultar_producto(self, codigo):
    sql = f'SELECT * FROM productos WHERE codigo = {codigo};'
    self.cursor.execute(sql)
    row = self.cursor.fetchone()
    if row:
        codigo, descripcion, stock, precio = row
    return Producto(codigo, descripcion, stock, precio)
    return False
def modificar_producto(self, codigo, nueva_descripcion, nuevo_stock, 
nuevo_precio):
    producto = self.consultar_producto(codigo)
                                   
    if producto:
        producto.modificar(nueva_descripcion, nuevo_stock, 
    nuevo_precio)
    sql = f'UPDATE productos SET descripcion = "{nueva_descripcion}",cantidad = {nuevo_stock}, precio = {nuevo_precio} WHERE codigo ={codigo};'
    self.cursor.execute(sql)
    self.conexion.commit()
def eliminar_producto(self, codigo):
    sql = f'DELETE FROM productos WHERE codigo = {codigo};'
    self.cursor.execute(sql)
    if self.cursor.rowcount > 0:
        print(f'Producto {codigo} eliminado.')
        self.conexion.commit()
    else:
        print(f'Producto {codigo} no encontrado.')
def eliminar_producto(self, codigo):
    sql = f'DELETE FROM productos WHERE codigo = {codigo};'
    self.cursor.execute(sql)    
    if self.cursor.rowcount > 0:
        print(f'Producto {codigo} eliminado.')
        self.conexion.commit()
    else:
        print(f'Producto {codigo} no encontrado.')
def __init__(self):
    self.conexion = sqlite3.connect('inventario.db') # Conexión a la BD
    self.cursor = self.conexion.cursor()
    self.items = []
def agregar(self, codigo, stock, inventario):
    producto = inventario.consultar_producto(codigo)
    if producto is False:
        print("El producto no existe.")
        return False
    if producto.stock < stock:
        print("Cantidad en stock insuficiente.")
        return False
    for item in self.items:
        if item.codigo == codigo:
            item.stock += stock
            sql = f'UPDATE productos SET stock = stock - {stock} WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        self.conexion.commit()
    return True
    nuevo_item = Producto(codigo, producto.descripcion,producto.stock, 
    producto.precio)
    self.items.append(nuevo_item)
    sql = f'UPDATE productos SET stock = stock - {producto.stock} WHERE codigo = {codigo};'
    self.cursor.execute(sql)
    self.conexion.commit()
    return True
def quitar(self, codigo, stock, inventario):
    for item in self.items:
        if item.codigo == codigo:
            if stock > item.stock:
                print("Cantidad a quitar mayor a la stock en el carrito.")
                return False
        item.stock -= stock
    if item.stock == 0:
        self.items.remove(item)
    sql = f'UPDATE productos SET cantidad = cantidad + {stock} WHERE codigo = {codigo};'
    self.cursor.execute(sql)
    self.conexion.commit()
    return True
def quitar(self, codigo, stock, inventario):
    for item in self.items:
        if item.codigo == codigo:
            if stock > item.stock:
                print("Cantidad a quitar mayor a la cantidad en el carrito.")
        return False
        item.stock -= stock
        if item.stock == 0:
            self.items.remove(item)
            sql = f'UPDATE productos SET stock = stock + {stock} WHERE codigo = {codigo};'
            self.cursor.execute(sql)
            self.conexion.commit()
        return True
# Programa principal
# Crear la base de datos y la tabla si no existen
create_database()
# Crear una instancia de la clase Inventario
mi_inventario = Inventario()
# Agregar productos al inventario
mi_inventario.agregar_producto(1, "Viaje a Mendoza hotel 4 estrellas 7 dias 6 noches", 10, 190000)
mi_inventario.agregar_producto(2, "Viaje a Iguazu hotel 5 estrellas 12 dias 10 noches", 45, 150000)
mi_inventario.agregar_producto(3, "Viaje a El Calafate hotel 4,5 estrellas 5 dias 4 noches", 25, 120000)
mi_inventario.agregar_producto(3, "Viaje a Salta hotel 4 estrellas 14 dias 13 noches", 38, 220000)
mi_inventario.agregar_producto(3, "Viaje a Tucuman hotel 3,5 estrellas 6 dias 5 noches", 55, 115000)
# Consultar algún producto del inventario
print(mi_inventario.consultar_producto(3)) #Existe, se muestra la direcciónde memoria
print(mi_inventario.consultar_producto(4)) #No existe, se muestra False
# Listar los productos del inventario
mi_inventario.listar_productos()

