import requests
direccion_api = "https://api.dictionaryapi.dev/api/v2/entries/en/example"
consulta_dic = requests.get(direccion_api)
bloque = consulta_dic.json()
vocablo = bloque[0]["word"]
significado = bloque[0]["meanings"][0]["definitions"][0]["definition"]
print("Término:", vocablo)
print("Definición:", significado)
