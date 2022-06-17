# resposta do curso
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRINAGULO', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')


# minha resposta, com ajuda do curso. Essa é a forma simples.
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
if n1 == n2 == n3:
    print('Os segmentos acima podem formar um triangulo EQUILÁTERO')
elif n1 != n2 != n3 != n1:
    print('Os segmentos acima podem formar um triangulo ESCALENO')
else:
    print('Os segmentos acima podem formar um triangulo ISÓSCELES')
