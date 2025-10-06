import streamlit as st
import json
import gspread
from google.oauth2.service_account import Credentials

st.title("🔐 Test de conexión con Google Sheets")

try:
    # Leer credenciales como JSON desde secrets
    creds_json = st.secrets["GOOGLE_SHEETS_CREDENTIALS"]
    creds_dict = json.loads(creds_json)

    # Crear credenciales
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    # Conectar con Google Sheets
    client = gspread.authorize(creds)
    sheet = client.open_by_key(st.secrets["SPREADSHEET_ID"])
    worksheet = sheet.sheet1
    values = worksheet.get_all_values()

    st.success("✅ Conectado correctamente a Google Sheets")
    st.write("Primera fila:", values[0] if values else "Hoja vacía")

except Exception as e:
    st.error(f"❌ Error conectando a Google Sheets: {e}")
