from flask import Flask, jsonify
from flask import request
import pandas as pd 

app = Flask(__name__)

# nome integrantes
# Rafael Serino Kiss 1903107
# Lucas da Silva Santos 1904209

# contruindo as funcionalidades
@app.route('/')
def hello_word():
    return "A aplicação está no ar"


# exercicio 1
@app.route('/jogo/')
def pegarvendas():
    dados = pd.read_csv('./futebol.csv', sep=";")

    list_dados = []
    for index, row in dados.iterrows():
        list_dados.append({'Time da casa' : str(row['home_team_name']),
                      "Time visitante": str(row['away_team_name']),
                      "placar":  str(row['home_team_goal_count']) + "-"+ str(row['away_team_goal_count']),
                      "data partidas jogos": str(row['date_GMT'])
                      })
    return jsonify(list_dados)


# exercicio 2
@app.route('/casa/')
def pegarTimesCasa():
    dados = pd.read_csv('./futebol.csv', sep=";")

    # implementação para receber como parâmetro, bonus
    # list_times = []
    # list_times.append(request.args.get('time1'))
    # list_times.append(request.args.get('time2'))
    # list_times.append(request.args.get('time3'))

    list_times = ["Olimpia", "Guaireña", "Millwall"]

    list_dados = {}
    for time in list_times:
        list_dados.update({time: {
            "quantidade de gols":str(dados.loc[dados["home_team_name"] == time, "home_team_goal_count"].sum() + 
                                    dados.loc[dados["away_team_name"] == time, "away_team_goal_count"].sum()),
            "contagem de jogos": str(dados["home_team_name"].value_counts()[time] +  dados["away_team_name"].value_counts()[time])
        }})
    return jsonify(list_dados)

# exercicio 3
@app.route('/juizes/')
def pegaJogosPorJuizes():
    dados = pd.read_csv('./futebol.csv', sep=";")

    dados_juizes = dados["referee"].value_counts()

    list_dados = []
    for key in dados_juizes.keys():
         list_dados.append({"Nome Juiz": key,
                            "Quantidade jogos" : str(dados_juizes[key]) })
    return jsonify(list_dados)
app.run()