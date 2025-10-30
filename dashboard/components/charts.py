"""
Componentes de gráficos para o dashboard
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Optional


def line_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    color: str = "#1f77b4"
):
    """
    Cria um gráfico de linha usando Plotly

    Args:
        df: DataFrame com os dados
        x_col: Nome da coluna do eixo X
        y_col: Nome da coluna do eixo Y
        title: Título do gráfico
        x_label: Label do eixo X
        y_label: Label do eixo Y
        color: Cor da linha
    """
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df[x_col],
        y=df[y_col],
        mode='lines+markers',
        line=dict(color=color, width=3),
        marker=dict(size=8),
        name=y_label or y_col
    ))

    fig.update_layout(
        title=title,
        xaxis_title=x_label or x_col,
        yaxis_title=y_label or y_col,
        hovermode='x unified',
        template='plotly_white',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def multi_line_chart(
    df: pd.DataFrame,
    x_col: str,
    y_cols: list,
    title: str,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None
):
    """
    Cria um gráfico com múltiplas linhas

    Args:
        df: DataFrame com os dados
        x_col: Nome da coluna do eixo X
        y_cols: Lista de nomes das colunas para o eixo Y
        title: Título do gráfico
        x_label: Label do eixo X
        y_label: Label do eixo Y
    """
    fig = go.Figure()

    colors = px.colors.qualitative.Plotly

    for i, y_col in enumerate(y_cols):
        fig.add_trace(go.Scatter(
            x=df[x_col],
            y=df[y_col],
            mode='lines+markers',
            name=y_col,
            line=dict(color=colors[i % len(colors)], width=2),
            marker=dict(size=6)
        ))

    fig.update_layout(
        title=title,
        xaxis_title=x_label or x_col,
        yaxis_title=y_label or 'Valor',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    st.plotly_chart(fig, use_container_width=True)


def bar_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    color: str = "#1f77b4",
    horizontal: bool = False
):
    """
    Cria um gráfico de barras

    Args:
        df: DataFrame com os dados
        x_col: Nome da coluna do eixo X
        y_col: Nome da coluna do eixo Y
        title: Título do gráfico
        x_label: Label do eixo X
        y_label: Label do eixo Y
        color: Cor das barras
        horizontal: Se True, cria gráfico horizontal
    """
    if horizontal:
        fig = go.Figure(go.Bar(
            x=df[y_col],
            y=df[x_col],
            orientation='h',
            marker=dict(color=color)
        ))
    else:
        fig = go.Figure(go.Bar(
            x=df[x_col],
            y=df[y_col],
            marker=dict(color=color)
        ))

    fig.update_layout(
        title=title,
        xaxis_title=x_label or x_col,
        yaxis_title=y_label or y_col,
        template='plotly_white',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def pie_chart(
    labels: list,
    values: list,
    title: str,
    colors: Optional[list] = None
):
    """
    Cria um gráfico de pizza

    Args:
        labels: Lista de labels
        values: Lista de valores
        title: Título do gráfico
        colors: Lista de cores (opcional)
    """
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=colors) if colors else None,
        hole=0.3
    )])

    fig.update_layout(
        title=title,
        template='plotly_white',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def area_chart(
    df: pd.DataFrame,
    x_col: str,
    y_cols: list,
    title: str,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None
):
    """
    Cria um gráfico de área empilhada

    Args:
        df: DataFrame com os dados
        x_col: Nome da coluna do eixo X
        y_cols: Lista de nomes das colunas para o eixo Y
        title: Título do gráfico
        x_label: Label do eixo X
        y_label: Label do eixo Y
    """
    fig = go.Figure()

    colors = px.colors.qualitative.Pastel

    for i, y_col in enumerate(y_cols):
        fig.add_trace(go.Scatter(
            x=df[x_col],
            y=df[y_col],
            mode='lines',
            name=y_col,
            fill='tonexty' if i > 0 else 'tozeroy',
            line=dict(width=0.5, color=colors[i % len(colors)]),
            stackgroup='one'
        ))

    fig.update_layout(
        title=title,
        xaxis_title=x_label or x_col,
        yaxis_title=y_label or 'Valor',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    st.plotly_chart(fig, use_container_width=True)


def heatmap(
    df: pd.DataFrame,
    title: str,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    colorscale: str = 'Blues'
):
    """
    Cria um heatmap

    Args:
        df: DataFrame com os dados (formato matriz)
        title: Título do gráfico
        x_label: Label do eixo X
        y_label: Label do eixo Y
        colorscale: Escala de cores
    """
    fig = go.Figure(data=go.Heatmap(
        z=df.values,
        x=df.columns,
        y=df.index,
        colorscale=colorscale,
        hoverongaps=False
    ))

    fig.update_layout(
        title=title,
        xaxis_title=x_label or '',
        yaxis_title=y_label or '',
        template='plotly_white',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def gauge_chart(
    value: float,
    title: str,
    max_value: float = 100,
    color: str = "#1f77b4"
):
    """
    Cria um gráfico tipo gauge (velocímetro)

    Args:
        value: Valor atual
        title: Título do gráfico
        max_value: Valor máximo
        color: Cor do gauge
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title},
        delta={'reference': max_value * 0.8},
        gauge={
            'axis': {'range': [None, max_value]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, max_value * 0.5], 'color': "lightgray"},
                {'range': [max_value * 0.5, max_value * 0.8], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_value * 0.9
            }
        }
    ))

    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
