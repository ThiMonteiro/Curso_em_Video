# resposta do curso
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss': # Enquanto (While) a resp estiver em (IN ) 'Ss"
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

print('-'*20)

# minha resposta (treinando)
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss': # Enquanto (While) resp estiver em (in) Ss:
    num = int(input('Digite um valor: '))
    soma += num
    quant += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if quant == 1: # Se (if) o primeiro valor
        maior = menor = num  # ele vai ser o maior e menor, equanto não aparecer outro
    else: # SENÃO (Else)
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('Você digitou {} números e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
