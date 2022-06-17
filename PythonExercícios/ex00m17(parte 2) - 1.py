# resposta do curso
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {mai} Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {men} Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
print()


print('='*50)

# minha resposta (com ajuda do curso)

temp = [] # Eu vou ter uma lista temporaria
princ = [] # E vou ter uma lista principal
mai = men = 0
while True:
    temp.append(str(input('Nome: '))) # Vou jogar o nome para a lista temporaria
    temp.append(float(input('Peso: '))) # Vou jogar o pesoa para a lista temporaria
    if len(princ) == 0: # SE (if) eu não cadastrei ninguem ainda quer dizer que...
        mai = men = temp[1] # ele é "maior" e "menor" até agora
    else: # SENÃO (Else) for o primeiro
        if temp[1] > mai: # SE (if) o temp [1] (Peso) for maior do que o maior atual, ele passa ser o maior
            mai = temp[1]
        if temp[1] < men: #Se (if) o temp [1] (Peso) for menor do que o menor atual, ele passa ser o menor
            men = temp[1]
    princ.append(temp[:]) # Vou fazer uma copia da lista temporaria para a principal
    temp.clear() # depois de ter feito a copia da lista temporaria, vou jogar para principal
    opçao = str(input('Quer continuar? [S/N] '))
    if opçao.upper() == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} Kg. Peso de ',end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {men} Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
print()

