# resposta do curso
listanum = []
mai = 0
men = 0
for c in range (0, 5):
    listanum.append(int(input(f'Me diga um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} nas posições ',end='')
for i, v in enumerate (listanum):
    if v == men:
        print(f'{i}...', end=' ')
print()


print('-='*50)


# minha resposta (comm ajuda do curso)
valores = []
mai = 0
men = 0
for cont in range (0, 5):
    valores.append(int(input(f'Me diga um valor para a posição {cont}: ')))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]
print('='*50)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()