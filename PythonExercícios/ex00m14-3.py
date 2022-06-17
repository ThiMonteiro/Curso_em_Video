# resposta do curso
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Primeiro valor: '))
opção = 0 # Isso no While é um ponto de partida, como se fosse no Range
while opção != 5: # Enquanto (While) opção não diferente ( ! = ) de 5, o programa vai funcionar
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto =  n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*20)
    sleep(1)
print('Fim do programa! Volte sempre!')

print('-'*20)

# minha resposta (treinando)
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
opção = 0
while opção != 5:
    print('[ 1 ] SOMA')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    opção = int(input('Qual opção você deseja? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} e {} foi: {}'.format(num1, num2, soma))
    elif opção == 2:
        multiplicar = num1 * num2
        print('A multiplicação entre {} e {} foi: {}'.format(num1, num2, multiplicar))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        elif num1 < num2:
            maior = num2
        print('Entre {} e {} o maior valor digitado foi: {}'.format(num1, num2, maior))
    elif opção == 4:
        print('Ok! Coloque os novos números')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite um valor: '))
    elif opção == 5:
        print('Finalizando....')
    print('-='*20)
print('Volte sempre! = )')