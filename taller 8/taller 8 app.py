import numpy as np

# 1. Definir la Función de Activación (Escalón)
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

# 2. Definir la Estructura de la Neurona
def perceptron(X, W, b):
    # Producto punto (Combinación lineal)
    # Equivalente a: (X[0]*W[0]) + (X[1]*W[1]) ...
    Z = np.dot(X, W) + b

    # Activación
    salida = funcion_escalon(Z)
    return salida

# 3. Datos del problema (Compuerta Lógica AND)
# El AND solo da 1 si ambas entradas son 1.
entradas = np.array([1, 1])  # Vector X
pesos = np.array([0.5, 0.5]) # Vector W
sesgo = -0.8                 # Constante b

# 4. Inferencia (Forward pass)
resultado = perceptron(entradas, pesos, sesgo)
print("El Perceptrón disparó el valor:", resultado)