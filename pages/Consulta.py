import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")

st.markdown("Lista de Clientes Cadastrados")
st.dataframe(dados)