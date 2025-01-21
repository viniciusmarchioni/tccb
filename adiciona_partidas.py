import os
import requests
import mysql.connector

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

id_campeonato = 475  #brasileirão 71, euro copa 4, Argentina 5942, premiere league 39, la liga 140, serie b 72, CDB 73, serie A italiana 135, Bundesliga 78


fixtures_url = 'https://v3.football.api-sports.io/fixtures'
fixtures_params = {
    'league': id_campeonato,
    'season': 2025,
    'timezone':'America/Sao_Paulo',
    'status': 'FT'
    }
fixtures_response = requests.get(fixtures_url, headers=headers, params=fixtures_params)
fixtures = fixtures_response.json()

for i in fixtures['response']:
    matchid = i['fixture']['id']
    id_time_casa = i['teams']['home']['id']
    id_time_fora = i['teams']['away']['id']
    nome_time_casa = i['teams']['home']['name']
    nome_time_fora = i['teams']['away']['name']
    data = i['fixture']['date']
    
    cursor.execute("INSERT IGNORE INTO times VALUES(%s, %s)",(id_time_casa,nome_time_casa))
    cursor.execute("INSERT IGNORE INTO times VALUES(%s, %s)",(id_time_fora,nome_time_fora))
    
    
    print(i['teams']['home']['name'], "x",i['teams']['away']['name'])
    try:
        lineups_url = 'https://v3.football.api-sports.io/fixtures/lineups'
        lineups_params = {
            "fixture": matchid
            }
        lineups_response = requests.get(lineups_url, headers=headers, params=lineups_params)
        lineups = lineups_response.json()['response']
        formacao_time_casa = lineups[0]['formation']
        formacao_time_fora = lineups[1]['formation']
        cursor.execute("INSERT INTO partidas VALUES(%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE formacao_time_casa = VALUES(formacao_time_casa), formacao_time_fora = VALUES(formacao_time_fora), data=VALUES(data)"
                       ,(matchid,id_time_casa,id_time_fora,formacao_time_casa,formacao_time_fora,id_campeonato,data))
    except:
        print(f"Erro: {nome_time_casa} x {nome_time_fora}")

conn.commit()
cursor.close()
conn.close()