#Informando o usuário sobre o programa
print('Digite um número e mostrarei a tabuada deste. Digite um valor negativo para sair.')
#Criando uma estrutura de repetição que mostrará a tabuada dos números digitados
while True:
    #Esperando o usuário informar um número
    num = int(input('Digite um número:'))
    #Se o número for negativo, o programa para.
    if num < 0:
        break
    #Escrevendo a tabuada do número informado de 1 a 10
    for c in range(1, 11):
        print(f'{num} X {c} = {num*c}')

