# ============================================
# SERVICIO: Gestión del Inventario
# CRUD de Productos
# ============================================

import os
from modelos.producto import Producto


class InventarioServicio:

    def __init__(self, ruta_archivo: str = None):

        base_dir = os.path.dirname(__file__)

        ruta_archivo = os.path.join(
            base_dir,
            "registros",
            "inventario.txt"
        )

        self.ruta_archivo = ruta_archivo
        self.productos = []  # Lista de productos
        self.cargar_desde_archivo()

    # ----------- ASEGURAR ARCHIVO -----------

    def asegurar_archivo(self):

        carpeta = os.path.dirname(self.ruta_archivo)

        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                pass

    # ----------- CARGAR DESDE ARCHIVO -----------

    def cargar_desde_archivo(self):

        self.asegurar_archivo()
        self.productos.clear()

        with open(self.ruta_archivo, "r", encoding="utf-8") as f:

            for linea in f:

                linea = linea.strip()

                if not linea:
                    continue

                producto = self._linea_a_producto(linea)

                if producto:
                    self.productos.append(producto)

    # ----------- GUARDAR EN ARCHIVO -----------

    def guardar_en_archivo(self):

        self.asegurar_archivo()

        with open(self.ruta_archivo, "w", encoding="utf-8") as f:

            for p in self.productos:
                f.write(self._producto_a_linea(p) + "\n")

    # ----------- CONVERSIÓN PRODUCTO -> TEXTO -----------

    def _producto_a_linea(self, producto: Producto):

        nombre = producto.get_nombre().replace("|", "/")
        categoria = producto.get_categoria().replace("|", "/")

        return f"{producto.get_id()}|{nombre}|{producto.get_precio()}|{categoria}"

    # ----------- CONVERSIÓN TEXTO -> PRODUCTO -----------

    def _linea_a_producto(self, linea):

        try:

            partes = linea.split("|")

            if len(partes) != 4:
                return None

            id_p = int(partes[0])
            nombre = partes[1]
            precio = float(partes[2])
            categoria = partes[3]

            return Producto(id_p, nombre, precio, categoria)

        except Exception:
            return None

    # ----------- AGREGAR PRODUCTO -----------

    def agregar_producto(self):

        try:

            id_p = int(input("ID del producto: "))
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")

            if self.buscar_por_id(id_p):
                print("⚠️ Ya existe un producto con ese ID")
                return

            nuevo = Producto(id_p, nombre, precio, categoria)

            self.productos.append(nuevo)

            print("✅ Producto agregado")

        except ValueError:
            print("⚠️ Error en los datos ingresados")

    # ----------- LISTAR PRODUCTOS -----------

    def listar_productos(self):

        if not self.productos:
            print("📭 No hay productos en el inventario")
            return

        print("\n📦 INVENTARIO DE LA TIENDA")

        for p in self.productos:
            print(p)

    # ----------- BUSCAR POR NOMBRE -----------

    def buscar_por_nombre(self, nombre_producto):

        for p in self.productos:

            if p.get_nombre() == nombre_producto:
                return p

        return None

    # ----------- BUSCAR POR ID -----------

    def buscar_por_id(self, id_producto):

        for p in self.productos:

            if p.get_id() == id_producto:
                return p

        return None

    # ----------- ACTUALIZAR PRODUCTO -----------

    def actualizar_producto(self):

        try:

            id_p = int(input("ID a actualizar: "))

            producto = self.buscar_por_id(id_p)

            if not producto:
                print("❌ Producto no encontrado")
                return

            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_categoria = input("Nueva categoría: ")

            producto.set_nombre(nuevo_nombre)
            producto.set_precio(nuevo_precio)
            producto.set_categoria(nueva_categoria)

            print("✅ Producto actualizado")

        except ValueError:
            print("⚠️ Datos inválidos")

    # ----------- ELIMINAR PRODUCTO -----------

    def eliminar_producto(self):

        try:

            id_p = int(input("ID a eliminar: "))

            producto = self.buscar_por_id(id_p)

            if not producto:
                print("❌ Producto no encontrado")
                return

            self.productos.remove(producto)

            print("🗑️ Producto eliminado")

        except ValueError:
            print("⚠️ ID inválido")