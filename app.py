# =========================
# IMPORTAÇÃO DAS BIBLIOTECAS
# =========================

import streamlit as st      # Cria a interface web (inputs, botões, mensagens)
import requests             # Faz requisições HTTP (GET, POST, etc.)
import json                 # Converte dicionários Python para JSON
import urllib3              # Controla avisos de conexão (SSL)
import pandas as pd


# =========================
# CONFIGURAÇÕES INICIAIS
# =========================


# st.set_page_config(
#     page_title="Teste",
#     page_icon="🧪",
#     layout="wide"
# )


# Divide a tela em 2 colunas
# col_esq, col_dir = st.columns(2)


# Desativa avisos de SSL (usado quando a API não tem certificado confiável)
urllib3.disable_warnings()

# URL base do Firebase
link = "https://meuprojetocris-default-rtdb.firebaseio.com"






st.subheader('Nova Venda')

# Lista fixa de motivos
lista_motivos = [
    "Venda Normal",
    "Troca",
    "Devolução",
    "Cancelamento",
    "Outro"
]


with st.form("form_venda"):


    cliente = st.text_input("Cliente")

    produto = st.text_input("Produto")
    

    # Campo de lista (dropdown)
    motivo = st.selectbox(
        "Motivo da Venda",
        lista_motivos
    )


    enviar = st.form_submit_button("Cadastrar Venda")
    


if enviar:

    # 1️⃣ Validação
    if cliente == "" or produto == "":
        st.warning("⚠️ Preencher todos os campos")

    else:
        # 2️⃣ Monta os dados da venda
        dados_venda = {
            "cliente": cliente,
            "produto": produto,
            "motivo": motivo  # 👈 novo campo
        }

        # 3️⃣ Envia para o banco
        resposta = requests.post(
            url=f"{link}/Vendas.json",
            data=json.dumps(dados_venda),
            verify=False,
            timeout=10
        )

        # 4️⃣ Verifica se salvou
        if resposta.status_code == 200:
            st.success("✅ Venda Efetuada")
        else:
            st.error("❌ Erro ao salvar no banco")
