import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Asistente Convivencia - Profe Oriela", page_icon="🏫")

st.title("🛡️ Generador de Acciones PME")
st.subheader("Coordinación de Convivencia Escolar")

# Barra lateral
with st.sidebar:
    st.title("Configuración")
    api_key = st.text_input("Ingresa tu Gemini API Key", type="password")

if api_key:
    try:
        # CONFIGURACIÓN MAESTRA PARA EVITAR EL ERROR 404
        genai.configure(api_key=api_key)
        
        # Seleccionamos el modelo más estable para marzo 2026
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        
        ambito = st.selectbox("Ámbito de la Acción", ["Formación", "Participación", "Prevención", "Gestión"])
        objetivo = st.text_area("¿Cuál es el nudo crítico o meta?")

        if st.button("✨ Generar Acción Técnica"):
            if not objetivo:
                st.warning("Escribe un nudo crítico primero.")
            else:
                with st.spinner('Redactando propuesta formativa...'):
                    # El prompt ahora es más específico para evitar errores de red
                    prompt = f"Como experto en Convivencia Escolar en Chile, redacta una acción PME para el ámbito {ambito} sobre: {objetivo}. Incluye Nombre, Descripción, Medios de Verificación y Responsable."
                    
                    # Forzamos la generación simple
                    response = model.generate_content(prompt)
                    
                    st.success("¡Propuesta Lista!")
                    st.markdown("---")
                    st.markdown(response.text)
                    
    except Exception as e:
        # Este mensaje te dirá si el problema es la clave o el modelo
        st.error(f"Aviso técnico: {e}")
else:
    st.warning("👈 Ingresa tu API Key en la barra lateral.")
