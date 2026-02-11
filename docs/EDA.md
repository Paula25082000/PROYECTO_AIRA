# Guía narrativa del EDA – AIRA (IA para la salud en la Región Europea de la OMS)

## 1. Propósito del análisis y visión general

Este Análisis Exploratorio de Datos (EDA) tiene como objetivo entender **el grado de preparación y madurez de los países europeos en el uso de la Inteligencia Artificial (IA) para la salud**, utilizando el cuestionario AIRA de la OMS como marco estructurador.

Más que un simple inventario de respuestas, el EDA busca responder a preguntas narrativas clave:

- ¿En qué punto del camino hacia la IA en salud se encuentra cada país?
- ¿Cómo se conectan **estrategia, regulación, gobernanza de datos, aplicaciones reales** y **capacidades humanas**?
- ¿Dónde están las palancas y los cuellos de botella principales para la adopción ética y sostenible de la IA en salud?

El análisis se apoya en **visualizaciones interactivas** (mapas coropléticos, gráficos de barras y tablas dinámicas) construidas con `pandas` y `plotly`, y se organiza en 5 bloques que siguen la arquitectura conceptual del cuestionario AIRA:

1. Contexto estratégico (AIRA_1 – AIRA_7)
2. Contexto normativo (AIRA_8 – AIRA_36)
3. Gobernanza de los datos sanitarios (AIRA_37 – AIRA_46)
4. Aplicaciones de la IA para la salud (AIRA_47 – AIRA_53)
5. Desarrollo de capacidades en IA (AIRA_71 – AIRA_75)

Esta guía resume la lógica del EDA, las decisiones metodológicas y **las historias que se pueden contar** a partir de él, con el objetivo de que sirva como **blueprint para futuros paneles de inteligencia de negocio (BI)**.

---

## 2. Metodología técnica del EDA

### 2.1 Fuente de datos y estructura

- **Fuente**: conjunto de datos AIRA publicado por la OMS Europa.
- **Archivo**: `Data/AIRAData_final.csv`.
- **Unidades de análisis**: combinaciones `país – indicador AIRA`.
- **Identificadores clave**:
	- `COUNTRY_REGION`: código ISO de país.
	- `Measure_code`: código del indicador (AIRA_1, AIRA_2, …).
	- `AIRA_SIMPLE`: respuesta codificada (YES, NO, UD, DNK, N/A).

En el notebook se realiza:

- Carga del dataset con `pandas` y verificación básica de dimensiones y primeras filas.
- Creación de diccionarios auxiliares para **traducción a español**:
	- Códigos de país → nombre de país (`country_names`).
	- Respuestas → etiquetas en español (`response_names`).
	- Respuestas → valores numéricos para colorear mapas (`value_mapping`).

Esto permite trabajar con visualizaciones semánticamente claras (etiquetas legibles) y, al mismo tiempo, mantener una codificación estructurada internamente.

### 2.2 Enfoque visual y analítico

Para casi todas las variables AIRA se repite un **patrón de análisis muy estable**, ideal para trasladar a un panel BI:

1. **Filtro por indicador** (`Measure_code == 'AIRA_xx'`).
2. Enriquecimiento con columnas derivadas:
	 - Nombre del país.
	 - Respuesta en español.
	 - Valor numérico para color.
3. **Mapa coroplético de Europa** (plotly `choropleth`):
	 - Muestra, país a país, el estado de cada indicador.
	 - Escala de color coherente: verde (Sí), ámbar (En desarrollo), rojo (No), azul (No sabe), gris (No aplicable).
4. **Gráfico de barras**:
	 - Distribución de respuestas (conteo de países por categoría).
	 - Etiquetas con valores absolutos para lectura rápida.
5. **Salida textual de apoyo** (prints):
	 - Número de países por categoría de respuesta.
	 - Listado de países para determinadas categorías (especialmente “Sí” y “En desarrollo”).
6. **Tablas pivotadas interactivas** (plotly `Table`):
	 - Filas: países.
	 - Columnas: conjunto de variables de la sección.
	 - Celdas coloreadas según la respuesta.

Esta combinación permite pasar de una visión **macro (mapa y barras)** a una visión **micro por país (tabla)**, que es exactamente el tipo de flujo que interesa replicar en un panel de inteligencia.

---

## 3. Sección 1 – Contexto estratégico (AIRA_1 – AIRA_7)

### 3.1 Qué mide esta sección

La Sección 1 explora si los países han sentado las bases estratégicas para la IA en salud:

- **AIRA_1**: Estrategia nacional específica de IA para el sector salud.
- **AIRA_2**: Estrategia nacional transversal de IA (no sectorial) que incluye salud.
- **AIRA_3 – AIRA_7**: Modelos de **supervisión y gobernanza institucional** de la IA en salud:
	- Agencia gubernamental existente.
	- Nueva agencia gubernamental.
	- Consejo asesor de expertos.
	- Nueva entidad independiente financiada por el gobierno.
	- Múltiples agencias con responsabilidades compartidas.

En términos de storytelling, esta sección responde a la pregunta:

> “¿Existe una **visión país** de la IA en salud y quién está al mando de esa agenda?”

### 3.2 Cómo se ha analizado

- Para cada variable AIRA_1 a AIRA_7 se generan:
	- Un **mapa de Europa** que permite ver rápidamente qué países tienen estrategia o mecanismos de supervisión activos.
	- Un **gráfico de barras** con el recuento de países por respuesta.
- Se construye una **tabla pivotada de sección** (AIRA_1–AIRA_7) que, por país, muestra la combinación de:
	- Existencia de estrategia sectorial y/o multisectorial.
	- Tipo(s) de organismo responsable de la supervisión.

### 3.3 Lectura analítica y mensajes clave

Aunque el notebook imprime el detalle de conteos y países por categoría en cada variable, el valor está en la **lectura cruzada**:

- Países que **ya disponen de estrategia nacional de IA en salud (AIRA_1 = Sí)** pueden considerarse en un estadio más avanzado de madurez estratégica.
- Los que **solo cuentan con estrategia multisectorial (AIRA_2 = Sí)** pero sin estrategia específica en salud pueden estar en una fase de **alineación general de IA**, pero todavía sin foco sectorial.
- La configuración de supervisión (AIRA_3–AIRA_7) permite distinguir entre modelos:
	- **Centralizados** (una agencia única).
	- **Especializados** (nueva agencia u organismo específico).
	- **Distribuidos** (múltiples agencias con responsabilidades compartidas).

En un futuro panel, esta sección puede articular un **“índice sintético de contexto estratégico”**, combinando:

- Existencia de estrategia sectorial.
- Existencia de estrategia transversal.
- Presencia de al menos un mecanismo formal de supervisión.

Este índice podría funcionar como **punto de entrada narrativo**: un mapa que muestre el grado de madurez estratégica y permita al usuario profundizar en el resto de secciones.

---

## 4. Sección 2 – Contexto normativo (AIRA_8 – AIRA_36)

### 4.1 Qué mide esta sección

La Sección 2 examina **cómo se traduce la estrategia en regulación concreta**. Incluye:

- **Medidas legislativas específicas para IA en salud** (AIRA_8).
- Evaluación de brechas en la legislación existente y desarrollo de:
	- Orientaciones multisectoriales (AIRA_9–AIRA_10).
	- Enmiendas a leyes existentes (AIRA_11).
	- Nuevas leyes obligatorias, multisectoriales o sectoriales (AIRA_12–AIRA_13).
- **Soft law y principios éticos** (AIRA_14–AIRA_15).
- **Enfoque basado en el riesgo** (AIRA_16), alineado con marcos como la Ley de IA de la UE.
- Directrices éticas y herramientas de evaluación de impacto (AIRA_17–AIRA_21).
- Definición de **regímenes de responsabilidad legal** (AIRA_22–AIRA_24).
- Rol de agencias reguladoras y cooperación entre reguladores (AIRA_25–AIRA_26).
- Requisitos mínimos estándar sobre:
	- Documentación y trazabilidad.
	- Integridad de datos.
	- Gestión del riesgo y ciberseguridad.
	- Monitorización post-comercialización (AIRA_27–AIRA_31).
- Políticas de adquisición, auditoría, mecanismos de reparación y certificación (AIRA_32–AIRA_35).
- Requisitos sobre el **impacto ambiental** de los sistemas de IA (AIRA_36).

Narrativamente, esta sección responde a:

> “¿La IA en salud se gobierna con **reglas claras y robustas**, o se mueve todavía en zonas grises?”

### 4.2 Cómo se ha analizado

- Para AIRA_8, AIRA_9 y AIRA_10 se generan visualizaciones específicas (mapa + barras + análisis textual).
- Para AIRA_11–AIRA_36 se automatiza la generación de:
	- Mapa de Europa por variable.
	- Gráfico de barras con distribución de respuestas.
	- Bloque de texto que resume cuántos países responden “Sí”, “En desarrollo”, “No”, etc., listando ejemplos.
- Se construye una **tabla pivotada de toda la sección** (AIRA_8–AIRA_36), dividida en dos tablas interactivas (parte 1 y parte 2) para facilitar la lectura.

### 4.3 Lectura analítica y mensajes clave

La clave aquí no es tanto una única cifra, sino **patrones**:

- Países con **medidas legislativas ya vigentes (AIRA_8 = Sí)** y, al mismo tiempo, con:
	- Enfoque basado en riesgo (AIRA_16).
	- Directrices éticas y herramientas de evaluación de impacto (AIRA_17–AIRA_21).
	- Mecanismos claros de responsabilidad (AIRA_22–AIRA_24).
	- Exigencias de monitorización post-comercialización (AIRA_31).

	pueden considerarse **jurisdicciones con marcos regulatorios relativamente avanzados**.

- La presencia de muchas respuestas “En desarrollo” sugiere **un ecosistema en transición**, donde la prioridad puede estar en acompañar con guías, buenas prácticas y cooperación entre reguladores.

En un panel BI, esta sección es ideal para construir **indicadores de madurez regulatoria**, por ejemplo:

- Número de dimensiones regulatorias cubiertas (ética, riesgo, responsabilidad, seguridad, certificación, impacto ambiental…).
- % de países con al menos X elementos regulados.
- Mapas de calor por país vs. tipo de medida (filas: países; columnas: grandes bloques normativos).

Esto permite contar una historia del tipo:

> “Los países que más se acercan al despliegue amplio de IA en salud son aquellos que **no solo experimentan**, sino que **normalizan la IA dentro de un marco jurídico sólido**.”

---

## 5. Sección 3 – Gobernanza de los datos sanitarios (AIRA_37 – AIRA_46)

### 5.1 Qué mide esta sección

Aquí se analiza si los países disponen de la **infraestructura institucional y normativa de datos** necesaria para que la IA sea viable y fiable:

- Estrategia y marco de gobernanza de datos de salud (AIRA_37–AIRA_38).
- Existencia de **autoridades de datos de salud** y **centros/plataformas de datos** (AIRA_39–AIRA_40).
- Estándares para almacenes de datos (AIRA_41).
- Regulación del **uso secundario de datos** para investigación y gestión de servicios (AIRA_42).
- Extracción rutinaria de datos de historias clínicas electrónicas (EHR) para crear registros y bases regionales/nacionales (AIRA_43–AIRA_44).
- Reglas para compartir datos con empresas privadas y para intercambio transfronterizo (AIRA_45–AIRA_46).

En lenguaje de historia, esta sección responde a:

> “¿Los países han construido el **sistema circulatorio de datos** que la IA en salud necesita para funcionar?”

### 5.2 Cómo se ha analizado

- Para AIRA_37 se genera un análisis detallado (mapa + barras + listado de países por categoría).
- AIRA_38–AIRA_46 se procesan de forma automatizada, como en la sección normativa: mapa + barras + resumen textual para cada variable.
- Se crea una **tabla pivotada** para todas las variables de la sección, con colores en las celdas que facilitan identificar rápidamente:
	- Países con ecosistemas de datos completos.
	- Países que todavía carecen de hubs, autoridades o marcos claros para uso secundario.

### 5.3 Lectura analítica y mensajes clave

Analíticamente, pueden identificarse varios perfiles de país:

- Países con **estrategia de datos, autoridad de datos y centro nacional de datos de salud** → alta capacidad para proyectos de IA a gran escala, incluyendo investigación y analítica avanzada.
- Países que tienen estrategia de IA pero **sin infraestructura de datos consolidada** → riesgo de que la IA se quede en pilotos aislados.
- Países con reglas claras de intercambio transfronterizo y con el sector privado → mayor potencial para proyectos colaborativos internacionales y ecosistemas público-privados.

En un dashboard, esta sección podría articularse en un **“índice de gobernanza de datos”** y visualizaciones como:

- Mapa que muestre el nivel de preparación de datos.
- Matriz país vs. elemento de gobernanza (estrategia, autoridad, hub, uso secundario, intercambio, etc.).

Esta narrativa se conecta de forma natural con la Sección 4 (aplicaciones): **sin datos, no hay IA operativa**.

---

## 6. Sección 4 – Aplicaciones de la IA para la salud (AIRA_47 – AIRA_53)

### 6.1 Qué mide esta sección

Esta sección se centra en **casos de uso concretos** de IA en los sistemas sanitarios:

- **AIRA_47**: Automatización de tareas logísticas y administrativas.
- **AIRA_48**: Plataformas conversacionales para asistencia a pacientes.
- **AIRA_49**: Cirugía asistida por IA y robótica médica.
- **AIRA_50**: Diagnóstico asistido por IA.
- **AIRA_51**: Predicción de pronóstico / estratificación de riesgo.
- **AIRA_52**: Verificadores de síntomas y apoyo al tratamiento.
- **AIRA_53**: Monitorización remota de pacientes asistida por IA.

En clave de storytelling, esta sección responde a:

> “¿Dónde está la IA **tocando la práctica clínica y la gestión sanitaria** de forma tangible?”

### 6.2 Cómo se ha analizado

- Se detalla AIRA_47 con mapa, barras y análisis textual.
- AIRA_48–AIRA_53 se procesan de forma automatizada con mapas, barras y resúmenes para cada caso de uso.
- Se genera una **tabla por país** que muestra en qué aplicaciones ya se utiliza IA, está en desarrollo o no se aplica.

### 6.3 Lectura analítica y mensajes clave

Esta sección es especialmente útil para:

- Comparar la **difusión de diferentes tipos de aplicaciones** (p. ej., es razonable esperar que la automatización administrativa esté más extendida que la cirugía asistida por IA).
- Detectar **patrones de especialización**: países más avanzados en monitorización remota, vs. países que se centran en diagnósticos asistidos, etc.
- Relacionar aplicaciones con:
	- Madurez regulatoria (Sección 2).
	- Gobernanza de datos (Sección 3).

Un panel BI puede construir, por ejemplo:

- Un gráfico de barras apiladas por país que muestre el número de aplicaciones con respuesta “Sí” / “En desarrollo”.
- Un “ranking” de casos de uso por grado de adopción en la región.

Esto facilita contar historias del tipo:

> “La IA se está consolidando primero en tareas administrativas y soporte a la decisión, mientras que casos más críticos como la cirugía asistida avanzan de forma más gradual.”

---

## 7. Sección 5 – Desarrollo de capacidades en IA (AIRA_71 – AIRA_75)

### 7.1 Qué mide esta sección

Esta sección analiza si los países están **preparando a su fuerza laboral y ecosistema de talento** para la IA en salud:

- **AIRA_71**: Programas educativos sobre IA en salud.
- **AIRA_72**: Programas gubernamentales o colaboraciones transfronterizas para investigación en IA.
- **AIRA_73**: Formación en IA previa al ejercicio profesional (pregrado/posgrado) para profesionales sanitarios.
- **AIRA_74**: Formación en IA en el ejercicio profesional (formación continua).
- **AIRA_75**: Creación de nuevos perfiles y carreras profesionales en IA y ciencia de datos en salud.

La pregunta narrativa aquí es:

> “¿Estamos formando a las personas que necesitará la IA en salud mañana?”

### 7.2 Cómo se ha analizado

- AIRA_71 se trabaja con mapa + barras + análisis textual.
- AIRA_72–AIRA_75 se generan de forma automatizada, con mapas, barras y resumen por variable.
- Se construye una **tabla país vs. capacidades** que muestra en qué dimensiones formativas y de talento se está invirtiendo.

### 7.3 Lectura analítica y mensajes clave

Esta sección es clave para identificar **brechas de sostenibilidad**:

- Países que ya usan IA en aplicaciones clínicas (Sección 4) pero **sin programas formativos robustos** corren el riesgo de:
	- Dependencia de proveedores externos.
	- Dificultades para la adopción responsable y comprensiva por parte del personal clínico.
- Países con creación de nuevos perfiles profesionales (AIRA_75 = Sí) están apostando por una **institucionalización de la ciencia de datos en salud**.

En un dashboard, esta sección puede presentarse como un **índice de capacidades en IA**, que complemente los índices estratégicos, normativos y de datos.

---

## 8. Conexión entre secciones: de la estrategia al impacto

Más allá de analizar cada bloque por separado, el valor del EDA está en la **lectura longitudinal** que permite contar una historia de madurez de IA en salud con cinco capas:

1. **Estrategia** (Sección 1): ¿Existe una visión país y quién lidera?
2. **Normativa** (Sección 2): ¿Hay marcos jurídicos y éticos que la soporten?
3. **Datos** (Sección 3): ¿Hay infraestructura y gobernanza para alimentar a la IA?
4. **Aplicaciones** (Sección 4): ¿Qué casos de uso están ya en práctica o desarrollo?
5. **Capacidades** (Sección 5): ¿Se está formando y ampliando la fuerza laboral y el talento?

Esta estructura encaja perfectamente con un storytelling de **“viaje de madurez”** y con un panel de BI diseñado como **pipeline de preparación para la IA**:

- Un país que puntúe alto en estrategia y normativa, pero bajo en datos y capacidades, aparece como **“visionario pero infraestructurado”**.
- Un país con mucha actividad en aplicaciones pero poca claridad regulatoria puede ser **“experimentador en zona gris regulatoria”**.
- Un país avanzado en todas las capas se aproxima a un perfil de **“ecosistema IA en salud consolidado”**.

---

## 9. Ideas para un futuro panel de inteligencia

A partir de este EDA, se pueden derivar varios componentes reutilizables para un dashboard interactivo (Power BI, Tableau, Looker, etc.):

### 9.1 Filtros (slicers) recomendados

- **País** (o grupo de países).
- **Sección / Dimensión** (estrategia, normativa, datos, aplicaciones, capacidades).
- **Código AIRA** (para bajar al detalle de una pregunta concreta).
- **Tipo de respuesta** (Sí, En desarrollo, No, N/A).

### 9.2 Indicadores clave (KPIs) por dimensión

- % de países con estrategia nacional de IA en salud.
- % de países con legislación específica de IA en salud.
- % de países con autoridad de datos de salud y data hub nacional.
- Número medio de aplicaciones de IA en uso por país.
- % de países con programas formativos estructurados en IA para profesionales sanitarios.

### 9.3 Visualizaciones sugeridas

- **Mapa principal de madurez** (estratégica / normativa / datos / aplicaciones / capacidades) con posibilidad de cambiar de dimensión.
- **Heatmaps país vs. grandes bloques de indicadores** (ej. filas: países; columnas: secciones agregadas).
- **Gráficos de barras comparativos** para aplicaciones (cuántos países usan cada tipo de aplicación de IA).
- **Perfiles tipo de país** (segmentación):
	- “Alta regulación + baja aplicación”.
	- “Alta aplicación + regulación en desarrollo”.
	- “Alto en todas las dimensiones” (líderes).

### 9.4 Storytelling posible en el panel

1. **Portada**: mapa de la región con índice global de madurez de IA en salud.
2. **Pestaña Estrategia**: detalle de estrategias y estructuras de supervisión.
3. **Pestaña Regulación**: comparativa de elementos regulatorios clave.
4. **Pestaña Datos**: situación de gobernanza y uso secundario de datos.
5. **Pestaña Aplicaciones**: dónde está operando hoy la IA en salud.
6. **Pestaña Capacidades**: brechas y avances en formación y talento.

Cada pestaña puede apoyarse directamente en la lógica y tablas ya construidas en el notebook EDA2.ipynb.

---

## 10. Cómo reutilizar este EDA

Esta guía sintetiza el trabajo técnico del notebook y lo traduce en **un relato estructurado y accionable**. Para reutilizarlo en el futuro:

- Usa esta guía como **documento de referencia** para:
	- Definir nuevas métricas agregadas (índices de madurez).
	- Seleccionar variables clave para paneles ejecutivos.
	- Preparar presentaciones o informes escritos sobre IA en salud en Europa.
- Toma las tablas pivotadas y visualizaciones del notebook como **prototipos técnicos** que pueden replicarse en herramientas de BI.
- Amplía el análisis incorporando capas adicionales (por ejemplo, segmentación por UE vs. no UE, ingreso nacional, etc.) si los datos lo permiten.

El valor de este EDA no es solo describir el estado actual, sino **ayudar a formular las preguntas correctas** sobre hacia dónde debería moverse la política pública, la regulación y la inversión en IA para la salud en la Región Europea de la OMS.

---

## 11. Sección 6 – Tipologías de países mediante Machine Learning (Clustering)

Aunque el EDA se apoya fundamentalmente en análisis descriptivos y visualizaciones, se ha incorporado una **Sección 6 de Machine Learning** para ir un paso más allá y **identificar tipologías de países** según su grado de preparación y adopción de la IA en salud.

### 11.1 Objetivo del clustering

El objetivo del clustering es pasar de una visión puramente indicador a indicador a una **visión de conjunto por país**, respondiendo a preguntas como:

- ¿Existen grupos naturales de países que compartan un patrón de fortalezas y debilidades en IA para la salud?
- ¿Cómo se diferencian estos grupos en términos de estrategia, regulación, datos, aplicaciones y capacidades?

En lugar de fijar tipologías de forma subjetiva, se utiliza un algoritmo de **aprendizaje no supervisado (K-means)** que descubre patrones directamente a partir de los datos AIRA.

### 11.2 Preparación de los datos

Para poder aplicar Machine Learning, las respuestas AIRA se transforman en un formato numérico y completo:

1. **Reestructuración del dataset**:
	- Formato original: una fila por combinación `país–indicador`.
	- Formato para clustering: una fila por país y **75 columnas AIRA**, es decir, una matriz `53 países × 75 variables`.

2. **Codificación de respuestas categóricas**:
	- Las respuestas textuales (YES, UD, NO) se convierten en valores numéricos que reflejan el **nivel de implementación**:
	  - YES → 2 (implementado)
	  - UD → 1 (en desarrollo / no sabe)
	  - NO → 0 (no implementado)
	- Esta codificación **ordinal** permite calcular distancias entre países e interpretar los resultados (un país con más 2s está, en general, más avanzado).

3. **Manejo de valores faltantes**:
	- Si algún país no responde a un indicador, se genera un valor faltante.
	- Para no perder países ni variables, los valores vacíos se imputan mediante la **mediana de cada variable** (valor “típico” entre 0, 1 y 2 para ese indicador en la región).

El resultado es un **dataset numérico completo**, adecuado para aplicar algoritmos de clustering y técnicas de reducción de dimensionalidad.

### 11.3 Algoritmo y elección del número de clusters

El análisis utiliza el algoritmo **K-means**, que agrupa países de forma que los que quedan dentro del mismo cluster sean lo más parecidos posible entre sí y lo más diferentes posible de los de otros grupos.

Para decidir cuántos clusters (K) utilizar, se prueban distintos valores y se evalúa la calidad del agrupamiento mediante:

- **Método del codo (inercia)**: observa cómo disminuye la suma de distancias internas al aumentar K.
- **Coeficiente de silueta**: mide, para cada país, lo bien que encaja en su cluster frente a los demás (valores cercanos a 1 indican buena separación).

En este análisis, el **coeficiente de silueta señala que K = 2 es la opción más adecuada**, es decir, los países se organizan de forma natural en **dos grandes tipologías** de madurez en IA para la salud.

### 11.4 Visualización con reducción de dimensionalidad (PCA)

Como trabajar con 75 dimensiones es imposible de visualizar, se aplica **PCA (Análisis de Componentes Principales)** para proyectar los países en un plano 2D o 3D preservando la mayor parte posible de la variabilidad de los datos.

- Cada país se representa como un punto en el espacio de las primeras componentes principales (PC1, PC2, PC3).
- El color del punto indica el cluster asignado por K-means.

Estas visualizaciones permiten **ver físicamente la separación entre grupos de países**, reforzando la interpretación del clustering y facilitando su comunicación a audiencias no técnicas.

### 11.5 Tipologías de países identificadas

El modelo identifica dos grandes grupos (resumen basado en ExplicacionML.ipynb):

#### 🔵 Cluster 0 – Desarrollo irregular

- Aproximadamente **tres cuartas partes de los países**.
- **Puntaje medio global** en torno a 40/100.
- Perfil típico:
  - **Gobernanza de datos** en un nivel moderado (efecto de marcos europeos como el GDPR).
  - **Estrategia y regulación** claramente rezagadas.
  - Aplicaciones de IA presentes, pero más fragmentadas y con menor profundidad.

Interpretación: son países donde la IA en salud **avanza de forma desigual**. Existen infraestructuras de datos y algunos casos de uso, pero sin un marco estratégico y regulatorio plenamente consolidado que articule una visión país.

#### 🟢 Cluster 1 – Transición avanzada

- Minoría de países (alrededor de **un cuarto del total**).
- **Puntaje medio global** en torno a 65/100.
- Perfil típico:
  - **Aplicaciones de IA** ampliamente desplegadas (especialmente en diagnóstico, monitorización y analítica avanzada).
  - **Gobernanza de datos** sólida y madurada.
  - **Regulación** sensiblemente más desarrollada que en el Cluster 0.
  - Estrategia nacional presente, aunque sigue siendo un área con margen de mejora.

Interpretación: estos países se encuentran en una **fase de transición avanzada**, donde la IA en salud está pasando de proyectos aislados a formar parte estructural de políticas, servicios y capacidades institucionales.

### 11.6 Lecturas analíticas clave

A partir de la comparación entre clusters, pueden extraerse varios mensajes que enriquecen el EDA descriptivo:

1. **La regulación marca la gran brecha**
	- Las diferencias más pronunciadas entre clusters aparecen en **regulación específica de IA en salud** y en **requisitos formales (responsabilidad, evaluación de impacto, supervisión post-comercialización)**.
	- Esto sugiere que avanzar hacia un marco regulatorio claro es un **acelerador crítico** para pasar de un uso experimental a un despliegue más generalizado y seguro.

2. **La estrategia no siempre va primero**
	- Incluso en el Cluster 1, las puntuaciones de estrategia no son tan altas como las de aplicaciones o datos.
	- Muchos países parecen avanzar **“de abajo arriba”**: primero despliegan casos de uso y capacidades, y posteriormente formalizan estrategias nacionales más completas.

3. **Suelo común en gobernanza de datos**
	- Gracias a marcos europeos compartidos, incluso países del Cluster 0 muestran niveles moderados de gobernanza de datos.
	- Esto crea un **piso mínimo de madurez** que puede facilitar la adopción posterior de IA si se fortalecen estrategia, regulación y capacidades.

4. **Tipologías útiles para la acción**
	- El clustering no solo clasifica países; ofrece un punto de partida para **diseñar intervenciones diferenciadas**:
	  - Países del Cluster 0: acompañar en desarrollo regulatorio, fortalecimiento de estrategia y consolidación de capacidades humanas.
	  - Países del Cluster 1: profundizar en la evaluación de impacto, la equidad, la sostenibilidad y el escalado responsable de aplicaciones.

### 11.7 Cómo se integra esta sección en el EDA

La Sección 6 de Machine Learning no sustituye al análisis descriptivo, sino que lo **condensa en dos grandes perfiles de madurez**. En combinación con las secciones previas:

- Permite pasar de **mapas y tablas por indicador** a **mapas por tipología de país**.
- Facilita que responsables de política, organismos internacionales y equipos de BI diseñen **dashboards que segmenten la región por niveles de madurez**, y no solo por valores absolutos de cada pregunta AIRA.

En síntesis, el clustering añade una **capa de inteligencia sintética** al EDA, ayudando a transformar un conjunto amplio de indicadores en **historias claras sobre grupos de países y trayectorias de desarrollo en IA para la salud**.

