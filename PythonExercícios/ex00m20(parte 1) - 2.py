# resposta do curso
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')

print('=-'*30)

# Minha resposta
def texto(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))

# programa principal
texto('Thiago Monteiro de Sousa')
texto('Rhebeca C. C. Marinho')
texto('Zara')