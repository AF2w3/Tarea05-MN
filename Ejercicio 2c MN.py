from math import cos, sin, pi

def f(x):
    return x - cos(x)

def f_derivada(x):
    return 1 + sin(x)

def metodo_newton():
    p0 = pi / 4  # Punto inicial dentro del intervalo [0, pi/2]
    tolerancia = 1e-4
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p1 = p0 - f(p0) / f_derivada(p0)
        if abs(p1 - p0) < tolerancia:
            return f" El resultado de la ecuación x - cos x = 0 es: {p1:.4}"
        p0 = p1

    return "No se encontró una solución dentro de la tolerancia"

resultado = metodo_newton()
print(resultado)