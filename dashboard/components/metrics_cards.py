"""
Componentes de cards de métricas para o dashboard
"""
import streamlit as st
from typing import Optional


def metric_card(
    label: str,
    value: str,
    delta: Optional[str] = None,
    delta_color: str = "normal",
    help_text: Optional[str] = None,
    icon: Optional[str] = None
):
    """
    Renderiza um card de métrica estilizado

    Args:
        label: Título da métrica
        value: Valor principal a exibir
        delta: Valor de variação (opcional)
        delta_color: Cor do delta ('normal', 'inverse', 'off')
        help_text: Texto de ajuda ao passar o mouse
        icon: Emoji ou ícone para exibir ao lado do label
    """
    if icon:
        label = f"{icon} {label}"

    st.metric(
        label=label,
        value=value,
        delta=delta,
        delta_color=delta_color,
        help=help_text
    )


def metrics_row(metrics_data: list):
    """
    Renderiza uma linha de múltiplas métricas

    Args:
        metrics_data: Lista de dicionários com dados das métricas
                     Cada dict deve conter: label, value, delta (opcional),
                     delta_color (opcional), help_text (opcional), icon (opcional)

    Exemplo:
        metrics_row([
            {"label": "Total Vídeos", "value": "150", "delta": "+10", "icon": "🎬"},
            {"label": "Em Processamento", "value": "5", "icon": "⚙️"},
        ])
    """
    cols = st.columns(len(metrics_data))

    for col, metric_data in zip(cols, metrics_data):
        with col:
            metric_card(
                label=metric_data.get('label'),
                value=metric_data.get('value'),
                delta=metric_data.get('delta'),
                delta_color=metric_data.get('delta_color', 'normal'),
                help_text=metric_data.get('help_text'),
                icon=metric_data.get('icon')
            )


def status_badge(status: str, status_color: dict = None) -> str:
    """
    Cria um badge HTML para status

    Args:
        status: Texto do status
        status_color: Dicionário com cores por status

    Returns:
        String HTML do badge
    """
    if status_color is None:
        status_color = {
            'Concluído': '#28a745',
            'Processando': '#007bff',
            'Pendente': '#ffc107',
            'Falhou': '#dc3545',
            'Na Fila': '#6c757d'
        }

    color = status_color.get(status, '#6c757d')

    return f"""
    <span style="
        background-color: {color};
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    ">
        {status}
    </span>
    """


def progress_bar(progress: int, label: str = None, color: str = "#1f77b4"):
    """
    Renderiza uma barra de progresso customizada

    Args:
        progress: Valor de 0 a 100
        label: Label opcional para a barra
        color: Cor da barra em hex
    """
    if label:
        st.write(label)

    st.progress(progress / 100)
    st.caption(f"{progress}%")


def info_box(title: str, content: str, box_type: str = "info"):
    """
    Renderiza uma caixa de informação estilizada

    Args:
        title: Título da caixa
        content: Conteúdo/mensagem
        box_type: Tipo da caixa ('info', 'success', 'warning', 'error')
    """
    box_colors = {
        'info': '#d1ecf1',
        'success': '#d4edda',
        'warning': '#fff3cd',
        'error': '#f8d7da'
    }

    text_colors = {
        'info': '#0c5460',
        'success': '#155724',
        'warning': '#856404',
        'error': '#721c24'
    }

    bg_color = box_colors.get(box_type, box_colors['info'])
    text_color = text_colors.get(box_type, text_colors['info'])

    st.markdown(
        f"""
        <div style="
            background-color: {bg_color};
            color: {text_color};
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid {text_color};
            margin: 10px 0;
        ">
            <strong>{title}</strong><br>
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )
