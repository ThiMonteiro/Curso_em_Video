# metade
def metade(preço = 0):
    res = preço / 2
    return res


# dobro
def dobro(preço = 0):
    res = preço * 2
    return res


#aumentar
def aumentar(preço = 0, taxa = 0):
    return preço + (preço * taxa/100)


#diminuir
def diminuir(preço = 0, taxa = 0):
    return preço - (preço * taxa/100)


def moeda(preço = 0):
    return f'R${preço:.0f},00'
