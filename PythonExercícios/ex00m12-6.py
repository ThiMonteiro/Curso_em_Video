# resposta do curso
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JUNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')

print('-='*20)

# minha resposta
from datetime import date
nascimento = int(input('Informe a data de nascimento: '))
idade = date.today().year - nascimento
if idade <= 9:
    print('Sua idade é {}'.format(idade))
    print('Categoria: MIRIM.')
elif idade > 9 and idade <= 14:
    print('Sua idade é {}'.format(idade))
    print('Categoria: INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Sua idade é {}'.format(idade))
    print('Categoria: JUNIOR.')
elif idade > 19 and idade <= 20:
    print('Sua idade é {}'.format(idade))
    print('Categoria: SÊNIOR.')
elif idade > 20:
    print('Sua idade é {}'.format(idade))
    print('Categoria: MASTER.')
