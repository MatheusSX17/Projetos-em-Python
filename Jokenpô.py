#Importando a biblioteca de escolha de inteiros
from random import randint
#Importando a biblioteca de tempo
from time import sleep
#Cada item está associado a um número: Pedra = 0, Papel = 1 e Tesoura = 2
print('====== JOKENPÔ ======')
itens = ('Pedra', 'Papel', 'Tesoura')
#Computador escolhe:
computador = randint(0, 2)
#Opções
print('''Suas opçôes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
#Jogador escolhe
jogador = int(input('ESCOLHA!!!:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('='*11)
#Mostrando quais itens o computador e o jogador escolheram
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('='*11)
#Mostrando os resultados a partir de cada escolha
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!!')
    else:
        print('COMPUTADOR VENCEU!!')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('VOCÊ VENCEU!!')
if computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!')
    else:
        print('EMPATE')

