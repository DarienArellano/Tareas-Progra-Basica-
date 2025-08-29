x1= input("Ingrese el valor de x1:")
x2= input("Ingrese el valor de x2:")
y1= input("Ingrese el valor de y1:")
y2= input("Ingrese el valor de y2:")
pendiente= (float(y2)-float(y1))/(float(x2)-float(x1))
b= float(y1)-pendiente*float(x1)
print("La pendiente es:", pendiente)
print("La ecuacion en forma pendiente-interseccion es: y=", pendiente, "x +", b)

