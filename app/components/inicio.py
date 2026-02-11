"""
Página de Inicio de AIRA
=========================
Esta es la página principal que da la bienvenida al usuario
y proporciona información general sobre el proyecto.
"""

import streamlit as st
from config import TEXTO_BIENVENIDA, DESCRIPCION_PROYECTO


def render_inicio():
    """
    Renderiza la página de inicio con información general del proyecto.
    """
    # Título principal
    st.title("🏥 AIRA: Encuesta de Preparación para la Implementación de la IA en el Sector Sanitario")
    st.subheader("Análisis de la Encuesta AIRA - Región Europea de la OMS")
    
    # Texto de bienvenida
    st.markdown(TEXTO_BIENVENIDA)
    
    # Descripción del proyecto
    st.markdown(DESCRIPCION_PROYECTO)
    
    # Sección visual con métricas
    st.divider()
    st.subheader("📈 Visión General del Análisis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Países Analizados",
            value="53",
            delta="Región Europea OMS"
        )
    
    with col2:
        st.metric(
            label="Variables AIRA",
            value="75",
            delta="5 Secciones Temáticas"
        )
    
    with col3:
        st.metric(
            label="Clusters Identificados",
            value="2",
            delta="Tipologías de Países"
        )
    
    # Caja de información importante
    st.info("""
    **💡 Cómo navegar:**
    
    Utiliza el **menú lateral** para explorar: Origen de Datos, EDA por Sección AIRA, 
    Machine Learning (Clustering) y Conclusiones. Los gráficos son interactivos y descargables.
    """)
    
    # Sección sobre las 5 áreas clave
    st.divider()
    st.subheader("🎯 Las 5 Áreas Clave del Análisis AIRA")
    
    areas = [
        {
            "emoji": "🎨",
            "nombre": "Estrategia",
            "descripcion": "Estrategias nacionales y mecanismos de supervisión de IA en salud"
        },
        {
            "emoji": "⚖️",
            "nombre": "Regulación",
            "descripcion": "Marco regulatorio, ética, responsabilidad y estándares legales"
        },
        {
            "emoji": "💾",
            "nombre": "Gobernanza de Datos",
            "descripcion": "Estrategias de datos, infraestructura y regulación del uso de datos"
        },
        {
            "emoji": "🏥",
            "nombre": "Aplicaciones",
            "descripcion": "Implementación práctica de sistemas de IA en el sector salud"
        },
        {
            "emoji": "🎓",
            "nombre": "Capacidades",
            "descripcion": "Formación, talento y capacidades humanas en IA"
        }
    ]
    
    for area in areas:
        with st.expander(f"{area['emoji']} **{area['nombre']}**"):
            st.markdown(area['descripcion'])
    
    # Footer con créditos
    st.divider()
    st.caption("Análisis desarrollado con Python, Streamlit, Plotly, Pandas y Scikit-learn")
