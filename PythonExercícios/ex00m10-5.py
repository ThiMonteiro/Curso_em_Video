# resposta do curso (analisando o ano do computador e usando datetime)
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

print('-=-'*20)

# resposta do curso (forma mais simples de fazer)
ano = int(input('\033[36mQue ano quer analisar?\033[36m '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano {} é BISSEXTO\033[m'.format(ano))
else:
    print('\033[31mO ano {} NÃO é BISSEXTO\033[m'.format(ano))
print('-=-'*20)

# minha resposta (treinando)
ano = int(input('Que ano deseja analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))

# treinando
ano = int(input('Qual ano deseja ver? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))