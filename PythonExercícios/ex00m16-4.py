# resposta do curso
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o ultimo número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

print('\n============================================')

# minha resposta (com ajuda do curso)

numero1 = int(input('\nDigite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
numero4 = int(input('Digite um numero: '))
armazenador = (numero1, numero2, numero3, numero4)
print(f'Você digitou os valores: {armazenador}')
print(f'O valor 9 apareceu {armazenador.count(9)} vezes')
if 3 in armazenador:
    print(f'O valor 3 apareceu na {armazenador.index(3)+1} posição')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in armazenador:
    if n % 2 == 0:
        print(n, end=' ')