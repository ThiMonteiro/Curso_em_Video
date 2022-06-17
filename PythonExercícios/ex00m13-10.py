# resposta do curso
maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1: # SE a primeiro pessoa (P == 1) tiver o maior peso (Maior = peso) e menor peso (Menor == peso)
        maior = peso
        menor = peso
    else:
        if peso > maior: # SE o peso da primeira pessoa for menor do que a segunda, esse passa ser o mais pesado
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))


print('-='*20)


# minha resposta
soma = 0
cont = 0
for pess in range (1, 6):
    peso = float(input('Informe o peso da {}º pessoa:Kg '.format(pess)))
    if peso <= 65:
        print('Seu peso ESTÁ BOM')
        soma = soma + 1
    else:
        print('Seu peso NÃO ESTÁ BOM')
        cont = cont + 1
    print('-'*20)
print('Somente {} pessoas estão com peso BOM'.format(soma))
print('Somente {} pessoas estão com peso RUIM'.format(cont))

