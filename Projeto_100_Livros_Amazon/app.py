import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer_reviews.csv")
df_top100_books = pd.read_csv("datasets/top_trending_books.csv")

price_max = df_top100_books["book price"].max()

price_min = df_top100_books["book price"].min()

#printando o filtro
filter_price = st.sidebar.select_slider(
    "Price Range",
    options=df_top100_books["book price"].sort_values().unique(),
    value=price_max  # Valor inicial padrão
)
#filter_price = st.sidebar.select_slider("Price Range", price_min, price_max)

df_books = df_top100_books[df_top100_books["book price"] <= filter_price]

#printando a tabela
df_books

fig = px.bar(df_top100_books["year of publication"].value_counts())

fig2 = px.histogram(df_books["book price"])

#separando em colunas tipo divs
col1, col2 = st.columns(2)

#printando os graficos
col1.plotly_chart(fig)
col2.plotly_chart(fig2)






