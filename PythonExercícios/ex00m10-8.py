# resposta do curso
print('\033[31m-=\033[m'*20)
print('\033[33mAnalisador de Triângulos\033[m')
print('\033[31m-=\033[m'*20)
r1 = float(input('\033[34mPrimeiro segmento:\033[m '))
r2 = float(input('\033[34mSegundo segmento:\033[m '))
r3 = float(input('\033[34mTerceiro segmento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs segmentos acima PODEM FORMAR triângulo\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR triângulo\033[m')

print('-=-'*20)

# minha resposta (treinando)
r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

print('-=-'*20)

# treinando
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')