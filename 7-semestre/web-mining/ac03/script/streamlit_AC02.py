import streamlit as st
import pandas as pd
import altair as alt
from datetime import date
import plotly.express as px
import math


# nome da aplicação

st.write(
    '''
    **Jogos loja Nuuvem**
    '''
)

def get_data():
    path = '../1_bases_tratadas/base_tratada.csv'
    return pd.read_csv(path, sep=',')

df = get_data()

df_data = df['preco']

min_data = min(df_data)

max_data = max(df_data)

indicador = ["Preço total & valor descontos", "outliers & jogos mais caros"]


escolha_do_indicador = st.sidebar.selectbox("Escolha um indicador", indicador)



df2 = df.copy()


def grafico_ploty_scatter(base, xcampo, ycampo):
    fig = px.scatter(base, x = xcampo, y=ycampo, color="intervalo_preco")
    return st.plotly_chart(fig)

def grafico_ploty_box(base, campo):
    fig = px.box(base[campo])
    return st.plotly_chart(fig)

def grafico_line(base):
   return st.line_chart(base)

def grafico_bar(base, campo):
    return st.bar_chart(base[campo])


def preco_intervalo_encoder(x):
    if (x>=0 and x<50):
        return "<50"
    if (x>=50 and x<100):
        return ">=50 e <100"
    if (x>=100 and x<150):
        return ">=100 e <150"
    else:
        return "+150"


df_ajustado = df[["preco" ]]
preco_calculado = (df["preco"]/(1 - (df["porcentagem_desconto"]/100))) - df["preco"]

df_ajustado["preco_descontado"] = preco_calculado


if(escolha_do_indicador == indicador[0]):

    st.bar_chart(df_ajustado)

    media_preco_total = df_ajustado.loc[:, "preco"].add(df_ajustado.loc[:,"preco_descontado"]).mean()

    media_preco_desconto = df_ajustado["preco"].mean()
    mensagem = f'''
    Foi realizado a análise individual do preço original com o desconto, onde a média dos preços 
    sem descontos chegavam {media_preco_total:.2f}

    Já com os descontos aplicados, á média dos preços dos jogos chegam a {media_preco_desconto:.2f}

    Também foi identificado que a maioria dos jogos não possuiam descontos
    '''

    st.write(mensagem)


if(escolha_do_indicador == indicador[1]):

    df_ajustado["porcentagem_desconto"] = df["porcentagem_desconto"]

    df_ajustado["preco_original"] = round(df["preco"]/(1 - (df["porcentagem_desconto"]/100)), 2)

    grafico_ploty_box(df_ajustado, "preco")

    df_ajustado["intervalo_preco"] = df_ajustado["preco"].apply(preco_intervalo_encoder)

    df_ajustado["nome"] = df["nome"]
    grafico_ploty_scatter(df_ajustado, "porcentagem_desconto","preco_original")


    mais_caros = df_ajustado.sort_values(by=["preco_original"], ascending=False).head(5)

    media_mais_caros = df_ajustado.sort_values(by=["preco_original"], ascending=False).head(5)["preco_original"].mean()


    ordem_colunas = ["nome","preco_original","porcentagem_desconto","preco"]
    mais_caros = mais_caros.reindex(columns=ordem_colunas)


    st.write(
    f'''
    Foi identificado que a maioria dos jogos com menos descontos e que atingiram preços muito altos, são lançamentos dos ultimos 2 anos,
    chegando a valores acima de R\$ 200,00 mesmo com descontos aplicados, com média de valores de R\$ {media_mais_caros:.2f}
    

    Nesses valores, foi identificado um número maior de jogos abaixo de 50 reais, conforme o gráfico de contagem abaixo:
    ''')

    st.dataframe( df_ajustado["intervalo_preco"].value_counts())

    st.write(
        f'''
        ## 5 Jogos mais caros
        '''
    )

    st.dataframe(mais_caros)
 

    


