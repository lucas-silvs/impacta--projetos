import boto3
import random
import datetime

# Cria conexão com AWS Dynamodb
boto3.setup_default_session(profile_name="default")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("buy_lucas_da_silva_santos")

opcoes_pagamento = ["pix", "debito", "credito", "boleto"]

perifericos = [
    "Webcam Logitech C920s HD Pro",
    "Teclado Gamer HyperX Alloy FPS Pro",
    "Mouse sem Fio Logitech M170",
    "Caixa de Som Bluetooth JBL Flip 5",
    "Headset Gamer HyperX Cloud II",
    "Monitor LED 24'' Samsung",
    "Gabinete Gamer Aerocool Cylon",
    "HD Externo Seagate Expansion 1TB",
    "SSD Kingston A2000 1TB",
    "Placa de Vídeo Gigabyte GeForce GTX 1660",
    "Processador AMD Ryzen 5 5600X",
    "Memória RAM Corsair Vengeance LPX 16GB",
    "Placa-mãe ASUS Prime B450M-Gaming/BR",
    "Impressora HP DeskJet Plus 4120",
    "Scanner Epson Perfection V39",
    "Roteador TP-Link Archer C6",
    "Switch D-Link DGS-1008A",
    "Câmera de Segurança Intelbras VHD 1220 B G4",
    "HD para Vigilância WD Purple 4TB",
    "Nobreak APC Back-UPS BZ1200-BR",
    "Filtro de Linha Clamper Energia 5",
    "Cabo HDMI 2.0 Ultra HD 4K",
    "Adaptador Bluetooth CSR 4.0",
    "Adaptador USB-C para HDMI",
    "Hub USB 3.0 com 7 Portas",
    "Leitor de Cartões de Memória Multilaser",
    "Gravador de DVD/CD Externo LG",
    "Fone de Ouvido Bluetooth JBL TUNE 500BT",
    "Caixa de Som Multimídia Genius SW-G2.1 2000",
    "Webcam Microsoft LifeCam HD-3000",
    "Teclado Microsoft Wired Keyboard 600",
    "Mouse sem Fio Microsoft Sculpt Comfort",
    "Monitor LED 23,8'' LG",
    "Gabinete Gamer PCYes Tiger Branco",
    "HD Externo WD Elements 2TB",
    "SSD Crucial MX500 1TB",
    "Placa de Vídeo MSI GeForce RTX 3070",
    "Processador Intel Core i7-11700K",
    "Memória RAM HyperX Fury RGB 32GB",
    "Placa-mãe ASRock B550M-HDV",
    "Impressora Epson EcoTank L3150",
    "Scanner Canon CanoScan LiDE 400",
    "Roteador Intelbras WRN 300",
    "Switch TP-Link TL-SF1005D",
    "Câmera de Segurança Wi-Fi Intelbras IC3",
    "HD para Vigilância Seagate SkyHawk 8TB",
    "Nobreak NHS Mini III 600VA",
    "Filtro de Linha SMS 5 Tomadas",
    "Cabo VGA com Filtro Stéreo",
    "Adaptador USB 3.0 para Ethernet",
    "Adaptador USB Wi-Fi TP-Link Archer T2U Nano"
]

purchases = []

for i in range(10):
    periferico = random.choice(perifericos)
    perifericos.pop(perifericos.index(periferico))
    compra =    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": periferico,
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    }
    purchases.append(compra)
    

for purchase in purchases:
    table.put_item(Item=purchase)