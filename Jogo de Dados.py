#Importando a biblioteca de sorteio de um número inteiro
from random import randint
#Importando a função que mostrará o resultado após um certo tempo
from time import sleep
#Importando a ferramenta que organizará meu ranking
from operator import itemgetter
#Sorteando o dado de cada jogador
jogo = {'Jogador 1': randint(1,6)
        ,'Jogador 2': randint(1,6)
        ,'Jogador 3': randint(1,6)
        ,'Jogador 4': randint(1,6)}
#Montando meu ranking
ranking = dict()
#Cada jogador (k) tirou um valor (v) no jogo
for k, v in jogo.items():
    #Escrevendo cada resultado:
    print(f' O {k} tirou {v}')
    #Um segundo para montar o ranking
    sleep(1)
    #‘Ranking’ montado em ordem decrescente pelo número retirado
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
