# SET = elementos únicos + sin orden + no indexado

productos = [
    "Arroz",
    "Leche",
    "Arroz",   # duplicado
    "Azúcar"
]

inventario_unico = set(productos)

print("Inventario original:", productos)
print("Productos únicos:", inventario_unico)

# Agregar producto nuevo
inventario_unico.add("Aceite")
print("Con add:", inventario_unico)

# Verificar existencia (búsqueda rápida)
print("¿Existe Leche?", "Leche" in inventario_unico)

# Operaciones de conjuntos entre categorías de productos
grupo_alimentos = {"Arroz", "Leche", "Pan"}
grupo_limpieza = {"Leche", "Detergente"}

print("Unión de productos:", grupo_alimentos | grupo_limpieza)
print("Intersección de productos:", grupo_alimentos & grupo_limpieza)
print("Diferencia de productos:", grupo_alimentos - grupo_limpieza)
