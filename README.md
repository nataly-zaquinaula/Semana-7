Sistema de Restaurante
Programa en Python para registrar y buscar productos y clientes de un restaurante, usando clases (POO).
Archivos del proyecto
restaurante_app/
├── main.py                  # Aquí se ejecuta el programa (el menú)
├── modelos/
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
└── servicios/
    └── restaurante.py       # Clase Restaurante (guarda y busca los datos)
Cómo ejecutarlo
Abrir la carpeta restaurante_app y correr:
python main.py
Menú
1. Registrar producto
2. Listar productos
3. Buscar producto
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
7. Salir
Qué hace cada archivo
producto.py: define cómo es un producto (nombre, categoría, precio, disponible) y valida que los datos sean correctos.
cliente.py: define cómo es un cliente (nombre, correo, ID).
restaurante.py: guarda los productos y clientes en listas, y tiene los métodos para registrar, listar y buscar.
main.py: muestra el menú, pide los datos al usuario y llama a los métodos de restaurante.py.