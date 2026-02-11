"""
Configuración y constantes para AIRA
=====================================
Este módulo contiene todas las configuraciones, diccionarios de mapeo,
nombres de países, variables AIRA y grupos de secciones utilizados
en toda la aplicación.
"""

import os

# ==================== CONFIGURACIÓN GENERAL ====================

# Ruta absoluta al archivo de datos (funciona desde cualquier directorio)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'Data', 'AIRAData_final.csv')

# Configuración de Plotly
PLOTLY_CONFIG = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['lasso2d', 'select2d']
}

# ==================== DICCIONARIOS DE MAPEO ====================

# Mapeo de códigos ISO de país a nombres en español
COUNTRY_NAMES = {
    'ALB': 'Albania', 'AND': 'Andorra', 'ARM': 'Armenia', 'AUT': 'Austria',
    'AZE': 'Azerbaiyán', 'BLR': 'Bielorrusia', 'BEL': 'Bélgica', 'BIH': 'Bosnia y Herzegovina',
    'BGR': 'Bulgaria', 'HRV': 'Croacia', 'CYP': 'Chipre', 'CZE': 'República Checa',
    'DNK': 'Dinamarca', 'EST': 'Estonia', 'FIN': 'Finlandia', 'FRA': 'Francia',
    'GEO': 'Georgia', 'DEU': 'Alemania', 'GRC': 'Grecia', 'HUN': 'Hungría',
    'ISL': 'Islandia', 'IRL': 'Irlanda', 'ISR': 'Israel', 'ITA': 'Italia',
    'KAZ': 'Kazajistán', 'KGZ': 'Kirguistán', 'LVA': 'Letonia', 'LTU': 'Lituania',
    'LUX': 'Luxemburgo', 'MLT': 'Malta', 'MDA': 'Moldavia', 'MCO': 'Mónaco',
    'MNE': 'Montenegro', 'NLD': 'Países Bajos', 'MKD': 'Macedonia del Norte', 'NOR': 'Noruega',
    'POL': 'Polonia', 'PRT': 'Portugal', 'ROU': 'Rumania', 'RUS': 'Rusia',
    'SMR': 'San Marino', 'SRB': 'Serbia', 'SVK': 'Eslovaquia', 'SVN': 'Eslovenia',
    'ESP': 'España', 'SWE': 'Suecia', 'CHE': 'Suiza', 'TJK': 'Tayikistán',
    'TKM': 'Turkmenistán', 'TUR': 'Turquía', 'UKR': 'Ucrania', 'GBR': 'Reino Unido',
    'UZB': 'Uzbekistán'
}

# Mapeo de respuestas AIRA a español
RESPONSE_LABELS = {
    'YES': 'Sí',
    'NO': 'No',
    'UD': 'En desarrollo',
    'DNK': 'No sabe',
    'N/A': 'No aplicable'
}

# Mapeo de respuestas a valores numéricos para visualización
VALUE_MAPPING = {
    'YES': 2,
    'UD': 1,
    'NO': 0,
    'DNK': -1,
    'N/A': -2
}

# Colores para las respuestas en mapas y gráficos
# Colores discretos específicos para cada respuesta
COLOR_DISCRETE_MAP = {
    'YES': '#4caf50',    # Verde (Sí)
    'NO': '#f44336',     # Rojo (No)
    'UD': '#ffeb3b',     # Amarillo (En desarrollo)
    'DNK': '#2196f3',    # Azul (No sabe)
    'N/A': '#9e9e9e'     # Gris (No aplicable)
}

# Escala de color para mapas (mantener para compatibilidad)
COLOR_SCALE = [
    [0.0, '#f44336'],    # Rojo (No)
    [0.25, '#ffeb3b'],   # Amarillo (En desarrollo)
    [0.5, '#4caf50'],    # Verde (Sí)
    [0.75, '#2196f3'],   # Azul (No sabe)
    [1.0, '#9e9e9e']     # Gris (No aplicable)
]

# ==================== GRUPOS DE VARIABLES AIRA ====================

# Sección 1: Contexto estratégico
AIRA_SECCION_1 = {
    'nombre': 'Contexto Estratégico',
    'rango': range(1, 8),
    'variables': ['AIRA_1', 'AIRA_2', 'AIRA_3', 'AIRA_4', 'AIRA_5', 'AIRA_6', 'AIRA_7'],
    'descripcion': 'Estrategias nacionales y mecanismos de supervisión de IA en salud'
}

# Sección 2: Contexto normativo
AIRA_SECCION_2 = {
    'nombre': 'Contexto Normativo',
    'rango': range(8, 37),
    'variables': [f'AIRA_{i}' for i in range(8, 37)],
    'descripcion': 'Marco regulatorio, ética, responsabilidad y estándares legales'
}

# Sección 3: Gobernanza de datos
AIRA_SECCION_3 = {
    'nombre': 'Gobernanza de Datos Sanitarios',
    'rango': range(37, 47),
    'variables': [f'AIRA_{i}' for i in range(37, 47)],
    'descripcion': 'Estrategias de datos, infraestructura y regulación del uso de datos'
}

# Sección 4: Aplicaciones de IA
AIRA_SECCION_4 = {
    'nombre': 'Aplicaciones de IA para la Salud',
    'rango': range(47, 54),
    'variables': [f'AIRA_{i}' for i in range(47, 54)],
    'descripcion': 'Implementación práctica de sistemas de IA en el sector salud'
}

# Sección 5: Desarrollo de capacidades
AIRA_SECCION_5 = {
    'nombre': 'Desarrollo de Capacidades',
    'rango': range(71, 76),
    'variables': [f'AIRA_{i}' for i in range(71, 76)],
    'descripcion': 'Formación, talento y capacidades humanas en IA'
}

# Diccionario completo de secciones
SECCIONES = {
    'seccion_1': AIRA_SECCION_1,
    'seccion_2': AIRA_SECCION_2,
    'seccion_3': AIRA_SECCION_3,
    'seccion_4': AIRA_SECCION_4,
    'seccion_5': AIRA_SECCION_5
}

# ==================== TÍTULOS DE VARIABLES AIRA ====================

AIRA_TITULOS = {
    'AIRA_1': 'Estrategia nacional de IA en el sector de la salud',
    'AIRA_2': 'Estrategia nacional de IA transversal (no sectorial)',
    'AIRA_3': 'Supervisión a través de agencia gubernamental existente',
    'AIRA_4': 'Supervisión a través de nueva agencia gubernamental',
    'AIRA_5': 'Supervisión a través de consejo asesor de expertos',
    'AIRA_6': 'Supervisión a través de organismo independiente',
    'AIRA_7': 'Supervisión por múltiples agencias compartidas',
    'AIRA_8': 'Medidas legislativas para gobernanza de IA en salud',
    'AIRA_9': 'Evaluación de lagunas en legislación existente',
    'AIRA_10': 'Desarrollo de orientaciones sobre legislación existente',
    'AIRA_11': 'Modificación de legislación y políticas existentes',
    'AIRA_12': 'Nuevas leyes obligatorias transversales sobre IA',
    'AIRA_13': 'Leyes obligatorias específicas por sector',
    'AIRA_14': 'Normas de soft law o principios éticos sectoriales',
    'AIRA_15': 'Códigos de buenas prácticas y estándares voluntarios',
    'AIRA_16': 'Adopción de enfoque basado en el riesgo',
    'AIRA_17': 'Directrices sobre implicaciones éticas',
    'AIRA_18': 'Listas de verificación o herramientas éticas',
    'AIRA_19': 'Orientaciones sobre evaluación de impacto algorítmico',
    'AIRA_20': 'Orientaciones sobre evaluación de impacto en protección de datos',
    'AIRA_21': 'Orientaciones sobre evaluación de impacto en derechos fundamentales',
    'AIRA_22': 'Orientaciones sobre regímenes de responsabilidad existentes',
    'AIRA_23': 'Nuevo régimen de responsabilidad específico para IA en salud',
    'AIRA_24': 'Nuevo régimen de responsabilidad para IA (no específico)',
    'AIRA_25': 'Identificación de agencias reguladoras',
    'AIRA_26': 'Cooperación entre agencias reguladoras',
    'AIRA_27': 'Requisitos de documentación y trazabilidad',
    'AIRA_28': 'Requisitos de transparencia y explicabilidad',
    'AIRA_29': 'Requisitos de robustez y seguridad',
    'AIRA_30': 'Requisitos de privacidad y protección de datos',
    'AIRA_31': 'Requisitos de monitorización post-comercialización',
    'AIRA_32': 'Políticas de adquisición pública de IA',
    'AIRA_33': 'Mecanismos de auditoría',
    'AIRA_34': 'Mecanismos de reparación y recurso',
    'AIRA_35': 'Certificación de sistemas de IA',
    'AIRA_36': 'Requisitos sobre impacto ambiental',
    'AIRA_37': 'Estrategia de gobernanza de datos de salud',
    'AIRA_38': 'Marco de gobernanza de datos de salud',
    'AIRA_39': 'Autoridad de datos de salud',
    'AIRA_40': 'Centro o plataforma nacional de datos de salud',
    'AIRA_41': 'Estándares para almacenes de datos',
    'AIRA_42': 'Regulación del uso secundario de datos',
    'AIRA_43': 'Extracción rutinaria de datos de EHR para registros',
    'AIRA_44': 'Creación de bases de datos regionales/nacionales',
    'AIRA_45': 'Reglas para compartir datos con sector privado',
    'AIRA_46': 'Reglas para intercambio transfronterizo de datos',
    'AIRA_47': 'Aplicaciones de IA en diagnóstico',
    'AIRA_48': 'Aplicaciones de IA en tratamiento',
    'AIRA_49': 'Aplicaciones de IA en vigilancia epidemiológica',
    'AIRA_50': 'Aplicaciones de IA en gestión de recursos',
    'AIRA_51': 'Aplicaciones de IA en investigación',
    'AIRA_52': 'Aplicaciones de IA en telemedicina',
    'AIRA_53': 'Aplicaciones de IA en salud pública',
    'AIRA_71': 'Programas de formación en IA para profesionales de salud',
    'AIRA_72': 'Programas académicos en IA y salud',
    'AIRA_73': 'Centros de investigación en IA y salud',
    'AIRA_74': 'Políticas de atracción de talento en IA',
    'AIRA_75': 'Colaboración internacional en desarrollo de capacidades'
}

# ==================== GRUPOS PARA ANÁLISIS ML ====================

# Grupos de variables para cálculo de scores por área
AIRA_GRUPOS = {
    'Estrategia': ['AIRA_1', 'AIRA_2'],
    'Regulación': [f'AIRA_{i}' for i in range(8, 37)],
    'Gobernanza de Datos': [f'AIRA_{i}' for i in range(37, 47)],
    'Aplicaciones': [f'AIRA_{i}' for i in range(47, 54)],
    'Capacidades': [f'AIRA_{i}' for i in range(71, 76)]
}

# ==================== CONFIGURACIÓN DE ESTILOS ====================

# CSS personalizado para la aplicación
CUSTOM_CSS = """
<style>
    /* Estilos generales */
    .main {
        padding: 2rem;
    }
    
    /* Título principal */
    h1 {
        color: #1e3a8a;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    /* Subtítulos */
    h2 {
        color: #2563eb;
        font-size: 2rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 0.5rem;
    }
    
    h3 {
        color: #3b82f6;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    /* Tarjetas de información */
    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #f8fafc;
    }
    
    /* Botones */
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #2563eb;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Selectbox y otros widgets */
    .stSelectbox {
        margin-bottom: 1rem;
    }
    
    /* Dataframes */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* Secciones expandibles */
    .streamlit-expanderHeader {
        background-color: #f1f5f9;
        border-radius: 8px;
        font-weight: 600;
        color: #1e3a8a;
    }
    
    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1e3a8a;
        color: white;
        text-align: center;
        padding: 1rem;
        font-size: 0.9rem;
    }
    
    /* Alertas */
    .stAlert {
        border-radius: 8px;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    /* Ocultar páginas automáticas de Streamlit en el sidebar */
    section[data-testid="stSidebarNav"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        overflow: hidden !important;
    }
    
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Ocultar la navegación de páginas */
    ul[data-testid="stSidebarNavItems"] {
        display: none !important;
    }
</style>
"""

# ==================== TEXTOS DE LA APLICACIÓN ====================

# Texto de bienvenida
TEXTO_BIENVENIDA = """
Bienvenido a **AIRA** - un análisis exhaustivo del estado de preparación 
y madurez de los países europeos en el uso de la Inteligencia Artificial para la salud.
"""

# Descripción del proyecto
DESCRIPCION_PROYECTO = """
### 📊 Sobre este proyecto

Esta aplicación analiza datos del **Assessment of Implementation Readiness for AI (AIRA)** 
de la Región Europea de la OMS.

**Objetivo**: Entender el grado de preparación de 53 países europeos para implementar 
IA en sus sistemas de salud mediante análisis exploratorio de datos (EDA) y Machine Learning (Clustering).

**Datos**: 75 indicadores AIRA organizados en 5 secciones temáticas (estrategia, regulación, 
gobernanza de datos, aplicaciones y capacidades), con respuestas categóricas del periodo 2024-2025.
"""
