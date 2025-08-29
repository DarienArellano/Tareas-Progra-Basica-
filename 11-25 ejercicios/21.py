evento= input("Ingrese el nombre del evento: ")
fecha= input("Ingrese la fecha del evento: ")
asistentes= input("Ingrese la cantidad de asistentes: ")
agua= 1.5 * int(asistentes)
carne= 0.350 * int(asistentes)
salsa= agua/4
print(f"Para el evento {evento} que se realizara el dia {fecha} se necesitaran {agua} litros de agua, {carne} kg de carne y {salsa} litros de salsa.")

