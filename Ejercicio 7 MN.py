#Método de Newton

def f(x):
    return x**(1/3)

def f_derivada(x):
    return (1/3) * x**(-2/3)

def encontrar_solucion():
    p0 = 1
    tolerancia = 1e-6
    max_iteraciones = 100

    for i in range(1, max_iteraciones + 1):
        p1 = p0 - f(p0) / f_derivada(p0)
        if abs(p1 - p0) < tolerancia:
            return p1
        p0 = p1

    return f"No se encontró una solución dentro de la tolerancia después de {max_iteraciones} iteraciones"

resultado = encontrar_solucion()
print(resultado)