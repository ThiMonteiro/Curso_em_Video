# resposta do curso
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')

print('-='*50)

# minha resposta
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média de {dados["Nome"]}: '))
print('-'*30)
if dados['Media'] >= 6:
    dados['Situação'] = ('Aprovado')
else:
    dados['Situação'] = ('Reprovado')
for k, v in dados.items():
    print(f'{k} é igual {v}')

