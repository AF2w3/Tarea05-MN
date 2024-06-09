# Método de Newton
import math

def f(x):
    return -x**3 - math.cos(x)

def f_derivada(x):
    return -3*x**2 + math.sin(x)

def metodo_de_newton(p0, tolerancia, max_iteraciones):
    for k in range(1, max_iteraciones + 1):
        p1 = p0 - f(p0) / f_derivada(p0)
        if abs(p1 - p0) < tolerancia:
            return p1
        p0 = p1
    return p0

def main():
    p0 = -1
    tolerancia = 1e-6
    max_iteraciones = 100
    p2 = metodo_de_newton(p0, tolerancia, max_iteraciones)
    print(f"Valor de p2 usando método de newton es: {p2:.3}")

main()