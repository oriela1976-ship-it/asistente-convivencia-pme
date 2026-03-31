import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="Asistente Convivencia - Profe Oriela", page_icon="🏫")

st.title("🛡️ Generador de Acciones PME")
st.subheader("Coordinación de Convivencia Escolar")

# Barra lateral para la configuración
with st.sidebar:
    st.title("Configuración")
    api_key = st.text_input("Ingresa tu Gemini API Key", type="password")
    st.info("Obtén tu clave en Google AI Studio")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Este es el modelo más nuevo y estable (2026)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        ambito = st.selectbox("Ámbito de la Acción", ["Formación", "Participación", "Prevención", "Gestión"])
        objetivo = st.text_area("¿Cuál es el nudo crítico o meta?")

        if st.button("✨ Generar Acción Técnica"):
            if not objetivo:
                st.warning("Por favor, escribe un nudo crítico.")
            else:
                with st.spinner('Redactando propuesta técnica...'):
                    # Prompt optimizado para Chile
                    prompt = f"""Actúa como experto en Convivencia Escolar en Chile. 
                    Redacta una acción PME para el ámbito {ambito} que resuelva: {objetivo}. 
                    Entrega el resultado con:
                    - Nombre de la acción.
                    - Descripción detallada (acciones formativas).
                    - Medios de Verificación.
                    - Responsable sugerido."""
                    
                    response = model.generate_content(prompt)
                    st.success("¡Propuesta Generada!")
                    st.markdown("---")
                    st.markdown(response.text)
                    
    except Exception as e:
        st.error(f"Error de conexión: {e}. Revisa que tu API Key sea correcta.")
else:
    st.warning("👈 Por favor, ingresa tu API Key en la barra lateral para comenzar.")
