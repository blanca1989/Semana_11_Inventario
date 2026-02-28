# TUPLA = ordenada + inmutable

producto = ("Arroz", 1.25, 50)  # nombre, precio, stock

print("Producto:", producto)

# Acceso por índice
print("Precio del producto:", producto[1])

# Intento de cambio (debería fallar porque la tupla es inmutable)
# producto[0] = "Azúcar"   # Descomenta para ver el error TypeError