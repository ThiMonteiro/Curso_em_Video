# resposta do curso
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end ='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

print('-='*20)

# minha resposta
casa = float(input('Qual é o valor do imóvel? R$ '))
salario = float(input('Quanto você recebe? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
parcelas = casa / (anos * 12)
limite = salario * 30 / 100
print('Anlisando....')
if parcelas <= salario*(30/100):
    print('PARABÉNS!! Seu empréstimo foi APROVADO!!')
    print('Valor do imóvel: R${:.2f}.'.format(casa))
    print('Valor das parcelas: R$ {:.2f}'.format(parcelas))
else:
    print('Seu empréstimo NÂO FOI APROVADO!!')
    print('Valor do imóvel R$ {:.2f}'.format(casa))
    print('Valor da parcelas R${:.2f}'.format(parcelas))
