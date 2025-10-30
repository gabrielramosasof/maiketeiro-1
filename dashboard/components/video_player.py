"""
Componente de player de vídeo para o dashboard
"""
import streamlit as st
from streamlit_player import st_player
from typing import Optional


def video_player(
    url: str,
    title: Optional[str] = None,
    height: int = 400,
    controls: bool = True,
    playing: bool = False,
    muted: bool = False
):
    """
    Renderiza um player de vídeo

    Args:
        url: URL do vídeo (YouTube, Vimeo, local, etc)
        title: Título do vídeo
        height: Altura do player em pixels
        controls: Se True, mostra controles
        playing: Se True, inicia automaticamente
        muted: Se True, inicia sem som
    """
    if title:
        st.subheader(title)

    st_player(
        url,
        height=height,
        controls=controls,
        playing=playing,
        muted=muted
    )


def video_with_transcription(
    video_url: str,
    transcription: str,
    title: Optional[str] = None,
    video_height: int = 400
):
    """
    Renderiza um player de vídeo com transcrição sincronizada

    Args:
        video_url: URL do vídeo
        transcription: Texto da transcrição
        title: Título do vídeo
        video_height: Altura do player em pixels
    """
    if title:
        st.subheader(title)

    col1, col2 = st.columns([3, 2])

    with col1:
        st_player(video_url, height=video_height)

    with col2:
        st.markdown("### Transcrição")
        st.markdown(
            f"""
            <div style="
                height: {video_height}px;
                overflow-y: auto;
                padding: 15px;
                background-color: #f8f9fa;
                border-radius: 8px;
                font-size: 14px;
                line-height: 1.6;
            ">
                {transcription}
            </div>
            """,
            unsafe_allow_html=True
        )


def video_gallery(
    videos: list,
    columns: int = 3
):
    """
    Renderiza uma galeria de vídeos

    Args:
        videos: Lista de dicionários com dados dos vídeos
                Cada dict deve conter: url, title (opcional), thumbnail (opcional)
        columns: Número de colunas na galeria
    """
    cols = st.columns(columns)

    for idx, video in enumerate(videos):
        col = cols[idx % columns]

        with col:
            if 'thumbnail' in video and video['thumbnail']:
                st.image(video['thumbnail'], use_container_width=True)

            if 'title' in video:
                st.markdown(f"**{video['title']}**")

            if st.button(
                "▶️ Assistir",
                key=f"play_video_{idx}",
                use_container_width=True
            ):
                st.session_state[f'selected_video_{idx}'] = video['url']

            # Se selecionado, mostra o player
            if f'selected_video_{idx}' in st.session_state:
                with st.expander("Player", expanded=True):
                    st_player(st.session_state[f'selected_video_{idx}'])


def video_thumbnail_card(
    thumbnail_url: str,
    title: str,
    duration: str,
    status: str,
    on_click_callback: Optional[callable] = None
):
    """
    Renderiza um card de thumbnail de vídeo

    Args:
        thumbnail_url: URL da thumbnail
        title: Título do vídeo
        duration: Duração formatada (ex: "15:30")
        status: Status do vídeo
        on_click_callback: Função a ser chamada ao clicar
    """
    status_colors = {
        'Concluído': '#28a745',
        'Processando': '#007bff',
        'Pendente': '#ffc107',
        'Falhou': '#dc3545'
    }

    color = status_colors.get(status, '#6c757d')

    st.markdown(
        f"""
        <div style="
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 15px;
        ">
            <img src="{thumbnail_url}" style="width: 100%; height: auto;">
            <div style="padding: 10px;">
                <div style="
                    background-color: {color};
                    color: white;
                    padding: 3px 8px;
                    border-radius: 4px;
                    font-size: 11px;
                    display: inline-block;
                    margin-bottom: 8px;
                ">
                    {status}
                </div>
                <h4 style="margin: 5px 0; font-size: 14px;">{title}</h4>
                <p style="margin: 0; font-size: 12px; color: #666;">⏱️ {duration}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if on_click_callback and st.button("▶️ Assistir", key=f"btn_{title}"):
        on_click_callback()


def placeholder_video():
    """
    Renderiza um placeholder quando não há vídeo disponível
    """
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            color: white;
            font-size: 24px;
            font-weight: bold;
        ">
            🎬 Nenhum vídeo selecionado
        </div>
        """,
        unsafe_allow_html=True
    )
