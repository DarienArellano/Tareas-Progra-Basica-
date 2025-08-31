edad= int(input("Ingrese su edad: "))
if int(edad) <0 or int(edad) > 120:
    print("Edad invalida")
else: 
    if int(edad) < 10:
        print("Eres un niño")
    elif int(edad) < 17:
        print("Eres un adolescente")
    elif int(edad) < 29:
        print("Eres un joven")
    elif int(edad) < 59:
        print("Eres un adulto")
    else:    
        print("Eres un adulto mayor")