nombre = input("Ingrese el nombre del vendedor: ")
ventas = float(input("Ingrese el volumen de ventas: "))
if ventas < 1000:
    print(f"El vendedor {nombre} esta despedido")
elif ventas <= 4999:
    print(f"EL vendedor {nombre} esta en periodo de prueba")
elif ventas <= 9999:
    print(f"El vendedor {nombre} tiene un bono del 5%")
elif ventas >= 10000:
    print(f"El vendedor {nombre} tiene un bono del 10%")
    