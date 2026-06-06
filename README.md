# 🔥 SpaceFire Alert

## 📌 Sobre o Projeto

O SpaceFire Alert é uma plataforma de monitoramento inteligente de queimadas baseada em dados espaciais do Programa Queimadas do INPE.

A solução utiliza informações captadas por satélites para transformar grandes volumes de dados ambientais em indicadores visuais, mapas interativos e análises que auxiliam a identificação rápida de áreas críticas, contribuindo para a prevenção de incêndios florestais e para a tomada de decisões ambientais.

Este projeto foi desenvolvido para a Global Solution FIAP 2026, dentro do tema **Space Connect**, demonstrando como tecnologias espaciais podem gerar impacto positivo na sociedade através do monitoramento ambiental.

---

# 🚀 Problema

As queimadas representam um dos principais desafios ambientais do Brasil, causando:

- Perda de biodiversidade;
- Emissão de gases de efeito estufa;
- Danos à saúde pública;
- Impactos econômicos e sociais.

Embora existam dados públicos disponibilizados por órgãos como o INPE, muitas vezes essas informações não estão acessíveis de forma simples para análise e tomada de decisão.

---

# 💡 Solução

O SpaceFire Alert centraliza e transforma dados de satélite em um dashboard interativo que permite:

- Monitorar focos de queimadas em tempo real;
- Identificar estados e municípios mais afetados;
- Visualizar áreas críticas em mapas geográficos;
- Analisar a intensidade dos focos através do indicador FRP (Fire Radiative Power);
- Filtrar informações por estado, bioma e satélite.

---

# 🛰️ Relação com a Economia Espacial

O projeto utiliza dados provenientes de satélites de observação da Terra, demonstrando uma aplicação prática da economia espacial para resolver problemas ambientais.

A solução transforma informações orbitais em inteligência acessível para:

- Órgãos governamentais;
- ONGs ambientais;
- Pesquisadores;
- Empresas do setor ambiental;
- Sociedade civil.

---

# 🏗️ Arquitetura da Solução

```text
Satélites INPE
       │
       ▼
Programa Queimadas
       │
       ▼
ETL Python
(Coleta automática)
       │
       ▼
Tratamento dos Dados
       │
       ▼
Dashboard Streamlit
       │
       ▼
Usuário Final
```

---

# 📊 Funcionalidades

## Indicadores Principais

- Total de focos detectados
- Quantidade de municípios monitorados
- Quantidade de biomas monitorados
- Intensidade máxima registrada (FRP)

## Visualizações

- Top 10 estados com mais focos
- Top 10 municípios mais afetados
- Distribuição por bioma
- Distribuição por satélite
- Histograma de intensidade dos focos (FRP)
- Mapa nacional interativo

## Recursos

- Atualização automática dos dados
- Integração com fonte oficial do INPE
- Filtros dinâmicos
- Interface web responsiva

---

# 🛠️ Tecnologias Utilizadas

### Linguagem

- Python 3.13

### Bibliotecas

- Streamlit
- Pandas
- Plotly
- Requests

### Fonte de Dados

Programa Queimadas - INPE

https://dataserver-coids.inpe.br/queimadas/

---

# 📂 Estrutura do Projeto

```text
spacefire-gs1-4sio/

├── data/
│   └── raw/
│       └── focos_diario_br.csv
│
├── etl/
│   └── coleta_dados.py
│
├── src/
│   └── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# ⚙️ Como Executar

## 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
```

## 2. Criar Ambiente Virtual

```bash
python -m venv venv
```

## 3. Ativar Ambiente

Windows:

```bash
venv\Scripts\activate
```

## 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

## 5. Executar Aplicação

```bash
streamlit run src/app.py
```

---

# 📈 Fonte dos Dados

Os dados são obtidos automaticamente através do Programa Queimadas do Instituto Nacional de Pesquisas Espaciais (INPE).

Os arquivos disponibilizados pelo INPE são atualizados diariamente e contêm:

- Localização geográfica;
- Data e hora da detecção;
- Satélite responsável;
- Município;
- Estado;
- Bioma;
- Intensidade do foco (FRP).

---

# 🌎 Impacto Esperado

O SpaceFire Alert busca democratizar o acesso a dados espaciais, permitindo que informações ambientais complexas sejam visualizadas de forma simples e intuitiva.

Entre os benefícios esperados estão:

- Apoio à prevenção de queimadas;
- Monitoramento ambiental contínuo;
- Maior transparência de dados públicos;
- Incentivo ao uso de tecnologias espaciais para sustentabilidade;
- Apoio à tomada de decisão baseada em dados.

---

# 👥 Equipe

Projeto desenvolvido para a Global Solution FIAP 2026.

Tema: Space Connect

Turma: 4SIOA

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.