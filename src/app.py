import pandas as pd
import streamlit as st
import plotly.express as px
import subprocess
import sys
from pathlib import Path

st.set_page_config(
    page_title="SpaceFire Alert",
    page_icon="🔥",
    layout="wide"
)

# ==========================================
# CSS CUSTOMIZADO
# ==========================================

st.markdown("""
<style>

/* Fundo principal */
.stApp {
    background-color: #0F172A;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1E293B;
}

/* Títulos */
h1, h2, h3 {
    color: #F8FAFC !important;
}

/* Textos */
p, div, label {
    color: #E2E8F0;
}

/* Botões */
.stButton > button {
    background-color: #DC2626;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background-color: #B91C1C;
}

/* Cards KPI */
[data-testid="stMetric"] {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #DC2626;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.3);
}

/* Alertas */
[data-testid="stAlert"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# CAMINHOS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = (
    BASE_DIR /
    "data" /
    "raw" /
    "focos_diario_br.csv"
)

# ==========================================
# DOWNLOAD AUTOMÁTICO
# ==========================================

if not csv_path.exists():

    subprocess.run(
        [
            sys.executable,
            str(BASE_DIR / "etl" / "coleta_dados.py")
        ]
    )

# ==========================================
# CABEÇALHO
# ==========================================

st.markdown("""
<div style='
background: linear-gradient(90deg,#991B1B,#DC2626);
padding:25px;
border-radius:20px;
margin-bottom:20px;
'>
<h1 style='
color:white;
text-align:center;
margin-bottom:5px;
'>
🔥 SpaceFire Alert
</h1>

<p style='
color:white;
text-align:center;
font-size:18px;
margin:0;
'>
Monitoramento Inteligente de Queimadas via Satélite
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# BOTÃO DE ATUALIZAÇÃO
# ==========================================

if st.button("🔄 Atualizar Dados do INPE"):

    subprocess.run(
        [
            sys.executable,
            str(BASE_DIR / "etl" / "coleta_dados.py")
        ]
    )

    st.success("Dados atualizados com sucesso!")

    st.rerun()

# ==========================================
# CARREGAMENTO
# ==========================================

df = pd.read_csv(csv_path)

df["data_hora_gmt"] = pd.to_datetime(
    df["data_hora_gmt"]
)

ultima_data = df["data_hora_gmt"].max()

st.info(
    f"🛰 Dados atualizados até: "
    f"{ultima_data.strftime('%d/%m/%Y %H:%M')}"
)

# ==========================================
# FILTROS
# ==========================================

st.sidebar.header("🎛 Filtros")

estados = st.sidebar.multiselect(
    "Estado",
    sorted(df["estado"].dropna().unique())
)

biomas = st.sidebar.multiselect(
    "Bioma",
    sorted(df["bioma"].dropna().unique())
)

satelites = st.sidebar.multiselect(
    "Satélite",
    sorted(df["satelite"].dropna().unique())
)

if estados:
    df = df[df["estado"].isin(estados)]

if biomas:
    df = df[df["bioma"].isin(biomas)]

if satelites:
    df = df[df["satelite"].isin(satelites)]

# ==========================================
# KPIs
# ==========================================

st.subheader("📈 Indicadores Principais")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🔥 Focos Detectados",
    f"{len(df):,}"
)

col2.metric(
    "📍 Municípios",
    df["municipio"].nunique()
)

col3.metric(
    "🌳 Biomas",
    df["bioma"].nunique()
)

col4.metric(
    "🔥 FRP Máximo",
    round(df["frp"].max(), 1)
)


# ==========================================
# GRÁFICOS
# ==========================================

col_esq, col_dir = st.columns(2)

with col_esq:

    st.subheader("🔥 Top Estados")

    top_estados = (
        df["estado"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_estados.columns = [
        "estado",
        "quantidade"
    ]

    fig_estados = px.bar(
        top_estados,
        x="estado",
        y="quantidade",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig_estados,
        use_container_width=True
    )

with col_dir:

    st.subheader("🌳 Distribuição por Bioma")

    fig_bioma = px.pie(
        df,
        names="bioma",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig_bioma,
        use_container_width=True
    )

# ==========================================
# SATÉLITES
# ==========================================

st.subheader("🛰 Detecção por Satélite")

top_sat = (
    df["satelite"]
    .value_counts()
    .reset_index()
)

top_sat.columns = [
    "satelite",
    "quantidade"
]

fig_sat = px.bar(
    top_sat,
    x="satelite",
    y="quantidade",
    template="plotly_dark"
)

st.plotly_chart(
    fig_sat,
    use_container_width=True
)

# ==========================================
# MAPA
# ==========================================

st.subheader("🗺 Mapa Nacional de Focos")

mapa = px.scatter_map(
    df,
    lat="lat",
    lon="lon",
    hover_name="municipio",
    hover_data=[
        "estado",
        "bioma",
        "frp"
    ],
    zoom=3
)

mapa.update_layout(
    height=750
)

st.plotly_chart(
    mapa,
    use_container_width=True
)
# ==========================================
# TOP 10 MUNICÍPIOS
# ==========================================

st.subheader("🏆 Top 10 Municípios com Mais Focos")

top_municipios = (
    df["municipio"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_municipios.columns = [
    "municipio",
    "quantidade"
]

fig_municipios = px.bar(
    top_municipios,
    x="municipio",
    y="quantidade",
    template="plotly_dark",
    title="Municípios Mais Afetados"
)

fig_municipios.update_layout(
    xaxis_title="Município",
    yaxis_title="Quantidade de Focos"
)

st.plotly_chart(
    fig_municipios,
    use_container_width=True
)

# ==========================================
# INTENSIDADE DOS FOCOS (FRP)
# ==========================================

st.subheader("🔥 Intensidade dos Focos (FRP)")

fig_frp = px.histogram(
    df,
    x="frp",
    nbins=30,
    template="plotly_dark",
    title="Distribuição da Intensidade dos Focos"
)

fig_frp.update_layout(
    xaxis_title="FRP (Fire Radiative Power)",
    yaxis_title="Quantidade de Ocorrências"
)

st.plotly_chart(
    fig_frp,
    use_container_width=True
)

# ==========================================
# INSIGHTS
# ==========================================

st.subheader("🤖 Análise Automática")

estado_critico = (
    df["estado"]
    .value_counts()
    .idxmax()
)

municipio_critico = (
    df["municipio"]
    .value_counts()
    .idxmax()
)

st.success(
    f"🔥 Estado com maior incidência: {estado_critico}"
)

st.success(
    f"📍 Município mais afetado: {municipio_critico}"
)

st.success(
    f"🛰 Total de focos monitorados: {len(df):,}"
)

# ==========================================
# RODAPÉ
# ==========================================

st.markdown("---")

st.caption(
    "SpaceFire Alert • Global Solution FIAP • Dados fornecidos pelo Programa Queimadas INPE"
)