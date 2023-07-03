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

class Producto:
    # Definimos el constructor e inicializamos los atributos de instancia
        def __init__(self, codigo, descripcion, cantidad, precio):
            self.codigo = codigo # Código 
            self.descripcion = descripcion # Descripción
            self.cantidad = cantidad # Cantidad disponible (cantidad)
            self.precio = precio # Precio 
        # Este método permite modificar un producto.
        def modificar(self, nueva_descripcion, nuevo_cantidad, nuevo_precio):
            self.descripcion = nueva_descripcion # Modifica la descripción
            self.cantidad = nuevo_cantidad # Modifica la cantidad
            self.precio = nuevo_precio # Modifica el precio
class Inventario:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
        self.productos = []
    def agregar_producto(self, codigo, descripcion, cantidad, precio):
        producto_existente = self.consultar_producto(codigo)
        if producto_existente:
            print("Ya existe un producto con ese código.")
            return False
        nuevo_producto = Producto(codigo, descripcion, cantidad, precio)
        self.productos.append(nuevo_producto)
        sql = f'INSERT INTO productos VALUES ({codigo}, "{descripcion}",{cantidad}, {precio});'
        self.cursor.execute(sql)
        self.conexion.commit()
        return True
    def consultar_producto(self, codigo):
        sql = f'SELECT * FROM productos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, cantidad, precio = row
            return Producto(codigo, descripcion, cantidad, precio)
        return False
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, 
    nuevo_precio):
        producto = self.consultar_producto(codigo)                
        if producto:
            producto.modificar(nueva_descripcion, nueva_cantidad, 
        nuevo_precio)
        sql = f'UPDATE productos SET descripcion = "{nueva_descripcion}", cantidad = {nueva_cantidad}, precio = {nuevo_precio} WHERE codigo ={codigo};'
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
    def listar_productos(self):
        print("-"*50)
        print("Lista de productos en el inventario:")
        print("Codigo\tDescripción\t\tCant\tPrecio")
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, descripcion, cantidad, precio = row
            print(f"'{codigo}\t{descripcion}\t{cantidad}\t{precio}'")
        print("-"*50)

class Carrito:
    def __init__(self):
        self.conexion = sqlite3.connect('inventario.db') # Conexión a la BD
        self.cursor = self.conexion.cursor()
        self.items = []
    def agregar(self, codigo, cantidad, inventario):
        producto = inventario.consultar_producto(codigo)
        if producto is False:
            print("El producto no existe.")
            return False
        if producto.cantidad < cantidad:
            print("Cantidad en stock insuficiente.")
            return False
        
        for item in self.items:
            if item.codigo == codigo:
                item.cantidad += cantidad
                sql = f'UPDATE productos SET cantidad = cantidad - {cantidad} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return True
            
        nuevo_item = Producto(codigo, producto.descripcion, cantidad, 
        producto.precio)
        self.items.append(nuevo_item)
        sql = f'UPDATE productos SET cantidad = cantidad - {cantidad} WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        self.conexion.commit()
        return True    
    def quitar(self, codigo, cantidad, inventario):
        for item in self.items:
            if item.codigo == codigo:
                if cantidad > item.cantidad:
                    print("Cantidad a quitar mayor a la cantidad en el carrito.")
                    return False
                item.cantidad -= cantidad
                if item.cantidad == 0:
                    self.items.remove(item)
                sql = f'UPDATE productos SET cantidad = cantidad + {cantidad} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return True
        print("El producto no se encuentra en el carrito")
        return False
    def mostrar(self):
        print("-"*50)
        print("Lista de productos en el carrito:")
        print("Codigo\tDescripción\t\tCant\tPrecio")
        for item in self.items:
            print(f"'{item.codigo}\t{item.descripcion}\t{item.cantidad}\t{item.precio}'")
        print("-"*50)

# Programa principal
# Crear la base de datos y la tabla si no existen
create_database()

# Crear una instancia de la clase Inventario
mi_inventario = Inventario()
mi_carrito = Carrito()

# Agregar productos al inventario
mi_inventario.agregar_producto(1, "Viaje a Mendoza hotel 4 estrellas 7 dias 6 noches", 10, 190000)
mi_inventario.agregar_producto(2, "Viaje a Iguazu hotel 5 estrellas 12 dias 10 noches", 45, 150000)
mi_inventario.agregar_producto(3, "Viaje a El Calafate hotel 4,5 estrellas 5 dias 4 noches", 25, 120000)
mi_inventario.agregar_producto(4, "Viaje a Salta hotel 4 estrellas 14 dias 13 noches", 38, 220000)
mi_inventario.agregar_producto(5, "Viaje a Tucuman hotel 3,5 estrellas 6 dias 5 noches", 55, 115000)

# Consultar algún producto del inventario
print(mi_inventario.consultar_producto(3)) #Existe, se muestra la direcciónde memoria
print(mi_inventario.consultar_producto(7)) #No existe, se muestra False

# Listar los productos del inventario
mi_inventario.listar_productos()

# Agregar 1 unidad de codigo 2 al carrito
mi_carrito.agregar(2, 1, mi_inventario)
# Agregar 3 unidad de codigo 1 al carrito
mi_carrito.agregar(1, 3, mi_inventario)
# Agregar 2 unidad de codigo 3 al carrito
mi_carrito.agregar(3, 2, mi_inventario)

# Listar productos del carrito
mi_carrito.mostrar()

# Quitar 1 unidad de codigo 1 del carrito
mi_carrito.quitar(1, 1, mi_inventario)

# Listar productos del carrito
mi_carrito.mostrar()

# Mostrar inventario
mi_inventario.listar_productos()



