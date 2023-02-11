import json

import requests

url = "http://127.0.0.1:8000/produtos/register/api/v1/"

data={
    "nome": "ChatGptddsdsddss",
    "imagem": None,
    "slug": "",
    "preco_marketing": 150,
    "score": 10}
headers = { 
    "Content-Type": "application/json"
    }

response = requests.request("POST", url, headers=headers, data=json.dumps(data))

response = response.json()
print(response["id"])
