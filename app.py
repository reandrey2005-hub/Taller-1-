
hechos = {
    "monto": 7500,
    "pais_extranjero": True,
    "hora_nocturna": True,
    "cliente_frecuente": False
}


reglas = [
    {
        "id": "R1",
        "condicion": lambda h: h.get("monto", 0) > 5000,
        "conclusion": {"transaccion_inusual": True}
    },
    {
        "id": "R2",
        "condicion": lambda h: h.get("transaccion_inusual") == True and h.get("pais_extranjero") == True,
        "conclusion": {"bloquear_tarjeta": True}
    },
    {
        "id": "R3",
        "condicion": lambda h: h.get("transaccion_inusual") == True and h.get("hora_nocturna") == True,
        "conclusion": {"alerta_seguridad": True}
    },
    {
        "id": "R4",
        "condicion": lambda h: h.get("bloquear_tarjeta") == True and h.get("alerta_seguridad") == True,
        "conclusion": {"notificar_cliente": True}
    },
]


nuevos_hechos = True
ciclo = 0
while nuevos_hechos:
    ciclo += 1
    nuevos_hechos = False
    for regla in reglas:
        if regla["condicion"](hechos):
            for clave, valor in regla["conclusion"].items():
                if clave not in hechos:
                    hechos[clave] = valor
                    nuevos_hechos = True
                    print(f"Ciclo {ciclo} -> Disparando {regla['id']}: nuevo hecho {clave}={valor}")

print("\nMemoria final:", hechos)