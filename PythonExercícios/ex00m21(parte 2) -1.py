# Resposta do curso
def voto(ano):
    from datetime import date # Escopo de importação
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

print('-='*41)

# Minha resposta
from datetime import date

def voto(ano):
    if ano < 16:
        print(f'Com {data} anos: NÃO VOTA.')
    elif 18 <= ano <= 70:
        print(f'Com {data} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {data} anos: VOTO OPCIONAL.')


# programa principal
print('-='*20)
idade = int(input('Em que ano você nasceu? '))
data = date.today().year - idade
voto(data)
