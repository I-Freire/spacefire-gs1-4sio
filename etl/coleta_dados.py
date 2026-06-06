from datetime import datetime, timedelta
import pandas as pd
import os

# Cria pasta caso não exista
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

        print(f"✅ Download concluído!")
        print(f"📊 {len(df)} registros baixados.")
        print(f"📅 Data dos dados: {data_formatada}")

        return True

    except Exception as erro:
        print(f"❌ Arquivo não encontrado para {data_formatada}")
        print(f"Erro: {erro}")
        return False


# tenta hoje
hoje = datetime.now()

if baixar_csv(hoje):
    exit()

# tenta ontem
ontem = hoje - timedelta(days=1)

if baixar_csv(ontem):
    exit()

raise Exception(
    "Não foi possível baixar os dados do INPE."
)