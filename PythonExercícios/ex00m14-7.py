# resposta do curso
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} > {}'.format(t1, t2), end='')
cont = 3 # por que 3? porque você já mostrou o primeiro e o segundo termo
while cont <= n: # Enquanto (While) cont for menor ou igual (! = ) N, faz o Loop
    t3 = t1 + t2
    print(' > {}'.format(t3),end=' ')
    t1 = t2 # o t1 passa a ser o t2
    t2 = t3 # o t2 passa a ser o t3. E assim vai por diante, porque ele passsa a andar para o lado
    cont += 1 # esse vai ser o contador
print('FIM')

# minha resposta (treinando)
print('='*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Digite quantos termos você deseja mostrar: '))
t1 = 0
t2 = 1
print('-'*30)
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' > {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
