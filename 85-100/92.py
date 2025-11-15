import re
parrafo_texto = "¡Hola mundo! Esto es una prueba. ¿Te gusta programar en Python?"
fragmentos = re.split(r'[.!?]+', parrafo_texto)
frases_limpias = [parte.strip() for parte in fragmentos if parte.strip()]
for frase in frases_limpias:
    print(frase)
