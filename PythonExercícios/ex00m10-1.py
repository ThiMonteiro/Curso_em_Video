# resposta do curso
from random import randint
from time import sleep
computador = randint(0, 5)# faz o computador "PENSAR"
print('\033[31m-=-\033[m'*20)
print('\033[36mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[31m-=-\033[m'*20)
jogador = int(input('\033[34mEm que número eu pensei?\033[m')) # Jogador tenta adivinhar
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGanhei! Eu pensei no número {} e não no {}!\033[m'.format(computador, jogador))

print('\033[31m-=-\033[m'*20)

# minha resposta ("treinando")
import random
computador = random.randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
if jogador == computador: # os dois sinais (= =) é para falar, exemplo: "Se o jogador pensou igual o computador
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))

print('-'*20)

# treinando
import random
print('Vou pensar em um numero entre 0 e 5..')
pc = random.randint(0, 5)
pessoa = int(input('Entre 0 e 5, Qual o numero pensado? '))
if pessoa == pc:
    print('PARABÉNS!!!')
    print('Você conseguiu me vencer!!')
else:
    print('GANHEI!!!')
    print('Eu pensei no número {} e não no {}.'.format(pc, pessoa))
