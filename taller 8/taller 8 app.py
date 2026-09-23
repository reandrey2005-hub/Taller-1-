import numpy as np

def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    return funcion_escalon(Z)


pesos = np.array([0.5, 0.5]) # Vector W (se mantiene)
sesgo = -0.2                 # CAMBIO: antes -0.8 (AND)


for entradas in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    resultado = perceptron(np.array(entradas), pesos, sesgo)
    print(f"Entrada {entradas} -> {resultado}")