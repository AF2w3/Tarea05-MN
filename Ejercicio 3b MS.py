# Método de la Secante

from math import cos, exp

def f(x):
    return 2*x + 3*cos(x) - exp(x)

def metodo_secante():
    p0 = 1
    p1 = 2
    tolerancia = 1e-5
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tolerancia:
            return f" La solución de la ecuación 2x + 3 * cos(x) - e^x = 0 es: {p2:.4}"
        p0 = p1
        p1 = p2

    return "No se encontró una solución dentro de la tolerancia"

resultado = metodo_secante()
print(resultado)