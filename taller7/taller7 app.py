import numpy as np
from sklearn.svm import SVC

# 1. Crear el dataset (X = Coordenadas, Y = Etiquetas binarias 0 o 1)
X = np.array([ [2,2], [3,3], [4,2], [6,6], [7,8], [8,7] ])
Y = np.array([ 0, 0, 0, 1, 1, 1 ])

# 2. Inicializar SVM con Kernel Lineal
modelo_svm = SVC(kernel='linear')

# 3. Entrenar el modelo (Aprender la ecuación del hiperplano)
modelo_svm.fit(X, Y)

# 4. Extraer los Vectores de Soporte descubiertos por la IA
vectores = modelo_svm.support_vectors_
print("Los Vectores de Soporte son:\n", vectores)

# 5. Predicción
nuevo_punto = np.array([[5, 4]])
pred = modelo_svm.predict(nuevo_punto)
print("El punto [5,4] pertenece a la clase:", pred[0])