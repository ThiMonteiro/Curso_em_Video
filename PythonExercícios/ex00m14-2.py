# resposta do curso
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False # Caso ainda o jogador não tiver acertado ele recebe FALSE (Falso)
palpites = 0 # esse "Palpites" vai fazer a contagem
while not acertou: # Enquanto (While) não (not) acertou
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1 # Toda vez que você dar um palpite ele vai contar com +1
    if jogador == computador: # Se (if) o jogador for igual (= =) ao computador
        acertou = True # ele vai receber True (Verdadeiro)
    else:
        if jogador < computador: # Se (if) o jogador pensou em um numero menor ( < ) que o computador
            print('Mais... Tente mais um vez.') # ele vai dizer isso
        elif jogador > computador: # Se (if) o jogador pensou em um numero maior ( > ) que o computador
            print('Menos... Tente mais uma vez.') # ele vai dizer isso
print('Acertou com {} tentativas. Parabéns'.format(palpites))

print('-'*20)

# minha resposta
count = 0
import random
computador = random.randint(0, 10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
while jogador != computador: # Enquanto (While) o jogador não for diferente (! =) do computador
    jogador = int(input('Tente novamente. Digite um número: '))
    count = count + 1
print('O computador pensou no numero {}'.format(computador))
print('Parabens!! Você jogou {} vezes para acertar.'.format(count))