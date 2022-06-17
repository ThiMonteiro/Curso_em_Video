# resposta do curso
while True: # Enquanto (While) for Verdadeiro (True)
    n = int(input('Que ver a tabuada de qual valor? '))
    print('-'*20)
    if n < 0: # SE (if) o N for menor (<) que 0, ele vai quebrar Senão...
        break
    for c in range (1, 11): # Ele vai fazer um contador em FOR fazendo a multiplicação... isso pode!! Se chama condição aninhada.
        print(f'{n} x {c} = {n*c}')
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

print('-'*50)

# minha resposta com ajuda do curso
while True:
    print('-'*30)
    opção = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if opção < 0:
        break
    for c in range (1, 11):
        print(f'{opção} x {c} = {opção * c}')
print('PROGRAMA ENCERRADO')