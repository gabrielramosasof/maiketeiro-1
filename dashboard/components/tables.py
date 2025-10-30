"""
Componentes de tabelas interativas para o dashboard
"""
import streamlit as st
import pandas as pd
from typing import Optional, List


def interactive_table(
    df: pd.DataFrame,
    title: Optional[str] = None,
    page_size: int = 10,
    searchable_columns: Optional[List[str]] = None,
    sortable: bool = True
):
    """
    Renderiza uma tabela interativa com busca e paginação

    Args:
        df: DataFrame para exibir
        title: Título da tabela
        page_size: Número de linhas por página
        searchable_columns: Colunas que podem ser pesquisadas
        sortable: Se True, permite ordenação
    """
    if title:
        st.subheader(title)

    # Busca
    if searchable_columns:
        search_term = st.text_input(
            "Buscar",
            placeholder=f"Buscar em: {', '.join(searchable_columns)}",
            key=f"search_{id(df)}"
        )

        if search_term:
            mask = df[searchable_columns].apply(
                lambda x: x.astype(str).str.contains(search_term, case=False, na=False)
            ).any(axis=1)
            df = df[mask]

    # Informações
    total_rows = len(df)
    st.caption(f"Total de registros: {total_rows}")

    # Ordenação
    if sortable and total_rows > 0:
        col1, col2 = st.columns([3, 1])
        with col1:
            sort_column = st.selectbox(
                "Ordenar por",
                options=df.columns.tolist(),
                key=f"sort_col_{id(df)}"
            )
        with col2:
            sort_order = st.selectbox(
                "Ordem",
                options=["Crescente", "Decrescente"],
                key=f"sort_order_{id(df)}"
            )

        ascending = sort_order == "Crescente"
        df = df.sort_values(by=sort_column, ascending=ascending)

    # Paginação
    if total_rows > page_size:
        total_pages = (total_rows - 1) // page_size + 1
        page = st.number_input(
            "Página",
            min_value=1,
            max_value=total_pages,
            value=1,
            key=f"page_{id(df)}"
        )

        start_idx = (page - 1) * page_size
        end_idx = min(start_idx + page_size, total_rows)

        st.caption(f"Exibindo {start_idx + 1}-{end_idx} de {total_rows}")
        df_page = df.iloc[start_idx:end_idx]
    else:
        df_page = df

    # Exibir tabela
    st.dataframe(df_page, use_container_width=True, hide_index=True)


def styled_dataframe(
    df: pd.DataFrame,
    title: Optional[str] = None,
    highlight_max: Optional[List[str]] = None,
    highlight_min: Optional[List[str]] = None,
    color_scale: Optional[dict] = None
):
    """
    Renderiza um DataFrame com estilos customizados

    Args:
        df: DataFrame para exibir
        title: Título da tabela
        highlight_max: Lista de colunas para destacar valor máximo
        highlight_min: Lista de colunas para destacar valor mínimo
        color_scale: Dicionário com escalas de cor por coluna
    """
    if title:
        st.subheader(title)

    styled = df.style

    if highlight_max:
        for col in highlight_max:
            if col in df.columns:
                styled = styled.highlight_max(subset=[col], color='lightgreen')

    if highlight_min:
        for col in highlight_min:
            if col in df.columns:
                styled = styled.highlight_min(subset=[col], color='lightcoral')

    if color_scale:
        for col, cmap in color_scale.items():
            if col in df.columns:
                styled = styled.background_gradient(subset=[col], cmap=cmap)

    st.dataframe(styled, use_container_width=True, hide_index=True)


def simple_table(
    data: list,
    columns: list,
    title: Optional[str] = None
):
    """
    Renderiza uma tabela simples a partir de uma lista de dados

    Args:
        data: Lista de listas ou lista de dicionários
        columns: Lista de nomes das colunas
        title: Título da tabela
    """
    if title:
        st.subheader(title)

    df = pd.DataFrame(data, columns=columns)
    st.dataframe(df, use_container_width=True, hide_index=True)


def data_editor(
    df: pd.DataFrame,
    title: Optional[str] = None,
    key: Optional[str] = None
):
    """
    Renderiza um editor de dados interativo

    Args:
        df: DataFrame para editar
        title: Título da tabela
        key: Chave única para o widget

    Returns:
        DataFrame editado
    """
    if title:
        st.subheader(title)

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        key=key or f"editor_{id(df)}"
    )

    return edited_df


def expandable_row_table(
    df: pd.DataFrame,
    summary_columns: List[str],
    detail_columns: List[str],
    title: Optional[str] = None
):
    """
    Renderiza uma tabela com linhas expansíveis para mostrar detalhes

    Args:
        df: DataFrame para exibir
        summary_columns: Colunas a serem mostradas no resumo
        detail_columns: Colunas a serem mostradas no detalhe
        title: Título da tabela
    """
    if title:
        st.subheader(title)

    for idx, row in df.iterrows():
        with st.expander(
            f"📄 {' | '.join([str(row[col]) for col in summary_columns[:3]])}"
        ):
            col1, col2 = st.columns(2)

            mid = len(detail_columns) // 2

            with col1:
                for col in detail_columns[:mid]:
                    st.write(f"**{col}:** {row[col]}")

            with col2:
                for col in detail_columns[mid:]:
                    st.write(f"**{col}:** {row[col]}")
