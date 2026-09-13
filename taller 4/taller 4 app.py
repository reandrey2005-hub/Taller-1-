import numpy as np

def centro_de_gravedad(x, curva):
    """Implementa la formula del Centroide (COG):
    COG = Sum(x * mu(x)) / Sum(mu(x))
    usando operaciones matriciales de NumPy."""
    x = np.array(x, dtype=float)
    curva = np.array(curva, dtype=float)
    return np.sum(x * curva) / np.sum(curva)


x_validacion = [10, 20, 30, 40]
mu_validacion = [0.2, 0.8, 0.8, 0.0]
resultado_validacion = centro_de_gravedad(x_validacion, mu_validacion)
print(f"Validacion COG (esperado 23.33): {resultado_validacion:.2f}")


x_frenado = np.linspace(0, 100, 100)

sigma = 15
centro = 70
curva_frenado = np.exp(-0.5 * ((x_frenado - centro) / sigma) ** 2)  # curva de Gauss


fuerza_frenado_crisp = centro_de_gravedad(x_frenado, curva_frenado)
print(f"Fuerza de frenado exacta (crisp): {fuerza_frenado_crisp:.2f} Newtons")