# resposta do curso
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

print('-'*20)

# minha resposta ( com ajuda do curso)
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

print('-='*20)

# treinando
impar = 0 # contador
contimpar = 0 # somador
for cont in range (1, 501, 2):
    print(cont, end=' ')
    if cont % 3 == 0:
        impar += 1
        contimpar += cont
print('\nVocê informou {} impares e a soma foi entre eles foi {}'.format(impar, contimpar))
