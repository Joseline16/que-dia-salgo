dias = [
    {"fecha": "2026-10-18", "temp_max": 17.2, "temp_min": 13.7, "lluvia": 7.6, "viento": 13.7},
    {"fecha": "2026-10-19", "temp_max": 17.7, "temp_min": 12.6, "lluvia": 0.1, "viento": 13.3},
    {"fecha": "2026-10-20", "temp_max": 19.3, "temp_min": 12.2, "lluvia": 0.0, "viento": 24.6},
    {"fecha": "2026-10-21", "temp_max": 18.7, "temp_min": 9.3, "lluvia": 0.0, "viento": 14.9},
    {"fecha": "2026-10-22", "temp_max": 21.2, "temp_min": 5.1, "lluvia": 0.0, "viento": 13.7},
    {"fecha": "2026-10-23", "temp_max": 20.2, "temp_min": 10.3, "lluvia": 0.0, "viento": 18.4},
    {"fecha": "2026-10-24", "temp_max": 20.4, "temp_min": 8.3, "lluvia": 0.0, "viento": 11.0},
]



def media(numeros):
    return sum(numeros)/len(numeros)

print(media([10,20,30]))


def describir_dia(dia):
    return f"{dia['fecha']}: max {dia['temp_max']} ºC, lluvia {dia['lluvia']} mm"

print(describir_dia(dias[0]))

print(describir_dia(dias[4]))