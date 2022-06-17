# Resposta do curso
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


# programa principal
print('Controle de terrenos')
print('-'*30)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
área(larg, comp)

print('=-'*30)

# minha resposta
def soma(larg, comp):
    s = larg * comp
    print('-'*30)
    print(f'A área de um terreno {larg}x{comp} é de {s}m².')


# programa principal
print('Controle de terrenos')
print('-'*30)
soma(larg = float(input('Largura (m): ')), comp = float(input('Comprimento (m): ')))