import requests
enlace_pk = "https://pokeapi.co/api/v2/pokemon/25"
respuesta_pk = requests.get(enlace_pk)
contenido = respuesta_pk.json()
etiqueta = contenido["name"]
catalogo_tipos = [t["type"]["name"] for t in contenido["types"]]
print("Nombre:", etiqueta)
print("Tipos:", catalogo_tipos)
