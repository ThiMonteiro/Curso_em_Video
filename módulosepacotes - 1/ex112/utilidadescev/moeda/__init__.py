# metade
def metade(preço = 0, format=False):
    res = preço / 2
    return res if not format else moeda(res)


# dobro
def dobro(preço = 0, format=False):
    res = preço * 2
    return res if not format else moeda(res)


#aumentar
def aumentar(preço = 0, taxa = 0, format=False):
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)

#diminuir
def diminuir(preço = 0, taxa = 0, format=False):
    res = preço - (preço * taxa/100)
    return res if format is False else moeda(res)

def moeda(preço = 0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

# resumo do valor
def resumo(preço=0, taxaa=0, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-'*30)

