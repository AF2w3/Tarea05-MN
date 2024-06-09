# Método de Newton
from math import tan, pi

def f(x):
    return tan(pi * x) - 6

def metodo_secante():
    p0 = 0
    p1 = 0.48
    tolerancia = 1e-6
    max_iteraciones = 10

    for i in range(1, max_iteraciones + 1):
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tolerancia:
            return p2
        p0 = p1
        p1 = p2

    return f"No se encontró una solución dentro de la tolerancia después de {max_iteraciones} iteraciones"

resultado = metodo_secante()
print(resultado)

