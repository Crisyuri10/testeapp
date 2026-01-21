
import streamlit as st      # Cria a interface web (inputs, botões, mensagens)
import requests             # Faz requisições HTTP (GET, POST, etc.)
import json                 # Converte dicionários Python para JSON
import urllib3              # Controla avisos de conexão (SSL)
import pandas as pd





# Desativa avisos de SSL (usado quando a API não tem certificado confiável)
urllib3.disable_warnings()

# URL base do Firebase
link = "https://meuprojetocris-default-rtdb.firebaseio.com"



st.subheader("Tabela")

# Lê os dados da tabela Vendas
dados = requests.get(f"{link}/Vendas.json", verify=False).json()

# Se não tiver nada no banco
if not dados:
    st.info("Nenhuma venda cadastrada")
else:
    # Converte os dados em tabela
    st.dataframe(pd.DataFrame.from_dict(dados, orient="index"))
