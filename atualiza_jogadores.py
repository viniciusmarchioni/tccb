'''
select distinct id_jogador from estatisticas e
inner join partidas p
on p.id = e.id_partida
where p.data > '2025-01-01';

'''

import os
import requests
import mysql.connector
from time import sleep

def checkNone(value):
    if(value==None or value is None):
        return 0
    else:
        return int(value)

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

fixtures_url = f'https://v3.football.api-sports.io/players'

cursor.execute(
'''
select distinct id_jogador from estatisticas e
inner join partidas p
on p.id = e.id_partida
''')
result = cursor.fetchall()
result =  [item[0] for item in result]

for i in result:

    params = {
            'id':i,
            'season':2025
    }

    response = requests.get(fixtures_url, headers=headers, params=params)
    players = response.json()
    
    try:
        nome = players['response'][0]['player']['name']
        image = players['response'][0]['player']['photo']
        nacionalidade = players['response'][0]['player']['nationality']
        aniversario = players['response'][0]['player']['birth']['date']
        lesionado = players['response'][0]['player']['injured']
        id_time = players['response'][0]['statistics'][0]['team']['id']

        cursor.execute(f'insert into jogadores values (%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE imagem=values(imagem),lesionado=values(lesionado),id_time=values(id_time)',
                    (i,nome,image,nacionalidade,aniversario,lesionado,id_time))

    except:
        print("Erro:",i)


conn.commit()

cursor.close()
conn.close()
