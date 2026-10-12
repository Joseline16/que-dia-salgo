import streamlit as st

st.title("¿Qué día salgo?")
st.write("Te digo cúal es el mejor día de la semana para hacer deporte al aire libre")

ciudad = st.text_input("¿En qué ciudad estás?", "Madrid")
st.write(f"Has elegido: {ciudad}")