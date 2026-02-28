# ============================================
# MODELO: Producto
# Representa un ítem del inventario de la tienda
# ============================================

class Producto:

    # ----------- CONSTRUCTOR -----------
    def __init__(self, id_producto, nombre, precio, categoria):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria

    # ----------- GETTERS -----------
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_categoria(self):
        return self.__categoria

    # ----------- SETTERS -----------
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("⚠️ Precio inválido")

    def set_categoria(self, categoria):
        self.__categoria = categoria

    # ----------- MÉTODO STR -----------
    def __str__(self):
        return (
            f"[{self.__id_producto}] "
            f"{self.__nombre} | "
            f"${self.__precio:.2f} | "
            f"{self.__categoria}"
        )