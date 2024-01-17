import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criando um título para o dashboard
st.title('Dashboard')

# Adicionando um gráfico de exemplo (pode ser substituído pelos seus próprios dados)
df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# Adicionando um gráfico de dispersão ao dashboard
st.scatter_chart(df)

# Adicionando um seletor de arquivo para carregar dados
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

# Carregando e exibindo dados do arquivo CSV, se fornecido
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('Dados do arquivo CSV:')
    st.write(data)

# Adicionando um widget de slider para escolher um número
number = st.slider('Escolha um número', 0, 100, 50)
st.write('Número escolhido:', number)

# Exibindo uma tabela com dados de exemplo
st.write('Dados de exemplo:')
st.table(df)

# Exibindo um gráfico de barras
st.bar_chart(df)

# Criando um mapa de calor usando Seaborn
#if not data.empty:
 #   st.subheader('Mapa de Calor')
  #  corr_matrix = data.corr()
   # sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    #st.pyplot()

# Adicionando uma seção de texto formatado usando Markdown
st.markdown('**Este é um texto em negrito usando Markdown.**')

# Adicionando um botão
if st.button('Clique em mim'):
    st.write('Botão clicado!')