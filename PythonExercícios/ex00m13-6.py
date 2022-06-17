# resposta do curso
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' > ')
print('ACABOU')

# minha resposta (treinando)
n1 = int(input('Primeiro termo: '))
r1 = int(input('Razão: '))
soma = n1 + (10 - 1) * r1
for c in range (n1, soma + r1, r1):
    print('{}'.format(c), end = ' > ')
print('ACABOU')


# treinando
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao # ENEZIMO TERMO DE UMA PA
for c in range (primeiro, decimo + razao, razao):
    print('{}'.format(c), end= ' > ')
print('FIM')
