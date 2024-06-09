# Método de Newton
def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

def f_derivada(x):
    return 920*x**3 + 54*x**2 + 18*x - 221

def metodo_newton():
    p0 = -0.5  # Punto medio del intervalo
    tolerancia = 1e-6
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p1 = p0 - f(p0) / f_derivada(p0)
        if abs(p1 - p0) < tolerancia:
            return f" La solución del polinomio de cuarto grado es: {p1:0.4}"
        p0 = p1

    return "No se encontró una solución dentro de la tolerancia"

resultado = metodo_newton()
print(resultado)







