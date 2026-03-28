#Importando a biblioteca de escolha:
from random import randint
#Computador sorteia um número de 0 a 10:
computador = randint(0, 10)
#Computador informa ao usuário que escolheu um número:
print('''Sou seu computador. Acabei de pensar em um número de 0 a 10''')
#Criando uma variável que dirá se o usuário acertou o número ou não:
acertou = False
#Criando um contador para contar o número de tentativas do usuário:
cont = 0
#Estrutura de repetição que acontecerá enquanto o usuário não acerta:
while not acertou:
#Usuário dá o palpite:
    j = int(input('Qual o seu palpite?'))
#Esse palpite é salvo na variável "cont"
    cont += 1
#Se o usuário acertar, o computador indica o resultado:
    if j == computador:
        acertou = True
#Se o usuário errar, o computador diz se o resultado é maior ou menor que o número dito pelo usuário
    elif j < computador:
        print('Mais... Tenta de novo')
    elif j > computador:
        print('Menos... Tenta de novo')
#O computador diz com quantas tentativas o usuário acertou
print('Acertou com {} tentativas'.format(cont))

















