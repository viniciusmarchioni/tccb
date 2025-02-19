import mysql.connector
from flask import Flask, jsonify, request
from fetchDBHelper import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
#TODO adicionar jogadores sem formação
@app.route("/jogadores/<id>/<formacao>", methods=["GET"])
def get_jogadores(id,formacao):

    goleiros = []
    defensores = []
    meias = []
    atacantes = []

    formacao_list = formacao.split("-")
    #transforma em uma lista de inteiros
    formacao_list = list(map(int, formacao_list))

    for i in fetch_players_plus(id, formacao, "G", 1):
        goleiros.append({"id":i.id,
                         "nome":i.nome,
                         "imagem":i.imagem,
                         "nacionalidade":i.nacionalidade,
                         "data_nacimento":i.data_nacimento,
                         "lesionado":bool(i.lesionado),
                         "id_time":i.id_time,
                         "estatisticas":{}
                         })
    
    for i in fetch_players_plus(id, formacao, "D", formacao_list[0]):
        estatisticas = media_estatisticas_plus("D",formacao,"duelos_Ganhos","desarmes","bloqueados",minutos=15,idplayer=i.id)
        defensores.append({"id":i.id,
                           "nome":i.nome,
                           "imagem":i.imagem,
                           "nacionalidade":i.nacionalidade,
                           "data_nacimento":i.data_nacimento,
                           "lesionado":bool(i.lesionado),
                           "id_time":i.id_time,
                           "estatisticas":{                               
                             'estatistica1':estatisticas[0],
                             'estatistica2':estatisticas[1],
                             'estatistica3':estatisticas[2]
                           }
                           })

    for i in fetch_players_plus(id, formacao, "M", sum(map(int, formacao_list[1:-1]))):
        estatisticas = media_estatisticas_plus("M",formacao,"passes_certos","assistencias","passes_chaves",minutos=15,idplayer=i.id)
        meias.append({"id":i.id,
                      "nome":i.nome,
                      "imagem":i.imagem,
                      "nacionalidade":i.nacionalidade,
                      "data_nacimento":i.data_nacimento,
                      "lesionado":bool(i.lesionado),
                      "id_time":i.id_time,
                      "estatisticas":{
                        'estatistica1':estatisticas[0],
                        'estatistica2':estatisticas[1],
                        'estatistica3':estatisticas[2]
                      }
                      })

    for i in fetch_players_plus(id, formacao, "F", formacao_list[-1]):
        estatisticas = media_estatisticas_plus("F",formacao,"gols","chutes_no_gol","assistencias",minutos=15,idplayer=i.id)
        atacantes.append({"id":i.id,
                          "nome":i.nome,
                          "imagem":i.imagem,
                          "nacionalidade":i.nacionalidade,
                          "data_nacimento":i.data_nacimento,
                          "lesionado":bool(i.lesionado),
                          "id_time":i.id_time,
                          "estatisticas":{
                            'estatistica1':estatisticas[0],
                            'estatistica2':estatisticas[1],
                            'estatistica3':estatisticas[2]
                          }
                          })
        
    return jsonify([{"goleiros":goleiros},{"defensores":defensores},{"meias":meias},{"atacantes":atacantes}]), 200


@app.route("/jogadores/<id>/", methods=["GET"])
def get_jogadores_sem_formacao(id):

    formacao = get_formations(id)[0]

    goleiros = []
    defensores = []
    meias = []
    atacantes = []

    formacao_list = formacao.split("-")
    #transforma em uma lista de inteiros
    formacao_list = list(map(int, formacao_list))

    for i in fetch_players_plus(id, formacao, "G", 1):
        goleiros.append({"id":i.id,
                         "nome":i.nome,
                         "imagem":i.imagem,
                         "nacionalidade":i.nacionalidade,
                         "data_nacimento":i.data_nacimento,
                         "lesionado":bool(i.lesionado),
                         "id_time":i.id_time,
                         "estatisticas":{}
                         })
    
    for i in fetch_players_plus(id, formacao, "D", formacao_list[0]):
        estatisticas = media_estatisticas_plus("D",formacao,"duelos_Ganhos","desarmes","bloqueados",minutos=15,idplayer=i.id)
        defensores.append({"id":i.id,
                           "nome":i.nome,
                           "imagem":i.imagem,
                           "nacionalidade":i.nacionalidade,
                           "data_nacimento":i.data_nacimento,
                           "lesionado":bool(i.lesionado),
                           "id_time":i.id_time,
                           "estatisticas":{                               
                             'estatistica1':estatisticas[0],
                             'estatistica2':estatisticas[1],
                             'estatistica3':estatisticas[2]
                           }
                           })

    for i in fetch_players_plus(id, formacao, "M", sum(map(int, formacao_list[1:-1]))):
        estatisticas = media_estatisticas_plus("M",formacao,"passes_certos","assistencias","passes_chaves",minutos=15,idplayer=i.id)
        meias.append({"id":i.id,
                      "nome":i.nome,
                      "imagem":i.imagem,
                      "nacionalidade":i.nacionalidade,
                      "data_nacimento":i.data_nacimento,
                      "lesionado":bool(i.lesionado),
                      "id_time":i.id_time,
                      "estatisticas":{
                        'estatistica1':estatisticas[0],
                        'estatistica2':estatisticas[1],
                        'estatistica3':estatisticas[2]
                      }
                      })

    for i in fetch_players_plus(id, formacao, "F", formacao_list[-1]):
        estatisticas = media_estatisticas_plus("F",formacao,"gols","chutes_no_gol","assistencias",minutos=15,idplayer=i.id)
        atacantes.append({"id":i.id,
                          "nome":i.nome,
                          "imagem":i.imagem,
                          "nacionalidade":i.nacionalidade,
                          "data_nacimento":i.data_nacimento,
                          "lesionado":bool(i.lesionado),
                          "id_time":i.id_time,
                          "estatisticas":{
                            'estatistica1':estatisticas[0],
                            'estatistica2':estatisticas[1],
                            'estatistica3':estatisticas[2]
                          }
                          })
        
    return jsonify([{"goleiros":goleiros},{"defensores":defensores},{"meias":meias},{"atacantes":atacantes}]), 200


@app.route("/media/<id>/<formacao>", methods=["GET"])
def get_media_geral(id,formacao):
    media_duelos = media_estatisticas("Duelos_Ganhos","D",formacao,15)
    media_desarmes = media_estatisticas("desarmes","D",formacao,15)
    media_bloqueios = media_estatisticas("bloqueados","D",formacao,15)
    media_passes_certos = media_estatisticas("passes_certos","M",formacao,15)
    media_assistencias = media_estatisticas("assistencias","M",formacao,15)
    media_dribles_completos = media_estatisticas("dribles_completos","M",formacao,15)
    media_gols = media_estatisticas("Gols","F",formacao,15)
    media_chutes_no_gol = media_estatisticas("chutes_no_gol","F",formacao)
    medias = {"duelos":media_duelos,
              "desarmes":media_desarmes,
              "bloqueios":media_bloqueios,
              "passesCertos":media_passes_certos,
              "assistencias":media_assistencias,
              "driblesCompletos":media_dribles_completos,
              "gols":media_gols,
              "chutes_no_gol":media_chutes_no_gol}
    
    return jsonify(medias)

@app.route("/times/<id>", methods=["GET"])
def get_detalhes(id):
    formacoes = get_formations(id)
    #TODO adicionar competições que o clube participa
    return jsonify({"formacoes":formacoes})


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

    return jsonify({"jogadores":jogadores_dict,"times":times_dict})


if __name__ == "__main__":
    app.run(host='localhost', port=5000,debug=True)