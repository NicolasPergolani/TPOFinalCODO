import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
# Configurar la conexión a la base de datos SQLite
DATABASE = 'inventario.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe
def create_table():    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
    codigo INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    stock INTEGER NOT NULL,
    precio REAL NOT NULL
    ) ''')
    conn.commit()
    cursor.close()
    conn.close()
# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
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


class Inventario:
# Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.productos = [] # Lista de productos en el inventario (variable de clase)
    def agregar_producto(self, codigo, descripcion, stock, precio):
        producto_existente = self.consultar_producto(codigo)
        if producto_existente:
            return jsonify({'message': 'Ya existe un producto con ese código.'}), 400
        nuevo_producto = Producto(codigo, descripcion, stock, precio)
        sql = f'INSERT INTO productos VALUES ({codigo}, "{descripcion}",{stock}, {precio});'
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado correctamente.'}), 200

    def consultar_producto(self, codigo):
        sql = f'SELECT * FROM productos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, stock, precio = row
            return Producto(codigo, descripcion, stock, precio)
        return None
    def modificar_producto(self, codigo, nueva_descripcion, nuevo_stock,nuevo_precio):
        producto = self.consultar_producto(codigo)
        if producto:
            producto.modificar(nueva_descripcion, nuevo_stock,nuevo_precio)

            sql = f'UPDATE productos SET descripcion = "{nueva_descripcion}",stock = {nuevo_stock}, precio = {nuevo_precio} WHERE codigo ={codigo};'

            self.cursor.execute(sql)
            self.conexion.commit()
            return jsonify({'message': 'Producto modificado correctamente.'}), 200
        return jsonify({'message': 'Producto no encontrado.'}), 404
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        productos = []
        for row in rows:
            codigo, descripcion, stock, precio = row
            producto = {'codigo': codigo, 'descripcion': descripcion,'stock': stock, 'precio': precio}
            productos.append(producto)
        return jsonify(productos), 200
    def eliminar_producto(self, codigo):
        sql = f'DELETE FROM productos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Producto eliminado correctamente.'}),200
        return jsonify({'message': 'Producto no encontrado.'}), 404
 

class Carrito:
# Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
        self.items = []
# Este método permite agregar productos del inventario al carrito.
    def agregar(self, codigo, stock, inventario):
        producto = inventario.consultar_producto(codigo)
        if producto is None:
            return jsonify({'message': 'El producto no existe.'}), 404
        if producto.stock < stock:
            return jsonify({'message': 'Cantidad en stock insuficiente.'}),400
        for item in self.items:
            if item.codigo == codigo:
                item.stock += stock
                sql = f'UPDATE productos SET stock = cantidad -{stock} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return jsonify({'message': 'Producto agregado al carrito correctamente.'}), 200
        nuevo_item = Producto(codigo, producto.descripcion, stock,producto.precio)
        self.items.append(nuevo_item)
        sql = f'UPDATE productos SET cantidad = stock - {stock} WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado al carrito correctamente.'}), 200
# Este método quita unidades de un elemento del carrito, o lo elimina.
    def quitar(self, codigo, stock, inventario):
        for item in self.items:
            if item.codigo == codigo:
                if stock > item.stock:
                    return jsonify({'message': 'Cantidad a quitar mayor a la cantidad en el carrito.'}), 400

                item.stock -= stock
                if item.stock == 0:
                    self.items.remove(item)
                sql = f'UPDATE productos SET cantidad = stock + {stock} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return jsonify({'message': 'Producto quitado del carrito correctamente.'}), 200
        return jsonify({'message': 'El producto no se encuentra en el carrito.'}), 404
    def mostrar(self):
        productos_carrito = []
        for item in self.items:
            producto = {'codigo': item.codigo, 'descripcion': item.descripcion, 'stock': item.stock, 'precio': item.precio}

            productos_carrito.append(producto)
        return jsonify(productos_carrito), 200

app = Flask(__name__)
CORS(app)
carrito = Carrito() # Instanciamos un carrito
inventario = Inventario() # Instanciamos un inventario

# Ruta para obtener los datos de un producto según su código
@app.route('/productos/<int:codigo>', methods=['GET'])
def obtener_producto(codigo):
    producto = inventario.consultar_producto(codigo)
    if producto:
        return jsonify({
        'codigo': producto.codigo,
        'descripcion': producto.descripcion,
        'stock': producto.stock,
        'precio': producto.precio
    }), 200
    return jsonify({'message': 'Producto no encontrado.'}), 404 
# Ruta para obtener el index
@app.route('/')
def index():
    return 'API de Inventario'
# Ruta para obtener la lista de productos del inventario
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return inventario.listar_productos()
# Ruta para agregar un producto al inventario
@app.route('/productos', methods=['POST'])
def agregar_producto():
    codigo = request.json.get('codigo')
    descripcion = request.json.get('descripcion')
    stock = request.json.get('stock')
    precio = request.json.get('precio')
    return inventario.agregar_producto(codigo, descripcion, stock,
precio)
# Ruta para modificar un producto del inventario
@app.route('/productos/<int:codigo>', methods=['PUT'])
def modificar_producto(codigo):
    nueva_descripcion = request.json.get('descripcion')
    nuevo_stock = request.json.get('stock')
    nuevo_precio = request.json.get('precio')
    return inventario.modificar_producto(codigo, nueva_descripcion,nuevo_stock, nuevo_precio)
# Ruta para eliminar un producto del inventario
@app.route('/productos/<int:codigo>', methods=['DELETE'])
def eliminar_producto(codigo):
    return inventario.eliminar_producto(codigo)
# Ruta para agregar un producto al carrito
@app.route('/carrito', methods=['POST'])
def agregar_carrito():
    codigo = request.json.get('codigo')
    stock = request.json.get('stock')
    inventario = Inventario()
    return carrito.agregar(codigo, stock, inventario)
# Ruta para quitar un producto del carrito
@app.route('/carrito', methods=['DELETE'])
def quitar_carrito():
    codigo = request.json.get('codigo')
    stock = request.json.get('stock')
    inventario = Inventario()
    return carrito.quitar(codigo, stock, inventario)
# Ruta para obtener el contenido del carrito
@app.route('/carrito', methods=['GET'])
def obtener_carrito():
    return carrito.mostrar()
if __name__ == '__main__':
    app.run()
