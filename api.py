import mysql.connector
from flask import Flask, jsonify, request
from fetchDBHelper import *
from flask_cors import CORS
from previsao_XGBoost import prever_resultado

app = Flask(__name__)
CORS(app)


def getbool(str):
    if (str == "true" or str == "True"):
        return True
    else:
        return False


@app.route("/jogadores/<id>", methods=["GET"])
def get_info_time(id):

    formacao = get_formations(id)

    if (formacao == []):
        return jsonify(), 404

    # transforma em uma lista de inteiros
    formacao_list = list(map(int, formacao[0].split('-')))
    goleiros = []
    defensores = []
    meias = []
    atacantes = []

    for i in fetch_players_plus(id, formacao[0], "G", 1):
        goleiros.append(i.__dict__)

    for i in fetch_players_plus(id, formacao[0], "D", formacao_list[0]):
        defensores.append(i)

    for i in fetch_players_plus(id, formacao[0], "M", sum(map(int, formacao_list[1:-1]))):
        meias.append(i)

    for i in fetch_players_plus(id, formacao[0], "F", formacao_list[-1]):
        atacantes.append(i)

    return jsonify({
        "aproveitamento": get_aproveitamento(id, formacao[0]),
        "formações": formacao,
        "goleiro": [i for i in goleiros],
        "defensores": [i.__dict__ for i in defensores],
        "meias": [i.__dict__ for i in meias],
        "atacantes": [i.__dict__ for i in atacantes]
    }), 200


@app.route("/times/teste/<id>/<formacao>", methods=["GET"])
def get_jogadores_formacao(id, formacao):

    # transforma em uma lista de inteiros
    formacao_list = list(map(int, formacao.split('-')))

    goleiros = []
    defensores = []
    meias = []
    atacantes = []

    for i in fetch_players_plus(id, formacao, "G", 1):
        goleiros.append(i.__dict__)

    for i in fetch_players_plus(id, formacao, "D", formacao_list[0]):
        defensores.append(i)

    for i in fetch_players_plus(id, formacao, "M", sum(map(int, formacao_list[1:-1]))):
        meias.append(i)

    for i in fetch_players_plus(id, formacao, "F", formacao_list[-1]):
        atacantes.append(i)

    return jsonify({
        "aproveitamento": get_aproveitamento(id, formacao),
        "goleiro": [i for i in goleiros],
        "defensores": [i.__dict__ for i in defensores],
        "meias": [i.__dict__ for i in meias],
        "atacantes": [i.__dict__ for i in atacantes]
    }), 200


@app.route("/jogadores/<id>/<formacao>", methods=["GET"])
def get_jogadores(id, formacao):

    goleiros = []
    defensores = []
    meias = []
    atacantes = []

    formacao_list = formacao.split("-")
    # transforma em uma lista de inteiros
    formacao_list = list(map(int, formacao_list))

    for i in fetch_players_plus(id, formacao, "G", 1):
        goleiros.append({"id": i.id,
                         "nome": i.nome,
                         "imagem": i.imagem,
                         "nacionalidade": i.nacionalidade,
                         "data_nacimento": i.data_nacimento,
                         "lesionado": bool(i.lesionado),
                         "id_time": i.id_time,
                         "estatisticas": {}
                         })

    for i in fetch_players_plus(id, formacao, "D", formacao_list[0]):
        estatisticas = media_estatisticas_plus(
            "D", formacao, "duelos_Ganhos", "desarmes", "bloqueados", minutos=15, idplayer=i.id)
        defensores.append({"id": i.id,
                           "nome": i.nome,
                           "imagem": i.imagem,
                           "nacionalidade": i.nacionalidade,
                           "data_nacimento": i.data_nacimento,
                           "lesionado": bool(i.lesionado),
                           "id_time": i.id_time,
                           "estatisticas": {
                               'estatistica1': estatisticas[0],
                               'estatistica2': estatisticas[1],
                               'estatistica3': estatisticas[2]
                           }
                           })

    for i in fetch_players_plus(id, formacao, "M", sum(map(int, formacao_list[1:-1]))):
        estatisticas = media_estatisticas_plus(
            "M", formacao, "passes_certos", "assistencias", "passes_chaves", minutos=15, idplayer=i.id)
        meias.append({"id": i.id,
                      "nome": i.nome,
                      "imagem": i.imagem,
                      "nacionalidade": i.nacionalidade,
                      "data_nacimento": i.data_nacimento,
                      "lesionado": bool(i.lesionado),
                      "id_time": i.id_time,
                      "estatisticas": {
                          'estatistica1': estatisticas[0],
                          'estatistica2': estatisticas[1],
                          'estatistica3': estatisticas[2]
                      }
                      })

    for i in fetch_players_plus(id, formacao, "F", formacao_list[-1]):
        estatisticas = media_estatisticas_plus(
            "F", formacao, "gols", "chutes_no_gol", "assistencias", minutos=15, idplayer=i.id)
        atacantes.append({"id": i.id,
                          "nome": i.nome,
                          "imagem": i.imagem,
                          "nacionalidade": i.nacionalidade,
                          "data_nacimento": i.data_nacimento,
                          "lesionado": bool(i.lesionado),
                          "id_time": i.id_time,
                          "estatisticas": {
                              'estatistica1': estatisticas[0],
                              'estatistica2': estatisticas[1],
                              'estatistica3': estatisticas[2]
                          }
                          })

    return jsonify([{"goleiros": goleiros}, {"defensores": defensores}, {"meias": meias}, {"atacantes": atacantes}]), 200


@app.route("/jogadores/<id>/", methods=["GET"])
def get_jogadores_sem_formacao(id):

    formacao = get_formations(id)[0]

    goleiros = []
    defensores = []
    meias = []
    atacantes = []

    formacao_list = formacao.split("-")
    # transforma em uma lista de inteiros
    formacao_list = list(map(int, formacao_list))

    for i in fetch_players_plus(id, formacao, "G", 1):
        goleiros.append({"id": i.id,
                         "nome": i.nome,
                         "imagem": i.imagem,
                         "nacionalidade": i.nacionalidade,
                         "data_nacimento": i.data_nacimento,
                         "lesionado": bool(i.lesionado),
                         "id_time": i.id_time,
                         "estatisticas": {}
                         })

    for i in fetch_players_plus(id, formacao, "D", formacao_list[0]):
        estatisticas = media_estatisticas_plus(
            "D", formacao, "duelos_Ganhos", "desarmes", "bloqueados", minutos=15, idplayer=i.id)
        defensores.append({"id": i.id,
                           "nome": i.nome,
                           "imagem": i.imagem,
                           "nacionalidade": i.nacionalidade,
                           "data_nacimento": i.data_nacimento,
                           "lesionado": bool(i.lesionado),
                           "id_time": i.id_time,
                           "estatisticas": {
                               'estatistica1': estatisticas[0],
                               'estatistica2': estatisticas[1],
                               'estatistica3': estatisticas[2]
                           }
                           })

    for i in fetch_players_plus(id, formacao, "M", sum(map(int, formacao_list[1:-1]))):
        estatisticas = media_estatisticas_plus(
            "M", formacao, "passes_certos", "assistencias", "passes_chaves", minutos=15, idplayer=i.id)
        meias.append({"id": i.id,
                      "nome": i.nome,
                      "imagem": i.imagem,
                      "nacionalidade": i.nacionalidade,
                      "data_nacimento": i.data_nacimento,
                      "lesionado": bool(i.lesionado),
                      "id_time": i.id_time,
                      "estatisticas": {
                          'estatistica1': estatisticas[0],
                          'estatistica2': estatisticas[1],
                          'estatistica3': estatisticas[2]
                      }
                      })

    for i in fetch_players_plus(id, formacao, "F", formacao_list[-1]):
        estatisticas = media_estatisticas_plus(
            "F", formacao, "gols", "chutes_no_gol", "assistencias", minutos=15, idplayer=i.id)
        atacantes.append({"id": i.id,
                          "nome": i.nome,
                          "imagem": i.imagem,
                          "nacionalidade": i.nacionalidade,
                          "data_nacimento": i.data_nacimento,
                          "lesionado": bool(i.lesionado),
                          "id_time": i.id_time,
                          "estatisticas": {
                              'estatistica1': estatisticas[0],
                              'estatistica2': estatisticas[1],
                              'estatistica3': estatisticas[2]
                          }
                          })

    return jsonify([{"goleiros": goleiros}, {"defensores": defensores}, {"meias": meias}, {"atacantes": atacantes}, {'formacao': formacao}]), 200


@app.route("/media/<formacao>", methods=["GET"])
def get_media_geral(formacao):
    media_duelos = media_estatisticas("Duelos_Ganhos", "D", formacao, 15)
    media_desarmes = media_estatisticas("desarmes", "D", formacao, 15)
    media_bloqueios = media_estatisticas("bloqueados", "D", formacao, 15)
    media_passes_certos = media_estatisticas(
        "passes_certos", "M", formacao, 15)
    media_assistencias = media_estatisticas("assistencias", "M", formacao, 15)
    media_dribles_completos = media_estatisticas(
        "dribles_completos", "M", formacao, 15)
    media_gols = media_estatisticas("Gols", "F", formacao, 15)
    media_chutes_no_gol = media_estatisticas("chutes_no_gol", "F", formacao)
    medias = {"duelos": float(media_duelos),
              "desarmes": float(media_desarmes),
              "bloqueios": float(media_bloqueios),
              "passesCertos": float(media_passes_certos),
              "assistencias": float(media_assistencias),
              "driblesCompletos": float(media_dribles_completos),
              "gols": float(media_gols),
              "chutes_no_gol": float(media_chutes_no_gol)}

    return jsonify(medias)


@app.route("/times/<id>", methods=["GET"])
def get_detalhes(id):
    formacoes = get_formations(id)
    # TODO adicionar competições que o clube participa
    return jsonify({"formacoes": formacoes})


@app.route("/<pesquisa>", methods=["GET"])
def pesquisa(pesquisa):
    jogadores_dict = []
    times_dict = []
    jogadores = pesquisa_jogador(pesquisa)
    time = pesquisa_time(pesquisa)

    for i in jogadores:
        jogadores_dict.append(i.__dict__)

    for i in time:
        times_dict.append(i.__dict__)

    return jsonify({"jogadores": jogadores_dict, "times": times_dict})


@app.route("/medias/", methods=["GET"])
def get_media():
    media_atacantes = media_geral("F")
    media_atacantes = {
        "estatistica1": float(media_atacantes[0]),
        "estatistica2": float(media_atacantes[1]),
        "estatistica3": float(media_atacantes[1]),
    }

    media_meias = media_geral("M")
    media_meias = {
        "estatistica1": float(media_meias[0]),
        "estatistica2": float(media_meias[1]),
        "estatistica3": float(media_meias[1]),
    }

    media_defensores = media_geral("D")
    media_defensores = {
        "estatistica1": float(media_defensores[0]),
        "estatistica2": float(media_defensores[1]),
        "estatistica3": float(media_defensores[1]),
    }
    return jsonify({"media_atacantes": media_atacantes, "media_meias": media_meias, "media_defensores": media_defensores})


@app.route("/teste/<id>", methods=["GET"])
def testeJogador(id):

    est_formacao_favorita, formacao_favorita, qtd_partidas_formacao_favorita = estatisticas_formacao_favorita(
        id)

    est_posicao_favorita, posicao_favorita, qtd_partidas_pos = estatisticas_posicao_favorita(
        id)

    est_total, partidas_jogadas_total = todas_as_estatisticas(id)

    estatisticas = {
        "nota": est_total.nota,
        "impedimentos_total": est_total.impedimentos,
        "impedimentos_avg": est_total.impedimentos / partidas_jogadas_total,
        "chutes_total": est_total.chutes,
        "chutes_avg": est_total.chutes / partidas_jogadas_total,
        "chutes_no_gol_total": est_total.chutes_no_gol,
        "chutes_no_gol_avg": est_total.chutes_no_gol / partidas_jogadas_total,
        "gols_total": est_total.gols,
        "gols_avg": est_total.gols / partidas_jogadas_total,
        "gols_sofridos_total": est_total.gols_sofridos,
        "gols_sofridos_avg": est_total.gols_sofridos / partidas_jogadas_total,
        "assistencias_total": est_total.assistencias,
        "assistencias_avg": est_total.assistencias / partidas_jogadas_total,
        "defesas_total": est_total.defesas,
        "defesas_avg": est_total.defesas / partidas_jogadas_total,
        "passes_total": est_total.passes,
        "passes_avg": est_total.passes / partidas_jogadas_total,
        "passes_chaves_total": est_total.passes_chaves,
        "passes_chaves_avg": est_total.passes_chaves / partidas_jogadas_total,
        "passes_certos_total": est_total.passes_certos,
        "passes_certos_avg": est_total.passes_certos / partidas_jogadas_total,
        "desarmes_total": est_total.desarmes,
        "desarmes_avg": est_total.desarmes / partidas_jogadas_total,
        "bloqueados_total": est_total.bloqueados,
        "bloqueados_avg": est_total.bloqueados / partidas_jogadas_total,
        "interceptados_total": est_total.interceptados,
        "interceptados_avg": est_total.interceptados / partidas_jogadas_total,
        "duelos_total": est_total.duelos,
        "duelos_avg": est_total.duelos / partidas_jogadas_total,
        "duelos_ganhos_total": est_total.duelos_ganhos,
        "duelos_ganhos_avg": est_total.duelos_ganhos / partidas_jogadas_total,
        "dribles_tentados_total": est_total.dribles_tentados,
        "dribles_tentados_avg": est_total.dribles_tentados / partidas_jogadas_total,
        "dribles_completos_total": est_total.dribles_completos,
        "dribles_completos_avg": est_total.dribles_completos / partidas_jogadas_total,
        "jogadores_passados_total": est_total.jogadores_passados,
        "jogadores_passados_avg": est_total.jogadores_passados / partidas_jogadas_total,
        "faltas_sofridas_total": est_total.faltas_sofridas,
        "faltas_sofridas_avg": est_total.faltas_sofridas / partidas_jogadas_total,
        "faltas_cometidas_total": est_total.faltas_cometidas,
        "faltas_cometidas_avg": est_total.faltas_cometidas / partidas_jogadas_total,
        "cartoes_amarelos_total": est_total.cartoes_amarelos,
        "cartoes_amarelos_avg": est_total.cartoes_amarelos / partidas_jogadas_total,
        "cartoes_vermelhos_total": est_total.cartoes_vermelhos,
        "cartoes_vermelhos_avg": est_total.cartoes_vermelhos / partidas_jogadas_total,
        "penaltis_cometidos_total": est_total.penaltis_cometidos,
        "penaltis_cometidos_avg": est_total.penaltis_cometidos / partidas_jogadas_total,
    }

    estatisticasFormfav = {
        "nota": est_formacao_favorita.nota,
        "impedimentos_total": est_formacao_favorita.impedimentos,
        "impedimentos_avg": est_formacao_favorita.impedimentos / qtd_partidas_formacao_favorita,
        "chutes_total": est_formacao_favorita.chutes,
        "chutes_avg": est_formacao_favorita.chutes / qtd_partidas_formacao_favorita,
        "chutes_no_gol_total": est_formacao_favorita.chutes_no_gol,
        "chutes_no_gol_avg": est_formacao_favorita.chutes_no_gol / qtd_partidas_formacao_favorita,
        "gols_total": est_formacao_favorita.gols,
        "gols_avg": est_formacao_favorita.gols / qtd_partidas_formacao_favorita,
        "gols_sofridos_total": est_formacao_favorita.gols_sofridos,
        "gols_sofridos_avg": est_formacao_favorita.gols_sofridos / qtd_partidas_formacao_favorita,
        "assistencias_total": est_formacao_favorita.assistencias,
        "assistencias_avg": est_formacao_favorita.assistencias / qtd_partidas_formacao_favorita,
        "defesas_total": est_formacao_favorita.defesas,
        "defesas_avg": est_formacao_favorita.defesas / qtd_partidas_formacao_favorita,
        "passes_total": est_formacao_favorita.passes,
        "passes_avg": est_formacao_favorita.passes / qtd_partidas_formacao_favorita,
        "passes_chaves_total": est_formacao_favorita.passes_chaves,
        "passes_chaves_avg": est_formacao_favorita.passes_chaves / qtd_partidas_formacao_favorita,
        "passes_certos_total": est_formacao_favorita.passes_certos,
        "passes_certos_avg": est_formacao_favorita.passes_certos / qtd_partidas_formacao_favorita,
        "desarmes_total": est_formacao_favorita.desarmes,
        "desarmes_avg": est_formacao_favorita.desarmes / qtd_partidas_formacao_favorita,
        "bloqueados_total": est_formacao_favorita.bloqueados,
        "bloqueados_avg": est_formacao_favorita.bloqueados / qtd_partidas_formacao_favorita,
        "interceptados_total": est_formacao_favorita.interceptados,
        "interceptados_avg": est_formacao_favorita.interceptados / qtd_partidas_formacao_favorita,
        "duelos_total": est_formacao_favorita.duelos,
        "duelos_avg": est_formacao_favorita.duelos / qtd_partidas_formacao_favorita,
        "duelos_ganhos_total": est_formacao_favorita.duelos_ganhos,
        "duelos_ganhos_avg": est_formacao_favorita.duelos_ganhos / qtd_partidas_formacao_favorita,
        "dribles_tentados_total": est_formacao_favorita.dribles_tentados,
        "dribles_tentados_avg": est_formacao_favorita.dribles_tentados / qtd_partidas_formacao_favorita,
        "dribles_completos_total": est_formacao_favorita.dribles_completos,
        "dribles_completos_avg": est_formacao_favorita.dribles_completos / qtd_partidas_formacao_favorita,
        "jogadores_passados_total": est_formacao_favorita.jogadores_passados,
        "jogadores_passados_avg": est_formacao_favorita.jogadores_passados / qtd_partidas_formacao_favorita,
        "faltas_sofridas_total": est_formacao_favorita.faltas_sofridas,
        "faltas_sofridas_avg": est_formacao_favorita.faltas_sofridas / qtd_partidas_formacao_favorita,
        "faltas_cometidas_total": est_formacao_favorita.faltas_cometidas,
        "faltas_cometidas_avg": est_formacao_favorita.faltas_cometidas / qtd_partidas_formacao_favorita,
        "cartoes_amarelos_total": est_formacao_favorita.cartoes_amarelos,
        "cartoes_amarelos_avg": est_formacao_favorita.cartoes_amarelos / qtd_partidas_formacao_favorita,
        "cartoes_vermelhos_total": est_formacao_favorita.cartoes_vermelhos,
        "cartoes_vermelhos_avg": est_formacao_favorita.cartoes_vermelhos / qtd_partidas_formacao_favorita,
        "penaltis_cometidos_total": est_formacao_favorita.penaltis_cometidos,
        "penaltis_cometidos_avg": est_formacao_favorita.penaltis_cometidos / qtd_partidas_formacao_favorita,
    }

    estatisticasPosfav = {
        "nota": est_posicao_favorita.nota,
        "impedimentos_total": est_posicao_favorita.impedimentos,
        "impedimentos_avg": est_posicao_favorita.impedimentos / qtd_partidas_pos,
        "chutes_total": est_posicao_favorita.chutes,
        "chutes_avg": est_posicao_favorita.chutes / qtd_partidas_pos,
        "chutes_no_gol_total": est_posicao_favorita.chutes_no_gol,
        "chutes_no_gol_avg": est_posicao_favorita.chutes_no_gol / qtd_partidas_pos,
        "gols_total": est_posicao_favorita.gols,
        "gols_avg": est_posicao_favorita.gols / qtd_partidas_pos,
        "gols_sofridos_total": est_posicao_favorita.gols_sofridos,
        "gols_sofridos_avg": est_posicao_favorita.gols_sofridos / qtd_partidas_pos,
        "assistencias_total": est_posicao_favorita.assistencias,
        "assistencias_avg": est_posicao_favorita.assistencias / qtd_partidas_pos,
        "defesas_total": est_posicao_favorita.defesas,
        "defesas_avg": est_posicao_favorita.defesas / qtd_partidas_pos,
        "passes_total": est_posicao_favorita.passes,
        "passes_avg": est_posicao_favorita.passes / qtd_partidas_pos,
        "passes_chaves_total": est_posicao_favorita.passes_chaves,
        "passes_chaves_avg": est_posicao_favorita.passes_chaves / qtd_partidas_pos,
        "passes_certos_total": est_posicao_favorita.passes_certos,
        "passes_certos_avg": est_posicao_favorita.passes_certos / qtd_partidas_pos,
        "desarmes_total": est_posicao_favorita.desarmes,
        "desarmes_avg": est_posicao_favorita.desarmes / qtd_partidas_pos,
        "bloqueados_total": est_posicao_favorita.bloqueados,
        "bloqueados_avg": est_posicao_favorita.bloqueados / qtd_partidas_pos,
        "interceptados_total": est_posicao_favorita.interceptados,
        "interceptados_avg": est_posicao_favorita.interceptados / qtd_partidas_pos,
        "duelos_total": est_posicao_favorita.duelos,
        "duelos_avg": est_posicao_favorita.duelos / qtd_partidas_pos,
        "duelos_ganhos_total": est_posicao_favorita.duelos_ganhos,
        "duelos_ganhos_avg": est_posicao_favorita.duelos_ganhos / qtd_partidas_pos,
        "dribles_tentados_total": est_posicao_favorita.dribles_tentados,
        "dribles_tentados_avg": est_posicao_favorita.dribles_tentados / qtd_partidas_pos,
        "dribles_completos_total": est_posicao_favorita.dribles_completos,
        "dribles_completos_avg": est_posicao_favorita.dribles_completos / qtd_partidas_pos,
        "jogadores_passados_total": est_posicao_favorita.jogadores_passados,
        "jogadores_passados_avg": est_posicao_favorita.jogadores_passados / qtd_partidas_pos,
        "faltas_sofridas_total": est_posicao_favorita.faltas_sofridas,
        "faltas_sofridas_avg": est_posicao_favorita.faltas_sofridas / qtd_partidas_pos,
        "faltas_cometidas_total": est_posicao_favorita.faltas_cometidas,
        "faltas_cometidas_avg": est_posicao_favorita.faltas_cometidas / qtd_partidas_pos,
        "cartoes_amarelos_total": est_posicao_favorita.cartoes_amarelos,
        "cartoes_amarelos_avg": est_posicao_favorita.cartoes_amarelos / qtd_partidas_pos,
        "cartoes_vermelhos_total": est_posicao_favorita.cartoes_vermelhos,
        "cartoes_vermelhos_avg": est_posicao_favorita.cartoes_vermelhos / qtd_partidas_pos,
        "penaltis_cometidos_total": est_posicao_favorita.penaltis_cometidos,
        "penaltis_cometidos_avg": est_posicao_favorita.penaltis_cometidos / qtd_partidas_pos,
    }

    jogador_info = get_info_jogador(id)

    nome_time = jogador_info.nometime
    nota = estatisticas['nota']
    formacaofav = formacao_favorita
    posicaofav = posicao_favorita
    nome = jogador_info.nome
    imagem = jogador_info.imagem
    nacionalidade = jogador_info.nacionalidade
    lesionado = jogador_info.lesionado
    data_nascimento = jogador_info.data_nascimento
    id_time = jogador_info.id_time
    formacoes = get_formacoes_jogador(id)

    return jsonify({
        "partidas_jogadas": partidas_jogadas_total,
        "formacoes": formacoes,
        "nome": nome,
        "nome_time": nome_time,
        "nota": nota,
        "formacao_favorita": formacaofav,
        "posicao_favorita": posicaofav,
        "estatisticas": estatisticas,
        "estatisticas_formacao_favorita": estatisticasFormfav,
        "estatisticas_posicao_favorita": estatisticasPosfav,
        "id": jogador_info.id,
        "imagem": imagem,
        "nacionalidade": nacionalidade,
        "data_nascimento": data_nascimento,
        "lesionado": lesionado,
        "id_time": id_time,
        "destaques": get_destaques(id)})


@app.route("/teste/form/<id>/<form>", methods=["GET"])
def testeJogadorForm(id, form):

    est_formacao, qtd_partidas = estatisticas_formacao_especifica(id, form)

    jogador_info = get_info_jogador(id)

    estatisticas = {

        "partidas_jogadas": qtd_partidas,
        "nota": est_formacao.nota,
        "impedimentos_total": est_formacao.impedimentos,
        "impedimentos_avg": est_formacao.impedimentos / qtd_partidas,
        "chutes_total": est_formacao.chutes,
        "chutes_avg": est_formacao.chutes / qtd_partidas,
        "chutes_no_gol_total": est_formacao.chutes_no_gol,
        "chutes_no_gol_avg": est_formacao.chutes_no_gol / qtd_partidas,
        "gols_total": est_formacao.gols,
        "gols_avg": est_formacao.gols / qtd_partidas,
        "gols_sofridos_total": est_formacao.gols_sofridos,
        "gols_sofridos_avg": est_formacao.gols_sofridos / qtd_partidas,
        "assistencias_total": est_formacao.assistencias,
        "assistencias_avg": est_formacao.assistencias / qtd_partidas,
        "defesas_total": est_formacao.defesas,
        "defesas_avg": est_formacao.defesas / qtd_partidas,
        "passes_total": est_formacao.passes,
        "passes_avg": est_formacao.passes / qtd_partidas,
        "passes_chaves_total": est_formacao.passes_chaves,
        "passes_chaves_avg": est_formacao.passes_chaves / qtd_partidas,
        "passes_certos_total": est_formacao.passes_certos,
        "passes_certos_avg": est_formacao.passes_certos / qtd_partidas,
        "desarmes_total": est_formacao.desarmes,
        "desarmes_avg": est_formacao.desarmes / qtd_partidas,
        "bloqueados_total": est_formacao.bloqueados,
        "bloqueados_avg": est_formacao.bloqueados / qtd_partidas,
        "interceptados_total": est_formacao.interceptados,
        "interceptados_avg": est_formacao.interceptados / qtd_partidas,
        "duelos_total": est_formacao.duelos,
        "duelos_avg": est_formacao.duelos / qtd_partidas,
        "duelos_ganhos_total": est_formacao.duelos_ganhos,
        "duelos_ganhos_avg": est_formacao.duelos_ganhos / qtd_partidas,
        "dribles_tentados_total": est_formacao.dribles_tentados,
        "dribles_tentados_avg": est_formacao.dribles_tentados / qtd_partidas,
        "dribles_completos_total": est_formacao.dribles_completos,
        "dribles_completos_avg": est_formacao.dribles_completos / qtd_partidas,
        "jogadores_passados_total": est_formacao.jogadores_passados,
        "jogadores_passados_avg": est_formacao.jogadores_passados / qtd_partidas,
        "faltas_sofridas_total": est_formacao.faltas_sofridas,
        "faltas_sofridas_avg": est_formacao.faltas_sofridas / qtd_partidas,
        "faltas_cometidas_total": est_formacao.faltas_cometidas,
        "faltas_cometidas_avg": est_formacao.faltas_cometidas / qtd_partidas,
        "cartoes_amarelos_total": est_formacao.cartoes_amarelos,
        "cartoes_amarelos_avg": est_formacao.cartoes_amarelos / qtd_partidas,
        "cartoes_vermelhos_total": est_formacao.cartoes_vermelhos,
        "cartoes_vermelhos_avg": est_formacao.cartoes_vermelhos / qtd_partidas,
        "penaltis_cometidos_total": est_formacao.penaltis_cometidos,
        "penaltis_cometidos_avg": est_formacao.penaltis_cometidos / qtd_partidas,
    }

    nome_time = jogador_info.nometime
    nota = estatisticas['nota']
    nome = jogador_info.nome

    return jsonify({
        "partidas_jogadas": qtd_partidas,
        "nome": nome,
        "nome_time": nome_time,
        "nota": nota,
        "estatisticas": estatisticas,
        "destaques": get_destaques(id, form)})


@app.route("/teste/pos", methods=["GET"])
def testeJogadorPos():
    estatisticas = {
        "impedimentos_total": 5,
        "impedimentos_avg": 1.2,
        "chutes_total": 30,
        "chutes_avg": 7.5,
        "chutes_no_gol_total": 15,
        "chutes_no_gol_avg": 3.8,
        "gols_total": 8,
        "gols_avg": 2.0,
        "gols_sofridos_total": 6,
        "gols_sofridos_avg": 1.5,
        "assistencias_total": 10,
        "assistencias_avg": 2.5,
        "defesas_total": 12,
        "defesas_avg": 3.0,
        "passes_total": 200,
        "passes_avg": 50.0,
        "passes_chaves_total": 20,
        "passes_chaves_avg": 5.0,
        "passes_certos_total": 180,
        "passes_certos_avg": 45.0,
        "desarmes_total": 25,
        "desarmes_avg": 6.3,
        "bloqueados_total": 8,
        "bloqueados_avg": 2.0,
        "interceptados_total": 12,
        "interceptados_avg": 3.0,
        "duelos_total": 40,
        "duelos_avg": 10.0,
        "duelos_ganhos_total": 25,
        "duelos_ganhos_avg": 6.3,
        "dribles_tentados_total": 18,
        "dribles_tentados_avg": 4.5,
        "dribles_completos_total": 10,
        "dribles_completos_avg": 2.5,
        "jogadores_passados_total": 7,
        "jogadores_passados_avg": 1.8,
        "faltas_sofridas_total": 15,
        "faltas_sofridas_avg": 3.8,
        "faltas_cometidas_total": 10,
        "faltas_cometidas_avg": 2.5,
        "cartoes_amarelos_total": 3,
        "cartoes_amarelos_avg": 0.8,
        "cartoes_vermelhos_total": 1,
        "cartoes_vermelhos_avg": 0.3,
        "penaltis_cometidos_total": 2,
        "penaltis_cometidos_avg": 0.5
    }

    nome_time = "Corinthians"
    nota = 9.7
    nome = "Garro"
    return jsonify({
        "nome": nome,
        "nome_time": nome_time,
        "nota": nota,
        "estatisticas": estatisticas})


@app.route("/teste/pos/<pos>", methods=["GET"])
def get_media_pos(pos):
    stats = get_medias_total_posicao(pos)

    return jsonify(stats.__dict__)


@app.route("/pesquisaavancada/", methods=["GET"])
def get_pesquisa_avancada():
    formatdict = {
        "posicao": request.headers.get('posicao'),
        "formacao": request.headers.get('formacao'),
        "gols": getbool(request.headers.get('gols')),
        "desarmes": getbool(request.headers.get('desarmes')),
        "assistencias": getbool(request.headers.get('assistencias')),
        "passes_certos": getbool(request.headers.get('passes_certos')),
        "passes_chaves": getbool(request.headers.get('passes_chaves')),
        "faltas_sofridas": getbool(request.headers.get('faltas_sofridas')),
        "dribles_completos": getbool(request.headers.get('dribles_completos')),
        "chutes_no_gol": getbool(request.headers.get('chutes_no_gol')),
        "bloqueados": getbool(request.headers.get('bloqueados')),
    }

    result = pesquisa_avancada(formatdict)
    return jsonify({"resultado": result})


@app.route("/ia/", methods=["POST"])
def ia():
    try:
        req = request.get_json()

        time_mandante = req['time_mandante']
        time_visitante = req['time_visitante']
        formacao_mandante = req['formacao_mandante']
        formacao_visitante = req['formacao_visitante']
        condicao = req['condicao']
        momento_dia = req['momento_dia']

        result = prever_resultado(time_mandante, time_visitante,
                                  formacao_mandante, formacao_visitante, condicao, momento_dia)

        return jsonify({'empate': float(result[0]),
                        'mandante': float(result[1]),
                        'visitante': float(result[2])
                        }),200
    except:
        return jsonify(),500
    
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
