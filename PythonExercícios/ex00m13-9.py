# resposta do curso
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

print('-='*20)


# minha resposta
from datetime import date
atual = date.today().year
soma = 0
cont = 0
for c in range (1,8):
    nasci = int(input('Qual a sua data de nascimento da {}º pessoa? '.format(c)))
    idade = atual - nasci
    if idade >= 21:
        print('Sua idade é {}'.format(idade))
        print('Você ATINGIU a maior idade')
        soma += 1
    else:
        print('Sua idade é {}'.format(idade))
        print('Você NÂO atingiu a maior idade')
        cont += 1
    print('-='*20)
print('Somente {} atigiram a maioridadade.'.format(soma))
print('Somente {} ainda está na menor idade'.format(cont))

print('-='*20)

from datetime import date
data = date.today().year
totmenor = 0
totmaior = 0
for pess in range (1,8):
    nome = str(input('Qual é o seu nome? '))
    ano = int(input('Em que ano você nasceu? '))
    idade = data - ano
    print('-'*20)
    if idade < 21:
        totmenor += 1
    if idade >= 21:
        totmaior += 1
print('Temos {} maiores de idade e {} menores de idade'.format(totmaior, totmenor))
print('-'*20)