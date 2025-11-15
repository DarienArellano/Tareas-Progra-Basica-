import requests
import json
origen = "https://api.github.com"
solicitud = requests.get(origen)
paquete = solicitud.json()
with open("respuesta.json", "w", encoding="utf-8") as salida:
    json.dump(paquete, salida, ensure_ascii=False, indent=4)
print("Archivo generado correctamente.")
