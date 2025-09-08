c = float(input("Ingrese el capital incial: "))
i = float(input("Ingrese la tasa de interes: "))
n = float(input("Ingrese el numero de periodos: "))
M = c * (1 + i) ** n
print("El monto final es:", M)

respuesta = input("Desea continuar? (s/n): ")
while respuesta == "s":
    c = float(input("Ingrese el capital incial: "))
    i = float(input("Ingrese la tasa de interes: "))
    n = float(input("Ingrese el numero de periodos: "))
    M = c * (1 + i) ** n
    print("El monto final es:", M)
    print("Desea continuar? (s/n): ")
    respuesta = input()
if respuesta == "n":
    print("Gracias por usar el programa")




