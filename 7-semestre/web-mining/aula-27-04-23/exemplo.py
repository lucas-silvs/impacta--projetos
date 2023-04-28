import pandas as pd
import json
import requests


cep = input("digite o CEP:\n")

url = f"https://viacep.com.br/ws/{cep}/json"
req = requests.get(url)
json_req = json.loads(req.text)
print(json_req)