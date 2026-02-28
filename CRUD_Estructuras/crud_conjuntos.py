"""
crud_conjuntos_inventario.py
CRUD usando CONJUNTOS aplicado a productos del inventario de una tienda.
"""

class CrudConjuntosInventario:

    def __init__(self):
        """
        Inicializamos el conjunto con productos del inventario.
        """
        self.productos = {"arroz", "leche", "azúcar"}

    # -------------------------
    # CREATE
    # -------------------------

    def agregar(self, producto: str):

        antes = len(self.productos)
        self.productos.add(producto)
        despues = len(self.productos)

        if despues == antes:
            print(f"ℹ️ '{producto}' ya existe en el inventario.")
        else:
            print(f"✅ Producto agregado: {producto}")

    # -------------------------
    # READ (listar)
    # -------------------------

    def listar(self):

        if not self.productos:
            print("📭 Inventario vacío.")
            return

        print("\n📦 PRODUCTOS DEL INVENTARIO")

        for producto in self.productos:
            print(f" - {producto}")

    # -------------------------
    # READ (buscar)
    # -------------------------

    def buscar(self, producto: str):

        if producto in self.productos:
            print(f"🔎 Producto encontrado: {producto}")
            return True

        print(f"❌ Producto no encontrado: {producto}")
        return False

    # -------------------------
    # UPDATE
    # -------------------------

    def actualizar(self, viejo: str, nuevo: str):

        if viejo not in self.productos:
            print(f"⚠️ '{viejo}' no existe en el inventario.")
            return

        self.productos.remove(viejo)
        self.productos.add(nuevo)

        print(f"✏️ Producto actualizado: '{viejo}' -> '{nuevo}'")

    # -------------------------
    # DELETE
    # -------------------------

    def eliminar(self, producto: str):

        if producto in self.productos:
            self.productos.discard(producto)
            print(f"🗑️ Producto eliminado: {producto}")
        else:
            print(f"ℹ️ '{producto}' no existe en el inventario.")


# -------------------------
# MENÚ
# -------------------------

def menu():

    crud = CrudConjuntosInventario()

    while True:

        print("\n===== INVENTARIO (SET) =====")
        print("1) Listar productos")
        print("2) Agregar producto")
        print("3) Buscar producto")
        print("4) Actualizar producto")
        print("5) Eliminar producto")
        print("0) Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crud.listar()

        elif opcion == "2":
            producto = input("Producto a agregar: ").strip()
            crud.agregar(producto)

        elif opcion == "3":
            producto = input("Producto a buscar: ").strip()
            crud.buscar(producto)

        elif opcion == "4":
            viejo = input("Producto actual: ").strip()
            nuevo = input("Nuevo nombre del producto: ").strip()
            crud.actualizar(viejo, nuevo)

        elif opcion == "5":
            producto = input("Producto a eliminar: ").strip()
            crud.eliminar(producto)

        elif opcion == "0":
            print("👋 Saliendo del sistema")
            break

        else:
            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()