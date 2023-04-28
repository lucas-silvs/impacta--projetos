import pandas as pd
import json
import requests


moeda = input("digite a moeda que deseja: USD-BRL, EUR-BRL, BTC-BRL:\n")

url = f"https://economia.awesomeapi.com.br/last/{moeda}/"
req = requests.get(url)
json_req = json.loads(req.text)