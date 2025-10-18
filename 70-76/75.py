import sys
if len(sys.argv) != 3:
    print("Uso: python lector.py <nombre_archivo> <num_lineas>")
    sys.exit()
archivo_objetivo = sys.argv[1]
num_lineas = sys.argv[2]
if not num_lineas.isdigit():
    print("El segundo argumento debe ser un número entero.")
    sys.exit()
try:
    with open(archivo_objetivo, "r", encoding="utf-8") as f:
        limite = int(num_lineas)
        for i, fila in enumerate(f):
            if i >= limite:
                break
            print(fila.strip())
except FileNotFoundError:
    print("El archivo no existe.")
