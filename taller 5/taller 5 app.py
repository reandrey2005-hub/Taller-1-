from sklearn.tree import DecisionTreeClassifier, export_text
import numpy as np


X = np.array([ [60, 0], [45, 1], [30, 0], [100, 1], [20, 1] ])

Y = np.array([ 1, 0, 1, 1, 0 ])


arbol = DecisionTreeClassifier(max_depth=3)
arbol.fit(X, Y)  # .fit() es el proceso de entrenamiento matemático


nombres_variables = ["Ingresos", "Tiene_Deuda"]
reglas_texto = export_text(arbol, feature_names=nombres_variables)

print("Base de Reglas generada automáticamente:\n")
print(reglas_texto)