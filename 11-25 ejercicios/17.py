precio_venta= input("Ingrese el precio de venta:")
cantidad_vendida= input("Ingrese la cantidad vendida:")
costo_fijo= input("Ingrese el costo fijo:")
costo_variable= input("Ingrese el costo variable por pieza:")
ventas= float(precio_venta) * int(cantidad_vendida)
costo_total= float(costo_fijo) + (float(costo_variable) * int(cantidad_vendida))
ganancia= ventas - costo_total
print("El beneficio total de venta es:", ventas)