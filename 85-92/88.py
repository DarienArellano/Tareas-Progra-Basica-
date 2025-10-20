import re
parrafo = "Mis cumpleaños fueron 05/02/2023, 12/09/2024 y 01/01/2025"
dias_encontrados = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', parrafo)
print(dias_encontrados)
