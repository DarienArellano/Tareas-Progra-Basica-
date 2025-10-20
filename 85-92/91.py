import re
cadena_emails = "Contacta a manueldarien@gmail.com, aron8a@hotmail.com o roberto@empresa.com"
nombres_usuarios = re.findall(r'([\w\.-]+)@[\w\.-]+\.\w+', cadena_emails)
print(nombres_usuarios)
