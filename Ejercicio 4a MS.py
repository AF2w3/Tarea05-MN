# Método de la Secante
def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

def metodo_secante():
    p0 = -1
    p1 = 0
    tolerancia = 1e-6
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tolerancia:
            return f" La solución del polinomio de cuarto grado es: {p2:0.4}"
        p0 = p1
        p1 = p2

    return "No se encontró una solución dentro de la tolerancia"

resultado = metodo_secante()
print(resultado)






