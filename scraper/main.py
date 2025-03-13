from bs4 import BeautifulSoup
import requests
import re
from dotenv import load_dotenv
import os
import csv

load_dotenv()

url = os.getenv("URL_PLAYERS")
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)


if response.status_code == 200:
    print('Conexão bem-sucedida!')
else:
    print('ERRO: Falha na conexão:', response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'items'})

players = []
#positions = ["Goleiro", "Zagueiro","Volante","Meia Central","Meia Ofensivo", "Ponta Esquerda", "Ponta Direita", "Atacante", "Centroavante"]
import re

players = []
#Cria Looping para guardar cada informação

for row in table.find_all('tr')[1:]:  # Ignorar cabeçalho
    cols = row.find_all('td')
    print('colunas: ', cols)
    if len(cols) < 7: 
        continue
    full_text = cols[1].get_text(" ", strip=True)  # Nome + posição
    nationality = [img['alt'] for img in cols[6].find_all('img')]

    match = re.match(r"^(.+?)\s+((?:Goleiro|Zagueiro|Volante|Meia Central|Meia Ofensivo|Ponta Esquerda|Ponta Direita|Atacante|Centroavante))$", full_text)
    age = cols[5].get_text(strip=True)
    foot = cols[8].get_text(strip=True)
    height = cols[7].get_text(strip=True)
    market_value = cols[-1].get_text(strip=True) 

    if match:
        name = match.group(1).strip()
        position = match.group(2).strip()
        players.append((name, position, nationality, age, foot, height))

#Salvar arquivo em documento csv
csv_file = "Data/players.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(players)

print(f"Arquivo salvo em: {csv_file}")

for player in players:
   print(player)