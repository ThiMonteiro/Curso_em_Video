# resposta do curso
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))


print('-='*20)


# minha resposta
from datetime import date
data = int(input('Informe o ano do seu nascimento: '))
cal1 = date.today().year - data
if cal1 <= 17: # se a idade for MENOR(<) ou IGUAL(=) a 17
    print('Sua idade é {}.'.format(cal1))
    print('Falta {} ano(s), para fazer o alistamento.'.format(18 - cal1))
    print('Você ainda precisa se alistar!')
elif cal1 == 18 : # se for igual (==) a 18
    print('Sua idade é {}'.format(cal1))
    print('Você precisa ir se alistar!')
elif cal1 > 18: # se for maior (>) que 18
    print('Sua idade é {}'.format(cal1))
    print('Já se passaram {} ano(s) do seu alistamento.'.format(cal1 - 18))
    print('Você já passou do seu tempo de fazer o alistamento.')