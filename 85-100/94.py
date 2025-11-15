import requests
enlace = "https://api.github.com"
consulta = requests.get(enlace)
print("Status:", consulta.status_code)
if consulta.status_code == 200:
    print("Todo bien")
else:
    print("Error en la solicitud")
