trabajadores = []
asistencias = []
n = int(input("Ingrese el número de trabajadores: "))
for i in range(n):
    nombre = input(f"Nombre del trabajador {i+1}: ")
    asistencia = int(input(f"Asistencia de {nombre} (1=Sí, 0=No): "))
    trabajadores.append(nombre)
    asistencias.append(asistencia)
print("\nReporte de asistencia:")
for i in range(n):
    if asistencias[i] == 1:
        print(f"{trabajadores[i]} asistió a trabajar")
    else:
        print(f"{trabajadores[i]} no asistió a trabajar")
