# Resposta do curso
def fatorial(n, show=False):
    # DOC STRING
    """""
    -> Calcule o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial do Fatorial de um número n.
    """""
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa principal
print(fatorial(5, show=True))

print('-'*40)

# minha resposta (treinando)
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
print('-='*15)
print(fatorial(5, show=True))
