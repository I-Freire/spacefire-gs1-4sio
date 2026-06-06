import os
import sys
import subprocess
import pandas as pd
import streamlit as st
import plotly.express as px

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="SpaceFire Alert",
    layout="wide"
)

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

st.title("🔥 SpaceFire Alert")
st.subheader("Monitoramento Inteligente de Queimadas via Satélite")

if st.button("🔄 Atualizar Dados do INPE"):

    subprocess.run(
        [sys.executable, "etl/coleta_dados.py"]
    )

    subprocess.run(
        [sys.executable, "etl/carga_postgres.py"]
    )

    st.success("Dados atualizados com sucesso!")

df = pd.read_sql(
    "SELECT * FROM focos_incendio",
    engine
)

df["data_hora_gmt"] = pd.to_datetime(
    df["data_hora_gmt"]
)

ultima_data = df["data_hora_gmt"].max()

st.info(
    f"Dados atualizados até: "
    f"{ultima_data.strftime('%d/%m/%Y %H:%M')}"
)

estado_filtro = st.sidebar.multiselect(
    "Estado",
    sorted(df["estado"].unique())
)

bioma_filtro = st.sidebar.multiselect(
    "Bioma",
    sorted(df["bioma"].dropna().unique())
)

if estado_filtro:
    df = df[
        df["estado"].isin(estado_filtro)
    ]

if bioma_filtro:
    df = df[
        df["bioma"].isin(bioma_filtro)
    ]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Focos",
    len(df)
)

col2.metric(
    "Estados",
    df["estado"].nunique()
)

col3.metric(
    "Municípios",
    df["municipio"].nunique()
)

col4.metric(
    "FRP Médio",
    round(df["frp"].mean(), 2)
)

grafico_estados = px.bar(
    df["estado"]
    .value_counts()
    .head(10)
    .reset_index(),
    x="estado",
    y="count",
    title="Top Estados com Mais Focos"
)

st.plotly_chart(
    grafico_estados,
    use_container_width=True
)

grafico_bioma = px.pie(
    df,
    names="bioma",
    title="Distribuição por Bioma"
)

st.plotly_chart(
    grafico_bioma,
    use_container_width=True
)

grafico_sat = px.bar(
    df["satelite"]
    .value_counts()
    .reset_index(),
    x="satelite",
    y="count",
    title="Focos Detectados por Satélite"
)

st.plotly_chart(
    grafico_sat,
    use_container_width=True
)

mapa = px.scatter_map(
    df,
    lat="lat",
    lon="lon",
    hover_name="municipio",
    hover_data=[
        "estado",
        "bioma",
        "satelite"
    ],
    zoom=3
)

st.plotly_chart(
    mapa,
    use_container_width=True
)

st.subheader("📊 Análise Automática")

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

st.write(
    f"O estado com maior incidência "
    f"de focos foi **{estado_critico}**."
)

st.write(
    f"O município mais afetado foi "
    f"**{municipio_critico}**."
)