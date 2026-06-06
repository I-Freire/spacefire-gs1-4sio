from datetime import datetime, timedelta
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

def baixar_csv(data):
    data_formatada = data.strftime("%Y%m%d")

    url = (
        "https://dataserver-coids.inpe.br/"
        "queimadas/queimadas/focos/csv/diario/Brasil/"
        f"focos_diario_br_{data_formatada}.csv"
    )

    print(f"Tentando baixar: {url}")

    try:
        df = pd.read_csv(url)

        df.to_csv(
            "data/raw/focos_diario_br.csv",
            index=False
        )

        print(f"✅ {len(df)} registros baixados.")
        return True

    except Exception as erro:
        print(f"❌ Falha: {erro}")
        return False


hoje = datetime.now()

if not baixar_csv(hoje):
    ontem = hoje - timedelta(days=1)

    if not baixar_csv(ontem):
        raise Exception(
            "Não foi possível obter dados do INPE."
        )