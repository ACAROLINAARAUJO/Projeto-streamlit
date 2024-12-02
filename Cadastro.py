import streamlit as st
import pandas as pd
from datetime import date


def gravar_dados(nome,data_Nasc,tipo):
    if nome and data_Nasc <= date.today():
            with open ("clientes.csv","a",encoding="utf-8") as file:
                file.write(f"{nome},{data_Nasc},{tipo}\n")
            st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False



st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="📝"
)

st.markdown("Cadastramento de Cliente")
st.divider()

nome = st.text_input("Digite o nome do cliente:",
                     key="nome_cliente")

data_Nasc = st.date_input("Data de Nascimento:", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo do Cliente:", ["Pessoa Juridica","Pessoa Fisica"])

btn_Cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome,data_Nasc,tipo]
                          )
if btn_Cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente Cadastrado!",
                   icon="✅")
    else:
        st.error("Erro no Cadastro",
                 icon="❌")



