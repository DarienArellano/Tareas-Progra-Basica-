import pandas as pd
lista_productos = ['Fresa', 'Durazno', 'Mango']
lista_precios = [12, 10, 25]
lista_cantidades = [5, 8, 3]
tabla_frutas = pd.DataFrame({
    'Producto': lista_productos,
    'Precio': lista_precios,
    'Cantidad': lista_cantidades
})
print("Tabla de frutas:\n", tabla_frutas)
