# resposta do curso
num = int(input('Digite um número para ver sua tabuada: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

print('-='*20)

# minha resposta
num = int(input('Digite um número: '))
for cont in range (1, 11):
    soma = cont * num
    print('{} x {} = {} '.format(cont, num, soma))

print('-=' * 20)
#treinando
num = int(input('Digite um valor para ver sua tabuada: '))
for tab in range (1, 11):
    print('{} x {} = {}'.format(tab, num, num*tab))