contrasena = input("Introduce una contraseña: ")
intentos = 3
for i in range(intentos):
    confirmacion = input("Vuelve a introducir la contraseña: ")
    if confirmacion == contrasena:
        print("¡Contraseña confirmada con éxito!")
        break
    else:
        print("Las contraseñas no coinciden.")
else:
    print("Cuenta cancelada")