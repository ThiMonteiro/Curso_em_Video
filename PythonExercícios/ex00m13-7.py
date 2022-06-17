# resposta do curso
num = int(input('Digite um número: '))
tot = 0
for c in range (1, num  + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')

# minha resposta (treinando)
num = int(input('Digite um número: '))
cont = 0 # ele vai contar
for c in range (1, num + 1):
    if num % c == 0:
        cont = cont + 1
    else:
        print('{}'.format(c), end =' ')
print('O numero {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')

print('-'*20)

núm = int(input('Digite um valor: '))
tot = 0 # Contador. Toda vez que ele achar um número divisivel ele vai contar
for c in range (1, núm+1): # ele vai contar de 1 até o número colocado na opção (NÚM)
    if núm % c == 0:
        print('\033[33m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ') # ele vai contar até o numero que for colocado
print('\n\033[mO número {} foi divisivel {} vezes'.format(núm, tot))
if tot == 2: # SE ele foi divisivel 2 vezes é PRIMO
    print('Ele é PRIMO')
else: # SENÃO ele foi divisivel por mais de 2 vezes, ele NÃO É PRIMO
    print('Ele NÃO É PRIMO')