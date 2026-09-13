from sklearn.tree import DecisionTreeClassifier, export_text
import numpy as np


X = np.array([
    [22,  8, 3],   # joven, mucho tiempo online, ya compro antes
    [25,  7, 2],
    [45,  1, 0],   # mayor, poco tiempo online, nunca compro
    [50,  0, 0],
    [23,  9, 4],
    [60,  1, 0],
    [30,  6, 2],
    [55,  2, 1],
    [21, 10, 5],
    [48,  1, 0],
    [28,  6, 1],
    [65,  0, 0],
])


Y = np.array([1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0])


arbol = DecisionTreeClassifier(max_depth=3)
arbol.fit(X, Y)  # .fit() es el proceso de entrenamiento matematico


nombres_variables = ["Edad", "Horas_Online", "Compras_Previas"]
reglas_texto = export_text(arbol, feature_names=nombres_variables)

print("Base de Reglas generada automaticamente:\n")
print(reglas_texto)