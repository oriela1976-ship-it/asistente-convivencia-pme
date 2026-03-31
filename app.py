import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Asistente Convivencia - Profe Oriela", page_icon="🏫")
st.title("🛡️ Generador de Acciones PME")
st.subheader("Coordinación de Convivencia Escolar")

with st.sidebar:
    st.title("Configuración")
    api_key = st.text_input("Ingresa tu Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        ambito = st.selectbox("Ámbito de la Acción", ["Formación", "Participación", "Prevención", "Gestión"])
        objetivo = st.text_area("¿Cuál es el nudo crítico o meta?")
        if st.button("✨ Generar Acción Técnica"):
            with st.spinner('Redactando...'):
                prompt = f"Actúa como experto en Convivencia Escolar en Chile. Redacta una acción PME para el ámbito {ambito} que resuelva: {objetivo}. Incluye: Nombre, Descripción, Medios de Verificación y Responsable."
                response = model.generate_content(prompt)
                st.markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("👈 Ingresa tu API Key en la barra lateral.")
