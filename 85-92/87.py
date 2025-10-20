import re
mensaje = "Peso 48.5 kg, mido 1.63 metros y tengo 3 perros"
valores = re.findall(r'-?\d*\.?\d+', mensaje)
lista_numeros = [float(x) for x in valores if x != '']
print(lista_numeros)
