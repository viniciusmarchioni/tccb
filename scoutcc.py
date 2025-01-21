from fetchDBHelper import *

times = fetch_teams(True)
'''
print("Selecione o time:")
for i in range(len(times)):
    print(f"{i+1}- {times[i]}")
'''
#escolha = int(input())
escolha = 6
id_time = get_id(times[escolha-1])
formacoes = get_formations(id_time)
'''
print("Escolha a formação:")
for i in range(len(formacoes)):
    print(f"{i+1}- {formacoes[i]}")

escolha = int(input())
'''
escolha = 5
formacao = formacoes[escolha-1]
formacao_list = formacao.split("-")

print("Goleiro:")
goleiro_time = fetch_players(id_time,formacao,"G",1)
print(goleiro_time)



print("Zagueiros:")
zagueiros_time = fetch_players(id_time,formacao,"D",formacao_list[0])
media_duelos_time = []
media_duelos = media_estatisticas("Duelos_Ganhos","D",formacao)
for i in zagueiros_time:
    media_duelos_time.append(media_estatisticas("Duelos_Ganhos","D",formacao,0,i.id))
print(zagueiros_time)




print("Meias:")
meias_time = fetch_players(id_time,formacao,"M",sum(map(int, formacao_list[1:-1])))
media_passes_time = []
media_passes = media_estatisticas("Passes_Certos","M",formacao)
for i in meias_time:
    media_passes_time.append(media_estatisticas("Passes_Certos","M",formacao,0,i.id))
print(meias_time)





print("Atacantes:")
atacantes_time = fetch_players(id_time,formacao,"F", formacao_list[-1])
media_gols_time = []
media_gols = media_estatisticas("Gols","F",formacao)
for i in atacantes_time:
    media_gols_time.append(media_estatisticas("Gols","F",formacao,0,i.id))
print(atacantes_time)


#Relatório

def comparacao_media(jogadores_posicao,medias_time,media_geral,estatistica:str):
    for i in range(len(medias_time)):
        if(medias_time[i]>=media_geral):
            print("{} obteve uma média de {} nessa formação maior que a média geral dos jogadores da série A. {:.2f}/partida".format(jogadores_posicao[i],estatistica,medias_time[i]))

comparacao_media(zagueiros_time,media_duelos_time,media_duelos,"duelos ganhos")
comparacao_media(meias_time,media_passes_time,media_passes,"passes certos")
comparacao_media(atacantes_time,media_gols_time,media_gols,"gols")

gols_sofridos_casa,gols_sofridos_fora = avg_team_goals_conceded(id_time,formacao)
print("O time na formação {} obteve média de {:.2f} gols sofridos em casa e {:.2f} gols sofridos fora de casa.".format(formacao, gols_sofridos_casa, gols_sofridos_fora))

gols_marcados_casa,gols_marcados_fora = avg_team_goals_conceded(id_time,formacao)
print("O time na formação {} obteve média de {:.2f} gols em casa e {:.2f} gols fora de casa.".format(formacao, gols_marcados_casa, gols_marcados_fora))

#Relatório Contrapontos
print("===================Contrapontos===================")
media_gols_sofridos = avg_goals_conceded(formacao)
if(gols_sofridos_casa>media_gols_sofridos):
    print("Na {} em casa; o time sofreu mais gols que a média na mesma formação. Média:{:.2f}".format(formacao,media_gols_sofridos))
if(gols_sofridos_fora>media_gols_sofridos):
    print("Na {} fora de casa; o time sofreu mais gols que a média na mesma formação. Média:{:.2f}".format(formacao,media_gols_sofridos))

media_cartao_amarelo = avg_geral_stats("Cartoes_amarelos",formacao)
media_time_cartao_amarelo = avg_team_stats(id_time,"Cartoes_amarelos",formacao)
if(media_time_cartao_amarelo > media_cartao_amarelo):
    print("Na {}, o time recebe uma média maior de cartões amarelos do que outros times na mesma formação. Média:{:.2f} Geral:{:.2f}".format(formacao,media_time_cartao_amarelo,media_cartao_amarelo))

