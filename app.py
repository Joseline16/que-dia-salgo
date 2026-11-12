import streamlit as st

from clima import buscar_ciudad,  obtener_prevision

st.title("¿Qué día salgo?")
st.write("Te digo cuál es el mejor día de la semana para hacer deporte al aire libre.")

nombre = st.text_input("¿En qué ciudad estás?", "Madrid")

ciudad = buscar_ciudad(nombre)

if ciudad is None:
    st.warning(f"No encuentro ninguna ciudad llamada '{nombre}'.")
    st.stop()

st.subheader(f"Previsión para {ciudad['nombre']} ({ciudad['pais']})")

dias = obtener_prevision(ciudad["latitud"], ciudad["longitud"])
st.write(dias)