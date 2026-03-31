import streamlit as st
import google.generativeai as genai

# Configuración visual
st.set_page_config(page_title="Asistente Convivencia - Profe Oriela", page_icon="🏫")

st.title("🛡️ Generador de Acciones PME")
st.subheader("Coordinación de Convivencia Escolar")

# Barra lateral para la clave
with st.sidebar:
    st.title("Configuración")
    api_key = st.text_input("Ingresa tu Gemini API Key", type="password")
    st.info("Esta clave la obtienes en Google AI Studio.")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Formulario
    ambito = st.selectbox("Ámbito de la Acción", 
                         ["Formación", "Participación", "Prevención", "Gestión de la Convivencia"])
    
    objetivo = st.text_area("¿Cuál es el nudo crítico o meta? (Ej: Mejorar la resolución de conflictos en 2° medio)")

    if st.button("✨ Generar Acción Técnica"):
        with st.spinner('Redactando propuesta normativa...'):
            prompt = f"Actúa como experto en Convivencia Escolar en Chile. Redacta una acción PME para el ámbito {ambito} que resuelva: {objetivo}. Incluye: Nombre, Descripción formativa, Medios de Verificación y Responsable sugerido."
            response = model.generate_content(prompt)
            st.markdown("---")
            st.markdown(response.text)
else:
    st.warning("👈 Por favor, ingresa tu API Key en la barra lateral para activar el asistente.")
