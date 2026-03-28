#Importando a biblioteca de data atual:
from datetime import date
#Criando uma variável que vai somar todos os anos de trabalho:
soma = 0
#Criando um dicionário que guardará todas as informações do trabalhador
cadastro = dict()
#Requerindo dados:
cadastro['Nome'] = str(input('Nome do trabalhador(a):'))
cadastro['Ano'] = int(input('Ano de nascimento:'))
cadastro['Idade'] = date.today().year - cadastro['Ano']
cadastro['CTPS'] = int(input('Digite a quantidade de empregos que você já teve:'))
#Criando uma estrutura de repetição que coletará informações de cada experiência profissional a partir de uma condição:
if cadastro['CTPS'] != 0:
    for v in range(0 , cadastro['CTPS']):
        #Requerindo dados:
        print('Complete as informações abaixo de acordo com cada emprego:')
        cadastro['Contratação'] = int(input('Ano de contratação:'))
        cadastro['Salário'] = float(input('Qual o salário?:'))
        soma += date.today().year - cadastro['Contratação']
        #Calculando quando o trabalhador vai ser aposentar com base no tempo de serviços prestados
        if soma < 30:
            print(f'Você vai se aposentar com {(30 - soma) + cadastro['Idade']} anos de idade.')
        elif soma > 30:
            print(f'Você deveria ter se aposentado com {cadastro['Idade'] - (soma - 30)} anos de idade.')
        else:
            print('Você pode se aposentar agora.')

