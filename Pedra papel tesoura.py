from sys import exit
from random import choice

def goto(linenum):
    global line
    line = linenum

cores = {'titulo':'\33[7m',
         'limpo':'\33[m',
         'vermelho':'\33[7;31m',
         'amarelo':'\33[7;33m',
         'verde':'\33[7;32m'}

line = 0

while True:
    if line == 0:
        print('-='*20)
        print('{}Vamos jogar "Pedra, Papel e Tesoura"!{}'.format(cores['titulo'], cores['limpo']))
        print('-='*20,'\n')
        goto(1)
    elif line == 1:
        pedra = 'Pedra'
        papel = 'Papel'
        tesoura = 'Tesoura'
        lista = [pedra, papel, tesoura]
        print('Para escolher Pedra digite "pedra" ou "1"')
        print('Para escolher Papel digite "papel" ou "2"')
        print('Para escolher Tesousa digite "tesoura ou "3"\n')
        goto(2)
    elif line == 2:
        computer = choice(lista)
        jogador = str(input('Qual será a sua escolha? ')).strip().lower()
        goto(3)
    elif line == 3:
        checkjogador = jogador.isnumeric()
        if checkjogador == True:
            numjogador = int(jogador)
            if numjogador <= 3:
                goto(5)
            else:
                print('{}Erro! Comando não encontrado!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
        else:
            if jogador == 'pedra':
                goto(4)
            elif jogador == 'papel':
                goto(4)
            elif jogador == 'tesoura':
                goto(4)
            elif jogador == 'exit':
                exit()
            else:
                print('{}Erro! Comando não encontrado!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
    elif line == 4:
        if jogador == 'pedra':
            if computer == pedra:
                print('{}Eu também escolhi Pedra, então tivemos um empate!{}\n'.format(cores['amarelo'], cores['limpo']))
                goto(2)
            elif computer == papel:
                print('{}Eu escolhi Papel, então eu ganhei!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
            elif computer == tesoura:
                print('{}Eu escolhi Tesoura, então você ganhou!{}\n'.format(cores['verde'],cores['limpo']))
                goto(2)
            else:
                exit()
        elif jogador == 'papel':
            if computer == pedra:
                print('{}Eu escolhi Pedra, então você ganhou!{}\n'.format(cores['verde'],cores['limpo']))
                goto(2)
            elif computer == papel:
                print('{}Eu também escolhi papel, então tivemos um empate!{}\n'.format(cores['amarelo'], cores['limpo']))
                goto(2)
            elif computer == tesoura:
                print('{}Eu escolhi Tesoura, então eu ganhei!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
            else:
                exit()
        elif jogador == 'tesoura':
            if computer == pedra:
                print('{}Eu escolhi Pedra, então eu ganhei!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
            elif computer == papel:
                print('{}Eu escolhi Papel, então você ganhou!{}\n'.format(cores['verde'],cores['limpo']))
                goto(2)
            elif computer == tesoura:
                print('{}Eu também escolhi Tesoura, então tivemos um empate!{}\n'.format(cores['amarelo'], cores['limpo']))
                goto(2)
            else:
                exit()
    elif line == 5:
        if numjogador == 1:
            if computer == pedra:
                print('{}Eu também escolhi Pedra, então tivemos um empate!{}\n'.format(cores['amarelo'], cores['limpo']))
                goto(2)
            elif computer == papel:
                print('{}Eu escolhi Papel, então eu ganhei!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
            elif computer == tesoura:
                print('{}Eu escolhi Tesoura, então você ganhou!{}\n'.format(cores['verde'],cores['limpo']))
                goto(2)
            else:
                exit()
        elif numjogador == 2:
            if computer == pedra:
                print('{}Eu escolhi Pedra, então você ganhou!{}\n'.format(cores['verde'],cores['limpo']))
                goto(2)
            elif computer == papel:
                print('{}Eu também escolhi papel, então tivemos um empate!{}\n'.format(cores['amarelo'], cores['limpo']))
                goto(2)
            elif computer == tesoura:
                print('{}Eu escolhi Tesoura, então eu ganhei!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
        elif numjogador == 3:
            if computer == pedra:
                print('{}Eu escolhi Pedra, então eu ganhei!{}\n'.format(cores['vermelho'], cores['limpo']))
                goto(2)
            elif computer == papel:
                print('{}Eu escolhi Papel, então você ganhou!{}\n'.format(cores['verde'],cores['limpo']))
                goto(2)
            elif computer == tesoura:
                print('{}Eu também escolhi Tesoura, então tivemos um empate!{}\n'.format(cores['amarelo'], cores['limpo']))
                goto(2)
            else:
                exit()
        else:
            exit()
    else:
        exit()