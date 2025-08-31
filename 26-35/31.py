calificacion=float(input("Ingrese la calificación del estudiante: "))
if calificacion<6:
    print("La calificacion es irregular")
elif calificacion <= 9.9:
    print("La calificacion es regular")
elif calificacion == 10:
    print("La calificacion es excelencia")
else:
    print("Calificacion no valida")