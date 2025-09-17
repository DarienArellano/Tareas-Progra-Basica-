nombres = []
claves = []
existencias = []
n = int(input("Ingrese la cantidad de productos: "))
for i in range(n):
    nombres.append(input(f"Nombre del producto {i+1}: "))
    claves.append(input(f"Clave del producto {i+1}: "))
    existencias.append(int(input(f"Existencia del producto {i+1}: ")))
indice = int(input("\nIngrese el índice del producto que desea buscar (0 - {0}): ".format(n-1)))
print("\nInformación del producto:")
print(f"Nombre: {nombres[indice]}")
print(f"Clave: {claves[indice]}")
print(f"Existencia: {existencias[indice]}")
