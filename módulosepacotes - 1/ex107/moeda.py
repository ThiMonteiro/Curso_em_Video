# metade
def metade(preço):
    res = preço / 2
    return res


# dobro
def dobro(preço):
    res = preço * 2
    return res


#aumentar
def aumentar(preço, taxa):
    return preço + (preço * taxa/100)


#diminuir
def diminuir(preço, taxa):
    return preço - (preço * taxa/100)


