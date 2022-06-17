# resposta do curso
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valoress são IGUAIS')

print('-='*20)

# minha reposta
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2: # > Maior
    print('O PRIMEIRO ({}) é maior que o SEGUNDO ({})'.format(n1, n2))
elif n2 > n1: # > Maior
    print('O SEGUNDO ({}) é maior que o PRIMEIRO ({})'.format(n2, n1))
else:
    print('NÂO EXISTE VALOR MAIOR!')
    print('O PRIMEIRO VALOR ({}) e o SEGUNDO ({}) são iguais.'.format(n1, n2))

print('-----FINALIZADO-----')