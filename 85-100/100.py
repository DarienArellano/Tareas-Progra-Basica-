import requests
ruta_api = "https://pokeapi.co/api/v2/pokemon?limit=5"
peticion_poke = requests.get(ruta_api)
datos_poke = peticion_poke.json()
lista_resultados = datos_poke["results"]
for elemento in lista_resultados:
    print(elemento["name"])
