"""
crud_diccionarios.py
Sistema de Gestión de Inventario usando DICCIONARIOS.

DICCIONARIO = clave -> valor
En este caso:
ID_PRODUCTO -> {nombre, cantidad, precio}
"""

class CrudDiccionarios:

    def __init__(self):
        """
        Diccionario inicial del inventario
        """
        self.productos = {
            "P001": {"nombre": "Laptop", "cantidad": 10, "precio": 900},
            "P002": {"nombre": "Mouse", "cantidad": 50, "precio": 10},
            "P003": {"nombre": "Teclado", "cantidad": 25, "precio": 20}
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

        print(f"✅ Producto agregado: {nombre}")

    # -------------------------
    # READ (listar)
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
    # READ (buscar)
    # -------------------------
    def buscar(self, id_producto):

        if id_producto in self.productos:

            p = self.productos[id_producto]

            print(
                f"🔎 Encontrado → "
                f"{id_producto} | "
                f"{p['nombre']} | "
                f"Stock: {p['cantidad']} | "
                f"Precio: ${p['precio']}"
            )

            return p

        print("❌ Producto no encontrado")
        return None

    # -------------------------
    # UPDATE
    # -------------------------
    def actualizar(self, id_producto):

        if id_producto not in self.productos:
            print("⚠️ Producto no existe")
            return

        try:

            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))

            self.productos[id_producto]["cantidad"] = nueva_cantidad
            self.productos[id_producto]["precio"] = nuevo_precio

            print("✏️ Producto actualizado")

        except ValueError:
            print("⚠️ Datos inválidos")

    # -------------------------
    # DELETE
    # -------------------------
    def eliminar(self, id_producto):

        eliminado = self.productos.pop(id_producto, None)

        if eliminado is None:
            print("⚠️ Producto no existe")
        else:
            print(f"🗑️ Producto eliminado: {eliminado['nombre']}")


# -------------------------
# MENÚ PRINCIPAL
# -------------------------
def menu():

    inventario = CrudDiccionarios()

    while True:

        print("""
==============================
 SISTEMA INVENTARIO TIENDA
==============================
1) Listar productos
2) Agregar producto
3) Buscar producto
4) Actualizar producto
5) Eliminar producto
0) Salir
==============================
""")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            inventario.listar()

        elif opcion == "2":

            id_p = input("ID producto (ej: P004): ")
            nombre = input("Nombre: ")

            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar(id_p, nombre, cantidad, precio)
            except ValueError:
                print("⚠️ Cantidad y precio deben ser números")

        elif opcion == "3":
            id_p = input("ID producto: ")
            inventario.buscar(id_p)

        elif opcion == "4":
            id_p = input("ID producto: ")
            inventario.actualizar(id_p)

        elif opcion == "5":
            id_p = input("ID producto: ")
            inventario.eliminar(id_p)

        elif opcion == "0":
            print("👋 Saliendo del sistema")
            break

        else:
            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()