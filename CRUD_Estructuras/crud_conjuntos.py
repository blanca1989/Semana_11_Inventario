"""
crud_conjuntos.py
Sistema de Inventario de Tienda usando CONJUNTOS (SET)

SET = colección de elementos únicos
No admite duplicados.
"""

class CrudConjuntos:

    def __init__(self):
        """
        Inventario inicial de productos (sin duplicados)
        """
        self.productos = {
            "Laptop",
            "Mouse",
            "Teclado"
        }

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
    # READ
    # -------------------------
    def listar(self):

        if not self.productos:
            print("📭 Inventario vacío.")
            return

        print("\n📦 PRODUCTOS EN INVENTARIO")

        for producto in self.productos:
            print(f" - {producto}")

    # -------------------------
    # READ (buscar)
    # -------------------------
    def buscar(self, producto):

        if producto in self.productos:
            print(f"🔎 Producto encontrado: {producto}")
            return True

        print(f"❌ Producto no encontrado: {producto}")
        return False

    # -------------------------
    # UPDATE
    # -------------------------
    def actualizar(self, viejo, nuevo):

        if viejo not in self.productos:
            print(f"⚠️ El producto '{viejo}' no existe.")
            return

        self.productos.remove(viejo)

        self.productos.add(nuevo)

        print(f"✏️ Producto actualizado: '{viejo}' -> '{nuevo}'")

    # -------------------------
    # DELETE
    # -------------------------
    def eliminar(self, producto):

        if producto in self.productos:

            self.productos.discard(producto)

            print(f"🗑️ Producto eliminado: {producto}")

        else:

            print("⚠️ Producto no existe")


# -------------------------
# MENÚ DEL SISTEMA
# -------------------------
def menu():

    crud = CrudConjuntos()

    while True:

        print("""
==============================
 INVENTARIO TIENDA (SET)
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

            producto = input("Producto a agregar: ").strip()

            if producto:
                crud.agregar(producto)

        elif opcion == "3":

            producto = input("Producto a buscar: ")

            crud.buscar(producto)

        elif opcion == "4":

            viejo = input("Producto viejo: ")
            nuevo = input("Producto nuevo: ")

            crud.actualizar(viejo, nuevo)

        elif opcion == "5":

            producto = input("Producto a eliminar: ")

            crud.eliminar(producto)

        elif opcion == "0":

            print("👋 Saliendo del sistema")

            break

        else:

            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()