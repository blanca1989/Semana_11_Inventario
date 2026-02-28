"""
crud_listas.py
Sistema de Inventario de una tienda usando LISTAS.

LISTA = colección ORDENADA y MUTABLE
En este caso cada elemento será un producto del inventario.
"""

class CRUDListas:

    def __init__(self):

        """
        Lista inicial del inventario
        Cada producto es un diccionario
        """

        self.items = [
            {"id": "P001", "nombre": "Laptop", "cantidad": 10, "precio": 900},
            {"id": "P002", "nombre": "Mouse", "cantidad": 50, "precio": 10},
            {"id": "P003", "nombre": "Teclado", "cantidad": 25, "precio": 20}
        ]

    # -------------------------
    # CREATE
    # -------------------------
    def agregar(self, id_p, nombre, cantidad, precio):

        producto = {
            "id": id_p,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }

        self.items.append(producto)

        print(f"✅ Producto agregado: {nombre}")

    # -------------------------
    # READ (listar)
    # -------------------------
    def listar(self):

        if not self.items:
            print("📭 Inventario vacío.")
            return

        print("\n📦 INVENTARIO DE LA TIENDA")

        for indice, producto in enumerate(self.items):

            print(
                f"[{indice}] "
                f"{producto['id']} | "
                f"{producto['nombre']} | "
                f"Stock: {producto['cantidad']} | "
                f"Precio: ${producto['precio']}"
            )

    # -------------------------
    # READ (buscar)
    # -------------------------
    def buscar(self, nombre_producto):

        for indice, producto in enumerate(self.items):

            if producto["nombre"].lower() == nombre_producto.lower():

                print(
                    f"🔎 Encontrado en índice {indice}: "
                    f"{producto['id']} | "
                    f"{producto['nombre']} | "
                    f"Stock: {producto['cantidad']} | "
                    f"Precio: ${producto['precio']}"
                )

                return indice

        print("❌ Producto no encontrado")

        return None

    # -------------------------
    # UPDATE
    # -------------------------
    def actualizar(self, indice, nueva_cantidad, nuevo_precio):

        if 0 <= indice < len(self.items):

            producto = self.items[indice]

            producto["cantidad"] = nueva_cantidad
            producto["precio"] = nuevo_precio

            print("✏️ Producto actualizado")

        else:

            print("⚠️ Índice fuera de rango")

    # -------------------------
    # DELETE
    # -------------------------
    def eliminar(self, nombre_producto):

        for producto in self.items:

            if producto["nombre"].lower() == nombre_producto.lower():

                self.items.remove(producto)

                print(f"🗑️ Producto eliminado: {nombre_producto}")

                return

        print("⚠️ Producto no encontrado")


# -------------------------
# MENÚ
# -------------------------
def menu():

    crud = CRUDListas()

    while True:

        print("""
==============================
 INVENTARIO TIENDA (LISTAS)
==============================
1) Listar productos
2) Agregar producto
3) Buscar producto
4) Actualizar producto
5) Eliminar producto
0) Salir
==============================
""")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            crud.listar()

        elif opcion == "2":

            id_p = input("ID producto: ")
            nombre = input("Nombre: ")

            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                crud.agregar(id_p, nombre, cantidad, precio)

            except ValueError:

                print("⚠️ Cantidad y precio deben ser números")

        elif opcion == "3":

            nombre = input("Producto a buscar: ")

            crud.buscar(nombre)

        elif opcion == "4":

            crud.listar()

            try:

                indice = int(input("Índice a actualizar: "))
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))

                crud.actualizar(indice, cantidad, precio)

            except ValueError:

                print("⚠️ Datos inválidos")

        elif opcion == "5":

            nombre = input("Producto a eliminar: ")

            crud.eliminar(nombre)

        elif opcion == "0":

            print("👋 Saliendo del sistema")

            break

        else:

            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()