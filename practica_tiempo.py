dias = [
    {"fecha": "2026-10-18", "temp_max": 17.2, "temp_min": 13.7, "lluvia": 7.6, "viento": 13.7},
    {"fecha": "2026-10-19", "temp_max": 17.7, "temp_min": 12.6, "lluvia": 0.1, "viento": 13.3},
    {"fecha": "2026-10-20", "temp_max": 19.3, "temp_min": 12.2, "lluvia": 0.0, "viento": 24.6},
    {"fecha": "2026-10-21", "temp_max": 18.7, "temp_min": 9.3, "lluvia": 0.0, "viento": 14.9},
    {"fecha": "2026-10-22", "temp_max": 21.2, "temp_min": 5.1, "lluvia": 0.0, "viento": 13.7},
    {"fecha": "2026-10-23", "temp_max": 20.2, "temp_min": 10.3, "lluvia": 0.0, "viento": 18.4},
    {"fecha": "2026-10-24", "temp_max": 20.4, "temp_min": 8.3, "lluvia": 0.0, "viento": 11.0},
]

def hace_buen_tiempo(dia):
    return dia["lluvia"] == 0.0 and dia["viento"]<20.0
             
print(hace_buen_tiempo(dias[0]))
print(hace_buen_tiempo(dias[2]))
print(hace_buen_tiempo(dias[4]))

def fechas_buenas(dias):
    dias_buenos = []
    for d in dias:
        if hace_buen_tiempo(d):
            dias_buenos.append(d["fecha"])
    return dias_buenos

print(fechas_buenas(dias))

def dias_mas_frio(dias):
    minimo = dias[0]
    for dia in dias:
        if dia["temp_min"]<minimo["temp_min"]:
            minimo = dia
    return minimo

print(dias_mas_frio(dias))

def dia_mas_caluroso(dias):
    maximo = dias[0]
    for dia in dias:
        if dia["temp_max"]>maximo["temp_max"]:
            maximo = dia
    return maximo

print(dia_mas_caluroso(dias))

def total_lluvia(dias):
    total = 0
    for dia in dias:
        total += dia["lluvia"]
    return total
print(round(total_lluvia(dias),1))




def resumen(dias):
    return {
        "temp_max" : dias_mas_frio(dias)['temp_max'],
        "temp_min" : dia_mas_caluroso(dias)['temp_min'],
        "total_lluvia" : round(total_lluvia(dias),1),
    }
print(resumen(dias))

def puntuar_dia(dia):
    puntuacion = 10
    if dia["lluvia"]>0:
        puntuacion -= 3
    if dia["viento"]>20:
        puntuacion -= 2
    if dia["temp_max"]<18 :
        puntuacion -= 1
    return puntuacion
print(puntuar_dia(dias[2]))

def mejor_dia(dias):
    mejor = dias[0]
    for dia in dias:
        if puntuar_dia(dia)> puntuar_dia(mejor):
            mejor = dia
    return mejor

print(mejor_dia)