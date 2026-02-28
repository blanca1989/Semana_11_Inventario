# DICCIONARIO = pares clave:valor + mutable + acceso por clave

producto = {
    "nombre": "Arroz",
    "precio": 1.25,
    "stock": 50
}

print("Precio:", producto["precio"])

# Agregar nuevo dato
producto["categoria"] = "Alimentos"
print("Con categoría:", producto)

# Modificar dato
producto["stock"] = 60
print("Stock actualizado:", producto)

# Lectura segura con get (evita KeyError)
print("Proveedor:", producto.get("proveedor", "No registrado"))

# Iterar por items
for clave, valor in producto.items():
    print(clave, "=>", valor)

# Eliminar
producto.pop("precio")
print("Sin precio:", producto)