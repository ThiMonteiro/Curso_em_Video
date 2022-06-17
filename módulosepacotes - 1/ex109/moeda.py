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
