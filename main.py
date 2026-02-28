from servicios.inventario_servicio import InventarioServicio


def mostrar_menu():
    print("""
=============================
 🛒 SISTEMA INVENTARIO TIENDA
=============================
1. Agregar producto
2. Listar productos
3. Buscar producto por ID
4. Actualizar producto
5. Eliminar producto
6. Buscar producto por nombre
0. Salir
=============================
""")


def main():

    servicio = InventarioServicio()

    while True:

        mostrar_menu()

        try:
            opcion = int(input("Seleccione opción: "))

            if opcion == 1:
                servicio.agregar_producto()

            elif opcion == 2:
                servicio.listar_productos()

            elif opcion == 3:
                id_p = int(input("ID a buscar: "))
                p = servicio.buscar_por_id(id_p)

                if p:
                    print("🔎 Encontrado:", p)
                else:
                    print("❌ No existe")

            elif opcion == 4:
                servicio.actualizar_producto()

            elif opcion == 5:
                servicio.eliminar_producto()

            elif opcion == 6:
                nombre = input("Nombre a buscar: ")
                p = servicio.buscar_por_nombre(nombre)

                if p:
                    print("🔎 Encontrado:", p)
                else:
                    print("❌ No existe")

            elif opcion == 0:
                servicio.guardar_en_archivo()
                print("💾 Cambios guardados en inventario.txt")
                print("👋 Saliendo del sistema...")
                break

            else:
                print("⚠️ Opción inválida")

        except ValueError:
            print("⚠️ Debe ingresar números")


if __name__ == "__main__":
    main()