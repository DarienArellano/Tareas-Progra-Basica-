import math as mt
angulo_grados = 45
operacion_trig = mt.sin(mt.radians(angulo_grados)) + mt.cos(mt.pi)
print("a) Seno de 45° + coseno de pi =", operacion_trig)
exponente_valor = mt.e ** 2
resultado_raiz = mt.sqrt(exponente_valor)
print("b) Raíz de e elevado a la dos =", resultado_raiz)
producto_valores = mt.pi * mt.sqrt(2)
producto_redondeado = round(producto_valores, 3)
print("c) Multiplicación entre pi y raíz de dos =", producto_redondeado)
