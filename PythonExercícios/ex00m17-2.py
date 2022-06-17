# resposta do curso
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Deseja continuar: [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

print('-='*50)

# minha resposta (com ajuda do curso)
valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opçao == 'N':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')
print('Fim do programa')