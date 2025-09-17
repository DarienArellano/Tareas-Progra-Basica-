materias = []
calificaciones = []
n = int(input("Ingrese el número de materias: "))
for i in range(n):
    materia = input(f"Nombre de la materia {i+1}: ")
    calif = float(input(f"Calificación de {materia}: "))
    materias.append(materia)
    calificaciones.append(calif)
promedio = sum(calificaciones) / n
print("\nResultados:")
for i in range(n):
    print(f"{materias[i]}: {calificaciones[i]}")
print(f"\nPromedio general = {promedio:.2f}")
