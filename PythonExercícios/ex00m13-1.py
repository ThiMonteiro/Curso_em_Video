# resposta do curso
from time import sleep
for cont in range (10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOW!')

print('-'*30)

# minha resposta
print('''SIM - *PERMISSÂO CONCEDIDA*
NÃO - *PERMISSÂO NÂO CONCEDIDA*''')
permissão = str(input('PERMISSÃO DA CONTAGEM: ')).upper()
print('-='*20)
from time import sleep
for c in range (5, -1, -1):
    if permissão == 'SIM':
        print(c)
        sleep(1)
if permissão == 'SIM':
    print('BOOOOMMMMM!!!! POWWW!!! CABUMMM!!')
else:
    print('PERMISSÃO NÃO AUTORIZADA')

print('-'*30)

# treinando
from time import sleep
permissao = str(input('PERMISSÃO PARA CONTAGEM: [S/N] ')).upper().strip()[0]
for contagem in range (5, -1, -1):
    if permissao == 'S':
        print(contagem)
        sleep(1)
if permissao == 'S':
    print('BUMMM !! CABUUMMM')
else:
    print('OPERAÇÃO ENCERRADA...')