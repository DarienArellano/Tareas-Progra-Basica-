opcion = input("\nBuscar por (indice/nombre/clave): ").lower()
if opcion == "indice":
    idx = int(input("Ingrese el índice: "))
    print(productos[idx])
elif opcion == "nombre":
    nombre_buscar = input("Ingrese el nombre del producto: ")
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(p)
elif opcion == "clave":
    clave_buscar = input("Ingrese la clave del producto: ")
    for p in productos:
        if p["clave"] == clave_buscar:
            print(p)
