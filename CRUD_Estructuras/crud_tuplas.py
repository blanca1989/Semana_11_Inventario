"""
crud_tuplas_inventario.py
CRUD adaptado usando TUPLAS para un inventario de tienda.

Cada producto es una tupla:
(ID, nombre, cantidad, precio)

Las tuplas son INMUTABLES, por lo que para modificar
el inventario se crea una NUEVA tupla.
"""

class CrudTuplasInventario:
    def __init__(self):
        """
        Inventario inicial de la tienda (tupla de productos)
        """
        self.productos = (
            (1, "Arroz", 50, 1.25),
            (2, "Leche", 30, 0.90),
            (3, "Pan", 40, 0.50)
        )

    # READ
    def listar(self):
        if not self.productos:
            print("📭 Inventario vacío.")
            return

        print("\n📦 INVENTARIO (TUPLA)")
        for p in self.productos:
            print(f"ID:{p[0]} | Nombre:{p[1]} | Cantidad:{p[2]} | Precio:${p[3]}")

    # READ (buscar)
    def buscar(self, nombre):
        for p in self.productos:
            if p[1].lower() == nombre.lower():
                print(f"🔎 Encontrado: ID:{p[0]} | {p[1]} | Cantidad:{p[2]} | Precio:${p[3]}")
                return
        print("❌ Producto no encontrado")

    # CREATE
    def agregar(self, id, nombre, cantidad, precio):
        nuevo_producto = (id, nombre, cantidad, precio)
        self.productos = self.productos + (nuevo_producto,)
        print(f"✅ Producto agregado: {nombre}")

    # UPDATE
    def actualizar(self, id, nueva_cantidad, nuevo_precio):
        lista_temp = list(self.productos)

        for i, p in enumerate(lista_temp):
            if p[0] == id:
                lista_temp[i] = (p[0], p[1], nueva_cantidad, nuevo_precio)
                self.productos = tuple(lista_temp)
                print("✏️ Producto actualizado")
                return

        print("⚠️ Producto no encontrado")

    # DELETE
    def eliminar(self, id):
        nueva_lista = [p for p in self.productos if p[0] != id]

        if len(nueva_lista) == len(self.productos):
            print("⚠️ No se encontró el producto")
        else:
            self.productos = tuple(nueva_lista)
            print("🗑️ Producto eliminado")


def menu():
    inventario = CrudTuplasInventario()

    while True:
        print("\n===== INVENTARIO TIENDA (TUPLAS) =====")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.listar()

        elif opcion == "2":
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar(id, nombre, cantidad, precio)

        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            inventario.buscar(nombre)

        elif opcion == "4":
            id = int(input("ID del producto: "))
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar(id, cantidad, precio)

        elif opcion == "5":
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar(id)

        elif opcion == "0":
            print("👋 Saliendo del sistema")
            break

        else:
            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()