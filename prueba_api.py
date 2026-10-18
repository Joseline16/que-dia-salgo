import requests

url = "https://api.open-meteo.com/v1/forecast"
parametros = {
    "latitude": 40.42,
    "longitude": -3.70,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
    "timezone": "Europe/Madrid",
}
#hace la misma peticion que el navegador. 
respuesta = requests.get(url, params=parametros)
#dice si la conexion a la api esta correcta. 200 ok 
print("Codigo de estado:", respuesta.status_code)
#convierte el texto JSON en un diccionario de Python
datos = respuesta.json()
diario = datos["daily"]

#recorre las posiciones de 0 a 6 y para cada dia
#saca el dto de cada lista en esa posicion
for i in range(len(diario["time"])):
    print(
        diario["time"][i],
        "| max:", diario["temperature_2m_max"][i],
        "| min:", diario["temperature_2m_min"][i],
        "| lluvia:", diario["precipitation_sum"][i],
        "| viento:", diario["wind_speed_10m_max"][i],
    )