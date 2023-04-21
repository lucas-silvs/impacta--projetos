import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt



# nome da aplicação

st.write(
    '''
    # Jogos loja Nuuvem - AC03 Web Mining

    * Nome: Lucas da Silva Santos
    * RA: 1904209

    Os dados foram capturados do site www.nuuvem.com, uma plataforma nacional para compra de keys de jogos para computador
    e outros serviços para consoles como Gift Cards para Playstation 4 e 5, e Xbox Series X.

    Seleciona a análise pelos preços com desconto ou análise de outlier e intervalo de preços.
    '''
)

df = pd.read_csv('./1_bases_tratadas/base_tratada.csv', sep=',')

df_data = df['preco']

min_data = min(df_data)

max_data = max(df_data)

indicador = ["Preço total & valor descontos", "outliers & e análises de preços e descontos"]


escolha_do_indicador = st.sidebar.selectbox("Escolha um indicador", indicador)



df2 = df.copy()


def grafico_plotly_scatter(base, xcampo, ycampo):
    fig = px.scatter(base, x = xcampo, y=ycampo, color="intervalo_preco")
    return st.plotly_chart(fig)

def grafico_plotly_pie(base, campo):
    fig = px.pie(base, values="preco", names=campo, title='preços dos jogos em intervalos')
    return st.plotly_chart(fig)


def grafico_plotly_heatmap(base, xcampo, ycampo):
    fig = px.density_heatmap(base, x=xcampo, y=ycampo)
    return st.plotly_chart(fig)


def grafico_plotly_box(base, campo):
    fig = px.box(base[campo])
    return st.plotly_chart(fig)


def grafico_line(base):
   return st.line_chart(base)


def grafico_bar(base, campo):
    return st.bar_chart(base[campo])

def grafico_area_map(base):
    return st.area_chart(base)



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

    df_preco_original = pd.DataFrame()

    df_preco_original["preco_original"] = round(df["preco"]/(1 - (df["porcentagem_desconto"]/100)), 2) 


    st.line_chart(df_preco_original)

    st.write(f'''
    O Gráfico acima representa o valor original dos jogos sem o desconto atribuido, tendo em média o valor de 
    R\$ {df_preco_original["preco_original"].mean():.2f}
    ''')

    st.bar_chart(df_ajustado)

    media_preco_total = df_ajustado.loc[:, "preco"].add(df_ajustado.loc[:,"preco_descontado"]).mean()

    media_preco_desconto = df_ajustado["preco"].mean()
    mensagem = f'''
    No Gráfico acima representa o valor total dos produtos, o valor em azul claro é o preço atual, e valor 
    em azul escuro e o valor descontado, colocando o mouse acima é possivel obter o valor correspondente de cada
    valor.

    Já com os descontos aplicados, á média dos preços dos jogos chegam a  R\$ {media_preco_desconto:.2f}

    Também foi identificado que a maioria dos jogos não possuiam descontos, tendo a quantidade detalhada na página 
    "{indicador[1]}" 
    '''

    st.write(mensagem)


if(escolha_do_indicador == indicador[1]):

    df_ajustado["porcentagem_desconto"] = df["porcentagem_desconto"]

    

    df_ajustado["preco_original"] = round(df["preco"]/(1 - (df["porcentagem_desconto"]/100)), 2)

    grafico_plotly_box(df_ajustado, "preco")

    df_ajustado["intervalo_preco"] = df_ajustado["preco"].apply(preco_intervalo_encoder)

    df_ajustado["nome"] = df["nome"]
    grafico_plotly_scatter(df_ajustado, "porcentagem_desconto","preco_original")


    fig = px.pie(df_ajustado, values="preco", names="intervalo_preco", title='preços dos jogos em intervalos')
    teste  = st.plotly_chart(fig)
    # grafico_plotly_pie(df_ajustado, "intervalo_preco")

    st.write('''
    Baseado no Gráfico de pizza, foi identificado que o maior intervalo de desconto atual é o {} com %{} do total.
    ''')

    grafico_plotly_heatmap(df_ajustado, "preco", "porcentagem_desconto")

    mais_caros = df_ajustado.sort_values(by=["preco_original"], ascending=False).head(5)

    media_mais_caros = df_ajustado.sort_values(by=["preco"], ascending=False).head(5)["preco"].mean()


    ordem_colunas = ["nome","preco_original","porcentagem_desconto","preco"]
    mais_caros = mais_caros.reindex(columns=ordem_colunas)


    st.write(
    f'''
    Foi identificado que a maioria dos jogos com menos descontos e que atingiram preços muito altos, com média de valores de R\$ {media_mais_caros:.2f}
        
    Nesses valores, foi identificado um número maior de jogos abaixo de 50 reais, conforme o gráfico de contagem abaixo:
    ''')

    st.dataframe( df_ajustado["intervalo_preco"].value_counts())

    st.write(
        f'''
        ## 5 Jogos mais caros
        '''
    )

    st.dataframe(mais_caros)
 

    


