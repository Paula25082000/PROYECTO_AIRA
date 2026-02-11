"""
Utilidades para AIRA
====================
Este módulo contiene funciones auxiliares para carga de datos,
procesamiento, transformaciones y cálculos utilizados en toda la aplicación.
"""

import pandas as pd
import numpy as np
import streamlit as st
from config import (
    DATA_PATH, COUNTRY_NAMES, RESPONSE_LABELS, VALUE_MAPPING,
    AIRA_TITULOS, SECCIONES, AIRA_GRUPOS
)


# ==================== CARGA DE DATOS ====================

@st.cache_data
def cargar_datos():
    """
    Carga el dataset AIRA desde el archivo CSV.
    
    Returns:
        pd.DataFrame: DataFrame con los datos AIRA
    """
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except FileNotFoundError:
        st.error(f"❌ No se encontró el archivo de datos en: {DATA_PATH}")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error al cargar los datos: {str(e)}")
        st.stop()


# ==================== ENRIQUECIMIENTO DE DATOS ====================

def enriquecer_dataframe(df):
    """
    Enriquece el DataFrame con columnas adicionales útiles para visualización.
    
    Args:
        df (pd.DataFrame): DataFrame original
        
    Returns:
        pd.DataFrame: DataFrame enriquecido con nuevas columnas
    """
    df_enriquecido = df.copy()
    
    # Agregar nombre de país en español
    df_enriquecido['Pais'] = df_enriquecido['COUNTRY_REGION'].map(COUNTRY_NAMES)
    
    # Agregar etiqueta de respuesta en español
    df_enriquecido['Respuesta'] = df_enriquecido['AIRA_SIMPLE'].map(RESPONSE_LABELS)
    
    # Agregar valor numérico para visualización
    df_enriquecido['Valor'] = df_enriquecido['AIRA_SIMPLE'].map(VALUE_MAPPING)
    
    # Agregar título descriptivo de la variable
    df_enriquecido['Variable_Titulo'] = df_enriquecido['Measure_code'].map(AIRA_TITULOS)
    
    return df_enriquecido


def filtrar_por_variable(df, variable_aira):
    """
    Filtra el DataFrame por una variable AIRA específica.
    
    Args:
        df (pd.DataFrame): DataFrame completo
        variable_aira (str): Código de variable AIRA (ej: 'AIRA_1')
        
    Returns:
        pd.DataFrame: DataFrame filtrado y enriquecido
    """
    df_filtrado = df[df['Measure_code'] == variable_aira].copy()
    df_filtrado = enriquecer_dataframe(df_filtrado)
    return df_filtrado


def filtrar_por_seccion(df, numero_seccion):
    """
    Filtra el DataFrame por una sección completa.
    
    Args:
        df (pd.DataFrame): DataFrame completo
        numero_seccion (int): Número de sección (1, 2, 3, 4, 5)
        
    Returns:
        pd.DataFrame: DataFrame filtrado para la sección
    """
    seccion_key = f'seccion_{numero_seccion}'
    if seccion_key not in SECCIONES:
        return pd.DataFrame()
    
    variables = SECCIONES[seccion_key]['variables']
    df_filtrado = df[df['Measure_code'].isin(variables)].copy()
    return enriquecer_dataframe(df_filtrado)


# ==================== TRANSFORMACIONES PARA ML ====================

@st.cache_data
def preparar_datos_ml(df):
    """
    Prepara los datos para análisis de Machine Learning (clustering).
    Transforma de formato largo a ancho y codifica variables.
    
    Args:
        df (pd.DataFrame): DataFrame original en formato largo
        
    Returns:
        tuple: (df_pivot, df_encoded, df_filled)
            - df_pivot: DataFrame en formato ancho (países x variables)
            - df_encoded: DataFrame con codificación numérica
            - df_filled: DataFrame con valores faltantes imputados
    """
    # Crear tabla pivotada: filas = países, columnas = variables AIRA
    df_pivot = df.pivot(
        index='COUNTRY_REGION',
        columns='Measure_code',
        values='AIRA_SIMPLE'
    )
    
    # Mapeo de codificación para ML
    encoding_map = {
        'YES': 2,  # Completamente implementado
        'UD': 1,   # En desarrollo / No sabe
        'NO': 0,   # No implementado
        'DNK': 1,  # No sabe -> tratado como "en desarrollo"
        'N/A': 0   # No aplicable -> tratado como "no"
    }
    
    # Aplicar codificación
    df_encoded = df_pivot.replace(encoding_map)
    
    # Convertir a numérico, forzando valores no reconocidos a NaN
    df_encoded = df_encoded.apply(pd.to_numeric, errors='coerce')
    
    # Imputar valores faltantes con estrategia robusta
    df_filled = df_encoded.copy()
    
    for col in df_filled.columns:
        if df_filled[col].isnull().any():
            # Calcular mediana
            mediana = df_filled[col].median()
            
            # Si la mediana es NaN (columna completamente vacía), usar 0
            if pd.isna(mediana):
                df_filled[col].fillna(0, inplace=True)
            else:
                df_filled[col].fillna(mediana, inplace=True)
    
    # Verificación final: asegurarse de que no queden NaN
    # Si aún hay NaN, rellenar con 0
    df_filled = df_filled.fillna(0)
    
    # Verificar que no haya valores infinitos
    df_filled = df_filled.replace([np.inf, -np.inf], 0)
    
    return df_pivot, df_encoded, df_filled


# ==================== ANÁLISIS ESTADÍSTICO ====================

def calcular_distribucion_respuestas(df_filtrado):
    """
    Calcula la distribución de respuestas para un conjunto de datos filtrado.
    
    Args:
        df_filtrado (pd.DataFrame): DataFrame filtrado (debe tener columna 'Respuesta')
        
    Returns:
        pd.DataFrame: Conteo de respuestas ordenado
    """
    distribucion = df_filtrado['Respuesta'].value_counts().reset_index()
    distribucion.columns = ['Respuesta', 'Cantidad']
    
    # Ordenar según un orden lógico
    orden = ['Sí', 'En desarrollo', 'No', 'No sabe', 'No aplicable']
    distribucion['Respuesta'] = pd.Categorical(
        distribucion['Respuesta'], 
        categories=orden, 
        ordered=True
    )
    distribucion = distribucion.sort_values('Respuesta')
    
    return distribucion


def obtener_paises_por_respuesta(df_filtrado, respuesta):
    """
    Obtiene la lista de países que dieron una respuesta específica.
    
    Args:
        df_filtrado (pd.DataFrame): DataFrame filtrado
        respuesta (str): Respuesta a buscar ('Sí', 'No', etc.)
        
    Returns:
        list: Lista de nombres de países
    """
    paises = df_filtrado[df_filtrado['Respuesta'] == respuesta]['Pais'].tolist()
    return sorted(paises)


def calcular_scores_por_area(df_filled):
    """
    Calcula scores (0-100) por área temática para cada país.
    
    Args:
        df_filled (pd.DataFrame): DataFrame con datos codificados y sin valores faltantes
        
    Returns:
        pd.DataFrame: DataFrame con scores por área para cada país
    """
    scores_dict = {}
    
    for area, variables in AIRA_GRUPOS.items():
        # Filtrar solo las variables que existen en el DataFrame
        vars_existentes = [v for v in variables if v in df_filled.columns]
        
        if vars_existentes:
            # Calcular promedio de las variables del área
            scores_dict[area] = df_filled[vars_existentes].mean(axis=1)
    
    df_scores = pd.DataFrame(scores_dict)
    
    # Convertir a escala 0-100 (ya que los valores están en 0-2)
    df_scores = (df_scores / 2) * 100
    
    # Agregar score general
    df_scores['Score_General'] = df_scores.mean(axis=1)
    
    # Agregar nombre de país
    df_scores['Pais'] = df_scores.index.map(COUNTRY_NAMES)
    
    return df_scores


# ==================== CREACIÓN DE TABLAS PIVOTADAS ====================

def crear_tabla_pivotada_seccion(df, numero_seccion):
    """
    Crea una tabla pivotada para una sección específica.
    Filas: países, Columnas: variables AIRA de la sección
    
    Args:
        df (pd.DataFrame): DataFrame completo
        numero_seccion (int): Número de sección (1-5)
        
    Returns:
        pd.DataFrame: Tabla pivotada con nombres de países
    """
    seccion_key = f'seccion_{numero_seccion}'
    if seccion_key not in SECCIONES:
        return pd.DataFrame()
    
    variables = SECCIONES[seccion_key]['variables']
    
    # Filtrar por sección
    df_seccion = df[df['Measure_code'].isin(variables)].copy()
    
    # Crear pivot
    df_pivot = df_seccion.pivot(
        index='COUNTRY_REGION',
        columns='Measure_code',
        values='AIRA_SIMPLE'
    )
    
    # Reemplazar con etiquetas en español
    df_pivot = df_pivot.replace(RESPONSE_LABELS)
    
    # Agregar nombres de países
    df_pivot.insert(0, 'País', df_pivot.index.map(COUNTRY_NAMES))
    df_pivot.reset_index(drop=True, inplace=True)
    
    return df_pivot


# ==================== UTILIDADES PARA CLUSTERING ====================

def preparar_perfiles_clusters(df_clusters, df_scores):
    """
    Prepara perfiles descriptivos de los clusters identificados.
    
    Args:
        df_clusters (pd.DataFrame): DataFrame con asignación de clusters
        df_scores (pd.DataFrame): DataFrame con scores por área
        
    Returns:
        list: Lista de diccionarios con perfiles de cada cluster
    """
    df_merged = df_clusters.merge(
        df_scores, 
        left_on='COUNTRY_REGION', 
        right_index=True
    )
    
    perfiles = []
    
    for cluster_id in sorted(df_merged['Cluster'].unique()):
        cluster_data = df_merged[df_merged['Cluster'] == cluster_id]
        
        perfil = {
            'cluster_id': cluster_id,
            'n_paises': len(cluster_data),
            'paises': sorted(cluster_data['Pais'].tolist()),
            'score_general': cluster_data['Score_General'].mean(),
            'scores': {
                'Estrategia': cluster_data['Estrategia'].mean(),
                'Regulación': cluster_data['Regulación'].mean(),
                'Gobernanza de Datos': cluster_data['Gobernanza de Datos'].mean(),
                'Aplicaciones': cluster_data['Aplicaciones'].mean(),
                'Capacidades': cluster_data['Capacidades'].mean()
            }
        }
        
        perfiles.append(perfil)
    
    return perfiles


def asignar_tipologia(perfil_scores):
    """
    Asigna una tipología descriptiva basada en el perfil completo del cluster.
    Utiliza la lógica de clasificación del análisis EDA.
    
    Args:
        perfil_scores (dict): Diccionario con scores por área y score general
                             Claves: 'Estrategia', 'Regulación', 'Gobernanza de Datos', 
                                    'Aplicaciones', 'Capacidades', 'score_general'
        
    Returns:
        tuple: (emoji, nombre, color)
    """
    strategy = perfil_scores.get('Estrategia', 0)
    regulation = perfil_scores.get('Regulación', 0)
    governance = perfil_scores.get('Gobernanza de Datos', 0)
    applications = perfil_scores.get('Aplicaciones', 0)
    capabilities = perfil_scores.get('Capacidades', 0)
    avg_score = perfil_scores.get('score_general', 0)
    
    # Clasificar según patrones del EDA
    if avg_score > 70:
        return '🟢', 'Líderes en IA en Salud', '#4caf50'
    elif avg_score > 50:
        return '🟡', 'En Transición Avanzada', '#ffd600'
    elif strategy > 60 and applications < 40:
        return '🔵', 'Estrategia sin Implementación', '#2196f3'
    elif regulation > 60 and capabilities < 40:
        return '🟠', 'Regulación sin Capacidades', '#ff9800'
    elif applications > 50 and regulation < 40:
        return '🟣', 'Implementación sin Regulación', '#9c27b0'
    elif avg_score < 35:
        return '🔴', 'Rezagados en Gobernanza e Implementación', '#f44336'
    else:
        return '⚪', 'Desarrollo Irregular', '#9e9e9e'


# ==================== UTILIDADES DE FORMATO ====================

def formatear_porcentaje(valor, decimales=1):
    """
    Formatea un valor numérico como porcentaje.
    
    Args:
        valor (float): Valor a formatear (0-100)
        decimales (int): Número de decimales
        
    Returns:
        str: Valor formateado
    """
    return f"{valor:.{decimales}f}%"


def formatear_numero(valor, decimales=0):
    """
    Formatea un número con separador de miles.
    
    Args:
        valor (float): Valor a formatear
        decimales (int): Número de decimales
        
    Returns:
        str: Valor formateado
    """
    return f"{valor:,.{decimales}f}".replace(",", ".")


def obtener_color_respuesta(respuesta):
    """
    Retorna el color asociado a una respuesta.
    
    Args:
        respuesta (str): Respuesta ('Sí', 'No', etc.)
        
    Returns:
        str: Código de color hexadecimal
    """
    color_map = {
        'Sí': '#4caf50',           # Verde
        'En desarrollo': '#ffeb3b', # Amarillo
        'No': '#f44336',            # Rojo
        'No sabe': '#2196f3',       # Azul
        'No aplicable': '#9e9e9e'   # Gris
    }
    return color_map.get(respuesta, '#757575')


# ==================== VALIDACIONES ====================

def validar_dataframe(df):
    """
    Valida que el DataFrame tenga las columnas necesarias.
    
    Args:
        df (pd.DataFrame): DataFrame a validar
        
    Returns:
        bool: True si es válido, False en caso contrario
    """
    columnas_requeridas = ['Measure_code', 'AIRA_SIMPLE', 'COUNTRY_REGION']
    return all(col in df.columns for col in columnas_requeridas)


def obtener_info_dataset(df):
    """
    Obtiene información resumida del dataset.
    
    Args:
        df (pd.DataFrame): DataFrame
        
    Returns:
        dict: Diccionario con información del dataset
    """
    info = {
        'n_filas': len(df),
        'n_columnas': len(df.columns),
        'n_paises': df['COUNTRY_REGION'].nunique() if 'COUNTRY_REGION' in df.columns else 0,
        'n_variables': df['Measure_code'].nunique() if 'Measure_code' in df.columns else 0,
        'columnas': df.columns.tolist()
    }
    return info
