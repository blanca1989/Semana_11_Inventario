"""
crud_diccionarios_inventario.py
CRUD usando DICCIONARIOS aplicado a un INVENTARIO DE TIENDA.
"""

class CrudDiccionariosInventario:

    def __init__(self):
        """
        Diccionario del inventario
        ID -> datos del producto
        """

        self.productos = {

            "P001": {"nombre": "Arroz", "cantidad": 50, "precio": 1.20},
            "P002": {"nombre": "Leche", "cantidad": 30, "precio": 0.90},
            "P003": {"nombre": "Azúcar", "cantidad": 40, "precio": 1.10}

        }

    # -------------------------
    # CREATE
    # -------------------------

    def agregar(self, id_producto, nombre, cantidad, precio):

        if id_producto in self.productos:
            print("⚠️ El producto ya existe.")
            return

        self.productos[id_producto] = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }

        print("✅ Producto agregado al inventario")

    # -------------------------
    # READ (LISTAR)
    # -------------------------

    def listar(self):

        if not self.productos:
            print("📭 Inventario vacío")
            return

        print("\n📦 INVENTARIO DE LA TIENDA")

        for clave, datos in self.productos.items():

            print(
                f"{clave} | "
                f"{datos['nombre']} | "
                f"Stock: {datos['cantidad']} | "
                f"Precio: ${datos['precio']}"
            )

    # -------------------------
    # READ (BUSCAR)
    # -------------------------

    def buscar(self, clave):

        if clave in self.productos:

            datos = self.productos[clave]

            print(
                f"🔎 Producto encontrado:\n"
                f"{clave} | {datos['nombre']} | "
                f"Stock: {datos['cantidad']} | "
                f"Precio: ${datos['precio']}"
            )

            return datos

        print("❌ Producto no encontrado")
        return None

    # -------------------------
    # UPDATE
    # -------------------------

    def actualizar(self, clave, cantidad, precio):

        if clave in self.productos:

            self.productos[clave]["cantidad"] = cantidad
            self.productos[clave]["precio"] = precio

            print("✏️ Producto actualizado")

        else:
            print("⚠️ Producto no existe")

    # -------------------------
    # DELETE
    # -------------------------

    def eliminar(self, clave):

        eliminado = self.productos.pop(clave, None)

        if eliminado:
            print(f"🗑️ Producto eliminado: {clave}")
        else:
            print("⚠️ Producto no encontrado")


# -------------------------
# MENÚ
# -------------------------

def menu():

    crud = CrudDiccionariosInventario()

    while True:

        print("\n===== INVENTARIO TIENDA =====")
        print("1) Listar productos")
        print("2) Agregar producto")
        print("3) Buscar producto")
        print("4) Actualizar producto")
        print("5) Eliminar producto")
        print("0) Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            crud.listar()

        elif opcion == "2":

            id_p = input("ID producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            crud.agregar(id_p, nombre, cantidad, precio)

        elif opcion == "3":

            id_p = input("ID a buscar: ")
            crud.buscar(id_p)

        elif opcion == "4":

            id_p = input("ID a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))

            crud.actualizar(id_p, cantidad, precio)

        elif opcion == "5":

            id_p = input("ID a eliminar: ")
            crud.eliminar(id_p)

        elif opcion == "0":
            print("👋 Saliendo del sistema")
            break

        else:
            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()