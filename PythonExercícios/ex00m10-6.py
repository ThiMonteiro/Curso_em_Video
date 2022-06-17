# resposta do curso
a = int(input('\033[33mPrimeiro valor:\033[m '))
b = int(input('\033[33mSegundo Valor:\033[m '))
c = int(input('\033[33mTerceiro valor:\033[m '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[31mO menor valor digitado foi {}\033[m'.format(menor))
print('\033[32mO maior valor digitado foi {}\033[m'.format(maior))

print('-=-'*20)

# minha resposta (treinando)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

print('-'*20)

# treinando
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b > c:
    menor = b
if c < a and c > b:
    menor = b
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))