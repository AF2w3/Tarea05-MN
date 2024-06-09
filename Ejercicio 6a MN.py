# Método de Newton

from math import log, exp, cos, sin, pi

def f(x):
    return log(x**2 + 1) - exp(0.4 * x) * cos(pi * x)

def f_derivada(x):
    return (2 * x) / (x**2 + 1) - 0.4 * exp(0.4 * x) * cos(pi * x) + 0.4 * pi * exp(0.4 * x) * sin(pi * x)

def metodo_newton():
    p0 = -1
    tolerancia = 1e-6
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p1 = p0 - f(p0) / f_derivada(p0)
        if abs(p1 - p0) < tolerancia:
            return p1
        p0 = p1

    return f"No se encontró una solución dentro de la tolerancia después de {max_iteraciones} iteraciones"

resultado = metodo_newton()
print(resultado)