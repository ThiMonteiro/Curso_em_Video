# resposta do curso
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')

print('-='*50)

# minha resposta com ajuda do curso
print('='*50)
print('CADASTRE UMA PESSOA AQUI')
print('='*50)
cont_idade = 0
cont_homem = 0
cont_mulheres_com_menos_de_vinte = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
            cont_mulheres_com_menos_de_vinte += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-'*20)
    if opção == 'N':
            break
print(f'Total de pessoas com mais de 18: {cont_idade}')
print(f'Ao todo temos {cont_homem} homens cadastrados')
print(f'E temos {cont_mulheres_com_menos_de_vinte} mulheres com menos de 20 anos')
