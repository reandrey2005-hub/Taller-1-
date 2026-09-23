import numpy as np
from sklearn.neighbors import KNeighborsClassifier


X_entrenamiento = np.array([
    [20, 30, 0],
    [22, 32, 0],
    [25, 35, 1],
    [28, 38, 0],
    [23, 28, 0],
    [26, 30, 1],
    [40, 50, 2],
    [35, 45, 1],
    [45, 60, 3],
    [38, 52, 2],
    [42, 55, 2],
    [50, 65, 3]
])


Y_entrenamiento = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


nuevo_cliente = np.array([[30, 40, 1]])


for k in [1, 5]:
    modelo_knn = KNeighborsClassifier(n_neighbors=k)
    modelo_knn.fit(X_entrenamiento, Y_entrenamiento)
    prediccion = modelo_knn.predict(nuevo_cliente)
    print(f"K={k} -> Clase predicha:", prediccion[0])