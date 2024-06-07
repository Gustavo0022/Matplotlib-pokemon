import matplotlib.pyplot as plt
import pandas as pandas
import streamlit as st
from importlib import reload
plt=reload(plt)

def carregar_dados():
    data = pandas.read_csv("Pokemon.csv")
    return data

def home():
    st.title('Bem vindo à base de dados de Pokémon')
    st.subheader('Por Gustavo Gomes')

def grafico_linhas():
    st.title("Gráfico de linhas")


    data = carregar_dados()
    fig = plt.figure(figsize=(10,10))
    data.groupby("Generation")["HP"].mean().plot(marker="o")
    plt.title("Tendência de HP dos pokémons ao longo das gerações")
    plt.xlabel("geração")
    plt.ylabel("Média de HP")
    plt.grid()

    st.pyplot(fig)

    with st.expander("Código:"):
        with st.echo():
            data = carregar_dados()
            fig = plt.figure(figsize=(10,10))
            data.groupby("Generation")["HP"].mean().plot(marker="o")
            plt.title("Tendência de HP dos pokémons ao longo das gerações")
            plt.xlabel("geração")
            plt.ylabel("Média de HP")
            plt.grid()

def grafico_barras():
    st.title("Distribuição de pokémons por tipo")
    data = carregar_dados()

    fig = plt.figure(figsize=(10,10))

    

    type_counts = pandas.concat([data["Type1"], data["Type2"]]).value_counts()
    type_counts.plot(kind="bar")
    plt.title('Distribuição de pokémons por tipo')
    plt.xlabel('Tipo')
    plt.ylabel('Número de pokémon')
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    st.pyplot(fig)

    with st.expander("Código:"):
        with st.echo():
            type_counts = pandas.concat([data["Type1"], data["Type2"]]).value_counts()
            type_counts.plot(kind="bar")
            plt.title("Distribuição de pokémons por tipo")
            plt.xlabel("Tipo")
            plt.ylabel("Número de pokémon")
            plt.xticks(rotation=90)
            plt.grid(axis="y")
           

def grafico_boxplot():
    data = carregar_dados()

    st.title("Gráfico boxplot")

    fig = plt.figure(figsize= (10,10))
    stats = data[['HP', 'Attack', 'Defense','Sp. Atk', 'Sp. Def','Speed']]
    stats.boxplot()
    plt.title('Distribuição das stats de pokemon')
    st.pyplot(fig)

def grafico_pizza():

    st.title("Gráfico de pizza")
    dados = carregar_dados()
    legendary_counts = dados['Generation'].value_counts()

    fig = plt.figure(figsize=(10,10))

    plt.pie(legendary_counts, labels = ['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6', 'Gen 7', 'Gen 8', 'Gen 9'], autopct="%1.1f%%",startangle=140)
    st.pyplot(fig)
def main():
    st.sidebar.title("Base de dados pokémon")
    pages = {
        "Página Inicial" : home,
        "Linhas": grafico_linhas,
        "Barras": grafico_barras,
        "Boxplot": grafico_boxplot,
        "Pizza": grafico_pizza
    }

    selection = st.sidebar.selectbox("Ir para", list(pages.keys()))
    pages[selection]()

    st.sidebar.title("Sobre")
    st.sidebar.write("Feito por Gustavo Gomes Tavares durante o curso de MatPlotLib")

if __name__ == "__main__":
    main()