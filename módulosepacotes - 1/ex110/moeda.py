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
def resumo(p=0, a=0, r=0):
    from ex110 import moeda
    '''
    --> Função criada para resumo de valor
    :param p: Vai receber o Valor
    :param a: Vai receber o Aumento
    :param r: Vai receber a Redução
    :return
    '''
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado: {moeda.moeda(p)}')
    print(f'Dobro do preço: {moeda.moeda(p*2)}')
    print(f'Metade do preço: {moeda.moeda(p/2)}')
    print(f'{a}% de aumento: {moeda.moeda(p + (p * a/100))}')
    print(f'{r}% de redução: {moeda.moeda(p - (p * r/100))}')
    print('-'*30)


