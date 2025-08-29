nombre= input("Ingrese el nombre del estudiante: ")
boleta= input("Ingrese el número de boleta: ")
calificacion1= float(input("Ingrese la calificación 1: "))
calificacion2= float(input("Ingrese la calificación 2: "))
calificacion3= float(input("Ingrese la calificación 3: "))
calificacion4= float(input("Ingrese la calificación 4: "))
calificacion5= float(input("Ingrese la calificación 5: "))
promedio= (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5
print("El estudiante", nombre, "con boleta", boleta, "tiene un promedio de:", promedio)