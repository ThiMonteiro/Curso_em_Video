'''from time import sleep
fim = 5 # número interações, onde vai acabar as interações
cont = 0 # varialvel de controle, onde vai começar a contagem
while cont < 5: # Enquanto (While) cont (0) for menor (<) que fim (5)
    print('Faz alguma coisa....')
    sleep(1)
    cont = cont + 1'''

# resposta do curso
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e soma entre eles foi {}'.format(cont, soma))

print('-='*20)

# minha resposta treinando
num = 0 # variavel de controle
cont = 0 # contador
soma = 0 # essa vai ser a variavel de soma
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))