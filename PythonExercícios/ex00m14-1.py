# resposta do curso
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # ele vai tirar todos os espaços, e jogar tudo para maisculo, pegando somente a primeira letra.
while sexo not in 'MmFf': # Enquanto (While) não estiver (not) em (in) M ou F
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0] # ele vai tirar todos os espaços, e jogar tudo para maisculo, pegando somente a primeira letra.
print('Sexo {} registrado com sucesso'.format(sexo))

print('-'*20)

# minha resposta (treinando)
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

print('-'*20)

# minha resposta com FOR
for s in range (4):
    sexo = str(input('Qual é o seu sexo? [M/F] ')).upper()
    if sexo == 'M':
        print('Sexo: Masculino')
    elif sexo == 'F':
        print('Sexo: Feminino')
    else:
        print('Resposta Invalida')
print('Fim')