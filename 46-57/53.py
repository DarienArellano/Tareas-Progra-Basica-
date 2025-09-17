datos = []
while True:
    valor = input("Ingrese un dato (o 'no' para terminar): ")
    if valor.lower() == "no":
        break
    datos.append(valor)
print("\nLista ordenada:")
print(sorted(datos))
