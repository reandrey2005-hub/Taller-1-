
grados = {
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.5,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.2,
    "antiguedad_larga": 0.6,
}

def evaluar_reglas_bono(grados):

 
    activacion_r1 = max(grados["desempeno_pobre"], grados["antiguedad_corta"])

  
    activacion_r2 = grados["desempeno_promedio"]

    activacion_r3 = min(grados["desempeno_excelente"], grados["antiguedad_larga"])

    return {"BAJO": activacion_r1, "MEDIO": activacion_r2, "ALTO": activacion_r3}


fuerza_bonos = evaluar_reglas_bono(grados)
print("Fuerza de activacion para cada nivel de bono:", fuerza_bonos)


activacion_r3a = 0.4
activacion_r3b = 0.7
bono_alto_final = max(activacion_r3a, activacion_r3b)
print(f"Fuerza final agregada para Bono ALTO (T-Conorma / OR): {bono_alto_final}")