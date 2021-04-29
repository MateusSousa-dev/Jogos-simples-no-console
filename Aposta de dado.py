import random
import sys

def goto(linenum):
    global line
    line = linenum
i = print('Bem vindo ao Cassino')
line = 9
while True:
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    la = 1
    lb = 2
    lc = 3
    hd = 4
    he = 5
    hf = 6
    r = [a, b, c, d, e, f]
    n = random.choice(r)
    player = str(input('Qual será sua aposta? (Digite info para mais informações )')).strip().lower()
    if player == 'info':
        print('Modos de aposta são:\nUm número de 1 a 6 para aposta no número\nl para os números 1, 2 e 3\nh para os números 4, 5 e 6\nexit para sair')
        goto(9)
    elif player == 'h':
        if n == hd:
            print('PARABÉNS! Você acertou o número escolhido!\nO número escolhido foi {}'.format(n))
            goto(9)
        elif n == he:
            print('PARABÉNS! Você acertou o número escolhido!\nO número escolhido foi {}'.format(n))
            goto(9)
        elif n == hf:
          print('PARABÉNS! Você acertou o número escolhido!\nO número escolhido foi {}'.format(n))
          goto(9)
        else:
            print('Você errou! O número foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    elif player == 'l':
        if n == la:
             print('PARABÉNS! Você acertou o número escolhido!\nO número escolhido foi {}'.format(n))
             goto(9)
        elif n == lb:
            print('PARABÉNS! Você acertou o número escolhido!\nO número escolhido foi {}'.format(n))
            goto(9)
        elif n == lc:
            print('PARABÉNS! Você acertou o número escolhido!\nO número escolhido foi {}'.format(n))
            goto(9)
        else:
            print('Você errou! O número escolhido foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    elif player == 'exit':
        sys.exit()
    elif player == '1':
        if a == n:
            print('PARABÉNS! Você acertou o número escolhido!')
            goto(9)
        else:
            print('Você errou! O número escolhido foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    elif player == '2':
        if b == n:
            print('PARABÉNS! Você acertou o número escolhido!')
            goto(9)
        else:
            print('Você errou! O número escolhido foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    elif player == '3':
        if c == n:
            print('PARABÉNS! Você acertou o número escolhido!')
            goto(9)
        else:
            print('Você errou! O número escolhido foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    elif player == '4':
        if d == n:
            print('PARABÉNS! Você acertou o número escolhido!')
            goto(9)
        else:
            print('Você errou! O número escolhido foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    elif player == '5':
        if e == n:
            print('PARABÉNS! Você acertou o número escolhido!')
            goto(9)
        else:
            print('Você errou! O número escolhido foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    elif player == '6':
        if f == n:
            print('PARABÉNS! Você acertou o número escolhido!')
            goto(9)
        else:
            print('Você errou! O número escolhido foi {}\nDesejo mais sorte da próxima vez!'.format(n))
            goto(9)
    else:
        print('Desculpe, valor não indentificado!')
        goto(9)
