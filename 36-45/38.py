numero = 0  

while numero < 1 or numero > 5:   
    numero = int(input("Ingresa un número entero entre 1 y 5: "))
    if numero < 1 or numero > 5:
        print("Número inválido, intenta de nuevo.")

print("¡Correcto! El número ingresado es:", numero)