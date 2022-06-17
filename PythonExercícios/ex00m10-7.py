# resposta do curso
salário = float(input('\033[33mQual é o salário do funcionário? R$\033[m '))
if salário <=1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('\033[32mQuem ganhava R${:.2f} passa a ganhar R$ {:.2f} agora.\033[m'.format(salário, novo))

print('-=-'*20)

# minha resposta
salário = float(input('Qual é o seu salário: '))
n15 = (salário * 15) / 100
s15 = salário + n15
n10 = (salário * 10) / 100
s10 = salário + n10
if salário >= 1250 :
    print('Meus PARABÉNS!!')
    print('Você acaba de ter um aumento de 10%!!')
    print('Seu salário agora é R${:.2f}'.format(s10))
else:
    print('Meus PARABÉNS!!')
    print('Você acaba de ter um aumento de 15%!!')
    print('Seu salário agora é R${:.2f}'.format(s15))

print('-=-'*20)

# treinando
salario = float(input('Qual é seu salário atual? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f}, passa a ganhar R$ {:.2f} agora.'.format(salario, novo))