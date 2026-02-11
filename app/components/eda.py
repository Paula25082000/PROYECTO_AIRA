"""
Página de Análisis Exploratorio de Datos (EDA)
==============================================
Esta página contiene visualizaciones y análisis detallados
organizados por las 5 secciones temáticas del cuestionario AIRA.
"""

import streamlit as st
from utils import (
    cargar_datos, filtrar_por_variable, calcular_distribucion_respuestas,
    obtener_paises_por_respuesta, crear_tabla_pivotada_seccion
)
from visualizations import (
    crear_mapa_europa, crear_grafico_distribucion, crear_tabla_interactiva
)
from config import SECCIONES, AIRA_TITULOS


def render_eda():
    """
    Renderiza la página de análisis exploratorio de datos (EDA).
    """
    st.title("🔬 Análisis Exploratorio de Datos (EDA)")
    
    st.markdown("""
    Esta sección presenta visualizaciones interactivas y análisis detallados organizados 
    según las **5 secciones temáticas** del cuestionario AIRA.
    
    **Instrucciones:**
    - Selecciona una **sección temática** en el menú desplegable
    - Luego selecciona una **variable específica** para ver análisis detallado
    - O visualiza la **tabla resumen** de toda la sección
    """)
    
    st.divider()
    
    # ==================== CARGAR DATOS ====================
    with st.spinner("Cargando datos..."):
        df = cargar_datos()
    
    # ==================== SELECTOR DE SECCIÓN ====================
    st.subheader("📂 Selección de Sección y Variable")
    
    # Preparar opciones de secciones
    opciones_secciones = {
        "Sección 1 - Contexto Estratégico": "seccion_1",
        "Sección 2 - Contexto Normativo": "seccion_2",
        "Sección 3 - Gobernanza de Datos Sanitarios": "seccion_3",
        "Sección 4 - Aplicaciones de IA para la Salud": "seccion_4",
        "Sección 5 - Desarrollo de Capacidades": "seccion_5"
    }
    
    seccion_seleccionada_nombre = st.selectbox(
        "Selecciona una sección temática:",
        options=list(opciones_secciones.keys())
    )
    
    seccion_key = opciones_secciones[seccion_seleccionada_nombre]
    seccion_info = SECCIONES[seccion_key]
    
    # Mostrar descripción de la sección
    st.info(f"**{seccion_info['nombre']}**: {seccion_info['descripcion']}")
    
    # ==================== PESTAÑAS: ANÁLISIS POR VARIABLE vs TABLA RESUMEN ====================
    tab1, tab2 = st.tabs(["📊 Análisis por Variable", "📋 Tabla Resumen de Sección"])
    
    with tab1:
        render_analisis_por_variable(df, seccion_info)
    
    with tab2:
        render_tabla_resumen_seccion(df, seccion_key, seccion_info)


def render_analisis_por_variable(df, seccion_info):
    """
    Renderiza análisis detallado para una variable específica.
    """
    st.subheader("📊 Análisis Detallado por Variable")
    
    # Selector de variable
    variables_disponibles = seccion_info['variables']
    
    # Crear opciones con títulos descriptivos
    opciones_variables = {
        f"{var} - {AIRA_TITULOS.get(var, 'Sin título')}": var 
        for var in variables_disponibles
    }
    
    variable_seleccionada_nombre = st.selectbox(
        "Selecciona una variable para análisis detallado:",
        options=list(opciones_variables.keys())
    )
    
    variable_aira = opciones_variables[variable_seleccionada_nombre]
    
    st.divider()
    
    # Filtrar datos por variable
    df_filtrado = filtrar_por_variable(df, variable_aira)
    
    # Título de la variable
    titulo = AIRA_TITULOS.get(variable_aira, variable_aira)
    st.markdown(f"### {variable_aira}: {titulo}")
    
    # ==================== MAPA DE EUROPA ====================
    st.subheader("🗺️ Mapa de Europa")
    
    fig_mapa = crear_mapa_europa(
        df_filtrado,
        titulo=f"{variable_aira} - {titulo}",
        variable_aira=variable_aira
    )
    
    st.plotly_chart(fig_mapa, use_container_width=True)
    
    # ==================== DISTRIBUCIÓN DE RESPUESTAS ====================
    st.subheader("📊 Distribución de Respuestas")
    
    distribucion = calcular_distribucion_respuestas(df_filtrado)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        fig_barras = crear_grafico_distribucion(
            distribucion,
            titulo=f"Distribución de respuestas - {variable_aira}"
        )
        st.plotly_chart(fig_barras, use_container_width=True)
    
    with col2:
        st.markdown("**Conteo de países por respuesta:**")
        st.dataframe(
            distribucion,
            use_container_width=True,
            hide_index=True
        )
    
    # ==================== LISTADO DE PAÍSES POR RESPUESTA ====================
    st.subheader("🌍 Países por Categoría de Respuesta")
    
    # Crear expandibles por cada categoría
    for _, row in distribucion.iterrows():
        respuesta = row['Respuesta']
        cantidad = row['Cantidad']
        
        with st.expander(f"{respuesta} ({cantidad} países)"):
            paises = obtener_paises_por_respuesta(df_filtrado, respuesta)
            
            if paises:
                # Mostrar en columnas
                cols = st.columns(4)
                for idx, pais in enumerate(paises):
                    with cols[idx % 4]:
                        st.write(f"• {pais}")
            else:
                st.write("No hay países en esta categoría.")
    
    # ==================== INSIGHTS AUTOMÁTICOS ====================
    st.divider()
    st.subheader("💡 Insights Automáticos")
    
    # Calcular estadísticas
    total_paises = len(df_filtrado)
    si_count = len(df_filtrado[df_filtrado['Respuesta'] == 'Sí'])
    no_count = len(df_filtrado[df_filtrado['Respuesta'] == 'No'])
    ud_count = len(df_filtrado[df_filtrado['Respuesta'] == 'En desarrollo'])
    
    si_pct = (si_count / total_paises * 100) if total_paises > 0 else 0
    no_pct = (no_count / total_paises * 100) if total_paises > 0 else 0
    ud_pct = (ud_count / total_paises * 100) if total_paises > 0 else 0
    
    # Generar insights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Implementado completamente",
            f"{si_count} países",
            delta=f"{si_pct:.1f}%"
        )
    
    with col2:
        st.metric(
            "En desarrollo",
            f"{ud_count} países",
            delta=f"{ud_pct:.1f}%"
        )
    
    with col3:
        st.metric(
            "No implementado",
            f"{no_count} países",
            delta=f"{no_pct:.1f}%"
        )
    
    # Mensaje interpretativo
    if si_pct > 50:
        st.success(f"✅ **Mayoría implementando**: Más del 50% de los países ({si_pct:.1f}%) han implementado esta medida.")
    elif no_pct > 50:
        st.warning(f"⚠️ **Área de oportunidad**: Más del 50% de los países ({no_pct:.1f}%) aún no han implementado esta medida.")
    elif ud_pct > 30:
        st.info(f"🔄 **En transición**: Un porcentaje significativo ({ud_pct:.1f}%) está desarrollando esta medida.")
    else:
        st.info("📊 **Distribución equilibrada**: Las respuestas muestran una distribución variada entre países.")


def render_tabla_resumen_seccion(df, seccion_key, seccion_info):
    """
    Renderiza tabla resumen con todas las variables de una sección.
    """
    st.subheader(f"📋 Tabla Resumen - {seccion_info['nombre']}")
    
    st.markdown("""
    Esta tabla muestra las respuestas de todos los países para todas las variables 
    de la sección seleccionada. Las celdas están coloreadas según la respuesta:
    
    - 🟢 Verde: Sí (implementado)
    - 🟠 Ámbar: En desarrollo
    - 🔴 Rojo: No
    - 🔵 Azul: No sabe
    - ⚫ Gris: No aplicable
    """)
    
    with st.spinner("Generando tabla..."):
        # Extraer número de sección
        numero_seccion = int(seccion_key.split('_')[1])
        
        # Crear tabla pivotada
        df_pivot = crear_tabla_pivotada_seccion(df, numero_seccion)
        
        if df_pivot.empty:
            st.warning("No hay datos disponibles para esta sección.")
            return
        
        # Crear tabla interactiva
        fig_tabla = crear_tabla_interactiva(
            df_pivot,
            titulo=f"Tabla Resumen - {seccion_info['nombre']}"
        )
        
        st.plotly_chart(fig_tabla, use_container_width=True)
        
        # Opción de descarga
        csv = df_pivot.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar tabla como CSV",
            data=csv,
            file_name=f"aira_{seccion_key}_resumen.csv",
            mime="text/csv"
        )
    
    st.divider()
    
    # ==================== ANÁLISIS AGREGADO DE LA SECCIÓN ====================
    st.subheader("📊 Análisis Agregado de la Sección")
    
    # Filtrar datos de la sección
    df_seccion = df[df['Measure_code'].isin(seccion_info['variables'])].copy()
    
    # Calcular estadísticas agregadas
    total_respuestas = len(df_seccion)
    distribucion_seccion = df_seccion['AIRA_SIMPLE'].value_counts()
    
    st.markdown(f"""
    **Resumen general de la sección:**
    
    - Total de respuestas: **{total_respuestas:,}**
    - Variables analizadas: **{len(seccion_info['variables'])}**
    - Países evaluados: **{df_seccion['COUNTRY_REGION'].nunique()}**
    """)
    
    # Gráfico de distribución agregada
    from utils import enriquecer_dataframe
    df_seccion_enriq = enriquecer_dataframe(df_seccion)
    distribucion_seccion_df = calcular_distribucion_respuestas(df_seccion_enriq)
    
    fig_seccion = crear_grafico_distribucion(
        distribucion_seccion_df,
        titulo=f"Distribución agregada - {seccion_info['nombre']}"
    )
    
    st.plotly_chart(fig_seccion, use_container_width=True)
    
    # Métricas clave
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        si_total = distribucion_seccion.get('YES', 0)
        si_pct = (si_total / total_respuestas * 100) if total_respuestas > 0 else 0
        st.metric("Sí", f"{si_total}", delta=f"{si_pct:.1f}%")
    
    with col2:
        ud_total = distribucion_seccion.get('UD', 0)
        ud_pct = (ud_total / total_respuestas * 100) if total_respuestas > 0 else 0
        st.metric("En desarrollo", f"{ud_total}", delta=f"{ud_pct:.1f}%")
    
    with col3:
        no_total = distribucion_seccion.get('NO', 0)
        no_pct = (no_total / total_respuestas * 100) if total_respuestas > 0 else 0
        st.metric("No", f"{no_total}", delta=f"{no_pct:.1f}%")
    
    with col4:
        dnk_total = distribucion_seccion.get('DNK', 0)
        dnk_pct = (dnk_total / total_respuestas * 100) if total_respuestas > 0 else 0
        st.metric("No sabe", f"{dnk_total}", delta=f"{dnk_pct:.1f}%")
    
    # Mensaje interpretativo final
    st.info(f"""
    **Interpretación**: 
    
    En la sección de {seccion_info['nombre']}, un {si_pct:.1f}% de las respuestas indican 
    implementación completa, mientras que un {ud_pct:.1f}% están en desarrollo. 
    Esto sugiere {'un nivel avanzado de preparación' if si_pct > 40 else 'oportunidades significativas de mejora'} 
    en esta área temática.
    """)
