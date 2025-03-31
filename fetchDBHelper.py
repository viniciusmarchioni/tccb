import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DATABASE")
}


class Time:
    def __init__(self, id: int, nome: str, logo: str):
        self.id = id
        self.nome = nome
        self.logo = logo


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


class playersPlus:
    def __init__(self, id: int, nome: str, imagem: str, nacionalidade: str, data_nascimento: str, lesionado: bool, id_time: int, estatisticas):
        self.id = id
        self.nome = nome
        self.imagem = imagem
        self.nacionalidade = nacionalidade
        self.data_nacimento = data_nascimento
        self.lesionado = lesionado
        self.estatisticas = estatisticas
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


def obter_jogadores(id_time, formacao, posicao, limit: int = 1000):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query_param = []

    if (posicao == "D"):
        query_param.append("AVG(duelos_ganhos),")
        query_param.append("AVG(desarmes),")
        query_param.append("AVG(bloqueados)")
    elif (posicao == "M"):
        query_param.append("AVG(passes_certos),")
        query_param.append("AVG(assistencias),")
        query_param.append("AVG(passes_chaves)")
    else:
        query_param.append("AVG(gols),")
        query_param.append("AVG(assistencias),")
        query_param.append("AVG(chutes_no_gol)")

    cursor.execute(f'''
    SELECT id_jogador,j.nome, j.imagem, j.nacionalidade, j.data_nascimento,j.lesionado, SUM(minutos) as minutos, {query_param[0]+query_param[1]+query_param[2]}
    FROM estatisticas e
    INNER JOIN partidas p ON p.id = e.id_partida
    INNER JOIN jogadores j ON j.id = e.id_jogador
    WHERE
        e.id_time = %s
        AND j.id_time = e.id_time
        AND (
            (e.id_time = id_time_casa AND formacao_time_casa = %s)
            OR
            (e.id_time = id_time_fora AND formacao_time_fora = %s)
        )
        AND posicao = %s
    GROUP BY id_jogador
    ORDER BY minutos desc
    LIMIT %s;
    ''', (id_time, formacao, formacao, posicao, limit))
    result = cursor.fetchall()
    jogadores = []
    for i in result:
        jogadores.append(playersPlus(
            i[0], i[1], i[2], i[3], i[4], bool(i[5]), int(id_time), {'estatistica1': para_float(i[7]), 'estatistica2': para_float(i[8]), 'estatistica3': para_float(i[9])}))
    cursor.close()
    conn.close()
    return jogadores


def get_formations(team_id: int):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('''
                SELECT formacao_time_casa FROM partidas WHERE id_time_casa = %s and formacao_time_casa is not null
                GROUP BY formacao_time_casa
                union
                select formacao_time_fora from partidas where id_time_fora= %s and formacao_time_fora is not null
                group by formacao_time_fora;
                ''', (team_id, team_id))
    formacoes = cursor.fetchall()
    formacoes = [item[0] for item in formacoes]
    cursor.close()
    conn.close()
    return formacoes


def pesquisa_jogador(pesquisa: str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(
        f"select j.id,j.nome,j.imagem, t.nome from jogadores j inner join times t on id_time = t.id where j.nome like %s limit 10",(f"%{pesquisa}%",))

    result = cursor.fetchall()

    jogadores = []

    for i in result:
        jogadores.append(JogadorTime(i[0], i[1], i[2], i[3]))

    cursor.close()
    conn.close()
    return jogadores


def pesquisa_time(pesquisa: str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(
        f"select id,nome,logo from times t where nome like %s limit 10",(f"%{pesquisa}%",))

    result = cursor.fetchall()

    times = []

    for i in result:
        times.append(Time(i[0], i[1], i[2]))

    cursor.close()
    conn.close()
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
        result = cursor.fetchone()
        return result
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
        result = cursor.fetchone()
        return result
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
        result = cursor.fetchone()
        return result


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
    select posicao ,count(id_partida) as qtd_partida,avg(nota) as media_nota ,
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
        SUM(penaltis_cometidos) AS soma_penaltis_cometidos from estatisticas
    where id_jogador = %s
    group by posicao
    ''', (id_jogador,))

    result = cursor.fetchone()
    estatisticas = PlayerStats()
    estatisticas.arr(result)

    posicao_favorita = result[0]
    qtd_partidas = int(result[1])
    cursor.close()
    conn.close()
    return estatisticas, posicao_favorita, qtd_partidas


def estatisticas_jogador_formacao_especifica(id_jogador, formacao):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT
        formacao,
        COUNT(*) AS qtd_partidas,
        AVG(nota) AS media_nota,
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
    FROM (
        SELECT
            CASE
                WHEN e.id_time = p.id_time_casa THEN COALESCE(p.formacao_time_casa, %s)
                ELSE COALESCE(p.formacao_time_fora, %s)
            END AS formacao,
            e.*
        FROM estatisticas e
        INNER JOIN partidas p ON p.id = e.id_partida
        WHERE e.id_jogador = %s
            AND p.data < '2025-01-01'
            AND e.minutos > 15
    ) AS stats
    WHERE formacao = %s
    GROUP BY formacao;
    ''', (formacao, formacao, id_jogador, formacao))

    result = cursor.fetchone()
    estatisticas = PlayerStats()
    estatisticas.arr(result)

    qtd_partidas = int(result[1])

    cursor.close()
    conn.close()
    return estatisticas, qtd_partidas


def todas_as_estatisticas(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('''
    select 1,count(id_partida) as qtd_partida,avg(nota) as media_nota ,
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
        SUM(penaltis_cometidos) AS soma_penaltis_cometidos from estatisticas
    where id_jogador = %s
    ''', (id_jogador,))

    result = cursor.fetchone()
    estatisticas = PlayerStats()
    estatisticas.arr(result)

    qtd_partidas = int(result[1])
    cursor.close()
    conn.close()
    return estatisticas, qtd_partidas


def get_info_jogador(id_jogador):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('''
    select j.id,j.nome,imagem,nacionalidade,data_nascimento,lesionado,id_time,t.nome from jogadores j
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
    cursor.close()
    conn.close()
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
    and minutos > 15

    union

    select distinct formacao_time_fora from estatisticas
    inner join partidas p
    on p.id = id_partida
    where id_jogador = %s
    and p.id_time_fora = id_time
    and minutos > 15
    ''', (id_jogador, id_jogador))

    result = cursor.fetchall()

    formacoes = []

    for formacao in result:
        formacoes.append(formacao[0])
    cursor.close()
    conn.close()
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
    and minutos > 15
    ''', (posicao,))

    result = cursor.fetchone()
    stats = Stats()
    stats.arr(result)
    cursor.close()
    conn.close()
    return stats


def get_destaques(id, formacao=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    if (formacao != None):
        cursor.execute('''
        select nota,id_time_casa,id_time_fora,t.logo,t2.logo from (select * from estatisticas
        inner join partidas p
        on p.id = id_partida
        where id_jogador = %s
        and id_time_casa = id_time
        and formacao_time_casa = %s

        union

        select * from estatisticas
        inner join partidas p
        on p.id = id_partida
        where id_jogador = %s
        and id_time_fora = id_time
        and formacao_time_fora = %s
        ) as sub

        inner join times t
        on id_time_casa = t.id
        inner join times t2
        on id_time_fora = t2.id

        order by nota desc
        limit 3
        ''', (id, formacao, id, formacao))
    else:
        cursor.execute('''
        select nota,id_time_casa,id_time_fora,t.logo,t2.logo from (select * from estatisticas
        inner join partidas p
        on p.id = id_partida
        where id_jogador = %s
        and id_time_casa = id_time

        union

        select * from estatisticas
        inner join partidas p
        on p.id = id_partida
        where id_jogador = %s
        and id_time_fora = id_time
        ) as sub

        inner join times t
        on id_time_casa = t.id
        inner join times t2
        on id_time_fora = t2.id

        order by nota desc
        limit 3
        ''', (id, id))

    result = cursor.fetchall()
    destaques = []
    for i in result:
        destaques.append({
            "nota": i[0],
            "logo_mandante": i[3],
            "logo_visitante": i[4],
        })
    cursor.close()
    conn.close()
    return destaques


def get_aproveitamento(id, formacao):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('''
                   SELECT
                        desempenho,
                        COUNT(*) AS qtd
                    FROM (
                        SELECT
                            id_partida,
                            CASE
                                WHEN SUM(gols) > SUM(gols_sofridos) THEN 1  -- Vitória
                                WHEN SUM(gols) < SUM(gols_sofridos) THEN -1 -- Derrota
                                ELSE 0  -- Empate
                            END AS desempenho
                        FROM estatisticas e
                        INNER JOIN partidas p ON p.id = id_partida
                        WHERE e.id_time = %s
                        AND (
                            (e.id_time = id_time_casa AND formacao_time_casa = %s)
                            OR
                            (e.id_time = id_time_fora AND formacao_time_fora = %s)
                        )
                        GROUP BY id_partida  -- Agrupa antes de aplicar a lógica do CASE
                    ) AS subquery
                    GROUP BY desempenho;
                   ''', (id, formacao, formacao))

    vitorias = 0
    empates = 0
    derrotas = 0

    result = cursor.fetchall()
    for i in result:
        try:
            if (i[0] == 1):
                vitorias += i[1]
            elif (i[0] == 0):
                empates += i[1]
            else:
                derrotas += i[1]
        except:
            pass
    cursor.close()
    conn.close()
    return {"vitorias": vitorias, "empates": empates, "derrotas": derrotas}


def pesquisa_avancada(formatdict):

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        filtros = [chave for chave, valor in formatdict.items()
                   if valor is True]

        posicao = formatdict.get("posicao", "")
        formacao = formatdict.get("formacao", "")

        # Construindo a parte da soma dinâmica
        apoio = ""
        if filtros:
            apoio = ", SUM(" + " + ".join(filtros) + ") AS solicitacao"

        if filtros == []:
            apoio = ", avg(" + "e.nota"+") AS solicitacao"
        # Construindo a query
        query_build = f"""
        SELECT
            id_jogador, SUM(gols) AS gols, SUM(assistencias) AS assistencias, SUM(desarmes) AS desarmes,
            SUM(passes_certos) AS passes_certos, SUM(passes_chaves) AS chances_criadas,
            SUM(faltas_sofridas) AS faltas_sofridas, SUM(dribles_completos) AS dribles_completos,
            SUM(chutes_no_gol) AS chutes_no_gol, SUM(bloqueados) AS bloqueios, COUNT(id_partida) AS partidas_jogadas, avg(nota) as nota
            {apoio},
            j.nome, j.imagem, t.nome
        FROM estatisticas e
        INNER JOIN partidas p ON p.id = e.id_partida
        INNER JOIN jogadores j ON j.id = e.id_jogador
        INNER JOIN times t ON t.id = j.id_time
        WHERE TRUE
        """

        if formacao:
            query_build += f"""
            AND (
                (e.id_time = id_time_casa AND formacao_time_casa = "{formacao}")
                OR
                (e.id_time = id_time_fora AND formacao_time_fora = "{formacao}")
            )
            """

        if posicao:
            query_build += f" AND posicao = '{posicao}'"

        query_build += f"""
        GROUP BY id_jogador
        ORDER BY {"gols" if not apoio else "solicitacao"} DESC
        LIMIT 20
        """

        print(query_build)
        # Executando a query
        cursor.execute(query_build)
        result = cursor.fetchall()

        # Criando a lista de jogadores
        jogadores = [
            {
                "id": i[0],
                "gols": int(i[1]),
                "assistencias": int(i[2]),
                "desarmes": int(i[3]),
                "passes_certos": int(i[4]),
                "chances_criadas": int(i[5]),
                "faltas_sofridas": int(i[6]),
                "dribles_completos": int(i[7]),
                "chutes_no_gol": int(i[8]),
                "bloqueios": int(i[9]),
                "partidas_jogadas": int(i[10]),
                "nota": float(i[11]),
                "solicitacao": float(i[12]) if apoio else None,
                "nome": i[13],
                "imagem": i[14],
                "nomeTime": i[15],
            }
            for i in result
        ]
        cursor.close()
        conn.close()
        return jogadores
    except mysql.connector.Error as err:
        print(f"Erro no banco de dados: {err}")
    finally:
        cursor.close()
        conn.close()


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
