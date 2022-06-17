# resposta do curso (usando as ferramentas da aula 9)
num = int(input('Informe o valor: '))
n = str(num)
print('Analisando valor de {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

print('='*20)

# resposta do curso (usando função matemática)
num = int(input('Informe um valor: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando valor de {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

print('='*20)

# treinando
num = int(input('Digite um valor: '))
print('Analisando o valor de {}'.format(num))
print('Unidade: {}'.format(num // 1 % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000 % 10))