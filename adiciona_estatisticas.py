import os
import requests
import mysql.connector


def checkNone(value):
    if (value == None or value is None):
        return 0
    else:
        return int(value)


def checkNoneF(value):
    if (value == None or value is None):
        return 0
    else:
        return float(value)


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

fixtures_url = f'https://v3.football.api-sports.io/fixtures/players'


# Mude o valor de acordo com o campeonato desejado
query = "SELECT id FROM partidas where id_campeonato = 475"
cursor.execute(query)


rows = cursor.fetchall()
result = [item[0] for item in rows]

for i in result:
    fixtures_params = {
        'fixture': i
    }

    response = requests.get(
        fixtures_url, headers=headers, params=fixtures_params)
    fixtures = response.json()

    idmatch = fixtures['parameters']['fixture']

    for team_data in fixtures['response']:
        teamID = int(team_data['team']['id'])
        for player_data in team_data['players']:
            player_name = player_data['player']['name']
            player_id = player_data['player']['id']
            player_foto = player_data['player']['photo']
            cursor.execute("Insert ignore into jogadores(id,nome,imagem) values(%s,%s,%s)", (int(
                player_id), player_name, player_foto))
            print(f"Jogador: {player_name}")
            for stat in player_data['statistics']:
                minutos = stat['games']['minutes']
                numero = stat['games']['number']
                posicao = stat['games']['position']
                capitao = stat['games']['captain']
                banco = stat['games']['substitute']
                impedimentos = stat['offsides']
                chutes = stat['shots']['total']
                chutesNoGol = stat['shots']['on']
                gols = stat['goals']['total']
                golsTomados = stat['goals']['conceded']
                assistencias = stat['goals']['assists']
                defesas = stat['goals']['saves']
                passes = stat['passes']['total']
                passesChaves = stat['passes']['key']
                passesCertos = stat['passes']['accuracy']
                desarmes = stat['tackles']['total']
                bloqueios = stat['tackles']['blocks']
                interceptacoes = stat['tackles']['interceptions']
                duelos = stat['duels']['total']
                duelosGanhos = stat['duels']['won']
                driblesAttempt = stat['dribbles']['attempts']
                driblesCompletos = stat['dribbles']['success']
                jogadoresPassados = stat['dribbles']['past']
                faltasSofridas = stat['fouls']['drawn']
                faltasCometidas = stat['fouls']['committed']
                cartaoAmarelo = stat['cards']['yellow']
                cartaoVermelho = stat['cards']['red']
                penaltiCometido = stat['penalty']['commited']
                nota = stat['games']['rating']

                cursor.execute('''INSERT IGNORE INTO estatisticas (id_partida, id_time, id_jogador, minutos, numero, posicao, capitao, substituto, impedimentos, chutes, chutes_no_gol, gols, gols_sofridos, assistencias, defesas, passes, passes_chaves, passes_certos, desarmes, bloqueados, interceptados, duelos, duelos_ganhos, dribles_tentados, dribles_completos, jogadores_passados, faltas_sofridas, faltas_cometidas, cartoes_amarelos, cartoes_vermelhos, penaltis_cometidos,nota)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                                    ON DUPLICATE KEY UPDATE
                                        minutos = VALUES(minutos),
                                        numero = VALUES(numero),
                                        posicao = VALUES(posicao),
                                        capitao = VALUES(capitao),
                                        substituto = VALUES(substituto),
                                        impedimentos = VALUES(impedimentos),
                                        chutes = VALUES(chutes),
                                        chutes_no_gol = VALUES(chutes_no_gol),
                                        gols = VALUES(gols),
                                        gols_sofridos = VALUES(gols_sofridos),
                                        assistencias = VALUES(assistencias),
                                        defesas = VALUES(defesas),
                                        passes = VALUES(passes),
                                        passes_chaves = VALUES(passes_chaves),
                                        passes_certos = VALUES(passes_certos),
                                        desarmes = VALUES(desarmes),
                                        bloqueados = VALUES(bloqueados),
                                        interceptados = VALUES(interceptados),
                                        duelos = VALUES(duelos),
                                        duelos_ganhos = VALUES(duelos_ganhos),
                                        dribles_tentados = VALUES(dribles_tentados),
                                        dribles_completos = VALUES(dribles_completos),
                                        jogadores_passados = VALUES(jogadores_passados),
                                        faltas_sofridas = VALUES(faltas_sofridas),
                                        faltas_cometidas = VALUES(faltas_cometidas),
                                        cartoes_amarelos = VALUES(cartoes_amarelos),
                                        cartoes_vermelhos = VALUES(cartoes_vermelhos),
                                        penaltis_cometidos = VALUES(penaltis_cometidos),
                                        nota = values(nota);
                                        ''', (int(idmatch), teamID, int(player_id), checkNone(minutos), checkNone(numero), posicao, bool(capitao), bool(banco), checkNone(impedimentos), checkNone(chutes), checkNone(chutesNoGol), checkNone(gols),
                                              checkNone(golsTomados), checkNone(assistencias), checkNone(defesas), checkNone(
                    passes), checkNone(passesChaves), checkNone(passesCertos), checkNone(desarmes),
                    checkNone(bloqueios), checkNone(interceptacoes), checkNone(duelos), checkNone(
                    duelosGanhos), checkNone(driblesAttempt), checkNone(driblesCompletos),
                    checkNone(jogadoresPassados), checkNone(faltasSofridas), checkNone(faltasCometidas), checkNone(cartaoAmarelo), checkNone(cartaoVermelho), checkNone(penaltiCometido), checkNoneF(nota)))
conn.commit()
cursor.close()
conn.close()
