import requests
endpoint = "https://numbersapi.com/42?json"
peticion = requests.get(endpoint)
info = peticion.json()
print(info["text"])
