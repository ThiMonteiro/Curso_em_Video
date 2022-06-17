# resposta do curso
soma = cont = 0
while True: # Equanto (While) for Verdadeiro (True) - Loop Infinito.
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999: # SE (if) for igual (==) a 999 ele quebra e vai sair da execução.
        break
    cont += 1 # Vai contar quantos numeros foram digitados (Excluindo o 999).
    soma += num # Ele vai somar todos os numeros digitados (Tirando o 999).
print(f'A soma dos {cont} valores foi {soma}!') # Quando finalizar a execução do programa, ele vai sair e vai mostrar o resultado.

print('-'*50)

# miinha resposta
cont = 0
soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}!')
