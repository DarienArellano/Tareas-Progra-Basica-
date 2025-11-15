import re
clave_usuario = "MiClave123"
if (len(clave_usuario) >= 8 and
    re.search(r'[A-Z]', clave_usuario) and
    re.search(r'[a-z]', clave_usuario) and
    re.search(r'\d', clave_usuario)):
    print("Contraseña segura")
else:
    print("Insegura")
