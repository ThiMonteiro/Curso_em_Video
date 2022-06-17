#minha respota
produto = float(input('Qual é o valor do seu produto? R$ '))
print('Seu produto foi adicionado 5% de desconto')
porcentagem = (produto * 5) / 100
soma = produto - porcentagem
print('O produto que custava R${:.2f}, com desconto de 5% vai passar a valer R$ {:.2f} '.format(produto, soma))

#resposta do curso
produto = float(input('Qual é o valor do seu produto? R$'))
print('Seu produto foi adicionado 5% de desconto')
porcentagem = produto - (produto * 5 / 100)
print('O produto que custava R${:.2f}, com desconto de 5% vai passar a valer R$ {:.2f}'.format(produto, porcentagem))