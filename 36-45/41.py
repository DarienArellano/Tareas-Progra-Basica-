contra = input("Introduce una contraseña: ")
confirmacion = input("Vuelve a introducir la contraseña: ")
while confirmacion != contra:
    print("Las contraseñas no coinciden. Intenta de nuevo.")
    confirmacion = input("Vuelve a introducir la contraseña: ")

print("Contraseña confirmada")