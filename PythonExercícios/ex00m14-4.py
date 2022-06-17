# resposta do curso (Forma mais simples) - usando modulo
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# resposta do curso (modo tradicional)
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n # ele vai começar com o número que acabou de ser colocado na variavel
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0: # Enquanto (While) o contador for maior que C, ele precisa fazer
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 #Ele vai tirar um(1) de C
print('{}'.format(f))

# minha resposta (treinando)
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))


