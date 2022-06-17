n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é: {} \nseu triplo é {} \ne sua raiz quadrada é {:.4f}.'.format(n, d, t, r))

#minha resposta
n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é: {} \nseu triplo é {} \ne sua raiz quadrada é {:.4f}'.format(n, d, t, r))

# resposta avançada
import math
valor = int(input('Digite um valor: '))
d = math.pow(valor, 2)
t = math.pow(valor, 3) # esse triplo está errado
r = math.sqrt(valor)
print('O dobro de {} é: {} \nseu triplo é {} \ne sua raiz quadrada é {:.4f}'.format(valor, d, t, r))