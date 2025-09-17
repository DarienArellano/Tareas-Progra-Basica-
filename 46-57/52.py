productos = []
precios = []
ventas = []
for i in range(5):
    productos.append(input(f"Nombre del producto {i+1}: "))
    precios.append(float(input(f"Precio de {productos[i]}: ")))
    ventas.append(int(input(f"Ventas de {productos[i]}: ")))
print("\nReporte de productos")
print("Producto\tPrecio\tVentas\tIngreso")
for i in range(5):
    ingreso = precios[i] * ventas[i]
    print(f"{productos[i]}\t{precios[i]:.2f}\t{ventas[i]}\t{ingreso:.2f}")
