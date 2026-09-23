import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 1. Dataset de Entrenamiento: [Característica 1, Característica 2]
X_entrenamiento = np.array([
    [20, 30],  # Punto A
    [40, 50],  # Punto B
    [35, 45]   # Punto C
])

# Etiquetas: 0 = NO COMPRA, 1 = COMPRA
Y_entrenamiento = np.array([0, 1, 1])

# 2. Instanciar el modelo con K = 3
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# 3. "Entrenar" (Memorizar los datos)
modelo_knn.fit(X_entrenamiento, Y_entrenamiento)

# 4. Predecir un nuevo punto
nuevo_cliente = np.array([[30, 40]])
prediccion = modelo_knn.predict(nuevo_cliente)

print("Clase predicha:", prediccion[0])