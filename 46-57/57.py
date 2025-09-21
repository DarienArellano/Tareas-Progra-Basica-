
lista = [5, 9, 10, 2, 42, 89]
valor = float(input("Ingresa el valor: "))
encontrado = False
for elemento in lista:
    if elemento == valor:
        encontrado = True
        break
if encontrado:
    print(f"El valor {valor} está en la lista.")
else:
    print(f"El valor {valor} no está en la lista.")