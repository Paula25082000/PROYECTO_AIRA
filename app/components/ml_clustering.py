"""
Página de Machine Learning - Clustering
========================================
Esta página implementa análisis de clustering para identificar
tipologías de países según su preparación en IA para la salud.
"""

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

from utils import (
    cargar_datos, preparar_datos_ml, calcular_scores_por_area,
    preparar_perfiles_clusters, asignar_tipologia
)
from visualizations import (
    crear_grafico_metodo_codo, crear_grafico_silhouette,
    crear_grafico_pca_2d, crear_grafico_pca_3d,
    crear_grafico_radar_perfil, crear_grafico_comparacion_clusters
)
from config import COUNTRY_NAMES, AIRA_GRUPOS


def render_ml_clustering():
    """
    Renderiza la página de análisis de Machine Learning (Clustering).
    """
    st.title("🤖 Machine Learning - Clustering de Países")
    
    st.markdown("""
    Esta sección utiliza técnicas de **Machine Learning no supervisado** para identificar 
    **tipologías de países** basadas en sus respuestas al cuestionario AIRA.
    
    ### ¿Qué es Clustering?
    
    El **clustering** (agrupamiento) es una técnica que agrupa países con características similares 
    de manera automática, revelando patrones ocultos en los datos.
    
    ### Metodología
    
    1. **Preparación de datos**: Transformación de formato largo a ancho y codificación numérica
    2. **Algoritmo K-means**: Agrupamiento basado en similitud de respuestas
    3. **Validación**: Uso del coeficiente de silueta para determinar el K óptimo
    4. **Visualización**: Reducción dimensional con PCA para gráficos 2D/3D
    5. **Interpretación**: Análisis de perfiles por área temática
    """)
    
    st.divider()
    
    # ==================== PREPARACIÓN DE DATOS ====================
    st.header("1️⃣ Preparación de Datos")
    
    with st.spinner("Cargando y preparando datos para ML..."):
        df = cargar_datos()
        df_pivot, df_encoded, df_filled = preparar_datos_ml(df)
    
    st.success("✅ Datos preparados exitosamente para análisis de Machine Learning")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Países", df_filled.shape[0])
    
    with col2:
        st.metric("Variables AIRA", df_filled.shape[1])
    
    with col3:
        st.metric("Codificación", "0, 1, 2 (No-En desarrollo-Sí)")
    
    with st.expander("ℹ️ Ver detalles de la preparación de datos"):
        st.markdown("""
        **Transformaciones aplicadas:**
        
        1. **Pivoteo**: De formato largo (país-variable-respuesta) a formato ancho (países x variables)
        2. **Codificación numérica**: 
           - YES (Sí) → 2
           - UD (En desarrollo) / DNK (No sabe) → 1
           - NO → 0
           - N/A (No aplicable) → 0
        3. **Imputación**: Valores faltantes rellenados con la mediana de cada columna
        
        **¿Por qué esta codificación?**
        
        - Refleja el **nivel de implementación** de manera ordinal
        - Permite calcular **promedios significativos**
        - Facilita el **cálculo de distancias** entre países
        """)
        
        st.markdown("**Vista previa de datos codificados:**")
        st.dataframe(df_filled.head(10), width='stretch')
    
    st.divider()
    
    # ==================== DETERMINACIÓN DEL K ÓPTIMO ====================
    st.header("2️⃣ Determinación del Número Óptimo de Clusters (K)")
    
    st.markdown("""
    Para determinar cuántos clusters (grupos) son óptimos, probamos diferentes valores de K 
    y evaluamos la calidad del clustering con dos métricos:
    
    - **Método del Codo**: Busca el punto donde agregar más clusters no mejora mucho
    - **Coeficiente de Silueta**: Mide qué tan bien está asignado cada país a su cluster
    """)
    
    # Calcular K-means para diferentes valores de K
    k_range = range(2, 11)
    inertias = []
    silhouette_scores = []
    
    with st.spinner("Calculando K-means para diferentes valores de K..."):
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(df_filled)
            inertias.append(kmeans.inertia_)
            silhouette_scores.append(silhouette_score(df_filled, kmeans.labels_))
    
    # Determinar K óptimo
    k_optimo = list(k_range)[silhouette_scores.index(max(silhouette_scores))]
    
    st.success(f"✅ **K óptimo determinado: {k_optimo} clusters**")
    
    # Gráficos de validación
    col1, col2 = st.columns(2)
    
    with col1:
        fig_codo = crear_grafico_metodo_codo(inertias, k_range)
        st.plotly_chart(fig_codo, width='stretch')
    
    with col2:
        fig_silhouette = crear_grafico_silhouette(silhouette_scores, k_range)
        st.plotly_chart(fig_silhouette, width='stretch')
    
    with st.expander("ℹ️ ¿Cómo interpretar estos gráficos?"):
        st.markdown(f"""
        **Método del Codo (izquierda):**
        - La inercia siempre disminuye al aumentar K
        - Buscamos el "codo" donde la mejora se vuelve marginal
        - Sugiere un balance entre simplicidad y calidad
        
        **Coeficiente de Silueta (derecha):**
        - Rango: -1 (mal) a +1 (excelente)
        - Valores > 0.5: clustering bueno
        - **K = {k_optimo}** tiene el coeficiente más alto: **{max(silhouette_scores):.3f}**
        
        **Conclusión**: Los datos muestran una separación natural en **{k_optimo} grupos**.
        """)
    
    st.divider()
    
    # ==================== APLICACIÓN DEL CLUSTERING FINAL ====================
    st.header(f"3️⃣ Clustering Final con K = {k_optimo}")
    
    with st.spinner("Aplicando K-means final..."):
        kmeans_final = KMeans(n_clusters=k_optimo, random_state=42, n_init=10)
        clusters = kmeans_final.fit_predict(df_filled)
        
        # Crear DataFrame con clusters
        df_clusters = pd.DataFrame({
            'COUNTRY_REGION': df_filled.index,
            'Cluster': clusters
        })
        
        # Calcular scores por área (incluye columna 'Pais')
        df_scores = calcular_scores_por_area(df_filled)
    
    st.success(f"✅ Países agrupados en {k_optimo} clusters")
    
    # Tabla de asignación de clusters
    st.subheader("📋 Asignación de Países a Clusters")
    
    df_resultado = df_clusters.merge(df_scores, left_on='COUNTRY_REGION', right_index=True)
    df_resultado = df_resultado[['Pais', 'Cluster', 'Score_General', 'Estrategia', 
                                  'Regulación', 'Gobernanza de Datos', 'Aplicaciones', 'Capacidades']]
    df_resultado = df_resultado.sort_values(['Cluster', 'Score_General'], ascending=[True, False])
    
    st.dataframe(
        df_resultado.style.format({
            'Score_General': '{:.1f}',
            'Estrategia': '{:.1f}',
            'Regulación': '{:.1f}',
            'Gobernanza de Datos': '{:.1f}',
            'Aplicaciones': '{:.1f}',
            'Capacidades': '{:.1f}'
        }),
        width='stretch',
        hide_index=True
    )
    
    # Opción de descarga
    csv = df_resultado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar resultados de clustering como CSV",
        data=csv,
        file_name="aira_clustering_resultados.csv",
        mime="text/csv"
    )
    
    st.divider()
    
    # ==================== VISUALIZACIÓN CON PCA ====================
    st.header("4️⃣ Visualización de Clusters (Análisis PCA)")
    
    st.markdown("""
    Para visualizar los clusters, utilizamos **PCA (Análisis de Componentes Principales)** 
    que reduce las 75 dimensiones a 2D/3D conservando la mayor información posible.
    """)
    
    # Aplicar PCA
    with st.spinner("Aplicando PCA..."):
        pca_2d = PCA(n_components=2, random_state=42)
        pca_3d = PCA(n_components=3, random_state=42)
        
        pca_coords_2d = pca_2d.fit_transform(df_filled)
        pca_coords_3d = pca_3d.fit_transform(df_filled)
        
        labels = [COUNTRY_NAMES.get(code, code) for code in df_filled.index]
    
    varianza_2d = pca_2d.explained_variance_ratio_.sum() * 100
    varianza_3d = pca_3d.explained_variance_ratio_.sum() * 100
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Varianza explicada (2D)", f"{varianza_2d:.1f}%")
    
    with col2:
        st.metric("Varianza explicada (3D)", f"{varianza_3d:.1f}%")
    
    # Pestañas para visualización 2D y 3D
    tab1, tab2 = st.tabs(["📊 Visualización 2D", "🎲 Visualización 3D"])
    
    with tab1:
        fig_2d = crear_grafico_pca_2d(pca_coords_2d, clusters, labels)
        st.plotly_chart(fig_2d, width='stretch')
    
    with tab2:
        fig_3d = crear_grafico_pca_3d(pca_coords_3d, clusters, labels)
        st.plotly_chart(fig_3d, width='stretch')
    
    st.info(f"""
    **Interpretación de los gráficos:**
    
    - Cada punto representa un país
    - Los colores indican el cluster asignado
    - Distancia entre puntos = similitud (más cerca = más similar)
    - Los ejes (PC1, PC2, PC3) son combinaciones de las variables originales
    - La visualización conserva {varianza_2d:.1f}% (2D) y {varianza_3d:.1f}% (3D) de la información original
    """)
    
    st.divider()
    
    # ==================== PERFILES DE CLUSTERS ====================
    st.header("5️⃣ Perfiles de los Clusters")
    
    st.markdown("""
    Analizamos las características de cada cluster calculando los **scores promedio** 
    en cada una de las 5 áreas temáticas del cuestionario AIRA.
    """)
    
    # Preparar perfiles primero
    perfiles = preparar_perfiles_clusters(df_clusters, df_scores)
    
    # Definición de tipologías posibles
    st.subheader("📚 Tipologías de Clusters Posibles")
    
    st.markdown("""
    El modelo de clustering puede identificar **7 tipologías** de países según su perfil de preparación 
    en IA para la salud. La clasificación considera tanto el score general como los patrones específicos 
    entre las diferentes áreas temáticas:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🟢 Líderes en IA en Salud
        **Criterio:** Puntaje promedio > 70/100
        
        Países con altos niveles de madurez en todas las dimensiones.
        
        ---
        
        #### 🟡 En Transición Avanzada
        **Criterio:** Puntaje promedio > 50/100
        
        Países con desarrollo medio-alto en la mayoría de áreas.
        
        ---
        
        #### 🔵 Estrategia sin Implementación
        **Criterio:** Estrategia > 60 y Aplicaciones < 40
        
        Países con marcos estratégicos fuertes pero baja aplicación práctica.
        
        ---
        
        #### 🟠 Regulación sin Capacidades
        **Criterio:** Regulación > 60 y Capacidades < 40
        
        Países con marco regulatorio establecido pero limitadas capacidades operativas.
        """)
    
    with col2:
        st.markdown("""
        #### 🟣 Implementación sin Regulación
        **Criterio:** Aplicaciones > 50 y Regulación < 40
        
        Países con aplicaciones de IA pero marco normativo débil.
        
        ---
        
        #### 🔴 Rezagados en Gobernanza e Implementación
        **Criterio:** Puntaje promedio < 35/100
        
        Países en etapas iniciales en la mayoría de dimensiones.
        
        ---
        
        #### ⚪ Desarrollo Irregular
        **Criterio:** Perfil que no encaja en categorías anteriores
        
        Países con fortalezas y debilidades dispersas.
        """)
    
    st.divider()
    
    st.subheader("🎯 Clusters Identificados en los Datos")
    
    st.markdown(f"""
    El análisis ha identificado **{len(perfiles)} clusters** en los datos del cuestionario AIRA. 
    A continuación se presenta el perfil detallado de cada cluster:
    """)
    
    # Mostrar perfil de cada cluster
    for perfil in perfiles:
        cluster_id = perfil['cluster_id']
        n_paises = perfil['n_paises']
        score_general = perfil['score_general']
        
        # Preparar datos para asignar tipología
        perfil_completo = {
            'Estrategia': perfil['scores']['Estrategia'],
            'Regulación': perfil['scores']['Regulación'],
            'Gobernanza de Datos': perfil['scores']['Gobernanza de Datos'],
            'Aplicaciones': perfil['scores']['Aplicaciones'],
            'Capacidades': perfil['scores']['Capacidades'],
            'score_general': score_general
        }
        
        # Asignar tipología
        emoji, tipologia, color = asignar_tipologia(perfil_completo)
        
        st.markdown(f"### {emoji} Cluster {cluster_id}: {tipologia}")
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            st.metric("Países", n_paises)
            st.metric("Score General", f"{score_general:.1f}/100")
        
        with col2:
            # Encontrar área más fuerte y más débil
            scores_dict = perfil['scores']
            area_fuerte = max(scores_dict, key=scores_dict.get)
            area_debil = min(scores_dict, key=scores_dict.get)
            
            st.markdown(f"""
            **Área más fuerte:**  
            {area_fuerte} ({scores_dict[area_fuerte]:.1f})
            
            **Área más débil:**  
            {area_debil} ({scores_dict[area_debil]:.1f})
            """)
        
        with col3:
            st.markdown("**Países en este cluster:**")
            st.write(", ".join(perfil['paises']))
        
        # Gráfico radar del perfil (usando el color de la tipología)
        fig_radar = crear_grafico_radar_perfil(perfil, f"Perfil Cluster {cluster_id}", color)
        st.plotly_chart(fig_radar, width='stretch')
        
        # Tabla de scores detallada
        scores_df = pd.DataFrame({
            'Área': list(scores_dict.keys()),
            'Score': [f"{v:.1f}" for v in scores_dict.values()]
        })
        
        st.dataframe(scores_df, width='stretch', hide_index=True)
        
        st.divider()
    
    # ==================== COMPARACIÓN ENTRE CLUSTERS ====================
    st.header("6️⃣ Comparación entre Clusters")
    
    fig_comparacion = crear_grafico_comparacion_clusters(perfiles)
    st.plotly_chart(fig_comparacion, width='stretch')
    
    # Tabla comparativa
    st.subheader("📊 Tabla Comparativa de Scores")
    
    df_comparacion = pd.DataFrame([
        {
            'Cluster': perfil['cluster_id'],
            'N° Países': perfil['n_paises'],
            'Score General': perfil['score_general'],
            **perfil['scores']
        }
        for perfil in perfiles
    ])
    
    st.dataframe(
        df_comparacion.style.format({
            'Score General': '{:.1f}',
            'Estrategia': '{:.1f}',
            'Regulación': '{:.1f}',
            'Gobernanza de Datos': '{:.1f}',
            'Aplicaciones': '{:.1f}',
            'Capacidades': '{:.1f}'
        }),
        width='stretch',
        hide_index=True
    )
    
    st.divider()
    
    # ==================== INTERPRETACIÓN Y CONCLUSIONES ====================
    st.header("7️⃣ Interpretación de Resultados")
    
    st.markdown("""
    ### Principales Hallazgos del Clustering
    """)
    
    # Generar insights automáticos
    cluster_mayor = max(perfiles, key=lambda x: x['n_paises'])
    cluster_avanzado = max(perfiles, key=lambda x: x['score_general'])
    
    st.success(f"""
    **Distribución de países:**
    
    - El **Cluster {cluster_mayor['cluster_id']}** es el más numeroso con {cluster_mayor['n_paises']} países 
      ({cluster_mayor['n_paises']/sum(p['n_paises'] for p in perfiles)*100:.1f}% del total)
    - El **Cluster {cluster_avanzado['cluster_id']}** tiene el score general más alto ({cluster_avanzado['score_general']:.1f}/100)
    """)
    
    # Análisis de brechas
    st.markdown("### 📈 Análisis de Brechas entre Clusters")
    
    if len(perfiles) >= 2:
        # Calcular diferencias entre clusters
        for area in AIRA_GRUPOS.keys():
            valores = [p['scores'][area] for p in perfiles]
            brecha = max(valores) - min(valores)
            
            st.markdown(f"**{area}**: Brecha de {brecha:.1f} puntos entre clusters")
    
    st.info("""
    **Implicaciones para Políticas Públicas:**
    
    El análisis de clustering permite identificar grupos de países con necesidades similares, 
    facilitando:
    
    - 🎯 **Diseño de intervenciones dirigidas** según tipología
    - 🤝 **Intercambio de mejores prácticas** entre países del mismo cluster
    - 📊 **Benchmarking** con países en clusters más avanzados
    - 📈 **Planificación de trayectorias** para transitar entre clusters
    """)
