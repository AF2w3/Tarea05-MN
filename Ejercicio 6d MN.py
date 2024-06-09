# Método de la Secante
from math import log, exp, cos, pi

def f(x):
    return log(x**2 + 1) - exp(0.4 * x) * cos(pi * x)

def metodo_secante():
    p0 = 0.5
    p1 = 1
    tolerancia = 1e-6
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tolerancia:
            return f"La solución de la función es f(x) = ln(x^2 + 1) - exp(0.4 * x) * cos(pi * x) es : {p2:.4}"
        p0 = p1
        p1 = p2

    return f"No se encontró una solución dentro de la tolerancia después de {max_iteraciones} iteraciones"

resultado = metodo_secante()
print(resultado)



