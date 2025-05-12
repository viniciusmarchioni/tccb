import os
import requests
import mysql.connector
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DATABASE")
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

api_key = os.getenv("API_KEY")

headers = {
    'x-apisports-key': api_key
}

id_campeonato = 71  # brasileirão 71, euro copa 4, Argentina 5942, premiere league 39, la liga 140, serie b 72, CDB 73, serie A italiana 135, Bundesliga 78


fixtures_url = 'https://v3.football.api-sports.io/fixtures'
fixtures_params = {
    'league': id_campeonato,
    'season': 2025,
    'timezone': 'America/Sao_Paulo',
    'from': str(datetime.now().date().strftime('%Y-%m-%d')),
    'to': str((datetime.now().date() + timedelta(days=7)).strftime('%Y-%m-%d'))
}
fixtures_response = requests.get(
    fixtures_url, headers=headers, params=fixtures_params)
fixtures = fixtures_response.json()

for i in fixtures['response']:
    matchid = i['fixture']['id']
    id_time_casa = i['teams']['home']['id']
    id_time_fora = i['teams']['away']['id']
    nome_time_casa = i['teams']['home']['name']
    logo_time_casa = i['teams']['home']['logo']
    nome_time_fora = i['teams']['away']['name']
    logo_time_fora = i['teams']['away']['logo']
    data = i['fixture']['date']

    cursor.execute("INSERT IGNORE INTO times VALUES(%s, %s,%s)",
                   (id_time_casa, nome_time_casa,logo_time_casa))
    cursor.execute("INSERT IGNORE INTO times VALUES(%s, %s,%s)",
                   (id_time_fora, nome_time_fora,logo_time_fora))

    print(i['teams']['home']['name'], "x", i['teams']['away']['name'])
    try:
        lineups_url = 'https://v3.football.api-sports.io/fixtures/lineups'
        lineups_params = {
            "fixture": matchid
        }
        lineups_response = requests.get(
            lineups_url, headers=headers, params=lineups_params)
        lineups = lineups_response.json()['response']
        formacao_time_casa = None
        try:
            formacao_time_casa = lineups[0]['formation']
        except:
            formacao_time_casa = None

        formacao_time_fora = None

        try:
            formacao_time_casa = lineups[1]['formation']
        except:
            formacao_time_casa = None

        cursor.execute("INSERT INTO partidas VALUES(%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE formacao_time_casa = VALUES(formacao_time_casa), formacao_time_fora = VALUES(formacao_time_fora), data=VALUES(data)",
                       (matchid, id_time_casa, id_time_fora, formacao_time_casa, formacao_time_fora, id_campeonato, data))
    except:
        print(f"Erro: {nome_time_casa} x {nome_time_fora}")
    time.sleep(10)

conn.commit()
cursor.close()
conn.close()
