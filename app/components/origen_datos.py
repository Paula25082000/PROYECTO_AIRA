"""
Página de Origen y Exploración de Datos
========================================
Esta página explica el origen de los datos AIRA y permite
explorar las características del dataset.
"""

import streamlit as st
import pandas as pd
from utils import cargar_datos, obtener_info_dataset, enriquecer_dataframe
from config import COUNTRY_NAMES, RESPONSE_LABELS, AIRA_TITULOS


def render_origen_datos():
    """
    Renderiza la página de origen y exploración de datos.
    """
    st.title("📖 Origen y Exploración de Datos")
    
    # ==================== SECCIÓN: ORIGEN DE LOS DATOS ====================
    st.header("1. Origen de los Datos: AIRA Survey")
    
    st.markdown("""
    ### ¿Qué es AIRA?
    
    **AIRA** (Assessment of Implementation Readiness for AI) es un cuestionario desarrollado 
    por la **Organización Mundial de la Salud (OMS) - Región Europea** para evaluar el grado 
    de preparación de los países para implementar Inteligencia Artificial en sus sistemas de salud.
    
    ### Objetivos del Cuestionario
    
    El cuestionario AIRA busca:
    
    - 📊 **Evaluar** el estado actual de preparación en IA para salud
    - 🎯 **Identificar** brechas y áreas de mejora
    - 🤝 **Fomentar** el intercambio de mejores prácticas entre países
    - 📈 **Establecer** líneas base para monitorear progreso
    - 🌍 **Promover** la adopción ética y sostenible de IA en salud
    
    ### Metodología
    
    - **Período de recolección**: 2024-2025
    - **Países participantes**: 53 países de la Región Europea de la OMS
    - **Formato**: Encuesta estructurada con respuestas categóricas
    - **Secciones temáticas**: 5 bloques principales
    
    ### Fuente de Datos Oficial
    
    El dataset original está disponible en el portal de datos de la OMS Europa:
    
    🔗 **[AIRA Dataset - WHO Europe Gateway](https://gateway.euro.who.int/en/datasets/aira/)**
    """)
    
    # Imagen o diagrama conceptual (si se desea)
    st.info("""
    **📌 Nota Metodológica**: 
    
    Las respuestas del cuestionario AIRA son auto-reportadas por los países, 
    lo que significa que reflejan la percepción y conocimiento de las autoridades 
    nacionales de salud en el momento de la encuesta.
    """)
    
    st.divider()
    
    # ==================== SECCIÓN: EXPLORACIÓN DEL DATASET ====================
    st.header("2. Exploración del Dataset")
    
    # Cargar datos
    with st.spinner("Cargando datos..."):
        df = cargar_datos()
        df_enriquecido = enriquecer_dataframe(df)
    
    # Información general del dataset
    info = obtener_info_dataset(df)
    
    st.subheader("📊 Información General")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Filas Totales", f"{info['n_filas']:,}")
    
    with col2:
        st.metric("Países", info['n_paises'])
    
    with col3:
        st.metric("Variables AIRA", info['n_variables'])
    
    with col4:
        st.metric("Columnas", info['n_columnas'])
    
    st.divider()
    
    # ==================== PAÍSES PARTICIPANTES ====================
    st.subheader("🌍 Países Participantes")
    
    paises_unicos = sorted([COUNTRY_NAMES[code] for code in df['COUNTRY_REGION'].unique()])
    
    st.markdown(f"""
    El análisis incluye **{len(paises_unicos)} países** de la Región Europea de la OMS:
    """)
    
    # Mostrar en 4 columnas
    cols = st.columns(4)
    for idx, pais in enumerate(paises_unicos):
        with cols[idx % 4]:
            st.write(f"• {pais}")
    
    st.divider()
    
    # ==================== VARIABLES AIRA ====================
    st.subheader("📝 Variables AIRA")
    
    variables_unicas = sorted(df['Measure_code'].unique())
    
    st.markdown(f"""
    El dataset contiene **{len(variables_unicas)} variables AIRA** organizadas en 5 secciones temáticas:
    
    - **Sección 1 (AIRA_1 - AIRA_7)**: Contexto estratégico
    - **Sección 2 (AIRA_8 - AIRA_36)**: Contexto normativo
    - **Sección 3 (AIRA_37 - AIRA_46)**: Gobernanza de datos sanitarios
    - **Sección 4 (AIRA_47 - AIRA_53)**: Aplicaciones de IA para la salud
    - **Sección 5 (AIRA_71 - AIRA_75)**: Desarrollo de capacidades
    """)
    
    # Selector de sección para ver variables
    seccion_seleccionada = st.selectbox(
        "Selecciona una sección para ver sus variables:",
        options=[
            "Sección 1: Contexto Estratégico",
            "Sección 2: Contexto Normativo",
            "Sección 3: Gobernanza de Datos",
            "Sección 4: Aplicaciones de IA",
            "Sección 5: Desarrollo de Capacidades"
        ]
    )
    
    # Mapear sección a rango de variables
    rangos = {
        "Sección 1: Contexto Estratégico": range(1, 8),
        "Sección 2: Contexto Normativo": range(8, 37),
        "Sección 3: Gobernanza de Datos": range(37, 47),
        "Sección 4: Aplicaciones de IA": range(47, 54),
        "Sección 5: Desarrollo de Capacidades": range(71, 76)
    }
    
    rango = rangos[seccion_seleccionada]
    variables_seccion = [f"AIRA_{i}" for i in rango]
    
    # Crear DataFrame con títulos
    df_variables = pd.DataFrame({
        'Código': variables_seccion,
        'Título': [AIRA_TITULOS.get(v, 'Sin título') for v in variables_seccion]
    })
    
    st.dataframe(
        df_variables,
        width='stretch',
        hide_index=True
    )
    
    st.divider()
    
    # ==================== CATEGORÍAS DE RESPUESTA ====================
    st.subheader("✅ Categorías de Respuesta")
    
    st.markdown("""
    Las respuestas del cuestionario AIRA se clasifican en **5 categorías**:
    """)
    
    # Tabla de categorías con explicación
    categorias_data = {
        'Código': list(RESPONSE_LABELS.keys()),
        'Etiqueta': list(RESPONSE_LABELS.values()),
        'Significado': [
            '✅ La medida/política está implementada completamente',
            '❌ La medida/política no está implementada',
            '🔄 La medida/política está en desarrollo',
            '❓ El país no sabe o no tiene información',
            '⚫ La pregunta no aplica al contexto del país'
        ]
    }
    
    df_categorias = pd.DataFrame(categorias_data)
    
    st.dataframe(
        df_categorias,
        width='stretch',
        hide_index=True
    )
    
    st.divider()
    
    # ==================== DISTRIBUCIÓN GENERAL DE RESPUESTAS ====================
    st.subheader("📊 Distribución General de Respuestas")
    
    distribucion_general = df['AIRA_SIMPLE'].value_counts()
    distribucion_general_df = pd.DataFrame({
        'Respuesta': [RESPONSE_LABELS.get(k, k) for k in distribucion_general.index],
        'Cantidad': distribucion_general.values,
        'Porcentaje': (distribucion_general.values / distribucion_general.values.sum() * 100).round(2)
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.dataframe(
            distribucion_general_df,
            width='stretch',
            hide_index=True
        )
    
    with col2:
        st.markdown(f"""
        **Observaciones:**
        
        - Total de respuestas: **{distribucion_general.values.sum():,}**
        - Respuestas "Sí": **{distribucion_general.get('YES', 0):,}** 
          ({distribucion_general.get('YES', 0) / distribucion_general.values.sum() * 100:.1f}%)
        - Respuestas "No": **{distribucion_general.get('NO', 0):,}** 
          ({distribucion_general.get('NO', 0) / distribucion_general.values.sum() * 100:.1f}%)
        - En desarrollo: **{distribucion_general.get('UD', 0):,}** 
          ({distribucion_general.get('UD', 0) / distribucion_general.values.sum() * 100:.1f}%)
        """)
    
    st.divider()
    
    # ==================== BÚSQUEDA Y FILTRADO ====================
    st.subheader("🔍 Búsqueda y Filtrado")
    
    st.markdown("Explora los datos filtrando por país o variable:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pais_seleccionado = st.selectbox(
            "Selecciona un país:",
            options=['Todos'] + paises_unicos
        )
    
    with col2:
        variable_seleccionada = st.selectbox(
            "Selecciona una variable AIRA:",
            options=['Todas'] + variables_unicas
        )
    
    # Aplicar filtros
    df_filtrado = df_enriquecido.copy()
    
    if pais_seleccionado != 'Todos':
        codigo_pais = [k for k, v in COUNTRY_NAMES.items() if v == pais_seleccionado][0]
        df_filtrado = df_filtrado[df_filtrado['COUNTRY_REGION'] == codigo_pais]
    
    if variable_seleccionada != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['Measure_code'] == variable_seleccionada]
    
    st.markdown(f"**Resultados del filtro:** {len(df_filtrado)} registros")
    
    st.dataframe(
        df_filtrado[['Pais', 'Measure_code', 'Variable_Titulo', 'Respuesta']],
        width='stretch',
        hide_index=True
    )
    
    # Opción de descarga
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar datos filtrados como CSV",
        data=csv,
        file_name=f"aira_filtrado_{pais_seleccionado}_{variable_seleccionada}.csv",
        mime="text/csv"
    )
    
    st.divider()
    
    # ==================== RESUMEN Y PRÓXIMOS PASOS ====================
    st.subheader("🎯 Próximos Pasos")
    
    st.success("""
    **¡Datos explorados exitosamente!** 
    
    Ahora que comprendes la estructura y origen de los datos, puedes:
    
    1. 🔬 **Explorar el Análisis EDA** para visualizaciones detalladas por sección
    2. 🤖 **Revisar el análisis de Machine Learning** para ver tipologías de países
    3. 💡 **Consultar las Conclusiones** para insights clave y recomendaciones
    
    Usa el menú lateral para navegar a las siguientes secciones.
    """)
