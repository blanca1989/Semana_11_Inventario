# LISTA = ordenada + mutable + indexada

inventario = ["Arroz", "Leche", "Pan"]
print("Inventario inicial:", inventario)

# Acceso por índice (0,1,2...)
print("Primer producto:", inventario[0])

# Modificar (mutable)
inventario[1] = "Leche Descremada"
print("Inventario modificado:", inventario)

# Agregar al final
inventario.append("Azúcar")
print("Con append:", inventario)

# Insertar en posición
inventario.insert(1, "Aceite")
print("Con insert:", inventario)

# Eliminar por valor
inventario.remove("Pan")
print("Con remove:", inventario)

# Eliminar por índice y recuperar elemento
ultimo = inventario.pop()
print("Pop devuelve:", ultimo)

print("Inventario final:", inventario)