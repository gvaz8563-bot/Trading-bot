# app.py — versión básica de prueba
import streamlit as st
import datetime as dt

# Configuración de la página
st.set_page_config(page_title="Trading Bot 2025", layout="wide")

# Encabezado
st.title("🤖 Trading Bot 2025")
st.success("😊 Streamlit funcionando en modo básico")

# Mostrar hora actual
hora_actual = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"⏰ Hora actual: **{hora_actual}**")

# Mensaje de bienvenida
st.write("Bienvenido al panel básico del bot. 🚀")
