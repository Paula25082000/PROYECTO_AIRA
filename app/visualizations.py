"""
Visualizaciones para AIRA
=========================
Este módulo contiene funciones para crear visualizaciones interactivas
con Plotly Express y Plotly Graph Objects.
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from config import COLOR_SCALE, COLOR_DISCRETE_MAP, PLOTLY_CONFIG, RESPONSE_LABELS
from utils import obtener_color_respuesta


# ==================== MAPAS COROPLÉTICOS ====================

def crear_mapa_europa(df_filtrado, titulo, variable_aira):
    """
    Crea un mapa coroplético de Europa mostrando respuestas por país.
    
    Args:
        df_filtrado (pd.DataFrame): DataFrame filtrado por variable
        titulo (str): Título del mapa
        variable_aira (str): Código de variable AIRA
        
    Returns:
        plotly.graph_objects.Figure: Figura del mapa
    """
    # Mapeo de respuestas españolas a códigos originales para colores
    respuesta_to_code = {
        'Sí': 'YES',
        'No': 'NO',
        'En desarrollo': 'UD',
        'No sabe': 'DNK',
        'No aplicable': 'N/A'
    }
    
    # Crear columna con colores discretos basados en la respuesta
    df_mapa = df_filtrado.copy()
    df_mapa['Color_Respuesta'] = df_mapa['Respuesta'].map(
        lambda x: COLOR_DISCRETE_MAP.get(respuesta_to_code.get(x, 'N/A'), '#9e9e9e')
    )
    
    # Usar plotly graph_objects para tener control total sobre los colores
    fig = go.Figure()
    
    # Crear una traza por cada tipo de respuesta para tener leyenda discreta
    for respuesta_esp, codigo in respuesta_to_code.items():
        df_resp = df_mapa[df_mapa['Respuesta'] == respuesta_esp]
        
        if not df_resp.empty:
            fig.add_trace(go.Choropleth(
                locations=df_resp['COUNTRY_REGION'],
                z=[1] * len(df_resp),  # Valor constante, el color viene del marker
                text=df_resp['Pais'],
                customdata=df_resp[['Respuesta']],
                hovertemplate='<b>%{text}</b><br>Respuesta: %{customdata[0]}<extra></extra>',
                marker=dict(
                    line=dict(color='white', width=0.5)
                ),
                colorscale=[[0, COLOR_DISCRETE_MAP[codigo]], [1, COLOR_DISCRETE_MAP[codigo]]],
                showscale=False,
                name=respuesta_esp,
                legendgroup=respuesta_esp,
                showlegend=True
            ))
    
    fig.update_geos(
        scope='europe',
        showframe=False,
        showcoastlines=True,
        projection_type='mercator',
        bgcolor='rgba(0,0,0,0)',
        showcountries=True,
        countrycolor='lightgray'
    )
    
    fig.update_layout(
        title=titulo,
        title_font_size=18,
        title_font_color='white',
        height=500,
        margin=dict(l=0, r=0, t=50, b=0),
        paper_bgcolor='#1a202c',
        legend=dict(
            title="Respuesta",
            orientation='v',
            yanchor='top',
            y=0.98,
            xanchor='left',
            x=0.01,
            bgcolor='rgba(30, 30, 30, 0.95)',
            bordercolor='rgba(255, 255, 255, 0.2)',
            borderwidth=1,
            font=dict(
                color='white',
                size=12
            ),
            title_font=dict(
                color='white',
                size=13
            )
        )
    )
    
    return fig


# ==================== GRÁFICOS DE BARRAS ====================

def crear_grafico_distribucion(distribucion_df, titulo):
    """
    Crea un gráfico de barras horizontal mostrando distribución de respuestas.
    
    Args:
        distribucion_df (pd.DataFrame): DataFrame con columnas 'Respuesta' y 'Cantidad'
        titulo (str): Título del gráfico
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    # Asignar colores según la respuesta
    colores = [obtener_color_respuesta(resp) for resp in distribucion_df['Respuesta']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=distribucion_df['Respuesta'],
        x=distribucion_df['Cantidad'],
        orientation='h',
        marker=dict(color=colores),
        text=distribucion_df['Cantidad'],
        textposition='outside',
        textfont=dict(size=14, color='white'),
        hovertemplate='<b>%{y}</b><br>Países: %{x}<extra></extra>'
    ))
    
    fig.update_layout(
        title=titulo,
        title_font_size=18,
        title_font_color='white',
        xaxis_title='Número de Países',
        yaxis_title='',
        font=dict(size=13, color='white'),
        height=400,
        margin=dict(l=150, r=50, t=80, b=50),
        plot_bgcolor='#2d3748',
        paper_bgcolor='#1a202c',
        showlegend=False
    )
    
    fig.update_xaxes(gridcolor='#4a5568', tickfont=dict(size=13, color='white'), title_font=dict(color='white'))
    fig.update_yaxes(tickfont=dict(size=14, color='white'))
    
    return fig


def crear_grafico_barras_vertical(data_df, x_col, y_col, titulo, color_col=None):
    """
    Crea un gráfico de barras vertical genérico.
    
    Args:
        data_df (pd.DataFrame): DataFrame con los datos
        x_col (str): Columna para eje X
        y_col (str): Columna para eje Y
        titulo (str): Título del gráfico
        color_col (str, optional): Columna para colorear barras
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    if color_col:
        fig = px.bar(
            data_df,
            x=x_col,
            y=y_col,
            color=color_col,
            title=titulo,
            text=y_col
        )
    else:
        fig = px.bar(
            data_df,
            x=x_col,
            y=y_col,
            title=titulo,
            text=y_col
        )
    
    fig.update_traces(textposition='outside')
    
    fig.update_layout(
        title_font_size=18,
        title_font_color='white',
        font=dict(color='white'),
        height=500,
        plot_bgcolor='#2d3748',
        paper_bgcolor='#1a202c',
        showlegend=True if color_col else False
    )
    
    fig.update_xaxes(gridcolor='#4a5568', tickfont=dict(color='white'), title_font=dict(color='white'))
    fig.update_yaxes(gridcolor='#4a5568', tickfont=dict(color='white'), title_font=dict(color='white'))
    
    return fig


# ==================== TABLAS INTERACTIVAS ====================

def crear_tabla_interactiva(df_pivot, titulo):
    """
    Crea una tabla interactiva con colores según las respuestas.
    
    Args:
        df_pivot (pd.DataFrame): DataFrame en formato pivotado
        titulo (str): Título de la tabla
        
    Returns:
        plotly.graph_objects.Figure: Figura de la tabla
    """
    # Preparar datos para la tabla
    headers = df_pivot.columns.tolist()
    
    # Crear colores de celdas según respuestas
    cell_colors = []
    for col in df_pivot.columns:
        if col == 'País':
            cell_colors.append(['#f8fafc'] * len(df_pivot))
        else:
            colors_col = []
            for valor in df_pivot[col]:
                if pd.isna(valor):
                    colors_col.append('#ffffff')
                elif valor == 'Sí':
                    colors_col.append('#c8e6c9')  # Verde claro
                elif valor == 'En desarrollo':
                    colors_col.append('#fff9c4')  # Amarillo claro
                elif valor == 'No':
                    colors_col.append('#ffcdd2')  # Rojo claro
                elif valor == 'No sabe':
                    colors_col.append('#bbdefb')  # Azul claro
                else:  # No aplicable
                    colors_col.append('#e0e0e0')  # Gris claro
            cell_colors.append(colors_col)
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=[f'<b>{h}</b>' for h in headers],
            fill_color='#1e3a8a',
            font=dict(color='white', size=14),
            align='center',
            height=45
        ),
        cells=dict(
            values=[df_pivot[col] for col in headers],
            fill_color=cell_colors,
            align=['left'] + ['center'] * (len(headers) - 1),
            font=dict(size=13, color='#1a202c'),
            height=35,
            line=dict(color='#cbd5e0', width=1)
        )
    )])
    
    fig.update_layout(
        title=titulo,
        title_font_size=18,
        title_font_color='white',
        height=600,
        margin=dict(l=0, r=0, t=50, b=0),
        paper_bgcolor='#1a202c'
    )
    
    return fig


# ==================== GRÁFICOS DE SCORES Y PERFILES ====================

def crear_grafico_radar_perfil(perfil, titulo, color='#3b82f6'):
    """
    Crea un gráfico radar (spider) mostrando el perfil de un cluster.
    
    Args:
        perfil (dict): Diccionario con scores por área
        titulo (str): Título del gráfico
        color (str): Color hexadecimal para el gráfico (por defecto azul)
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    areas = list(perfil['scores'].keys())
    valores = list(perfil['scores'].values())
    
    # Convertir color hex a rgba para el relleno
    hex_color = color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    fillcolor = f'rgba({r}, {g}, {b}, 0.3)'
    
    # Color más oscuro para los marcadores (70% de brillo)
    r_dark, g_dark, b_dark = int(r * 0.7), int(g * 0.7), int(b * 0.7)
    marker_color = f'rgb({r_dark}, {g_dark}, {b_dark})'
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=valores + [valores[0]],  # Cerrar el polígono
        theta=areas + [areas[0]],
        fill='toself',
        fillcolor=fillcolor,
        line=dict(color=color, width=2),
        marker=dict(size=8, color=marker_color),
        name=titulo
    ))
    
    fig.update_layout(
        title=titulo,
        title_font_size=16,
        title_font_color='white',
        paper_bgcolor='#1a202c',
        font=dict(color='white'),
        polar=dict(
            bgcolor='#1a202c',
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                ticksuffix='',
                tickfont=dict(size=10, color='white'),
                gridcolor='rgba(255, 255, 255, 0.2)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='white'),
                gridcolor='rgba(255, 255, 255, 0.2)'
            )
        ),
        showlegend=False,
        height=500
    )
    
    return fig


def crear_grafico_comparacion_clusters(perfiles):
    """
    Crea un gráfico de barras agrupadas comparando scores de clusters.
    
    Args:
        perfiles (list): Lista de diccionarios con perfiles de clusters
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    areas = list(perfiles[0]['scores'].keys())
    
    fig = go.Figure()
    
    # Colores fijos por cluster: 0=azul, 1=verde, resto=otros colores
    colores_por_cluster = {
        0: '#2196f3',  # Azul
        1: '#10b981',  # Verde
        2: '#f59e0b',  # Naranja
        3: '#ef4444',  # Rojo
        4: '#8b5cf6',  # Morado
        5: '#06b6d4',  # Cyan
        6: '#ec4899',  # Rosa
    }
    
    for idx, perfil in enumerate(perfiles):
        cluster_id = perfil['cluster_id']
        valores = [perfil['scores'][area] for area in areas]
        
        fig.add_trace(go.Bar(
            name=f"Cluster {cluster_id}",
            x=areas,
            y=valores,
            marker_color=colores_por_cluster.get(cluster_id, '#9e9e9e'),
            text=[f"{v:.1f}" for v in valores],
            textposition='outside'
        ))
    
    fig.update_layout(
        title='Comparación de Scores por Área entre Clusters',
        title_font_size=16,
        title_font_color='white',
        xaxis_title='Área',
        yaxis_title='Score (0-100)',
        barmode='group',
        height=500,
        paper_bgcolor='#1a202c',
        plot_bgcolor='#1a202c',
        font=dict(color='white'),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            bgcolor='rgba(30, 30, 30, 0.8)',
            bordercolor='rgba(255, 255, 255, 0.2)',
            borderwidth=1,
            font=dict(color='white')
        )
    )
    
    fig.update_xaxes(gridcolor='rgba(255, 255, 255, 0.1)', tickfont=dict(color='white'), title_font=dict(color='white'))
    fig.update_yaxes(gridcolor='rgba(255, 255, 255, 0.1)', range=[0, 100], tickfont=dict(color='white'), title_font=dict(color='white'))
    
    return fig


# ==================== GRÁFICOS DE CLUSTERING ====================

def crear_grafico_metodo_codo(inertias, k_range):
    """
    Crea gráfico del método del codo para determinar K óptimo.
    
    Args:
        inertias (list): Lista de valores de inercia
        k_range (range): Rango de valores K probados
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(k_range),
        y=inertias,
        mode='lines+markers',
        line=dict(color='#3b82f6', width=3),
        marker=dict(size=10, color='#1e3a8a'),
        name='Inercia'
    ))
    
    fig.update_layout(
        title='Método del Codo - Determinación del K Óptimo',
        title_font_size=16,
        title_font_color='white',
        xaxis_title='Número de Clusters (K)',
        yaxis_title='Inercia',
        height=500,
        paper_bgcolor='#1a202c',
        plot_bgcolor='#1a202c',
        font=dict(color='white'),
        hovermode='x unified'
    )
    
    fig.update_xaxes(gridcolor='rgba(255, 255, 255, 0.1)', dtick=1, tickfont=dict(color='white'), title_font=dict(color='white'))
    fig.update_yaxes(gridcolor='rgba(255, 255, 255, 0.1)', tickfont=dict(color='white'), title_font=dict(color='white'))
    
    return fig


def crear_grafico_silhouette(silhouette_scores, k_range):
    """
    Crea gráfico del coeficiente de silueta para diferentes valores de K.
    
    Args:
        silhouette_scores (list): Lista de scores de silueta
        k_range (range): Rango de valores K probados
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    k_optimo = list(k_range)[silhouette_scores.index(max(silhouette_scores))]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(k_range),
        y=silhouette_scores,
        mode='lines+markers',
        line=dict(color='#10b981', width=3),
        marker=dict(size=10, color='#047857'),
        name='Coeficiente de Silueta'
    ))
    
    # Marcar el óptimo
    fig.add_vline(
        x=k_optimo,
        line_dash="dash",
        line_color="#ef4444",
        annotation_text=f"K óptimo = {k_optimo}",
        annotation_position="top",
        annotation_font_color="white"
    )
    
    fig.update_layout(
        title='Coeficiente de Silueta - Evaluación de Calidad de Clustering',
        title_font_size=16,
        title_font_color='white',
        xaxis_title='Número de Clusters (K)',
        yaxis_title='Coeficiente de Silueta',
        height=500,
        paper_bgcolor='#1a202c',
        plot_bgcolor='#1a202c',
        font=dict(color='white'),
        hovermode='x unified'
    )
    
    fig.update_xaxes(gridcolor='rgba(255, 255, 255, 0.1)', dtick=1, tickfont=dict(color='white'), title_font=dict(color='white'))
    fig.update_yaxes(gridcolor='rgba(255, 255, 255, 0.1)', tickfont=dict(color='white'), title_font=dict(color='white'))
    
    return fig


def crear_grafico_pca_2d(pca_coords, clusters, labels):
    """
    Crea un gráfico 2D de componentes principales con clusters coloreados.
    
    Args:
        pca_coords (np.ndarray): Coordenadas PCA (n_samples, 2)
        clusters (np.ndarray): Asignación de clusters
        labels (list): Etiquetas para cada punto (nombres de países)
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    # Colores fijos por cluster: 0=azul, 1=verde, resto=otros colores
    colores_por_cluster = {
        0: '#2196f3',  # Azul
        1: '#10b981',  # Verde
        2: '#f59e0b',  # Naranja
        3: '#ef4444',  # Rojo
        4: '#8b5cf6',  # Morado
        5: '#06b6d4',  # Cyan
        6: '#ec4899',  # Rosa
    }
    
    fig = go.Figure()
    
    for cluster_id in np.unique(clusters):
        mask = clusters == cluster_id
        
        fig.add_trace(go.Scatter(
            x=pca_coords[mask, 0],
            y=pca_coords[mask, 1],
            mode='markers+text',
            marker=dict(
                size=12,
                color=colores_por_cluster.get(cluster_id, '#9e9e9e'),
                line=dict(width=1, color='white')
            ),
            text=[labels[i] for i in range(len(labels)) if mask[i]],
            textposition='top center',
            textfont=dict(size=9),
            name=f'Cluster {cluster_id}',
            hovertemplate='<b>%{text}</b><br>PC1: %{x:.2f}<br>PC2: %{y:.2f}<extra></extra>'
        ))
    
    fig.update_layout(
        title='Visualización de Clusters en Espacio PCA (2D)',
        title_font_size=16,
        title_font_color='white',
        xaxis_title='Componente Principal 1',
        yaxis_title='Componente Principal 2',
        height=600,
        paper_bgcolor='#1a202c',
        plot_bgcolor='#1a202c',
        font=dict(color='white'),
        legend=dict(
            orientation='v',
            yanchor='top',
            y=1,
            xanchor='left',
            x=1.02,
            bgcolor='rgba(30, 30, 30, 0.8)',
            bordercolor='rgba(255, 255, 255, 0.2)',
            borderwidth=1,
            font=dict(color='white')
        )
    )
    
    fig.update_xaxes(gridcolor='rgba(255, 255, 255, 0.1)', zeroline=True, zerolinecolor='rgba(255, 255, 255, 0.3)', tickfont=dict(color='white'), title_font=dict(color='white'))
    fig.update_yaxes(gridcolor='rgba(255, 255, 255, 0.1)', zeroline=True, zerolinecolor='rgba(255, 255, 255, 0.3)', tickfont=dict(color='white'), title_font=dict(color='white'))
    
    return fig


def crear_grafico_pca_3d(pca_coords, clusters, labels):
    """
    Crea un gráfico 3D de componentes principales con clusters coloreados.
    
    Args:
        pca_coords (np.ndarray): Coordenadas PCA (n_samples, 3)
        clusters (np.ndarray): Asignación de clusters
        labels (list): Etiquetas para cada punto (nombres de países)
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico 3D
    """
    # Colores fijos por cluster: 0=azul, 1=verde, resto=otros colores
    colores_por_cluster = {
        0: '#2196f3',  # Azul
        1: '#10b981',  # Verde
        2: '#f59e0b',  # Naranja
        3: '#ef4444',  # Rojo
        4: '#8b5cf6',  # Morado
        5: '#06b6d4',  # Cyan
        6: '#ec4899',  # Rosa
    }
    
    fig = go.Figure()
    
    for cluster_id in np.unique(clusters):
        mask = clusters == cluster_id
        
        fig.add_trace(go.Scatter3d(
            x=pca_coords[mask, 0],
            y=pca_coords[mask, 1],
            z=pca_coords[mask, 2],
            mode='markers+text',
            marker=dict(
                size=8,
                color=colores_por_cluster.get(cluster_id, '#9e9e9e'),
                line=dict(width=0.5, color='white')
            ),
            text=[labels[i] for i in range(len(labels)) if mask[i]],
            textposition='top center',
            textfont=dict(size=8),
            name=f'Cluster {cluster_id}',
            hovertemplate='<b>%{text}</b><br>PC1: %{x:.2f}<br>PC2: %{y:.2f}<br>PC3: %{z:.2f}<extra></extra>'
        ))
    
    fig.update_layout(
        title='Visualización de Clusters en Espacio PCA (3D)',
        title_font_size=16,
        title_font_color='white',
        paper_bgcolor='#1a202c',
        font=dict(color='white'),
        scene=dict(
            xaxis_title='Componente Principal 1',
            yaxis_title='Componente Principal 2',
            zaxis_title='Componente Principal 3',
            bgcolor='#1a202c',
            xaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                zerolinecolor='rgba(255, 255, 255, 0.3)',
                tickfont=dict(color='white'),
                title_font=dict(color='white')
            ),
            yaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                zerolinecolor='rgba(255, 255, 255, 0.3)',
                tickfont=dict(color='white'),
                title_font=dict(color='white')
            ),
            zaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                zerolinecolor='rgba(255, 255, 255, 0.3)',
                tickfont=dict(color='white'),
                title_font=dict(color='white')
            )
        ),
        height=700,
        legend=dict(
            orientation='v',
            yanchor='top',
            y=1,
            xanchor='left',
            x=0,
            bgcolor='rgba(30, 30, 30, 0.8)',
            bordercolor='rgba(255, 255, 255, 0.2)',
            borderwidth=1,
            font=dict(color='white')
        )
    )
    
    return fig


# ==================== HEATMAPS ====================

def crear_heatmap_respuestas(df_pivot):
    """
    Crea un heatmap mostrando respuestas por país y variable.
    
    Args:
        df_pivot (pd.DataFrame): DataFrame pivotado (países x variables)
        
    Returns:
        plotly.graph_objects.Figure: Figura del heatmap
    """
    # Mapear respuestas a valores numéricos
    valor_map = {'Sí': 2, 'En desarrollo': 1, 'No': 0, 'No sabe': -1, 'No aplicable': -2}
    
    df_numeric = df_pivot.copy()
    for col in df_numeric.columns:
        if col != 'País':
            df_numeric[col] = df_numeric[col].map(valor_map)
    
    # Crear heatmap
    fig = go.Figure(data=go.Heatmap(
        z=df_numeric.drop('País', axis=1).values,
        x=df_numeric.drop('País', axis=1).columns,
        y=df_numeric['País'],
        colorscale=[
            [0, '#f44336'],   # Rojo (No)
            [0.25, '#ffeb3b'], # Amarillo (En desarrollo)
            [0.5, '#4caf50'],  # Verde (Sí)
            [0.75, '#2196f3'], # Azul (No sabe)
            [1, '#9e9e9e']     # Gris (No aplicable)
        ],
        hovertemplate='País: %{y}<br>Variable: %{x}<br>Valor: %{z}<extra></extra>',
        colorbar=dict(
            title="Estado",
            tickvals=[-2, -1, 0, 1, 2],
            ticktext=['N/A', 'No sabe', 'No', 'En desarrollo', 'Sí']
        )
    ))
    
    fig.update_layout(
        title='Mapa de Calor - Respuestas por País',
        title_font_size=16,
        title_font_color='#1e3a8a',
        xaxis_title='Variables AIRA',
        yaxis_title='Países',
        height=800,
        xaxis=dict(tickangle=-45)
    )
    
    return fig


# ==================== GRÁFICOS DE MÉTRICAS ====================

def crear_grafico_top_paises(df_scores, area, n=10):
    """
    Crea un gráfico de barras con el top N de países en un área específica.
    
    Args:
        df_scores (pd.DataFrame): DataFrame con scores por área
        area (str): Nombre del área a visualizar
        n (int): Número de países a mostrar
        
    Returns:
        plotly.graph_objects.Figure: Figura del gráfico
    """
    top_paises = df_scores.nlargest(n, area)[['Pais', area]].sort_values(area)
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=top_paises['Pais'],
        x=top_paises[area],
        orientation='h',
        marker=dict(
            color=top_paises[area],
            colorscale='Blues',
            showscale=False
        ),
        text=[f"{v:.1f}" for v in top_paises[area]],
        textposition='outside',
        textfont=dict(color='white'),
        hovertemplate='<b>%{y}</b><br>Score: %{x:.1f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=f'Top {n} Países - {area}',
        title_font_size=18,
        title_font_color='white',
        xaxis_title='Score (0-100)',
        yaxis_title='',
        font=dict(color='white'),
        height=400,
        margin=dict(l=150, r=50, t=80, b=50),
        plot_bgcolor='#2d3748',
        paper_bgcolor='#1a202c'
    )
    
    fig.update_xaxes(gridcolor='#4a5568', range=[0, 100], tickfont=dict(color='white'), title_font=dict(color='white'))
    fig.update_yaxes(tickfont=dict(color='white'))
    
    return fig
