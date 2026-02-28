"""
crud_listas_inventario.py
Demostración de CRUD usando LISTAS para el inventario de una tienda.
"""


class CRUDListas:

    def __init__(self):
        """
        CONSTRUCTOR:
        Inicializamos la lista con productos del inventario.
        """
        self.items = ["arroz", "leche", "azúcar"]  # inventario inicial

    # -------------------------
    # CREATE (agregar)
    # -------------------------
    def agregar(self, nuevo_item: str):

        self.items.append(nuevo_item)
        print(f"✅ Producto agregado al inventario: {nuevo_item}")

    # -------------------------
    # READ (listar)
    # -------------------------
    def listar(self):

        if not self.items:
            print("📭 El inventario está vacío.")
            return

        print("\n📦 INVENTARIO DE LA TIENDA:")

        for indice, valor in enumerate(self.items):
            print(f"  [{indice}] {valor}")

    # -------------------------
    # READ (buscar)
    # -------------------------
    def buscar(self, item_buscado: str):

        for indice, valor in enumerate(self.items):
            if valor == item_buscado:
                print(f"🔎 Producto encontrado '{item_buscado}' en índice {indice}")
                return indice

        print(f"❌ No se encontró el producto '{item_buscado}'")
        return None

    # -------------------------
    # UPDATE (actualizar)
    # -------------------------
    def actualizar(self, indice: int, nuevo_valor: str):

        if 0 <= indice < len(self.items):

            anterior = self.items[indice]
            self.items[indice] = nuevo_valor

            print(f"✏️ Producto actualizado índice {indice}: '{anterior}' -> '{nuevo_valor}'")

        else:
            print("⚠️ Índice fuera de rango. No se pudo actualizar.")

    # -------------------------
    # DELETE (eliminar)
    # -------------------------
    def eliminar(self, item_a_eliminar: str):

        try:
            self.items.remove(item_a_eliminar)
            print(f"🗑️ Producto eliminado del inventario: {item_a_eliminar}")

        except ValueError:
            print(f"⚠️ El producto '{item_a_eliminar}' no existe en el inventario.")


def menu():
    crud = CRUDListas()

    while True:

        print("\n===== INVENTARIO DE LA TIENDA (LISTA) =====")
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
            nuevo = input("Nuevo producto: ").strip()
            if nuevo:
                crud.agregar(nuevo)
            else:
                print("⚠️ No se agregó: nombre vacío.")

        elif opcion == "3":
            buscado = input("Producto a buscar: ").strip()
            crud.buscar(buscado)

        elif opcion == "4":

            crud.listar()

            try:
                indice = int(input("Índice del producto a actualizar: ").strip())
                nuevo_valor = input("Nuevo nombre del producto: ").strip()
                crud.actualizar(indice, nuevo_valor)

            except ValueError:
                print("⚠️ Índice inválido.")

        elif opcion == "5":

            eliminar = input("Producto a eliminar: ").strip()
            crud.eliminar(eliminar)

        elif opcion == "0":

            print("👋 Saliendo del sistema de inventario...")
            break

        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    menu()