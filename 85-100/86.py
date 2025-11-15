import re
direccion = "usuario123@hotmail.com"
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', direccion):
    print("Válido")
else:
    print("Inválido")
