import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="PME Convivencia - Profe Oriela")
st.title("🛡️ Generador de Acciones PME")

with st.sidebar:
    api_key = st.text_input("Ingresa tu Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        objetivo = st.text_area("¿Cuál es el nudo crítico?")
        if st.button("Generar Acción"):
            res = model.generate_content(f"Redacta una acción PME para convivencia sobre: {objetivo}")
            st.write(res.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Ingresa la clave en la izquierda.")
