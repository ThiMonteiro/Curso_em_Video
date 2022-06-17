# reposta do curso (forma mais complexa com FOR)
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo')'''

print('-='*20)

# resposta do curso (forma mais simples sem o FOR)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo')

print('-='*20)

# minha resposta (forma simples)
texto = str(input('Escreva a sua frase: ')).strip().upper()
if texto == texto[::-1]:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')

print('-='*20)

# minha resposta (com FOR)
for c in range (5):
    texto = str(input('Escreva alguma frase: ')).strip().upper()
    if texto == texto[::-1]:
        print('É UM PALÍNDROMO')
    else:
        print('NÃO É UM PALÍNDROMO')
    print('-=' * 20)

print('-='*20)
# treinando
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto [letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('PALINDROMO')
else:
    print('NÃO É PALINDROMO')