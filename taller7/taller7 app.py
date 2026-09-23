import numpy as np
from sklearn.svm import SVC


X = np.array([ [2,2], [3,3], [4,2], [6,6], [7,8], [8,7], [5,5] ])
Y = np.array([ 0, 0, 0, 1, 1, 1, 0 ])

nuevo_punto = np.array([[5, 4]])

modelo_lineal = SVC(kernel='linear')
modelo_lineal.fit(X, Y)
print("Vectores de Soporte (linear):\n", modelo_lineal.support_vectors_)
print("Predicción [5,4] (linear):", modelo_lineal.predict(nuevo_punto)[0])


modelo_rbf = SVC(kernel='rbf')
modelo_rbf.fit(X, Y)
print("Vectores de Soporte (rbf):\n", modelo_rbf.support_vectors_)
print("Predicción [5,4] (rbf):", modelo_rbf.predict(nuevo_punto)[0])