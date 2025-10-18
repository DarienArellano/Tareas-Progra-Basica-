from numpy import sin
from scipy.integrate import quad
def funcion_trigonometrica(valor_x):
    return sin(valor_x ** 2)
limite_inferior = 0
limite_superior = 2
resultado_integral, error_estimado = quad(funcion_trigonometrica, limite_inferior, limite_superior)
print("El valor aproximado de la integral es:", format(resultado_integral, ".5f"))
print("Error estimado:", format(error_estimado, ".5e"))
