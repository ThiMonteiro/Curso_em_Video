# resposta do curso
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 99.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(f'-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)

print('='*80)

# minha resposta
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 99.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('-'*50)
print(f'{listagem[0]:.<30}R${listagem[1]:>7.2f}')
print(f'{listagem[2]:.<30}R${listagem[3]:>7.2f}')
print(f'{listagem[4]:.<30}R${listagem[5]:>7.2f}')
print(f'{listagem[6]:.<30}R${listagem[7]:>7.2f}')
print(f'{listagem[8]:.<30}R${listagem[9]:>7.2f}')
print(f'{listagem[10]:.<30}R${listagem[11]:>7.2f}')
print(f'{listagem[12]:.<30}R${listagem[13]:>7.2f}')
print(f'{listagem[14]:.<30}R${listagem[15]:>7.2f}')
print(f'{listagem[16]:.<30}R${listagem[17]:>7.2f}')
print('-'*50)
