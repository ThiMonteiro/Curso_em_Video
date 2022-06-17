# resposta do curso
cont = ('zero', 'um', 'dois', 'tres',  'quatro', 'cinco', 'seis',  'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end= '')
print(f'Você digitou o numero {cont[num]}')

print('='*20)

# minha resposta
numeros = ('zero', 'um', 'dois', 'tres',  'quatro', 'cinco', 'seis',  'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    else:
        print('Tente novamente.', end= '')
print(f'Você digitou o numero {numeros[numero]}')

