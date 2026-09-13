# 1. Grados de membresía actuales (Resultados de la Fuzzificación)
grados = {
    "rentabilidad_alta": 0.6,
    "impacto_alto": 0.2,
    "riesgo_bajo": 0.4,
    "riesgo_alto": 0.7
}

# 2. Evaluación de Reglas Mamdani
def evaluar_reglas_proyecto(grados):

    # REGLA 1: SI (Rentabilidad_ALTA O Impacto_ALTO) Y Riesgo_BAJO
    # ENTONCES Aprobacion = SEGURA
    fuerza_or = max(grados["rentabilidad_alta"], grados["impacto_alto"])
    activacion_r1 = min(fuerza_or, grados["riesgo_bajo"])

    # REGLA 2: SI Riesgo_ALTO ENTONCES Aprobacion = DENEGADA
    activacion_r2 = grados["riesgo_alto"]

    return {"SEGURA": activacion_r1, "DENEGADA": activacion_r2}

# Ejecución
fuerza_conclusiones = evaluar_reglas_proyecto(grados)
print("Fuerza de activación para cada conclusión:", fuerza_conclusiones)