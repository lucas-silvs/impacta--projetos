import boto3

boto3.setup_default_session(profile_name="default")
dynamodb_client = boto3.client("dynamodb")
table_name = "music_lucas_da_silva_santos"


list_musicas = [
    {
    "nome": "Mazda Medusa",
    "artista": "YUNG LIXO",
    "album": "Sono Tapes II",
    "ano": "2020",
    "duracao": "03:01"
    },
    {
    "nome": "Syphon Filter",
    "artista": "YUNG LIXO, Yung Buda",
    "album": "Trashtalk",
    "ano": "2020",
    "duracao": "04:16"
    },
    {
    "nome": "Billy Knows Jimmie",
    "artista": "100 gecs",
    "album": "10,000 gecs",
    "ano": "2023",
    "duracao": "02:44"
    },

    {
    "nome": "Panic Room",
    "artista": "Au/Ra",
    "album": "Panic Room",
    "ano": "2018",
    "duracao": "03:58"
    },

    {
    "nome": "Jaws",
    "artista": "Sleep Token",
    "album": "Jaws",
    "ano": "2018",
    "duracao": "05:55"
    },

    {
    "nome": "Your First",
    "artista": "Paramore",
    "album": "This is Why",
    "ano": "2023",
    "duracao": "03:25"
    },

    {
    "nome": "Figure 8",
    "artista": "Paramore",
    "album": "This is Why",
    "ano": "2023",
    "duracao": "03:25" 
    },

    {
    "nome": "Vore",
    "artista": "Sleep Token",
    "album": "Vore",
    "ano": "2023",
    "duracao": "05:40"
    },

    {
    "nome": "The Only",
    "artista": "Static X",
    "album": "Shadow Zone",
    "ano": "2003",
    "duracao": "02:51"
    },

    {
    "nome": "Quinto Elemento",
    "artista": "YUNG LIXO",
    "album": "Trashtalk",
    "ano": "2020",
    "duracao": "03:58"
    },
    

]

lista_produtos = [

    {
    "tipo_produto": "Jogo",
    "preco": "",
    "hora": "",
    "ano": "",
    "forma_pagamento": ""
    }

]

for musica in list_musicas:
    response = dynamodb_client.put_item(
        TableName=table_name,
        Item={
            "nome_musica": {"S": musica["nome"]},
            "artista": {"S": musica["artista"]},
            "album": {"S": musica["album"]},
            "ano": {"N": musica["ano"]},
            "duracao": {"S": musica["duracao"]},
        },
    )