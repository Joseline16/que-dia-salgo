import requests

def buscar_ciudad(nombre):
    """Devuelve nombre, paísm latitud y longitud de una ciudad o None si no existe."""

    url = "https://geocoding-api.open-meteo.com/v1/search"
    parametros = {"name": nombre, "count": 1, "language": "es"}

    respuesta = requests.get(url,params=parametros,timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()

    if "results" not in datos:
        return None

    ciudad = datos["results"][0]
    return{
        "nombre": ciudad ["name"],
        "pais": ciudad.get("country",""),
        "latitud": ciudad["latitude"],
        "longitud": ciudad["longitude"],

    }
def obtener_prevision(latitud, longitud):
    """Devuelve una lista con la previsión de los próximos 7 días."""
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
        "timezone": "Europe/Madrid",
    }

    respuesta = requests.get(url, params=parametros, timeout=10)
    respuesta.raise_for_status()
    diario = respuesta.json()["daily"]

    dias = []
    for i in range(len(diario["time"])):
        dias.append({
            "fecha": diario["time"][i],
            "temp_max": diario["temperature_2m_max"][i],
            "temp_min": diario["temperature_2m_min"][i],
            "lluvia": diario["precipitation_sum"][i],
            "viento": diario["wind_speed_10m_max"][i],
        })
    return dias

if __name__ == "__main__":
    ciudad = buscar_ciudad("Albacete")
    print(ciudad)

    if ciudad: 
        for dia in obtener_prevision(ciudad["latitud"],ciudad["longitud"]):
            print (dia)
