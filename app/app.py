"""
AIRA - Aplicación Principal
============================
Análisis de Preparación para IA en Salud - Región Europea OMS

Esta es la aplicación principal que gestiona la navegación entre secciones
y coordina el análisis de datos AIRA.

Autor: Equipo de Análisis de Salud Digital
Fecha: 2025
Tecnologías: Streamlit, Plotly, Pandas, Scikit-learn
"""

import streamlit as st
import sys
from pathlib import Path

# Agregar directorio de páginas al path
sys.path.append(str(Path(__file__).parent))

# Importar configuración y páginas
from config import CUSTOM_CSS
from components.inicio import render_inicio
from components.origen_datos import render_origen_datos
from components.eda import render_eda
from components.ml_clustering import render_ml_clustering
from components.conclusiones import render_conclusiones


# ==================== CONFIGURACIÓN DE LA PÁGINA ====================

st.set_page_config(
    page_title="Panel AIRA - IA en Salud Europa",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.who.int/europe',
        'Report a bug': None,
        'About': """
        # AIRA
        
        Análisis de preparación para IA en salud en la Región Europea de la OMS.
        
        **Fuente de datos**: WHO Europe - AIRA Survey (2024-2025)
        
        **Tecnologías**: 
        - Python 3.x
        - Streamlit
        - Plotly
        - Pandas
        - Scikit-learn
        
        ---
        Desarrollado para análisis de datos de salud digital.
        """
    }
)


# ==================== APLICAR ESTILOS CSS PERSONALIZADOS ====================

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ==================== SIDEBAR - NAVEGACIÓN ====================

def render_sidebar():
    """
    Renderiza el sidebar con navegación y opciones adicionales.
    """
    with st.sidebar:
        # Logo o título
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;'>
            <h1 style='color: white; margin: 0; font-size: 1.8rem;'>🏥 AIRA</h1>
            <p style='color: white; margin: 0; font-size: 0.9rem;'>IA en Salud Europa</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navegación principal
        st.markdown("### 📂 Navegación")
        
        # Opciones de navegación
        opciones = {
            "🏠 Inicio": "inicio",
            "📖 Origen y Datos": "origen",
            "🔬 Análisis Exploratorio (EDA)": "eda",
            "🤖 Machine Learning - Clustering": "ml",
            "💡 Conclusiones": "conclusiones"
        }
        
        # Selector de página
        seleccion = st.radio(
            "Selecciona una sección:",
            options=list(opciones.keys()),
            label_visibility="collapsed"
        )
        
        # Guardar selección en session state
        st.session_state['pagina_actual'] = opciones[seleccion]
        
        st.divider()
        
        # ==================== OPCIONES ADICIONALES ====================
        st.markdown("### ⚙️ Tema General")
        
        # Tema (placeholder - Streamlit maneja esto automáticamente)
        st.caption("El tema se ajusta automáticamente según tu configuración del sistema.")
        
        st.divider()
        
        # ==================== SELECTOR DE TEMA PARA GRÁFICOS ====================
        st.markdown("### 🎨 Tema de Gráficos")
        
        tema_graficos = st.radio(
            "Selecciona el tema para los gráficos:",
            options=["🌙 Oscuro", "☀️ Claro"],
            index=0,  # Por defecto oscuro
            label_visibility="collapsed",
            help="Cambia el color de fondo y texto de los gráficos según tu preferencia"
        )
        
        # Guardar tema en session state
        st.session_state['tema_graficos'] = 'dark' if '🌙' in tema_graficos else 'light'


# ==================== FUNCIÓN PRINCIPAL ====================

def main():
    """
    Función principal que coordina la aplicación.
    """
    # Renderizar sidebar
    render_sidebar()
    
    # Obtener página actual de session state
    pagina = st.session_state.get('pagina_actual', 'inicio')
    
    # Renderizar página correspondiente
    try:
        if pagina == 'inicio':
            render_inicio()
        
        elif pagina == 'origen':
            render_origen_datos()
        
        elif pagina == 'eda':
            render_eda()
        
        elif pagina == 'ml':
            render_ml_clustering()
        
        elif pagina == 'conclusiones':
            render_conclusiones()
        
        else:
            st.error("❌ Página no encontrada")
            render_inicio()
    
    except Exception as e:
        st.error(f"""
        ❌ **Error al cargar la página**
        
        Ha ocurrido un error inesperado:
        
        ```
        {str(e)}
        ```
        
        Por favor, intenta:
        1. Recargar la página
        2. Verificar que todos los archivos estén presentes
        3. Revisar la consola para más detalles
        """)
        
        # Mostrar stack trace en expander para debugging
        with st.expander("🔍 Detalles técnicos (para desarrolladores)"):
            import traceback
            st.code(traceback.format_exc())
    
    # ==================== FOOTER GENERAL ====================
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background-color: #f8fafc; border-radius: 10px; margin-top: 3rem;'>
        <p style='margin: 0; color: #64748b; font-size: 0.9rem;'>
            <strong>AIRA</strong> | 
            Análisis de Preparación para IA en Salud - Región Europea OMS<br>
            Fuente de datos: <a href='https://www.who.int/europe' target='_blank'>WHO Europe</a> | 
            Desarrollado con ❤️ para la salud digital
        </p>
    </div>
    """, unsafe_allow_html=True)


# ==================== PUNTO DE ENTRADA ====================

if __name__ == "__main__":
    main()
