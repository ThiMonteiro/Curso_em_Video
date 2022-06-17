# resposta do curso
núm = [[], []] # dentro dessa lista eu estou declarando uma lista para numeros PARES[0] e a outra para ÍMPARES[1]
valor = 0 # vou declaror a varialvel valor
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0: # SE (If) esse valor for PAR, vai adicionar o numero na posição [0]
        núm[0].append(valor)
    else:# SENÃO (Else) esse valor for ÍMPAR, vai adicionar o numero na posição [1]
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')


print('='*50)


# minha resposta
temp = []
for cont in range(1,8):
    temp.append(int(input(f'Digite o {cont}º valor: ')))
    temp.sort()
print('-='*30)
print(f'Os valores digitados foram: {temp}')
print('Os valores PARES digitados foram: ', end='')
for p in temp:
    if p % 2 == 0:
        print(f'{p}', end=' ')
print()
print('Os valores IMPARES digitados foram: ',end='')
for i in temp:
    if i % 2 == 1:
        print(f'{i}', end=' ')
print()
