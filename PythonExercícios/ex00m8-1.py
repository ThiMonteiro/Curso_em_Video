# Cores: Vermelho, Amarelo e Lilás
# resposta do curso versão 1
import math
num = float(input('\033[31mDigite um valor: '))
print('\033[33mO valor digitado foi \033[35m{}\033[35m \033[33me a sua porção inteira é\033[33m \033[35m{}'.format(num, math.trunc(num)))

print('\033[1;34m-'*20)

# resposta do curso versão 2
from math import trunc
num = float(input('\033[31mDigite um valor: '))
print('\033[33mO valor digitado foi \033[35m{}\033[35m \033[33me a sua porção inteira é\033[33m \033[35m{}'.format(num, trunc(num)))

print('\033[1;34m-'*20)
# resposta do curso versão 3
num = float(input('\033[31mDigite um valor: '))
print('\033[33mO valor digitado foi \033[35m{} \033[33me a sua porção é \033[35m{}'.format(num, int(num)))

print('\033[1;34m-'*20)

# treinando
from math import trunc
num = float(input('\033[31mDigite um valor: '))
soma = trunc(num)
print('\033[33mO valor digitado foi \033[35m{} \033[33me a sua porção é \033[35m{}'.format(num, soma))
