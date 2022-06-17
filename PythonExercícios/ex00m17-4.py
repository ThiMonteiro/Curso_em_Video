# resposta do curso
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')


print('-'*40)



# minha resposta
lista = []
cont_num = 0
while True:
    num = int(input('Digite um valor: '))
    cont_num += 1
    lista.append(num)
    opçao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opçao == 'N':
        break
print('='*50)
print(f'Você digitou {cont_num} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
