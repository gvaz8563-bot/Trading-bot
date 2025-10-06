# app.py — Versión básica sin Google Sheets

import streamlit as st
import pandas as pd
import datetime as dt

# =========================
# Datos de prueba (para no depender de Sheets)
# =========================
def load_data():
    # DataFrame vacío con las columnas que usamos
    return pd.DataFrame(columns=[
        "FechaISO","HoraLocal","Ticker","Side","Entrada",
        "Prob_1m","Prob_5m","Prob_15m","Prob_1h","ProbFinal",
        "Estado","Resultado","Nota","Mercado"
    ])

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Panel de Señales", layout="wide")

# Hora actual
hora_actual = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown("### ⏰ Hora local: " + hora_actual)

# Título y estado del bot
st.title("🤖 Bot 2025")
st.success("😊 Bot Activo – corriendo en modo básico (sin Google Sheets)")

# Cargar datos (de prueba por ahora)
df = load_data()

# Pestañas
tabs = st.tabs([
    "
