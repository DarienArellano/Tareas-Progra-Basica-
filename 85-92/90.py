import re
comentario = "Ese jugador es Muy tonto y además Feo."
lista_vetadas = ["tonto", "feo"]
for insulto in lista_vetadas:
    regex = re.compile(insulto, re.IGNORECASE)
    comentario = re.sub(regex, "*" * len(insulto), comentario)
print(comentario)
