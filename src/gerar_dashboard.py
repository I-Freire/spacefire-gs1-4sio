# import pandas as pd
# from sqlalchemy import create_engine
# from dotenv import load_dotenv
# import plotly.express as px
# import os

# load_dotenv()

# engine = create_engine(
#     f"postgresql://{os.getenv('DB_USER')}:"
#     f"{os.getenv('DB_PASSWORD')}@"
#     f"{os.getenv('DB_HOST')}:"
#     f"{os.getenv('DB_PORT')}/"
#     f"{os.getenv('DB_NAME')}"
# )

# df = pd.read_sql(
#     "SELECT * FROM focos_incendio",
#     engine
# )

# total_focos = len(df)

# estados_monitorados = df["estado"].nunique()

# municipios_monitorados = df["municipio"].nunique()

# satelites = df["satelite"].nunique()

# frp_medio = round(
#     df["frp"].mean(),
#     2
# )

# frp_maximo = round(
#     df["frp"].max(),
#     2
# )

# estado_critico = (
#     df["estado"]
#     .value_counts()
#     .idxmax()
# )

# municipio_critico = (
#     df["municipio"]
#     .value_counts()
#     .idxmax()
# )

# grafico_estados = px.bar(
#     df["estado"]
#     .value_counts()
#     .head(10)
#     .reset_index(),
#     x="estado",
#     y="count",
#     title="Top Estados com Mais Focos"
# )

# grafico_biomas = px.pie(
#     df,
#     names="bioma",
#     title="Distribuição por Bioma"
# )

# grafico_satelites = px.bar(
#     df["satelite"]
#     .value_counts()
#     .reset_index(),
#     x="satelite",
#     y="count",
#     title="Focos Detectados por Satélite"
# )

# mapa = px.scatter_mapbox(
#     df,
#     lat="lat",
#     lon="lon",
#     hover_name="municipio",
#     hover_data=["estado", "bioma"],
#     zoom=3,
#     height=700
# )

# mapa.update_layout(
#     mapbox_style="open-street-map"
# )

# html = f"""
# <html>

# <head>
# <meta charset='utf-8'>
# <title>SpaceFire Alert</title>

# <style>

# body {{
#     font-family: Arial;
#     margin: 40px;
# }}

# .kpi {{
#     display:inline-block;
#     margin-right:40px;
#     font-size:20px;
# }}

# </style>

# </head>

# <body>

# <h1>🔥 SpaceFire Alert</h1>

# <h2>Monitoramento de Queimadas via Satélite</h2>

# <div class="kpi">
# <b>Total de Focos:</b> {total_focos}
# </div>

# <div class="kpi">
# <b>Estados:</b> {estados_monitorados}
# </div>

# <div class="kpi">
# <b>Municípios:</b> {municipios_monitorados}
# </div>

# <div class="kpi">
# <b>Satélites:</b> {satelites}
# </div>

# <div class="kpi">
# <b>FRP Médio:</b> {frp_medio}
# </div>

# <div class="kpi">
# <b>FRP Máximo:</b> {frp_maximo}
# </div>

# <hr>

# <h2>Análise Automática</h2>

# <p>
# O estado mais afetado foi
# <b>{estado_critico}</b>.
# </p>

# <p>
# O município mais afetado foi
# <b>{municipio_critico}</b>.
# </p>

# {grafico_estados.to_html(full_html=False)}

# {grafico_biomas.to_html(full_html=False)}

# {grafico_satelites.to_html(full_html=False)}

# {mapa.to_html(full_html=False)}

# </body>
# </html>
# """

# with open(
#     "reports/dashboard.html",
#     "w",
#     encoding="utf-8"
# ) as arquivo:
#     arquivo.write(html)

# print("Dashboard gerado com sucesso!")