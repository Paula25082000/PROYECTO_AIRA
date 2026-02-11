# 🏥 AIRA

**Análisis de Preparación para IA en Salud - Región Europea OMS**

Aplicación interactiva desarrollada con Streamlit para analizar el grado de preparación de 53 países europeos en la implementación de Inteligencia Artificial en sus sistemas de salud.

---

## 📋 Descripción del Proyecto

Esta aplicación analiza datos del **Assessment of Implementation Readiness for AI (AIRA)** de la Región Europea de la OMS, proporcionando:

- ✅ **Análisis Exploratorio de Datos (EDA)** completo con visualizaciones interactivas
- 🤖 **Machine Learning (Clustering)** para identificar tipologías de países
- 📊 **Visualizaciones dinámicas** con mapas, gráficos y tablas interactivas
- 💡 **Insights accionables** para políticas públicas

---

## 🎯 Características Principales

### 1. **Sección Inicio**
- Presentación del proyecto y metodología
- Métricas clave del análisis
- Guía de navegación

### 2. **Origen y Datos**
- Información sobre la fuente de datos AIRA
- Exploración del dataset
- Filtrado y búsqueda de datos
- Descarga de datos personalizados

### 3. **Análisis Exploratorio (EDA)**
- Análisis por las 5 secciones temáticas AIRA:
  - Contexto Estratégico
  - Contexto Normativo
  - Gobernanza de Datos
  - Aplicaciones de IA
  - Desarrollo de Capacidades
- Mapas coropléticos de Europa
- Gráficos de distribución
- Tablas pivotadas interactivas
- Insights automáticos por variable

### 4. **Machine Learning - Clustering**
- Preparación de datos para ML
- Determinación del K óptimo (método del codo + silueta)
- Aplicación de K-means
- Visualización con PCA (2D y 3D)
- Perfiles detallados de clusters
- Comparación entre tipologías de países

### 5. **Conclusiones**
- Hallazgos principales del análisis
- Recomendaciones por actor (gobiernos, ONG, sector privado)
- Limitaciones del estudio
- Próximos pasos sugeridos

---

## 🚀 Instalación y Ejecución

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar o descargar el proyecto

Asegúrate de tener la siguiente estructura de carpetas:

```
PROYECTO_AIRA/
├── app/
│   ├── app.py              # Aplicación principal
│   ├── config.py           # Configuración y constantes
│   ├── utils.py            # Funciones auxiliares
│   ├── visualizations.py   # Funciones de visualización
│   ├── requirements.txt    # Dependencias
│   └── pages/              # Módulos de páginas
│       ├── __init__.py
│       ├── inicio.py
│       ├── origen_datos.py
│       ├── eda.py
│       ├── ml_clustering.py
│       └── conclusiones.py
└── Data/
    └── AIRAData_final.csv  # Archivo de datos
```

### Paso 2: Instalar dependencias

Navega a la carpeta `app/` y ejecuta:

```bash
cd app
pip install -r requirements.txt
```

### Paso 3: Ejecutar la aplicación

Desde la carpeta `app/`, ejecuta:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📦 Dependencias

El proyecto utiliza las siguientes librerías principales:

- **streamlit** >= 1.28.0 - Framework para crear aplicaciones web interactivas
- **pandas** >= 2.0.0 - Análisis y manipulación de datos
- **numpy** >= 1.24.0 - Computación numérica
- **plotly** >= 5.17.0 - Visualizaciones interactivas
- **scikit-learn** >= 1.3.0 - Machine Learning (K-means, PCA)

---

## 🗂️ Estructura del Código

### Arquitectura Modular

El código está organizado en módulos especializados para facilitar mantenimiento y escalabilidad:

#### **config.py**
- Configuración global de la aplicación
- Diccionarios de mapeo (países, respuestas, variables)
- Constantes y textos
- Estilos CSS personalizados

#### **utils.py**
- Funciones de carga de datos
- Transformaciones y enriquecimiento de DataFrames
- Preparación de datos para ML
- Cálculos estadísticos y scores
- Utilidades de formato

#### **visualizations.py**
- Creación de mapas coropléticos
- Gráficos de barras y distribuciones
- Tablas interactivas con colores
- Gráficos de radar y comparación
- Visualizaciones de clustering (PCA, codo, silueta)
- Heatmaps

#### **pages/** (Módulos de páginas)
- **inicio.py**: Página de bienvenida y visión general
- **origen_datos.py**: Información sobre datos y exploración
- **eda.py**: Análisis exploratorio completo
- **ml_clustering.py**: Análisis de Machine Learning
- **conclusiones.py**: Hallazgos y recomendaciones

#### **app.py**
- Punto de entrada de la aplicación
- Gestión de navegación y estado
- Renderizado de páginas
- Manejo de errores

---

## 🎨 Características de UX/UI

- **Diseño responsive** que se adapta a diferentes tamaños de pantalla
- **CSS personalizado** con gradientes y animaciones sutiles
- **Navegación intuitiva** con menú lateral organizado
- **Gráficos interactivos** con zoom, filtrado y descarga
- **Colores consistentes** según tipo de respuesta:
  - 🟢 Verde: Sí (implementado)
  - 🟠 Ámbar: En desarrollo
  - 🔴 Rojo: No
  - 🔵 Azul: No sabe
  - ⚫ Gris: No aplicable
- **Métricas destacadas** con deltas y contexto
- **Expandibles** para información adicional sin abrumar
- **Tooltips y ayuda contextual** en secciones clave

---

## 📊 Datos

### Fuente
**WHO Europe - AIRA Survey (2024-2025)**

### Contenido
- **53 países** de la Región Europea de la OMS
- **75 variables AIRA** sobre preparación en IA para salud
- **5 secciones temáticas**:
  1. Contexto estratégico (7 variables)
  2. Contexto normativo (29 variables)
  3. Gobernanza de datos (10 variables)
  4. Aplicaciones de IA (7 variables)
  5. Desarrollo de capacidades (5 variables)

### Formato de Respuestas
- **YES**: Implementado completamente
- **NO**: No implementado
- **UD**: En desarrollo
- **DNK**: No sabe / No tiene información
- **N/A**: No aplicable

---

## 🔬 Metodología de Análisis

### Análisis Exploratorio de Datos (EDA)
1. Carga y limpieza de datos
2. Enriquecimiento con etiquetas descriptivas
3. Visualización por variable y sección
4. Análisis de distribuciones
5. Identificación de patrones

### Machine Learning (Clustering)
1. **Preparación**: Transformación de formato largo a ancho
2. **Codificación**: YES=2, UD=1, NO=0
3. **Imputación**: Valores faltantes con mediana
4. **Validación**: Método del codo + Coeficiente de Silueta
5. **Clustering**: K-means con K óptimo
6. **Visualización**: PCA para reducción a 2D/3D
7. **Interpretación**: Scores por área y perfiles de clusters

---

## 💡 Casos de Uso

### Para Gobiernos
- **Benchmarking**: Comparar preparación con otros países
- **Priorización**: Identificar áreas de mejora
- **Planificación**: Diseñar roadmaps basados en evidencia

### Para Organizaciones Internacionales
- **Asistencia técnica dirigida**: Intervenciones según tipología de país
- **Monitoreo**: Seguimiento de progreso regional
- **Intercambio de conocimiento**: Facilitar aprendizaje entre pares

### Para Investigadores
- **Estudios comparativos**: Análisis de políticas públicas
- **Predicción**: Modelar trayectorias de desarrollo
- **Causalidad**: Identificar factores críticos de éxito

### Para Sector Privado
- **Estrategia de mercado**: Identificar oportunidades por país
- **Productos diferenciados**: Adaptar soluciones a madurez del mercado
- **Partnerships**: Detectar países para colaboración

---

## 🛠️ Personalización

### Actualizar datos
Reemplaza el archivo `Data/AIRAData_final.csv` con nuevos datos manteniendo el mismo formato.

### Modificar estilos
Edita la variable `CUSTOM_CSS` en `config.py`.

### Agregar nuevas visualizaciones
Añade funciones en `visualizations.py` y úsalas en las páginas correspondientes.

### Crear nuevas secciones
1. Crea un nuevo archivo `.py` en `pages/`
2. Define función `render_NOMBRE()`
3. Importa y añade en `app.py`

---

## 📝 Comentarios y Documentación

Todo el código está **extensamente comentado** para facilitar:
- Comprensión de la lógica
- Mantenimiento futuro
- Ampliación de funcionalidades
- Reutilización de componentes

Cada archivo incluye:
- **Docstrings** en módulos, clases y funciones
- **Comentarios inline** para lógica compleja
- **Separadores visuales** para organización

---

## 🤝 Contribuciones

Para contribuir al proyecto:

1. Mantén la estructura modular
2. Documenta todo el código nuevo
3. Sigue las convenciones de nombres existentes
4. Prueba exhaustivamente antes de integrar
5. Actualiza este README si es necesario

---

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos y de análisis de políticas públicas.

**Fuente de datos**: WHO Europe - AIRA Survey  
**Uso**: Libre para investigación, educación y políticas públicas

---

## 📧 Contacto

Para preguntas, sugerencias o reportar problemas:

- Consulta la documentación de [WHO Europe](https://www.who.int/europe)
- Revisa los comentarios en el código
- Consulta la sección "About" en la aplicación

---

## 🙏 Agradecimientos

- **WHO Europe** por los datos del AIRA Survey
- **Comunidad de Streamlit** por el framework
- **Plotly** por las visualizaciones interactivas
- **Scikit-learn** por las herramientas de ML

---

## 📚 Referencias

- [WHO Europe AIRA](https://www.who.int/europe)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)

---

**Versión**: 1.0  
**Última actualización**: Febrero 2025  
**Estado**: Producción

---

*"La inteligencia artificial tiene el potencial de transformar la salud global, pero solo si se implementa con equidad, ética y evidencia."*
