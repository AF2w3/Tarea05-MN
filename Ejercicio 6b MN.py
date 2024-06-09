# Método de Newton
from math import log, exp, cos, sin, pi

def f(x):
    return log(x**2 + 1) - exp(0.4 * x) * cos(pi * x)

def f_derivada(x):
    return (2 * x) / (x**2 + 1) - 0.4 * exp(0.4 * x) * cos(pi * x) + 0.4 * pi * exp(0.4 * x) * sin(pi * x)

def encontrar_ceros():
    soluciones = []
    ceros_encontrados = 0
    p0 = 0.1  # Valor inicial positivo

    while ceros_encontrados < 4:
        #  método de Newton para encontrar la próxima solución
        p1 = p0 - f(p0) / f_derivada(p0)
        # Si la función cambia de signo, es posible que hayamos encontrado un cero
        if f(p0) * f(p1) < 0:
            soluciones.append(p1)
            ceros_encontrados += 1
        # Actualización del punto inicial p0
        p0 = p1 + 0.1
    return f"Soluciónes de la función f(x)=ln(x^2 +1)-e^0.4x es: {soluciones}"

resultado = encontrar_ceros()
print(resultado)

