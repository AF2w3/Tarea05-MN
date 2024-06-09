# Método de la Secante
import math

def f(x):
    return -x**3 - math.cos(x)

def metodo_de_la_secante(p0, p1, tolerancia, max_iteraciones):
    for k in range(1, max_iteraciones + 1):
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tolerancia:
            return p2
        p0 = p1
        p1 = p2
    return p2

def main():
    p0 = -1
    p1 = -0.5
    tolerancia = 1e-6
    max_iteraciones = 100
    p2 = metodo_de_la_secante(p0, p1, tolerancia, max_iteraciones)
    print(f"Valor de p2 usando método de la secante es: {p2:.3}")


main()
