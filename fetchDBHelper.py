import os
import mysql.connector

config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DATABASE")
}


class Time:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome


class PlayerStats:
    def __init__(self, **kwargs):
        self.nota = kwargs.get('nota', 0)
        self.impedimentos = kwargs.get('impedimentos', 0)
        self.chutes = kwargs.get('chutes', 0)
        self.chutes_no_gol = kwargs.get('chutes_no_gol', 0)
        self.gols = kwargs.get('gols', 0)
        self.gols_sofridos = kwargs.get('gols_sofridos', 0)
        self.assistencias = kwargs.get('assistencias', 0)
        self.defesas = kwargs.get('defesas', 0)
        self.passes = kwargs.get('passes', 0)
        self.passes_chaves = kwargs.get('passes_chaves', 0)
        self.passes_certos = kwargs.get('passes_certos', 0)
        self.desarmes = kwargs.get('desarmes', 0)
        self.bloqueados = kwargs.get('bloqueados', 0)
        self.interceptados = kwargs.get('interceptados', 0)
        self.duelos = kwargs.get('duelos', 0)
        self.duelos_ganhos = kwargs.get('duelos_ganhos', 0)
        self.dribles_tentados = kwargs.get('dribles_tentados', 0)
        self.dribles_completos = kwargs.get('dribles_completos', 0)
        self.jogadores_passados = kwargs.get('jogadores_passados', 0)
        self.faltas_sofridas = kwargs.get('faltas_sofridas', 0)
        self.faltas_cometidas = kwargs.get('faltas_cometidas', 0)
        self.cartoes_amarelos = kwargs.get('cartoes_amarelos', 0)
        self.cartoes_vermelhos = kwargs.get('cartoes_vermelhos', 0)
        self.penaltis_cometidos = kwargs.get('penaltis_cometidos', 0)

    def arr(self, array):
        self.nota = para_float(array[2])
        self.impedimentos = para_int(array[3])
        self.chutes = para_int(array[4])
        self.chutes_no_gol = para_int(array[5])
        self.gols = para_int(array[6])
        self.gols_sofridos = para_int(array[7])
        self.assistencias = para_int(array[8])
        self.defesas = para_int(array[9])
        self.passes = para_int(array[10])
        self.passes_chaves = para_int(array[11])
        self.passes_certos = para_int(array[12])
        self.desarmes = para_int(array[13])
        self.bloqueados = para_int(array[14])
        self.interceptados = para_int(array[15])
        self.duelos = para_int(array[16])
        self.duelos_ganhos = para_int(array[17])
        self.dribles_tentados = para_int(array[18])
        self.dribles_completos = para_int(array[19])
        self.jogadores_passados = para_int(array[20])
        self.faltas_sofridas = para_int(array[21])
        self.faltas_cometidas = para_int(array[22])
        self.cartoes_amarelos = para_int(array[23])
        self.cartoes_vermelhos = para_int(array[24])
        self.penaltis_cometidos = para_int(array[25])

    def __repr__(self):
        return str(self.__dict__)


class Stats:
    def __init__(self, **kwargs):
        self.impedimentos_avg = kwargs.get('impedimentos', 0)
        self.chutes_avg = kwargs.get('chutes', 0)
        self.chutes_no_gol_avg = kwargs.get('chutes_no_gol', 0)
        self.gols_avg = kwargs.get('gols', 0)
        self.gols_sofridos_avg = kwargs.get('gols_sofridos', 0)
        self.assistencias_avg = kwargs.get('assistencias', 0)
        self.defesas_avg = kwargs.get('defesas', 0)
        self.passes_avg = kwargs.get('passes', 0)
        self.passes_chaves_avg = kwargs.get('passes_chaves', 0)
        self.passes_certos_avg = kwargs.get('passes_certos', 0)
        self.desarmes_avg = kwargs.get('desarmes', 0)
        self.bloqueados_avg = kwargs.get('bloqueados', 0)
        self.interceptados_avg = kwargs.get('interceptados', 0)
        self.duelos_avg = kwargs.get('duelos', 0)
        self.duelos_ganhos_avg = kwargs.get('duelos_ganhos', 0)
        self.dribles_tentados_avg = kwargs.get('dribles_tentados', 0)
        self.dribles_completos_avg = kwargs.get('dribles_completos', 0)
        self.jogadores_passados_avg = kwargs.get('jogadores_passados', 0)
        self.faltas_sofridas_avg = kwargs.get('faltas_sofridas', 0)
        self.faltas_cometidas_avg = kwargs.get('faltas_cometidas', 0)
        self.cartoes_amarelos_avg = kwargs.get('cartoes_amarelos', 0)
        self.cartoes_vermelhos_avg = kwargs.get('cartoes_vermelhos', 0)
        self.penaltis_cometidos_avg = kwargs.get('penaltis_cometidos', 0)

    def arr(self, array):
        self.impedimentos_avg = para_float(array[0])
        self.chutes_avg = para_float(array[1])
        self.chutes_no_gol_avg = para_float(array[2])
        self.gols_avg = para_float(array[3])
        self.gols_sofridos_avg = para_float(array[4])
        self.assistencias_avg = para_float(array[5])
        self.defesas_avg = para_float(array[6])
        self.passes_avg = para_float(array[7])
        self.passes_chaves_avg = para_float(array[8])
        self.passes_certos_avg = para_float(array[9])
        self.desarmes_avg = para_float(array[10])
        self.bloqueados_avg = para_float(array[11])
        self.interceptados_avg = para_float(array[12])
        self.duelos_avg = para_float(array[13])
        self.duelos_ganhos_avg = para_float(array[14])
        self.dribles_tentados_avg = para_float(array[15])
        self.dribles_completos_avg = para_float(array[16])
        self.jogadores_passados_avg = para_float(array[17])
        self.faltas_sofridas_avg = para_float(array[18])
        self.faltas_cometidas_avg = para_float(array[19])
        self.cartoes_amarelos_avg = para_float(array[20])
        self.cartoes_vermelhos_avg = para_float(array[21])
        self.penaltis_cometidos_avg = para_float(array[22])

    def __repr__(self):
        return str(self.__dict__)


class players:
    def __init__(self, nome: str, id: int):
        self.nome = nome
        self.id = id

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.__str__()


class playersPlus:
    def __init__(self, id: int, nome: str, imagem: str, nacionalidade: str, data_nacimento: str, lesionado: bool, id_time: int):
        self.id = id
        self.nome = nome
        self.imagem = imagem
        self.nacionalidade = nacionalidade
        self.data_nacimento = data_nacimento
        self.lesionado = lesionado
        self.id_time = id_time

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.__str__()


class JogadorTime:
    def __init__(self, id: int, nome: str, imagem: str, nometime: str):
        self.id = id
        self.nome = nome
        self.imagem = imagem
        self.nometime = nometime


class Jogador:
    def __init__(self, id: int, nome: str, nacionalidade: str, imagem: str, data_nascimento: str, lesionado: bool, id_time: int, nometime: str):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.imagem = imagem
        self.data_nascimento = data_nascimento
        self.lesionado = lesionado
        self.id_time = id_time
        self.nometime = nometime


def media_estatisticas(estatistica, posicao: str, formacao: str, minutos: int = 0, idplayer: int = None):
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
    if (idplayer != None):
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


def fetch_players(id_time, formacao, position, limit: int = 1000):
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
        jogadores.append(players(i[0], i[1]))
    return jogadores


def fetch_players_plus(id_time, formacao, position, limit: int = 1000):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(f'''
                        SELECT 
                            j.id,j.nome,j.imagem,j.nacionalidade,j.data_nascimento,j.lesionado,j.id_time
                        FROM
                            jogadores j
                                INNER JOIN
                            estatisticas e ON e.id_jogador = j.id
                                INNER JOIN
                            partidas p ON e.id_partida = p.ID
                        WHERE
                            e.id_time = {id_time} AND e.posicao = '{position}'
                                AND (p.formacao_time_casa = '{formacao}'
                                OR p.formacao_time_fora = '{formacao}')
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
        jogadores.append(playersPlus(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    return jogadores


def fetch_teams(apenas_serie_A: bool = False):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if (not apenas_serie_A):
        cursor.execute("select nome from times")
        times = cursor.fetchall()
        times = [item[0] for item in times]
        cursor.close()
        conn.close()
        return times
    cursor.execute(
        "select distinct nome from times t inner join partidas p on p.id_time_casa = t.id where Year(p.data) < YEAR(CURDATE())")
    times = cursor.fetchall()
    times = [item[0] for item in times]
    cursor.close()
    conn.close()
    return times


def get_id(team_name: str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('select id from times where nome=%s', (team_name,))
    id_time = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()
    return id_time


def get_formations(team_id: int):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT formacao_time_casa FROM partidas WHERE id_time_casa = {team_id} GROUP BY formacao_time_casa union select formacao_time_fora from partidas where id_time_fora={team_id} group by formacao_time_fora")
    formacoes = cursor.fetchall()
    formacoes = [item[0] for item in formacoes]
    cursor.close()
    conn.close()
    return formacoes


def avg_team_goals_conceded(team_id: int, formation: str):
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
    return desempenho_casa[0], desempenho_fora[0]


def avg_goals_conceded(formation: str):
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


def avg_goals_scored(team_id: int, formation: str):
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
    return desempenho_casa[0], desempenho_fora[0]


def avg_geral_stats(stat: str, formation: str):
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


def avg_team_stats(id_team: int, stat: str, formation: str):
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


def para_float(value):
    try:
        value = float(value)
        return value
    except:
        return float(0)


def para_int(value):
    try:
        value = int(value)
        return value
    except:
        return int(0)


def media_estatisticas_plus(posicao: str, formacao: str, *estatisticas: str, minutos: int = 0, idplayer: int = None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    estatisticasql = ""

    for estatistica in estatisticas:
        estatisticasql += f"avg({estatistica}),"

    if (idplayer != None):
        cursor.execute(f'''
                        select {estatisticasql[:-1]}
                        from (select *
                        from estatisticas e
                        inner join partidas p 
                        on e.id_partida = p.id 
                        where e.posicao="{posicao}" 
                        and minutos>{minutos}
                        and p.formacao_time_casa="{formacao}"
                        and id_time = id_time_casa
                        and e.id_jogador={idplayer}

                        union

                        select *
                        from estatisticas e
                        inner join partidas p 
                        on e.id_partida = p.id 
                        where e.posicao="{posicao}" 
                        and minutos>{minutos}
                        and p.formacao_time_fora="{formacao}"
                        and id_time = id_time_fora
                        and e.id_jogador={idplayer}
                        ) as sub
                        ''')
        mediajogador = cursor.fetchall()
        mediajogador = mediajogador[0]
        cursor.close()
        conn.close()
        return [para_float(num) for num in mediajogador]

    cursor.execute(f'''
                   select avg({estatisticas}) 
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

    cursor.close()
    conn.close()
    return media


def pesquisa_jogador(pesquisa: str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(
        f"select j.id,j.nome,j.imagem, t.nome from jogadores j inner join times t on id_time = t.id where j.nome like '%{pesquisa}%' limit 50")

    result = cursor.fetchall()

    jogadores = []

    for i in result:
        jogadores.append(JogadorTime(i[0], i[1], i[2], i[3]))

    return jogadores


def pesquisa_time(pesquisa: str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(
        f"select id,nome from times t where nome like '%{pesquisa}%' limit 50")

    result = cursor.fetchall()

    times = []

    for i in result:
        times.append(Time(i[0], i[1]))

    return times


def media_geral(posicao: str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    if (posicao == "G"):
        return []
    elif (posicao == "D"):
        cursor.execute('''
        select avg(desarmes),avg(bloqueados),avg(interceptados) from estatisticas
        inner join partidas p
        on p.id = id_partida
        where minutos > 15 
        and id_campeonato = 71 
        and substituto = 0
        and posicao = 'D'
                ''')
        result = cursor.fetchall()
        return result[0]
    elif (posicao == "M"):
        cursor.execute('''
        select avg(passes_certos),avg(assistencias),avg(passes_chaves) from estatisticas
        inner join partidas p
        on p.id = id_partida
        where minutos > 15 
        and id_campeonato = 71 
        and substituto = 0
        and posicao = 'M'
                ''')
        result = cursor.fetchall()
        return result[0]
    else:
        cursor.execute('''
        select avg(gols),avg(chutes_no_gol),avg(assistencias) from estatisticas
        inner join partidas p
        on p.id = id_partida
        where minutos > 15 
        and id_campeonato = 71 
        and substituto = 0
        and posicao = 'F'
                ''')
        result = cursor.fetchall()
        return result[0]


def todas_as_medias_geral(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('''
    select SUM(impedimentos) AS soma_impedimentos,
        SUM(chutes) AS soma_chutes,
        SUM(chutes_no_gol) AS soma_chutes_no_gol,
        SUM(gols) AS soma_gols,
        SUM(gols_sofridos) AS soma_gols_sofridos,
        SUM(assistencias) AS soma_assistencias,
        SUM(defesas) AS soma_defesas,
        SUM(passes) AS soma_passes,
        SUM(passes_chaves) AS soma_passes_chaves,
        SUM(passes_certos) AS soma_passes_certos,
        SUM(desarmes) AS soma_desarmes,
        SUM(bloqueados) AS soma_bloqueados,
        SUM(interceptados) AS soma_interceptados,
        SUM(duelos) AS soma_duelos,
        SUM(duelos_ganhos) AS soma_duelos_ganhos,
        SUM(dribles_tentados) AS soma_dribles_tentados,
        SUM(dribles_completos) AS soma_dribles_completos,
        SUM(jogadores_passados) AS soma_jogadores_passados,
        SUM(faltas_sofridas) AS soma_faltas_sofridas,
        SUM(faltas_cometidas) AS soma_faltas_cometidas,
        SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
        SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
        SUM(penaltis_cometidos) AS soma_penaltis_cometidos,
        AVG(nota) as media_nota
        from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    ''', (id_jogador,))
    result = cursor.fetchone()
    print(result)


def formacao_favorita_jogador(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
    select formacao, avg(media_nota) as media_nota, sum(qtd_partida) as qtd_partida from (
    select formacao_time_casa as formacao,avg(nota) as media_nota,count(id_partida) as qtd_partida from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    and p.id_time_casa = e.id_time
    group by formacao

    union

    select formacao_time_fora as formacao,avg(nota) as media_nota,count(id_partida) as qtd_partida from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    and p.id_time_fora = e.id_time
    group by formacao
    ) as sub
    group by formacao
    order by media_nota desc
    ''', (id_jogador, id_jogador))

    result = cursor.fetchone()
    if (result[-1] > 3):
        return result[0]
    save_result = result
    result = cursor.fetchone()
    if (result[-1] > 3):
        return result[0]
    else:
        print(save_result[1]-result[1])
        if (save_result[1]-result[1] > 0.3):
            return result[0]
        else:
            return save_result[0]


def estatisticas_formacao_favorita(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''select formacao,sum(qtd_partida) as qtd_partidas,avg(media_nota) as media_nota,
    SUM(soma_impedimentos) AS soma_impedimentos,
    SUM(soma_chutes) AS soma_chutes,
    SUM(soma_chutes_no_gol) AS soma_chutes_no_gol,
    SUM(soma_gols) AS soma_gols,
    SUM(soma_gols_sofridos) AS soma_gols_sofridos,
    SUM(soma_assistencias) AS soma_assistencias,
    SUM(soma_defesas) AS soma_defesas,
    SUM(soma_passes) AS soma_passes,
    SUM(soma_passes_chaves) AS soma_passes_chaves,
    SUM(soma_passes_certos) AS soma_passes_certos,
    SUM(soma_desarmes) AS soma_desarmes,
    SUM(soma_bloqueados) AS soma_bloqueados,
    SUM(soma_interceptados) AS soma_interceptados,
    SUM(soma_duelos) AS soma_duelos,
    SUM(soma_duelos_ganhos) AS soma_duelos_ganhos,
    SUM(soma_dribles_tentados) AS soma_dribles_tentados,
    SUM(soma_dribles_completos) AS soma_dribles_completos,
    SUM(soma_jogadores_passados) AS soma_jogadores_passados,
    SUM(soma_faltas_sofridas) AS soma_faltas_sofridas,
    SUM(soma_faltas_cometidas) AS soma_faltas_cometidas,
    SUM(soma_cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(soma_cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(soma_penaltis_cometidos) AS soma_penaltis_cometidos
    from(
    select formacao_time_casa as formacao,avg(nota) as media_nota,count(id_partida) as qtd_partida ,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    and p.id_time_casa = e.id_time
    group by formacao

    union

    select formacao_time_fora as formacao,avg(nota) as media_nota,count(id_partida) as qtd_partida ,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    and p.id_time_fora = e.id_time
    group by formacao) as sub
    group by formacao
    order by media_nota desc''', (id_jogador, id_jogador))

    result = cursor.fetchone()
    if (result[1] > 3):
        estatisticas = PlayerStats()
        estatisticas.arr(result)
        qtd_partidas = int(result[1])
        formacao_favorita = result[0]
        return estatisticas, formacao_favorita, qtd_partidas

    save_result = result
    result = cursor.fetchone()
    if (result[1] > 3):
        estatisticas = PlayerStats()
        estatisticas.arr(result)
        qtd_partidas = int(result[1])
        formacao_favorita = result[0]
        return estatisticas, formacao_favorita, qtd_partidas

    else:
        if (save_result[2]-result[2] > 0.3):
            estatisticas = PlayerStats()
            estatisticas.arr(result)
            qtd_partidas = int(result[1])
            formacao_favorita = result[0]
            return estatisticas, formacao_favorita, qtd_partidas
        else:
            estatisticas = PlayerStats()
            estatisticas.arr(save_result)
            qtd_partidas = int(save_result[1])
            formacao_favorita = save_result[0]
            return estatisticas, formacao_favorita, qtd_partidas


def estatisticas_posicao_favorita(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
    select posicao ,sum(qtd_partida) as qtd_partidas,avg(media_nota) as media_nota,
    SUM(soma_impedimentos) AS soma_impedimentos,
    SUM(soma_chutes) AS soma_chutes,
    SUM(soma_chutes_no_gol) AS soma_chutes_no_gol,
    SUM(soma_gols) AS soma_gols,
    SUM(soma_gols_sofridos) AS soma_gols_sofridos,
    SUM(soma_assistencias) AS soma_assistencias,
    SUM(soma_defesas) AS soma_defesas,
    SUM(soma_passes) AS soma_passes,
    SUM(soma_passes_chaves) AS soma_passes_chaves,
    SUM(soma_passes_certos) AS soma_passes_certos,
    SUM(soma_desarmes) AS soma_desarmes,
    SUM(soma_bloqueados) AS soma_bloqueados,
    SUM(soma_interceptados) AS soma_interceptados,
    SUM(soma_duelos) AS soma_duelos,
    SUM(soma_duelos_ganhos) AS soma_duelos_ganhos,
    SUM(soma_dribles_tentados) AS soma_dribles_tentados,
    SUM(soma_dribles_completos) AS soma_dribles_completos,
    SUM(soma_jogadores_passados) AS soma_jogadores_passados,
    SUM(soma_faltas_sofridas) AS soma_faltas_sofridas,
    SUM(soma_faltas_cometidas) AS soma_faltas_cometidas,
    SUM(soma_cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(soma_cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(soma_penaltis_cometidos) AS soma_penaltis_cometidos

    from (
    select posicao,avg(nota) as media_nota,count(id_partida) as qtd_partida ,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
                       and minutos > 15

    and p.id_time_casa = e.id_time
    group by posicao

    union

    select posicao as formacao,avg(nota) as media_nota,count(id_partida) as qtd_partida ,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
                       and minutos > 15

    and p.id_time_fora = e.id_time
    group by posicao) as sub
    group by posicao
    order by qtd_partidas desc
    ''', (id_jogador, id_jogador))

    result = cursor.fetchone()
    estatisticas = PlayerStats()
    estatisticas.arr(result)

    posicao_favorita = result[0]
    qtd_partidas = int(result[1])
    return estatisticas, posicao_favorita, qtd_partidas


def estatisticas_formacao_especifica(id_jogador, formacao):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f'''
    select formacao,sum(qtd_partida) as qtd_partidas,avg(media_nota) as media_nota,
    SUM(soma_impedimentos) AS soma_impedimentos,
    SUM(soma_chutes) AS soma_chutes,
    SUM(soma_chutes_no_gol) AS soma_chutes_no_gol,
    SUM(soma_gols) AS soma_gols,
    SUM(soma_gols_sofridos) AS soma_gols_sofridos,
    SUM(soma_assistencias) AS soma_assistencias,
    SUM(soma_defesas) AS soma_defesas,
    SUM(soma_passes) AS soma_passes,
    SUM(soma_passes_chaves) AS soma_passes_chaves,
    SUM(soma_passes_certos) AS soma_passes_certos,
    SUM(soma_desarmes) AS soma_desarmes,
    SUM(soma_bloqueados) AS soma_bloqueados,
    SUM(soma_interceptados) AS soma_interceptados,
    SUM(soma_duelos) AS soma_duelos,
    SUM(soma_duelos_ganhos) AS soma_duelos_ganhos,
    SUM(soma_dribles_tentados) AS soma_dribles_tentados,
    SUM(soma_dribles_completos) AS soma_dribles_completos,
    SUM(soma_jogadores_passados) AS soma_jogadores_passados,
    SUM(soma_faltas_sofridas) AS soma_faltas_sofridas,
    SUM(soma_faltas_cometidas) AS soma_faltas_cometidas,
    SUM(soma_cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(soma_cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(soma_penaltis_cometidos) AS soma_penaltis_cometidos

    from (
    select formacao_time_casa as formacao,avg(nota) as media_nota,count(id_partida) as qtd_partida ,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    and p.id_time_casa = e.id_time
                       and minutos > 15

    and p.formacao_time_casa = %s

    union

    select formacao_time_fora as formacao,avg(nota) as media_nota,count(id_partida) as qtd_partida ,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
                       and minutos > 15

    and p.formacao_time_fora = %s
    and p.id_time_fora = e.id_time) as sub
    group by formacao
    ''', (id_jogador, formacao, id_jogador, formacao))

    result = cursor.fetchone()
    estatisticas = PlayerStats()
    estatisticas.arr(result)

    qtd_partidas = int(result[1])
    return estatisticas, qtd_partidas


def todas_as_estatisticas(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(f'''
    select count(qtd_partida),sum(qtd_partida) as qtd_partida,avg(media_nota) as media_nota,
    SUM(soma_impedimentos) AS soma_impedimentos,
    SUM(soma_chutes) AS soma_chutes,
    SUM(soma_chutes_no_gol) AS soma_chutes_no_gol,
    SUM(soma_gols) AS soma_gols,
    SUM(soma_gols_sofridos) AS soma_gols_sofridos,
    SUM(soma_assistencias) AS soma_assistencias,
    SUM(soma_defesas) AS soma_defesas,
    SUM(soma_passes) AS soma_passes,
    SUM(soma_passes_chaves) AS soma_passes_chaves,
    SUM(soma_passes_certos) AS soma_passes_certos,
    SUM(soma_desarmes) AS soma_desarmes,
    SUM(soma_bloqueados) AS soma_bloqueados,
    SUM(soma_interceptados) AS soma_interceptados,
    SUM(soma_duelos) AS soma_duelos,
    SUM(soma_duelos_ganhos) AS soma_duelos_ganhos,
    SUM(soma_dribles_tentados) AS soma_dribles_tentados,
    SUM(soma_dribles_completos) AS soma_dribles_completos,
    SUM(soma_jogadores_passados) AS soma_jogadores_passados,
    SUM(soma_faltas_sofridas) AS soma_faltas_sofridas,
    SUM(soma_faltas_cometidas) AS soma_faltas_cometidas,
    SUM(soma_cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(soma_cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(soma_penaltis_cometidos) AS soma_penaltis_cometidos

    from (
    select count(id_partida) as qtd_partida,avg(nota) as media_nota,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    and minutos > 15
    and p.id_time_casa = e.id_time

    union

    select count(id_partida) as qtd_partida,avg(nota) as media_nota,
    SUM(impedimentos) AS soma_impedimentos,
    SUM(chutes) AS soma_chutes,
    SUM(chutes_no_gol) AS soma_chutes_no_gol,
    SUM(gols) AS soma_gols,
    SUM(gols_sofridos) AS soma_gols_sofridos,
    SUM(assistencias) AS soma_assistencias,
    SUM(defesas) AS soma_defesas,
    SUM(passes) AS soma_passes,
    SUM(passes_chaves) AS soma_passes_chaves,
    SUM(passes_certos) AS soma_passes_certos,
    SUM(desarmes) AS soma_desarmes,
    SUM(bloqueados) AS soma_bloqueados,
    SUM(interceptados) AS soma_interceptados,
    SUM(duelos) AS soma_duelos,
    SUM(duelos_ganhos) AS soma_duelos_ganhos,
    SUM(dribles_tentados) AS soma_dribles_tentados,
    SUM(dribles_completos) AS soma_dribles_completos,
    SUM(jogadores_passados) AS soma_jogadores_passados,
    SUM(faltas_sofridas) AS soma_faltas_sofridas,
    SUM(faltas_cometidas) AS soma_faltas_cometidas,
    SUM(cartoes_amarelos) AS soma_cartoes_amarelos,
    SUM(cartoes_vermelhos) AS soma_cartoes_vermelhos,
    SUM(penaltis_cometidos) AS soma_penaltis_cometidos
    from estatisticas e
    inner join partidas p
    on p.id = e.id_partida
    where id_jogador = %s
    and data < '2025-01-01'
    and minutos > 15
    and p.id_time_fora = e.id_time) as sub''', (id_jogador, id_jogador))

    result = cursor.fetchone()
    estatisticas = PlayerStats()
    estatisticas.arr(result)

    qtd_partidas = int(result[1])
    return estatisticas, qtd_partidas


def get_info_jogador(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('''
    select j.*,t.nome from jogadores j
    inner join times t
    on j.id_time = t.id
    where j.id = %s''',
                   (id_jogador,))

    result = cursor.fetchone()
    id = result[0]
    nome = result[1]
    imagem = result[2]
    nacionalidade = result[3]
    data_nascimento = result[4]
    lesionado = result[5]
    id_time = result[-2]
    nome_time = result[-1]
    jogador = Jogador(id=id, nome=nome, nacionalidade=nacionalidade, imagem=imagem,
                      data_nascimento=data_nascimento, lesionado=bool(lesionado), id_time=id_time, nometime=nome_time)

    return jogador


def get_formacoes_jogador(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(f'''
    select distinct formacao_time_casa from estatisticas 
    inner join partidas p
    on p.id = id_partida
    where id_jogador = %s
    and p.id_time_casa = id_time

    union

    select distinct formacao_time_fora from estatisticas 
    inner join partidas p
    on p.id = id_partida
    where id_jogador = %s
    and p.id_time_fora = id_time
    ''', (id_jogador, id_jogador))

    result = cursor.fetchall()

    formacoes = []

    for formacao in result:
        formacoes.append(formacao[0])

    return formacoes


def get_medias_total_posicao(posicao):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('''
    select AVG(impedimentos) AS media_impedimentos,
    AVG(chutes) AS media_chutes,
    AVG(chutes_no_gol) AS media_chutes_no_gol,
    AVG(gols) AS media_gols,
    AVG(gols_sofridos) AS media_gols_sofridos,
    AVG(assistencias) AS media_assistencias,
    AVG(defesas) AS media_defesas,
    AVG(passes) AS media_passes,
    AVG(passes_chaves) AS media_passes_chaves,
    AVG(passes_certos) AS media_passes_certos,
    AVG(desarmes) AS media_desarmes,
    AVG(bloqueados) AS media_bloqueados,
    AVG(interceptados) AS media_interceptados,
    AVG(duelos) AS media_duelos,
    AVG(duelos_ganhos) AS media_duelos_ganhos,
    AVG(dribles_tentados) AS media_dribles_tentados,
    AVG(dribles_completos) AS media_dribles_completos,
    AVG(jogadores_passados) AS media_jogadores_passados,
    AVG(faltas_sofridas) AS media_faltas_sofridas,
    AVG(faltas_cometidas) AS media_faltas_cometidas,
    AVG(cartoes_amarelos) AS media_cartoes_amarelos,
    AVG(cartoes_vermelhos) AS media_cartoes_vermelhos,
    AVG(penaltis_cometidos) AS media_penaltis_cometidos from estatisticas
    where posicao = %s
    and minutos > 45
    ''', (posicao,))

    result = cursor.fetchone()
    stats = Stats()
    stats.arr(result)
    return stats
