"""
MAIKETEIRO Dashboard
Main Streamlit application for the MAIKETEIRO marketing assistant
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Import dashboard components
from dashboard.components import charts, metrics_cards, tables, video_player
from dashboard.data import mock_data

# Page configuration
st.set_page_config(
    page_title="MAIKETEIRO - Assistente de Marketing",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.25rem solid #1f77b4;
    }
    .sidebar-content {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.title("🎯 MAIKETEIRO")
        st.markdown("---")

        # Navigation
        page = st.selectbox(
            "Navegação",
            ["Dashboard", "Análise de Vídeos", "Relatórios", "Configurações"]
        )

        st.markdown("---")

        # Filters
        st.subheader("Filtros")
        date_range = st.date_input(
            "Período",
            [datetime.now() - timedelta(days=30), datetime.now()]
        )

        campaign_type = st.multiselect(
            "Tipo de Campanha",
            ["Social Media", "YouTube", "TikTok", "Instagram", "LinkedIn"],
            default=["Social Media", "YouTube"]
        )

    # Main content
    if page == "Dashboard":
        show_dashboard()
    elif page == "Análise de Vídeos":
        show_video_analysis()
    elif page == "Relatórios":
        show_reports()
    else:
        show_settings()

def show_dashboard():
    st.markdown('<h1 class="main-header">Dashboard MAIKETEIRO</h1>', unsafe_allow_html=True)

    # Key Metrics Row
    metrics_data = [
        {"label": "Total de Vídeos", "value": "1,247", "delta": "+12%", "icon": "🎬"},
        {"label": "Visualizações", "value": "2.4M", "delta": "+8%", "icon": "👁️"},
        {"label": "Engajamento", "value": "15.3%", "delta": "-2%", "delta_color": "inverse", "icon": "📈"},
        {"label": "Conversões", "value": "342", "delta": "+25%", "icon": "💰"}
    ]

    metrics_cards.metrics_row(metrics_data)

    st.markdown("---")

    # Charts Row
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Visualizações por Plataforma")

        # Sample data
        platforms = ['YouTube', 'TikTok', 'Instagram', 'LinkedIn']
        views = [850000, 650000, 480000, 420000]

        charts.pie_chart(
            labels=platforms,
            values=views,
            title="Distribuição de Visualizações"
        )

    with col2:
        st.subheader("Crescimento Mensal")

        # Sample time series data
        dates = pd.date_range(start='2024-01-01', end='2024-12-01', freq='M')
        growth_data = pd.DataFrame({
            'Data': dates,
            'Visualizações': np.random.randint(50000, 200000, len(dates)),
            'Engajamento': np.random.uniform(10, 20, len(dates))
        })

        charts.line_chart(
            df=growth_data,
            x_col='Data',
            y_col='Visualizações',
            title="Visualizações ao Longo do Tempo"
        )

    # Recent Videos Table
    st.subheader("Vídeos Recentes")
    recent_videos = mock_data.get_mock_videos(10)
    videos_df = mock_data.MockDataGenerator.videos_to_dataframe(recent_videos)
    tables.interactive_table(videos_df, title=None, page_size=5)

def show_video_analysis():
    st.header("🎬 Análise de Vídeos")

    # Video upload/analysis section
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Upload de Vídeo")
        uploaded_file = st.file_uploader(
            "Escolha um vídeo para análise",
            type=['mp4', 'mov', 'avi', 'mkv']
        )

        if uploaded_file:
            # Video player
            st.video(uploaded_file)

    with col2:
        st.subheader("Análise Automática")
        if st.button("Analisar Vídeo", type="primary"):
            with st.spinner("Analisando vídeo..."):
                # Mock analysis
                st.success("Análise completa!")

                # Analysis results
                st.subheader("Resultados da Análise")
                analysis_col1, analysis_col2 = st.columns(2)

                with analysis_col1:
                    st.metric("Duração", "12:34")
                    st.metric("Qualidade", "1080p")

                with analysis_col2:
                    st.metric("Tamanho", "245 MB")
                    st.metric("Formato", "MP4")

def show_reports():
    st.header("📊 Relatórios")

    # Report generation
    st.subheader("Gerar Relatório")

    report_type = st.selectbox(
        "Tipo de Relatório",
        ["Performance de Campanhas", "Análise de Vídeos", "Relatório Financeiro"]
    )

    date_range = st.date_input("Período do Relatório", [])

    if st.button("Gerar Relatório"):
        with st.spinner("Gerando relatório..."):
            st.success("Relatório gerado com sucesso!")

            # Mock report content
            st.subheader("Relatório de Performance")

            # Sample metrics
            report_data = {
                'Métrica': ['Visualizações Totais', 'Engajamento Médio', 'Conversões', 'ROI'],
                'Valor': ['2.4M', '15.3%', '342', '245%'],
                'Variação': ['+8%', '-2%', '+25%', '+12%']
            }

            tables.styled_dataframe(pd.DataFrame(report_data))

def show_settings():
    st.header("⚙️ Configurações")

    # API Keys section
    st.subheader("Chaves de API")

    with st.form("api_keys"):
        openai_key = st.text_input("OpenAI API Key", type="password")
        anthropic_key = st.text_input("Anthropic API Key", type="password")
        google_key = st.text_input("Google AI API Key", type="password")

        if st.form_submit_button("Salvar Chaves"):
            st.success("Chaves salvas com sucesso!")

    # Preferences
    st.subheader("Preferências")

    theme = st.selectbox("Tema", ["Claro", "Escuro", "Automático"])
    language = st.selectbox("Idioma", ["Português", "English"])

    auto_save = st.checkbox("Salvar automaticamente", value=True)

if __name__ == "__main__":
    main()