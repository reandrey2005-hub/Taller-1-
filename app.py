
hechos = {"llueve": True, "tiene_paraguas": False}

reglas = [
    {"id": "R1",
     "condiciones": {"llueve": True, "tiene_paraguas": False},
     "conclusion": {"se_moja": True}},

    {"id": "R2",
     "condiciones": {"se_moja": True},
     "conclusion": {"se_resfria": True}}
]


nuevos_hechos = True
while nuevos_hechos:
    nuevos_hechos = False
    for regla in reglas:
        # Verifica si todas las condiciones de la regla están en los hechos
        condiciones_cumplidas = all(hechos.get(k) == v for k, v in regla["condiciones"].items())

        if condiciones_cumplidas:
            for clave, valor in regla["conclusion"].items():
                if clave not in hechos:  # Si es un HECHO NUEVO
                    hechos[clave] = valor
                    nuevos_hechos = True  # Dispara un nuevo ciclo
                    print(f"Disparando {regla['id']} -> Nuevo hecho: {clave}={valor}")

print("Memoria final:", hechos)