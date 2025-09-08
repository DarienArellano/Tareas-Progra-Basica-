numero= int(input("Introduzca un numero: "))
cuadrado= pow(numero,2)
print("El cuadrado de", numero, "es", cuadrado)
print("Desea continuar? (s/n)")
respuesta= input()
while respuesta == "s":
    numero= int(input("Introduzca un numero: "))
    cuadrado= pow(numero,2)
    print("El cuadrado de", numero, "es", cuadrado)
    print("Desea continuar? (s/n)")
    respuesta= input()
if respuesta == "n":
    print("Gracias por usar el programa")

