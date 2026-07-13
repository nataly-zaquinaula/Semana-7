from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("=" * 42)
    print("           SISTEMA DE RESTAURANTE")
    print("=" * 42)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 42)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 42)
    print("7. Salir")

def registrar_producto(restaurante: Restaurante):
    print("\n--- Registrar nuevo producto ---")
    try:
        nombre = input("Nombre del producto: ")
        categoria = input("Categoria del producto: ")
        precio = float(input("Precio del producto: "))
        disponible_texto = input("¿Disponible? (s/n): ").strip().lower()
        disponible = disponible_texto == "s"

        producto = Producto(nombre, categoria, precio, disponible)
        restaurante.registrar_producto(producto)
    except ValueError as error:
        print(f"Error: {error}")


def registrar_cliente(restaurante: Restaurante):
    print("\n--- Registrar nuevo cliente ---")
    nombre = input("Nombre del cliente: ")
    correo = input("Correo del cliente: ")
    id_cliente = input("ID del cliente: ")

    cliente = Cliente(nombre, correo, id_cliente)
    restaurante.registrar_cliente(cliente)


def buscar_producto(restaurante: Restaurante):
    print("\n--- Buscar producto ---")
    nombre = input("Ingrese el nombre (o parte del nombre) a buscar: ")
    restaurante.buscar_producto(nombre)


def buscar_cliente(restaurante: Restaurante):
    print("\n--- Buscar cliente ---")
    dato = input("Ingrese el nombre o el ID del cliente a buscar: ")
    restaurante.buscar_cliente(dato)


def main():
    restaurante = Restaurante()

    opciones = {
        "1": lambda: registrar_producto(restaurante),
        "2": lambda: restaurante.listar_productos(),
        "3": lambda: buscar_producto(restaurante),
        "4": lambda: registrar_cliente(restaurante),
        "5": lambda: restaurante.listar_clientes(),
        "6": lambda: buscar_cliente(restaurante),
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "7":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opcion invalida. Intente nuevamente.")

        input("\nPresione ENTER para continuar...")


if _name_ == "_main_":
    main()