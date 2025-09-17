nombres = []
ahorros = []
n = int(input("Número de ahorradores: "))
for i in range(n):
    nombres.append(input(f"Nombre del ahorrador {i+1}: "))
    ahorros.append(float(input(f"Ahorro de {nombres[i]}: ")))
print("\nReporte de ahorradores:")
for i in range(n):
    if ahorros[i] < 1000:
        print(f"{nombres[i]} no tendrás para tu futuro")
    elif ahorros[i] >= 1000000:
        print(f"{nombres[i]} ya merito te retiras")
    else:
        print(f"{nombres[i]} sigue ahorrando")
