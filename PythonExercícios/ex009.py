salario = float(input('Quanto o seu funcionário recebe? R$'))
print('Esse mês seu funcionário teve um aumento de um reajuste de 15%')
aumento = (salario * 15) / 100
soma = salario + aumento
print('O seu funcionário que recebia R$ {} de salário, vai passar a receber com reajuste um valor de R$ {}'.format(salario, soma))