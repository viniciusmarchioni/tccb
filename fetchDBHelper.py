import os
import mysql.connector

config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DATABASE")
}

class players:
    def __init__(self, nome: str, id: int):
        self.nome = nome
        self.id = id

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.__str__()

def media_estatisticas(estatistica,posicao:str,formacao:str,minutos:int=0,idplayer:int=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(f'''
                   select avg({estatistica}) 
                    from estatisticas e 
                    inner join partidas p 
                    on E.id_partida = P.id 
                    where e.posicao="{posicao}" 
                    and (p.formacao_time_casa="{formacao}" or p.formacao_time_fora="{formacao}") 
                    and minutos>{minutos}
                    and p.id_campeonato = 71
                   ''')
    media = cursor.fetchall()
    media = media[0][0]
    if(idplayer!=None):
        cursor.execute(f'''
                        select avg({estatistica}) 
                        from estatisticas e
                        inner join partidas p 
                        on e.id_partida = p.id 
                        where e.posicao="{posicao}" 
                        and minutos>{minutos}
                        and (p.formacao_time_casa="{formacao}" or p.formacao_time_fora="{formacao}") 
                        and e.id_jogador={idplayer}
                        ''')
        mediajogador = cursor.fetchall()
        mediajogador = mediajogador[0][0]
        cursor.close()
        conn.close()
        return mediajogador
    cursor.close()
    conn.close()
    return media

def fetch_players(id_time,formacao,position, limit):
    config = {
    'user': 'root',
    'password': 'vinicius15',
    'host': '127.0.0.1',
    'database': 'db_fut'
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(f'''
        SELECT nome, j.id FROM jogadores j
        INNER JOIN estatisticas e ON e.id_jogador = j.id
        INNER JOIN partidas p ON e.id_partida = p.ID
        WHERE e.id_time = {id_time} 
        AND e.posicao = "{position}"
        AND (p.formacao_time_casa = "{formacao}"
        OR p.formacao_time_fora = "{formacao}")
        AND minutos > 0
        GROUP BY id
        ORDER BY SUM(minutos) DESC
        LIMIT {limit}
    ''')
    result = cursor.fetchall()
    jogadores = []

    cursor.close()
    conn.close()
    for i in result:
        jogadores.append(players(i[0],i[1]))
    return jogadores

def fetch_teams(apenas_serie_A:bool = False):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if(not apenas_serie_A):
        cursor.execute("select nome from times")
        times = cursor.fetchall()
        times = [item[0] for item in times]
        cursor.close()
        conn.close()
        return times
    cursor.execute("select distinct nome from times t inner join partidas p on p.id_time_casa = t.id where Year(p.data) < YEAR(CURDATE())")
    times = cursor.fetchall()
    times = [item[0] for item in times]
    cursor.close()
    conn.close()
    return times

def get_id(team_name:str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('select id from times where nome=%s',(team_name,))
    id_time = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()
    return id_time

def get_formations(team_id:int):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f"SELECT formacao_time_casa FROM partidas WHERE id_time_casa = {team_id} GROUP BY formacao_time_casa union select formacao_time_fora from partidas where id_time_fora={team_id} group by formacao_time_fora")
    formacoes = cursor.fetchall()
    formacoes = [item[0] for item in formacoes]
    cursor.close()
    conn.close()
    return formacoes

def avg_team_goals_conceded(team_id:int,formation:str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
            select coalesce(avg(gols_sofridos),0)
            from partidas p
            inner join estatisticas e
            on e.id_partida=p.id
            where id_time_casa={team_id}
            and e.id_time={team_id}
            and formacao_time_casa="{formation}" 
            and e.posicao="G" and minutos>0
        ''')
    result = cursor.fetchall()
    desempenho_casa = [i[0] for i in result]
    cursor.execute(f'''
                select coalesce(avg(gols_sofridos),0)
                from partidas p
                inner join estatisticas e
                on e.id_partida=p.id
                where id_time_fora={team_id}
                and e.id_time={team_id}
                and formacao_time_fora="{formation}" 
                and e.posicao="G" and minutos>0
            ''')
    result = cursor.fetchall()
    desempenho_fora = [i[0] for i in result]
    cursor.close()
    conn.close()
    return desempenho_casa[0],desempenho_fora[0]

def avg_goals_conceded(formation:str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
                   select avg(gols_sofridos)
                    from (
                    select gols_sofridos 
                    from estatisticas e
                    inner join partidas p
                    on p.id = e.id_partida
                    where formacao_time_casa = "{formation}"
                    and posicao = "G"
                    and id_time = id_time_casa
                    and minutos > 0
                    and p.id_campeonato = 71

                    union all

                    select gols_sofridos 
                    from estatisticas e
                    inner join partidas p
                    on p.id = e.id_partida
                    where formacao_time_fora = "{formation}"
                    and posicao = "G"
                    and id_time = id_time_fora
                    and minutos > 0
                    and p.id_campeonato = 71
                ) as gols;
            ''')
    result = cursor.fetchall()
    media_gols_sofridos = result[0][0]
    cursor.close()
    conn.close()
    return media_gols_sofridos

def avg_goals_scored(team_id:int,formation:str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
        select coalesce(avg(gols_partida),0) from (
        select sum(gols) as gols_partida from estatisticas e
        inner join partidas p
        on e.id_partida = p.id
        where p.id_time_casa={team_id}
        and formacao_time_casa="{formation}"
        and e.id_time={team_id}
        group by e.id_partida ) as subquery
        ''')
    
    desempenho_casa = cursor.fetchone()

    cursor.execute(f'''
        select coalesce(avg(gols_partida),0) from (
        select sum(gols) as gols_partida from estatisticas e
        inner join partidas p
        on e.id_partida = p.id
        where p.id_time_fora={team_id}
        and formacao_time_fora="{formation}"
        and e.id_time={team_id}
        group by e.id_partida ) as subquery
        ''')
    desempenho_fora = cursor.fetchone()
    cursor.close()
    conn.close()
    return desempenho_casa[0],desempenho_fora[0]

def avg_geral_stats(stat:str,formation:str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
    select avg(estatistica_escolhida) as total_estatistica
    from (
    select sum({stat}) as estatistica_escolhida
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_time = id_time_casa
    and id_campeonato = 71
    and formacao_time_casa = "{formation}"
    group by id_partida

    union all

    select sum({stat}) as estatistica_escolhida
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_time = id_time_fora
    and id_campeonato = 71
    and formacao_time_fora = "{formation}"
    group by id_partida
    ) as subquery;
    ''')
    result = cursor.fetchall()
    media = result[0][0]
    return media

def avg_team_stats(id_team:int,stat:str,formation:str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
    select avg(estatistica_escolhida) as total_estatistica
    from (
    select sum({stat}) as estatistica_escolhida
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_time = id_time_casa
    and id_campeonato = 71
    and id_time = {id_team}
    and formacao_time_casa = "{formation}"
    group by id_partida

    union all

    select sum({stat}) as estatistica_escolhida
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_time = id_time_fora
    and id_campeonato = 71
    and id_time = {id_team}
    and formacao_time_fora = "{formation}"
    group by id_partida
    ) as subquery;
    ''')
    result = cursor.fetchall()
    media = result[0][0]
    return media
