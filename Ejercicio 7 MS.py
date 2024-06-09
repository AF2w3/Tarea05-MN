#Método de la Secante
def f(x):
    return x**(1/3)

p0 = 5
p1 = 0.5
tolerancia = 1e-6
max_iteraciones = 100

for i in range(1, max_iteraciones + 1):
    p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
    if abs(p2 - p1) < tolerancia:
        print("La solución es:", p2)
        break
    p0, p1 = p1, p2
else:
    print(f"No se encontró una solución dentro de la tolerancia después de {max_iteraciones} iteraciones")