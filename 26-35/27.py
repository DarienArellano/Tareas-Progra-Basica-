incognita= input("Ingrese la operacion que desea realizar: ")
if incognita == "perimetro":
    lado = float(input("Ingrese el valor del lado del cuadrado: "))
    perimetro = lado * 4
    print("El perimetro del cuadrado es: ", perimetro)
elif incognita == "area":
    lado = float(input("Ingrese el valor del lado del cuadrado: "))
    area = lado * lado
    print("El area del cuadrado es: ", area)
else:
    print("Error al ingresar la operacion")