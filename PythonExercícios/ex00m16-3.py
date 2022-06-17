# resposta curso
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end= '')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

print('-='*50)

# minha resposta (com ajuda do curso)
from random import randint
gerador1 = randint(1, 10)
gerador2 = randint(1, 10)
gerador3 = randint(1, 10)
gerador4 = randint(1, 10)
gerador5 = randint(1, 10)
armazenador = (gerador1, gerador2, gerador3, gerador4, gerador5)
print('Os valores sorteados foram: ', end= '')
for n in armazenador:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(armazenador)}')
print(f'O menor valor sorteado foi {min(armazenador)}')
