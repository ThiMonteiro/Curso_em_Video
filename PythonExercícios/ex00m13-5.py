# resposta do curso
soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

print('-'*20)

# minha resposta (com ajuda dos comentarios)
s = 0 # é uma variavel que vai acumulando valores durante as iterações
for cont in range (6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        s = s + num
print('A soma dos numeros pares informados é {}'.format(s))

print('-'*20)
# treinando
soma = 0 # Somador
cont = 0 # contador
for c in range (1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} pares e a soma entre eles foi {}'.format(cont, soma))
