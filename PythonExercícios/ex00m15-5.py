# resposta do curso
total = totmil = menor = cont= 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()[0]
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço >= 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor= preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    print('-='*20)
    if resp == 'N':
        break
print('{:-^40}'.format(' FINALIZADO '))
print(f'O total da compra foi {total}')
print(f'Temos {totmil} custando mais de R$ 1000,00 ')
print(f'O produto mais barato foi {barato} que custa R${menor}')

print('-='*20)

# minha resposta com ajudo do curso
total = 0
totmil = 0
menor = 0
cont= 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()[0]
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço >= 1000:
        totmil += 1
    if cont == 1:
        menor= preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    print('-='*20)
    if resp == 'N':
        break
print('{:-^40}'.format(' FINALIZADO '))
print(f'O total da compra foi {total}')
print(f'Temos {totmil} custando mais de R$ 1000,00 ')
print(f'O produto mais barato foi {barato} que custa R${menor}')