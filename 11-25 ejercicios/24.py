capital_inicial= float(input("Ingrese el capital inicial: "))
tasa_interes= float(input("Ingrese la tasa de interés (en %): "))
periodo= int(input("Ingrese el numero de periodos: "))
i= tasa_interes / 100
monto_simple= capital_inicial * (1 + i * periodo)
monto_compuesto= capital_inicial * (1 + i) ** periodo
print(f"El monto total con interés simple es:", monto_simple)
print(f"El monto total con interés compuesto es:", monto_compuesto)
