import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

st.title("🔐 Test de conexión con Google Sheets")

try:
    # 1. Cargar credenciales desde secrets
    creds_dict = st.secrets["GOOGLE_SHEETS_CREDENTIALS"]
    spreadsheet_id = st.secrets["SPREADSHEET_ID"]

    # 2. Crear credenciales
    creds = Credentials.from_service_account_info(creds_dict)
    client = gspread.authorize(creds)

    # 3. Abrir hoja de cálculo
    sheet = client.open_by_key(spreadsheet_id)
    worksheet = sheet.sheet1  # la primera hoja

    # 4. Escribir un valor de prueba en la celda A1
    worksheet.update("A1", "✅ Conexión funcionando")

    # 5. Leer los primeros 5 registros y mostrarlos
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    st.success("Google Sheets conectado correctamente 🎉")
    st.write("Primeras filas leídas de la hoja:")
    st.dataframe(df.head())

except Exception as e:
    st.error(f"❌ Error conectando a Google Sheets: {e}")
