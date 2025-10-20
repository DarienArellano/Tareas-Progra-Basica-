import re
frase = "Mi Nombre Es Darien Y Me Gusta Programar En Python"
mayusculas = re.findall(r'\b[A-Z][a-zA-Z]*\b', frase)
print(mayusculas)
