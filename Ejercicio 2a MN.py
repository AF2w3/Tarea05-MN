# Método de Newton
def f(x):
    return x**3 - 2*x**2 - 5

def f_derivada(x):
    return 3*x**2 - 4*x

def metodo_de_newton(p0, tolerancia, max_iteraciones):
    for k in range(1, max_iteraciones + 1):
        p1 = p0 - f(p0) / f_derivada(p0)
        if abs(p1 - p0) < tolerancia:
            return p1
        p0 = p1
    return p0

def main():
    p0 = (1 + 4) / 2
    tolerancia = 1e-4
    max_iteraciones = 100
    solucion = metodo_de_newton(p0, tolerancia, max_iteraciones)
    print(f" El resultado de la ecuacion x^3-2x^2-5=0 es: {solucion:.4}")

main()