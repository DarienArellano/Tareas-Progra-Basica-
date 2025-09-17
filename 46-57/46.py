numeros = []
for i in range(10):
    num = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(num)

print("\nnumeros al cuadrado:")
for n in numeros:
    print(f"{n}^2 = {n**2}")
