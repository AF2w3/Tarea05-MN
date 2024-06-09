# Método Secante
def f(x):
    return x**3 + 3*x**2 - 1

def metodo_secante():
    p0 = -3
    p1 = 2
    tolerancia = 1e-4
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tolerancia:
            return f" El resultado de la ecuación x^3 + 3x^2 - 1 es: {p2:.4}"
        p0 = p1
        p1 = p2

    return "No se encontró una solución dentro de la tolerancia"

resultado = metodo_secante()
print(resultado)






