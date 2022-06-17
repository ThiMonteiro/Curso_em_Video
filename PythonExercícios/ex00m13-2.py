# resposta do curso (fazendo divisão)
for n in range (1,51):
    if n % 2 == 0:
        print(n, end = ' ')
print('Acabou')

print('-'*20)

# resposta do curso (mais complexa)
for n in range (2, 51, 2):
    print(n, end = ' ')
print('Acabou')

print('-'*20)

# minha resposta
for c in range (0, 51, 2):
    print(c, end = ' ')
print('NUMEROS PARES')

print('-'*20)

# treinando
par = 0 # contador
impar = 0 # contador
i = int(input('Inicio: '))
f = int(input('Fim: '))
for cont in range(i, f+1):
    print(cont, end=' ')
    if cont % 2 == 0:
        par = par + 1
    if cont % 2 != 0:
        impar = impar + 1
print('\nVocê informou {} pares e {} impares'.format(par, impar))


