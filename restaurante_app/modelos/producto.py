class Producto:
    """Representa un producto del menu del restaurante."""

    def _init_(self, nombre, categoria, precio, disponible=True):
        
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # ---------- Propiedad: nombre ----------
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        self._nombre = valor.strip()

    # ---------- Propiedad: categoria ----------
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("La categoria del producto no puede estar vacia.")
        self._categoria = valor.strip()

    # ---------- Propiedad: precio ----------
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = valor

    # ---------- Propiedad: disponible ----------
    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    def mostrar_informacion(self):
        """Muestra los datos del producto de forma legible."""
        estado = "Disponible" if self.disponible else "No disponible"
        print("-" * 40)
        print(f"Nombre     : {self.nombre}")
        print(f"Categoria  : {self.categoria}")
        print(f"Precio     : ${self.precio:.2f}")
        print(f"Estado     : {estado}")
        print("-" * 40)