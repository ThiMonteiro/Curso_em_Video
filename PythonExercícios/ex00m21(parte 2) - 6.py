# resposta do curso
def ajuda(com):
    help(com)


def título(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÈ LOGO')