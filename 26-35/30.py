valor1= float(input("Ingrese el precio uniatario del producto: "))
valor2= int(input("Ingrese la cantidad vendida: "))
valor3= float(input("Ingrese la cantidad de egreso de la empresa: "))
ingreso= valor1 * valor2
if ingreso<valor3:
    print("La empresa tuvo perdidas")
elif ingreso>valor3:
    print("La empresa tuvo ganancias")
elif ingreso==valor3:
    print("La empresa esta en equilibrio")
