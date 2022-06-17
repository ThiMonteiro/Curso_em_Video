# resposta do curso
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5: # desse jeito o python também entende
    print('O aluno está RECUPERAÇÂO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')

print('-='*20)

# minha reposta
n1 = float(input('Nota da Prova: '))
n2 = float(input('Nota do teste: '))
cal1 = (n1 + n2) / 2
if cal1 >= 7:
    print('Sua média foi: {}'.format(cal1))
    print('Aprovado')
elif cal1 >= 5 and cal1 < 7:
    print('Sua média foi: {}'.format(cal1))
    print('Recuperação')
elif cal1 < 5:
    print('Sua média foi: {}'.format(cal1))
    print('Reprovado')
