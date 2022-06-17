# resposta do curso
print('{:=^40}'.format(' Lojas Guanabara '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcela em {}x de R${:.2f} COM JUROS'.format(totparcela, parcela))
else:
    total = preço
    print('OPÇÂO INVÁLIDA de pagamento. Tente Novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))

print('-='*20)

# minha resposta
num = float(input('Informe o valor do produto: R$ '))
print('[ 1 ] À Vista (dinheiro/cheque)')
print('[ 2 ] À Vista (cartão)')
print('[ 3 ] 2x no cartão, sem juros')
print('[ 4 ] 3x no cartão, com juros 20%')
select = int(input('Digite a forma de pagamento: '))
if select == 1:
    cal1 = num - (num * 10 / 100)
    print('O seu produto que custava R$ {:.2f}, agora com 10% desconto vai custar R$ {:.2f}'.format(num, cal1))
elif select == 2:
    cal1 = num - (num * 5 / 100)
    print('O seu produto que custava R$ {:.2f}, agora com 5% de desconto vai custar R$ {:.2f}'.format(num, cal1))
elif select == 3:
    cal1 = num / 2
    print('O seu produto que custava R$ {:.2f}, em 2x vezes no cartão vai custar R$ {:.2f}'.format(num, cal1))
elif select == 4:
    cal1 = num + (num * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = cal1 + totparcela
    print('O seu produto que custava R$ {:.2f}, em 3x vezes no cartão vai custar R$ {:.2f}'.format(num, cal1))
else:
    select = num
    print('OPÇÃO INVÁLIDA')