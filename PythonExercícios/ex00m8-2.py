# cores: Vermelho, Amarelo, Azul, Verde
# minha resposta / curso
import math
print('\033[31m-=\033[m'*20)
print('\033[33m a² = b² + c²\033[m')
print('\033[33m Qual o valor da Hipotenusa: ?\033[m')
print('\033[31m-=\033[m'*20)
co = float(input('\033[34mDigite o valor de CO (Cateto Oposto): \033[m'))
ca = float(input('\033[34mDigite o valor de CA (Cateto Adjacente): \033[m'))
hi = math.hypot(co, ca)
print('\033[32mDe acordo com o teorema de Pitágoras, a hipotenusa vai medir {:.2f}.\033[m'.format(hi))

print('\033[31m-\033[m'*20)
# resposta do curso versão 1 (simples)
co = float(input('\033[34mComprimento do cateto oposto: \033[34m'))
ca = float(input('\033[34mComprimento do cateto adjacente: \033[34m'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('\033[32mA hipotenusa vai medir {:.2f}.\033[m'.format(hi))

print('\033[31m-\033[m'*20)
# treinando (minha resposta, usando somente "from")
from math import hypot
co = float(input('\033[34mComprimento do CO (Cateto Oposto): \033[34m'))
ca = float(input('\033[34mComprimento do CA (Cateto Adjacente: \033[34m'))
hi = hypot(co, ca)
print('\033[32mA hipotenusa vai medir {:.2f}.\033[m'.format(hi))









