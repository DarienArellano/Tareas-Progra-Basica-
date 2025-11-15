import requests
direccion = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"
respuesta_clima = requests.get(direccion)
datos = respuesta_clima.json()
temp_actual = datos["current_weather"]["temperature"]
vel_viento = datos["current_weather"]["windspeed"]
print("Temperatura:", temp_actual, "°C")
print("Viento:", vel_viento, "km/h")
