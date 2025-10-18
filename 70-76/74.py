import os
carpeta = input("Dime el nombre de la carpeta: ")
if os.path.isdir(carpeta):
    archivos = os.listdir(carpeta)
    csv_encontrados = [doc for doc in archivos if doc.endswith(".csv")]
    csv_encontrados.sort()
    print("\nArchivos CSV encontrados (ordenados):")
    for item in csv_encontrados:
        print(item)
else:
    print("La carpeta no existe.")
