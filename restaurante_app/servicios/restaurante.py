from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio que gestiona productos y clientes del restaurante."""

    def _init_(self):
        self._productos = []
        self._clientes = []

    # ---------- Metodos para productos ----------
    def registrar_producto(self, producto: Producto):
        """Agrega un nuevo producto a la lista del restaurante."""
        self._productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado correctamente.")

    def listar_productos(self):
        """Muestra todos los productos registrados."""
        if not self._productos:
            print("No hay productos registrados todavia.")
            return
        print("\n=== LISTA DE PRODUCTOS ===")
        for producto in self._productos:
            producto.mostrar_informacion()

    def buscar_producto(self, nombre):
        """Busca un producto por nombre (sin distinguir mayusculas)."""
        encontrados = [
            p for p in self._productos
            if nombre.strip().lower() in p.nombre.lower()
        ]
        if not encontrados:
            print(f"No se encontro ningun producto con el nombre '{nombre}'.")
            return
        print(f"\n=== RESULTADOS DE BUSQUEDA: '{nombre}' ===")
        for producto in encontrados:
            producto.mostrar_informacion()

    # ---------- Metodos para clientes ----------
    def registrar_cliente(self, cliente: Cliente):
        """Agrega un nuevo cliente a la lista del restaurante."""
        self._clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado correctamente.")

    def listar_clientes(self):
        """Muestra todos los clientes registrados."""
        if not self._clientes:
            print("No hay clientes registrados todavia.")
            return
        print("\n=== LISTA DE CLIENTES ===")
        for cliente in self._clientes:
            cliente.mostrar_informacion()

    def buscar_cliente(self, dato_busqueda):
        """Busca un cliente por nombre o por id_cliente."""
        dato_busqueda = dato_busqueda.strip().lower()
        encontrados = [
            c for c in self._clientes
            if dato_busqueda in c.nombre.lower()
            or dato_busqueda in c.id_cliente.lower()
        ]
        if not encontrados:
            print(f"No se encontro ningun cliente con el dato '{dato_busqueda}'.")
            return
        print(f"\n=== RESULTADOS DE BUSQUEDA: '{dato_busqueda}' ===")
        for cliente in encontrados:
            cliente.mostrar_informacion()