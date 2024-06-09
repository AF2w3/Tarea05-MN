from math import sin, pi

def f(x):
    return x - 0.8 - 0.2 * sin(x)

def metodo_secante():
    p0 = 0
    p1 = pi / 4  # Punto inicial dentro del intervalo [0, pi/2]
    tolerancia = 1e-4
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tolerancia:
            return f" El resultado de la ecuación x - 0.8 - 0.2 * sen(x). es: {p2:.4}"
        p0 = p1
        p1 = p2

    return "No se encontró una solución dentro de la tolerancia "
resultado = metodo_secante()
print(resultado)