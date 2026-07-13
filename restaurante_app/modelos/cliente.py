from dataclasses import dataclass

@dataclass
class Cliente:
    """Representa un cliente registrado en el sistema del restaurante."""
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self):
        """Muestra los datos del cliente de forma legible."""
        print("-" * 40)
        print(f"ID Cliente : {self.id_cliente}")
        print(f"Nombre     : {self.nombre}")
        print(f"Correo     : {self.correo}")
        print("-" * 40)