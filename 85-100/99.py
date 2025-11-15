import requests
valor_ingresado = input("Escribe un número: ")
enlace_num = f"https://numbersapi.com/{valor_ingresado}?json"
peticion_num = requests.get(enlace_num)
contenido_num = peticion_num.json()
print("Trivia:", contenido_num["text"])
