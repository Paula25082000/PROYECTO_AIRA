"""
Página de Conclusiones y Recomendaciones
=========================================
Esta página presenta los insights clave del análisis
y recomendaciones para políticas públicas.
"""

import streamlit as st


def render_conclusiones():
    """
    Renderiza la página de conclusiones y recomendaciones.
    """
    st.title("💡 Conclusiones y Recomendaciones")
    
    st.markdown("""
    Esta sección sintetiza los **hallazgos clave** del análisis exploratorio y de clustering, 
    proporcionando insights accionables para responsables de políticas públicas.
    """)
    
    st.divider()
    
    # ==================== RESUMEN EJECUTIVO ====================
    st.header("📋 Resumen Ejecutivo")
    
    st.markdown("""
    ### Objetivo del Análisis
    
    Evaluar el grado de **preparación y madurez** de 53 países de la Región Europea de la OMS 
    para implementar Inteligencia Artificial en sus sistemas de salud, identificando patrones, 
    brechas y tipologías de países.
    
    ### Metodología Aplicada
    
    1. **Análisis Exploratorio de Datos (EDA)**: Visualizaciones y análisis descriptivo de 75 variables AIRA
    2. **Machine Learning (Clustering)**: K-means para identificar tipologías de países
    3. **Análisis de Perfiles**: Evaluación de scores por área temática
    
    ### Datos Analizados
    
    - **53 países** de la Región Europea OMS
    - **75 variables AIRA** organizadas en 5 secciones temáticas
    - **3,975 puntos de datos** individuales
    - **Período**: 2024-2025
    """)
    
    st.divider()
    
    # ==================== HALLAZGOS PRINCIPALES ====================
    st.header("🔍 Hallazgos Principales")
    
    st.subheader("1. Identificación de Dos Tipologías de Países")
    
    st.success("""
    **Hallazgo Clave #1: Dos Grupos Naturales**
    
    El análisis de clustering identificó **2 tipologías principales** de países:
    
    - **Cluster 0 (77%)**: Desarrollo Irregular - 41 países
      - Score general: ~39/100
      - Área más débil: Regulación (18.7/100)
      - Área más fuerte: Gobernanza de Datos (55.1/100)
    
    - **Cluster 1 (23%)**: En Transición Avanzada - 12 países
      - Score general: ~65.5/100
      - Área más débil: Estrategia (40.5/100)
      - Área más fuerte: Aplicaciones (79.2/100)
    
    **Implicación**: La mayoría de países europeos aún están en etapas iniciales o intermedias 
    de preparación para IA en salud.
    """)
    
    st.divider()
    
    st.subheader("2. La Regulación como Factor Diferencial Clave")
    
    st.warning("""
    **Hallazgo Clave #2: Brecha Regulatoria**
    
    La **regulación** es el área con la mayor diferencia entre clusters (+39.9 puntos):
    
    - Cluster 0: 18.7/100
    - Cluster 1: 58.6/100
    
    **Implicación**: Un marco regulatorio sólido es **crítico** para pasar de desarrollo irregular 
    a transición avanzada. Los países que más avanzan en IA para salud son aquellos que no solo 
    experimentan, sino que **normalizan la IA dentro de un marco jurídico robusto**.
    """)
    
    st.divider()
    
    st.subheader("3. La Estrategia NO es un Pre-requisito")
    
    st.info("""
    **Hallazgo Clave #3: Implementación antes que Estrategia**
    
    El Cluster 1 (más avanzado) tiene:
    - **Aplicaciones fuertes** (79.2/100)
    - **Estrategia moderada** (40.5/100)
    
    **Implicación**: Muchos países avanzan **primero en implementación práctica** y luego 
    formalizan estrategias. La innovación en salud digital puede ocurrir sin esperar marcos 
    estratégicos completos.
    """)
    
    st.divider()
    
    st.subheader("4. Efecto del Contexto Europeo en Gobernanza de Datos")
    
    st.success("""
    **Hallazgo Clave #4: Piso Común Europeo**
    
    Incluso el Cluster 0 (desarrollo irregular) tiene **gobernanza de datos aceptable** (55.1/100).
    
    **Explicación**: La legislación europea común (GDPR, etc.) eleva el **estándar mínimo** 
    de todos los países en materia de datos.
    
    **Implicación**: Los marcos supranacionales pueden **homogeneizar** ciertos aspectos de 
    madurez digital, creando condiciones favorables para IA en salud.
    """)
    
    st.divider()
    
    # ==================== ANÁLISIS POR ÁREA TEMÁTICA ====================
    st.header("📊 Análisis por Área Temática")
    
    areas = [
        {
            "nombre": "🎨 Estrategia",
            "situacion": "Oportunidad de mejora",
            "descripcion": "Incluso países avanzados tienen scores moderados (40.5/100)",
            "recomendacion": "Desarrollar estrategias nacionales específicas de IA en salud, no solo transversales"
        },
        {
            "nombre": "⚖️ Regulación",
            "situacion": "Factor crítico diferencial",
            "descripcion": "Mayor brecha entre clusters (+39.9 puntos)",
            "recomendacion": "Priorizar desarrollo de marcos regulatorios, enfoques basados en riesgo y responsabilidad legal"
        },
        {
            "nombre": "💾 Gobernanza de Datos",
            "situacion": "Fortaleza relativa común",
            "descripcion": "Área más equilibrada gracias a GDPR",
            "recomendacion": "Continuar fortaleciendo infraestructura de datos y autoridades nacionales"
        },
        {
            "nombre": "🏥 Aplicaciones",
            "situacion": "Motor de innovación",
            "descripcion": "Países avanzados destacan en implementación práctica (79.2/100)",
            "recomendacion": "Fomentar proyectos piloto, sandbox regulatorios y evidencia de casos de uso exitosos"
        },
        {
            "nombre": "🎓 Capacidades",
            "situacion": "Infraestructura humana en desarrollo",
            "descripcion": "Scores moderados en ambos clusters",
            "recomendacion": "Invertir en formación, atracción de talento y centros de investigación en IA y salud"
        }
    ]
    
    for area in areas:
        with st.expander(f"{area['nombre']} - {area['situacion']}"):
            st.markdown(f"""
            **Situación actual:** {area['descripcion']}
            
            **Recomendación:** {area['recomendacion']}
            """)
    
    st.divider()
    
    # ==================== RECOMENDACIONES POR TIPO DE ACTOR ====================
    st.header("🎯 Recomendaciones por Actor")
    
    tab1, tab2 = st.tabs([
        "🏛️ Gobiernos", 
        "🏥 Sector Salud"
    ])
    
    with tab1:
        st.markdown("### Recomendaciones para Gobiernos")
        
        # Crear dos columnas para distribuir las recomendaciones horizontalmente
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Para países en Cluster 0 (Desarrollo Irregular):
            
            1. **Prioridad 1 - Regulación**
               - Desarrollar marcos regulatorios básicos para IA en salud
               - Adoptar enfoque basado en riesgo (alineado con Ley de IA de la UE)
               - Establecer requisitos mínimos de transparencia y responsabilidad
            
            2. **Prioridad 2 - Estrategia**
               - Crear estrategia sectorial específica de IA en salud
               - Definir mecanismos de supervisión institucional
               - Establecer roadmap con metas concretas y plazos
            
            3. **Prioridad 3 - Capacidades**
               - Invertir en formación de profesionales de salud en IA
               - Crear programas de atracción de talento
               - Fomentar colaboración con sector académico
            
            4. **Acción Rápida - Aprendizaje de Pares**
               - Benchmarking con países del Cluster 1
               - Intercambio de mejores prácticas
               - Participación en redes regionales de IA en salud
            """)
        
        with col2:
            st.markdown("""
            #### Para países en Cluster 1 (Transición Avanzada):
            
            1. **Consolidar Estrategia**
               - Formalizar estrategia nacional específica si aún no existe
               - Alinear iniciativas dispersas bajo marco común
               - Establecer KPIs y mecanismos de monitoreo
            
            2. **Profundizar Regulación**
               - Refinar requisitos de certificación y auditoría
               - Desarrollar regímenes de responsabilidad específicos
               - Establecer sandboxes regulatorios para innovación
            
            3. **Escalar Aplicaciones**
               - Mover de pilotos a implementación a gran escala
               - Crear repositorio de evidencia de impacto
               - Fomentar interoperabilidad entre sistemas
            
            4. **Liderazgo Regional**
               - Compartir aprendizajes con países menos avanzados
               - Co-desarrollar estándares regionales
               - Facilitar colaboración transfronteriza
            """)
    
    with tab2:
        st.markdown("### Recomendaciones para el Sector Salud")
        
        # Crear dos columnas para distribuir las recomendaciones horizontalmente
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            1. **Desarrollo de Capacidades Clínicas**
               - Formación en IA para profesionales de salud
               - Alfabetización digital de pacientes
               - Creación de roles especializados (ej: "IA Clinical Champions")
            
            2. **Infraestructura de Datos**
               - Digitalización completa de historias clínicas
               - Estandarización de datos (FHIR, SNOMED, ICD)
               - Creación de lagos de datos sanitarios accesibles para investigación
            
            3. **Participación en Gobernanza**
               - Colaborar en diseño de marcos regulatorios
               - Aportar perspectiva clínica en evaluación de riesgos
               - Participar en comités de ética de IA
            """)
        
        with col2:
            st.markdown("""
            4. **Evidencia de Impacto**
               - Documentar rigurosamente resultados de implementaciones
               - Publicar casos de uso exitosos (y fracasos)
               - Contribuir a repositorios de evidencia clínica de IA
            
            5. **Ética y Responsabilidad**
               - Desarrollar guías éticas institucionales
               - Establecer procesos de consentimiento informado para IA
               - Crear mecanismos de rendición de cuentas claros
            """)
    
    st.divider()
    
    # ==================== LIMITACIONES DEL ANÁLISIS ====================
    st.header("⚠️ Limitaciones del Análisis")
    
    st.markdown("### Limitaciones Metodológicas")
    
    # Crear dos columnas para distribuir las limitaciones metodológicas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        1. **Snapshot Temporal**
           - Los datos representan un momento específico (2024-2025)
           - No captura tendencias o velocidad de cambio
           - Repetir análisis en el futuro para validar resultados
        
        2. **Auto-reporte**
           - Basado en encuestas (posible sesgo de deseabilidad social)
           - Puede haber sobre/sub-estimación de capacidades
           - No hay verificación independiente de respuestas
        """)
    
    with col2:
        st.markdown("""
        3. **Simplificación Categórica**
           - Codificación 0-1-2 simplifica realidades complejas
           - "En desarrollo" puede significar cosas muy diferentes
           - No distingue calidad, solo presencia/ausencia
        
        4. **K=2 puede ser simplista**
           - Puede haber más matices con más clusters
           - Trade-off entre simplicidad interpretativa y precisión
        """)
    
    st.markdown("---")
    
    # Crear dos columnas para limitaciones contextuales y recomendaciones futuras
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Limitaciones Contextuales
        
        1. **No considera**:
           - Tamaño económico (PIB)
           - Población y escala del sistema de salud
           - Historia previa de digitalización
           - Factores socioculturales
        
        2. **Enfoque europeo**:
           - Hallazgos pueden no generalizar a otras regiones
           - Contexto regulatorio europeo (GDPR, etc.) es único
        """)
    
    with col2:
        st.markdown("""
        ### Recomendaciones para Análisis Futuro
        
        - Análisis longitudinal (repetir en 2-3 años)
        - Validación con métodos alternativos (clustering jerárquico, DBSCAN)
        - Incorporar variables contextuales (PIB, gasto en salud, índice de digitalización)
        - Estudios de caso cualitativos para profundizar hallazgos
        """)
