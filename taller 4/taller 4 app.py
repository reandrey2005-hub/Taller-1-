# Requiere instalar: pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz


x_bono = np.arange(0, 1001, 1)


curva_resultado = fuzz.trimf(x_bono, [200, 500, 800])
# Suponemos que la regla cortó el triángulo a una altura máxima de 0.6
curva_truncada = np.fmin(curva_resultado, 0.6)


bono_final_crisp = fuzz.defuzz(x_bono, curva_truncada, 'centroid')

print(f"El bono exacto a pagar es: ${bono_final_crisp:.2f}")