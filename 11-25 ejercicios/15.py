nombre= input("Ingrese el nombre del producto: ")
precio= float(input("Ingrese el precio del producto: "))
iva= precio * 0.16
total= precio + iva
print(f"el producto {nombre} tiene un precio final con IVA de", total)

