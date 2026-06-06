import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

df = pd.read_csv(
    "data/raw/focos_diario_br.csv"
)

df = df[
    [
        "data_hora_gmt",
        "estado",
        "municipio",
        "lat",
        "lon",
        "satelite",
        "bioma",
        "frp"
    ]
]

df.to_sql(
    "focos_incendio",
    engine,
    if_exists="replace",
    index=False
)

print(f"{len(df)} registros carregados.")