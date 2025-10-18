import sympy as sp
variable_x = sp.Symbol('x')
ecuacion_uno = sp.Eq(variable_x**2 - 5*variable_x + 7, 0)
solucion_uno = sp.solve(ecuacion_uno)
print("a) Solución de la primera ecuación:", solucion_uno)
ecuacion_dos = sp.Eq(7*variable_x**2 + 9*variable_x - 7, 8*variable_x**2 - 2*variable_x - 3)
solucion_dos = sp.solve(ecuacion_dos)
print("b) Solución de la segunda ecuación:", solucion_dos)
