import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carrego os dados com os tamanhos e valores das pizzas
df = pd.read_csv("pizzas.csv")

# Passo os valores para o meu modelo
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

# Treino o modelo com os tamnhos e valores 
modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diametro da pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com o diâmetro de {diametro:.2f} cm é de R${preco_previsto:.2f}.")