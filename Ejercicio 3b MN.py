# Método de Newton
from math import cos, sin, exp

def f(x):
    return 2*x + 3*cos(x) - exp(x)

def f_derivada(x):
    return 2 - 3*sin(x) - exp(x)

def metodo_newton():
    p0 = 1.5  # Punto inicial dentro del intervalo [1, 2]
    tolerancia = 1e-5
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p1 = p0 - f(p0) / f_derivada(p0)
        if abs(p1 - p0) < tolerancia:
            return f" La solución de la ecuación 2x + 3 * cos(x) - e^x = 0 es: {p1:.4}"
        p0 = p1

    return "No se encontró una solución dentro de la tolerancia"

resultado = metodo_newton()
print(resultado)